
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
National Changhua University of Education
<https://www.ncue.edu.tw/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("關於我們的網站")

st.header("地形剖面圖製作")
st.markdown("透過Gemini撰寫程式碼，輸入到google colab中，再加入特定路段geojson檔，設定取樣點100+1點，並利用太空梭雷達地形任務(SRTM) 數位高程資料集第四版CGIAR/SRTM90_V4中的高度資料，繪製特定路段的地形剖面圖，利用圖表方式呈現，橫軸為里程，縱軸為海拔高度。")
with st.expander("See source code"):
    with st.echo():
        # =====================================================
        # 1. 安裝與設定環境 (首次執行時可能需要幾分鐘)
        # =====================================================
        # 安裝必要套件
        !pip install -q geemap geopandas

        # 安裝中文字型 (Noto Sans CJK TC - 繁體中文)
        !apt-get -qq install -y fonts-noto-cjk

        # =====================================================
        # 2. 匯入必要函式庫
        # =====================================================
        import ee
        import geemap
        import geopandas as gpd
        import matplotlib.pyplot as plt
        import matplotlib.font_manager as fm
        import numpy as np
        from shapely.geometry import LineString # geopandas 會依賴 shapely
        
        # =====================================================
        # 3. 設定 Matplotlib 中文字型
        # =====================================================
        # 清除 Matplotlib 的字型快取，確保新安裝的字型被載入
        try:
            fm._fontManager.cache.clear()
        except AttributeError:
            try:
                fm._rebuild() # 舊版 Matplotlib
            except AttributeError:
            print("無法自動清除字型快取。如果字型未更新，請在安裝字型後嘗試『重新啟動執行階段』。")

        # 設定 Matplotlib 使用 Noto Sans CJK TC 字型並修正負號顯示
        plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False
        
        # =====================================================
        # 4. 初始化 Earth Engine
        # =====================================================
        try:
            ee.Initialize(project='ee-s1243001') # 請替換成您自己的 GEE Project ID
        except Exception as e:
            print(f"Earth Engine 初始化失敗，嘗試認證：{e}")
            ee.Authenticate()
            ee.Initialize(project='ee-s1243001') # 請替換成您自己的 GEE Project ID
        
        print("Earth Engine 初始化成功！")
        
        # =====================================================
        # 5. 載入並處理地理路徑資料 (GeoJSON)
        # =====================================================
        # 請確認您已掛載 Google Drive，並且 GeoJSON 檔案路徑正確
        geojson_path = '/content/drive/MyDrive/hualien_yilan.geojson' # 請修改為您的檔案實際路徑
        
        try:
            gdf = gpd.read_file(geojson_path)
        except Exception as e:
            print(f"讀取 GeoJSON 檔案失敗: {e}")
            print("請檢查檔案路徑是否正確，以及 Google Drive 是否已掛載。")
                # 若要掛載 Drive，可以執行以下程式碼 (取消註解)：
            # from google.colab import drive
            # drive.mount('/content/drive')
            # print("Google Drive 已掛載，請重新執行此儲存格或後續儲存格。")
            raise # 中斷執行，因為沒有路徑資料無法繼續
        
        # 過濾出 LineString 幾何型態
            gdf_lines = gdf[gdf.geometry.geom_type == 'LineString']
        
        if len(gdf_lines) == 0:
            raise ValueError("GeoJSON 檔案中沒有有效的 LineString 路徑")
        
        # 取得第一條路線 (Shapely LineString 物件)
        shapely_line = gdf_lines.iloc[0].geometry
        
        # 將 Shapely LineString 座標轉換為 Earth Engine LineString
        ee_line_coords = [[coord[0], coord[1]] for coord in list(shapely_line.coords)]
        ee_line = ee.Geometry.LineString(ee_line_coords)
        
        # =====================================================
        # 6. 沿實際路徑產生取樣點
        # =====================================================
        num_segments = 100  # 定義路徑上的線段數量 (會有 num_segments + 1 個點)
        
        # 從 Earth Engine 獲取線的總長度（公尺）
        try:
            total_length_meters = ee_line.length().getInfo()
        except ee.EEException as e:
            print(f"計算 Earth Engine 線段長度時發生錯誤: {e}")
            print("這可能是因為線段座標無效或 GEE 服務問題。")
            raise
            
        segment_length_meters = total_length_meters / num_segments
    
        ee_points_features = []
        print(f"總路徑長度: {total_length_meters:.2f} 公尺")
        print(f"將產生 {num_segments + 1} 個取樣點...")
        
        for i in range(num_segments + 1):
            # 計算沿線的比例距離 (0.0 到 1.0)
            fractional_dist = i / num_segments

            # 使用 shapely 的 interpolate 方法沿實際路徑插值取點
            # normalized=True 表示 fractional_dist 是相對於總長度的比例
            current_shapely_point = shapely_line.interpolate(fractional_dist, normalized=True)
    
            # 建立 Earth Engine Geometry Point
            ee_geom_point = ee.Geometry.Point([current_shapely_point.x, current_shapely_point.y])

            # 計算該點沿實際路徑的累積距離（公尺）
            current_distance_meters = i * segment_length_meters

            ee_points_features.append(ee.Feature(ee_geom_point, {"distance": current_distance_meters}))

            # 將 Python 列表中的 ee.Feature 轉換為 Earth Engine FeatureCollection
        points_fc = ee.FeatureCollection(ee_points_features)
        print(f"成功產生 {len(ee_points_features)} 個 Earth Engine Features。")

        # =====================================================
        # 7. 載入 SRTM Digital Elevation Data Version 4 高程資料
        # =====================================================
        # 使用 SRTM Digital Elevation Data Version 4 (CGIAR/SRTM90_V4)
        # SRTM90_V4 的波段名稱為 'elevation'
        srtm_dem_image = ee.Image("CGIAR/SRTM90_V4").select("elevation")
        print("SRTM Digital Elevation Data Version 4 資料已載入。")
        
        # =====================================================
        # 8. 在取樣點上提取高程資料
        # =====================================================
        # scale 參數建議與 DSM 的解析度一致或接近 (SRTM 約為 90公尺，但這裡使用 30 以確保密度)
        try:
            samples = srtm_dem_image.sampleRegions(
                collection=points_fc,
                scale=30,      # SRTM 原始解析度約 90 公尺，但通常取樣會用較小的 scale 增加密度
                geometries=True  # 保留幾何資訊（雖然此處主要用 'distance'）
            )
            # .getInfo() 會將伺服器端的 EE 物件轉換為客戶端的 Python 物件
            samples_info = samples.getInfo()
        except ee.EEException as e:
            print(f"從 SRTM DEM 提取高程樣本時發生錯誤: {e}")
            print("可能原因：")
            print("1. 取樣點位於無資料區域（例如水體，取決於 DEM 版本和處理）。")
            print("2. Earth Engine 資源限制或暫時性問題。")
            print("3. 'points_fc' 包含無效的幾何圖形。")
            raise
        
        print(f"成功提取到 {len(samples_info['features'])} 個樣本點的高程資料。")
        
        # =====================================================
        # 9. 整理高程資料以供繪圖
        # =====================================================
        distances = []
        elevations = []
        
        if not samples_info["features"]:
            print("警告：未提取到任何樣本點資料。剖面圖將是空的。")
        else:
            for f in samples_info["features"]:
                dist = f["properties"]["distance"]
                # 從 "elevation" 波段獲取高程值 (SRTM 的波段名稱)
                elev = f["properties"].get("elevation")
        
                if elev is not None: # 確保高程值存在
                    distances.append(dist)
                    elevations.append(elev)
                else:
                    # 如果某點沒有高程值 (例如在水體或資料邊緣)，可以選擇跳過或用特定值填充
                    print(f"警告：距離 {dist:.2f} 公尺處的點未獲取到有效高程值。")
                    # 為了保持剖面線連續性，可以考慮用 np.nan 或前後點插值 (此處簡單跳過)
                    # distances.append(dist)
                    # elevations.append(np.nan) # 如果想在圖上標示無資料點
        
        if not distances or not elevations:
            print("錯誤：沒有有效的高程數據可供繪圖。請檢查 GeoJSON 路徑、DEM 資料或取樣過程。")
        else:
            print("高程資料整理完畢，準備繪圖。")
        
        # =====================================================
        # 10. 繪製地形剖面圖
        # =====================================================
        if distances and elevations: # 確保有資料才繪圖
            plt.figure(figsize=(16, 7)) # 調整圖片大小以更好地顯示中文標籤
            plt.plot(distances, elevations, color='dodgerblue', linewidth=2)
        
            # 使用 fontname 參數明確指定字型 (作為 plt.rcParams 的補充)
            plt.title("地形剖面圖 (SRTM Digital Elevation Data Version 4)", fontname='Noto Sans CJK TC', fontsize=16)
            plt.xlabel("距離 (公尺)", fontname='Noto Sans CJK TC', fontsize=12)
            plt.ylabel("高程 (公尺)", fontname='Noto Sans CJK TC', fontsize=12)
        
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout() # 自動調整子圖參數，使之填充整個圖像區域
            plt.show()
        else:
            print("由於缺乏有效數據，無法繪製地形剖面圖。")
        
        # =====================================================
        # 可選：在地圖上顯示路徑和取樣點 (使用 geemap)
        # =====================================================
        if 'ee_line' in locals() and 'points_fc' in locals() and distances and elevations:
            try:
                Map = geemap.Map()
                Map.centerObject(ee_line, zoom=10) # 以路徑為中心調整地圖視野和縮放
                Map.addLayer(ee_line, {'color': 'FF0000'}, '分析路徑') # 紅色路徑
                Map.addLayer(points_fc, {'color': '0000FF'}, '取樣點') # 藍色取樣點
                # SRTM 的高程範圍可能不同，調整 palette 以適應
                Map.addLayer(srtm_dem_image, {'min': 0, 'max': 1000, 'palette': ['0000FF', '00FFFF', 'FFFF00', 'FF0000', 'FFFFFF']}, 'SRTM DEM 底圖')
                display(Map)
                print("路徑與取樣點已顯示在地圖上。")
            except Exception as e:
                print(f"使用 geemap 顯示地圖時發生錯誤: {e}")
        m.to_streamlit(height=700)
