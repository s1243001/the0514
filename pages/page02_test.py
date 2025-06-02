import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

# 頁面配置
st.set_page_config(
    page_title="路段補給站",
    page_icon="🍔",
    layout="wide"
)

st.title("路段上的補給站們")

# 定義路段資料，包含 GeoJSON 和 CSV 補給站檔案路徑
# 注意：這裡的檔案路徑已移除子目錄前綴
section_data = {
    '台北-新竹': {'geojson': "taipei_hsinchu.geojson", 'center': [24.949132, 121.182838], 'station_csv': "station_ts.csv"},
    '新竹-台中': {'geojson': "hsinchu_taichung.geojson", 'center': [24.462711, 120.740153], 'station_csv': "station_stc.csv"},
    '台中-嘉義': {'geojson': "taichung_jiayi.geojson", 'center': [23.809488, 120.292326], 'station_csv': "station_tcjia.csv"},
    '嘉義-高雄': {'geojson': "jiayi_kaohsung.geojson", 'center': [22.999866, 120.148435], 'station_csv': "station_jiakao.csv"},
    '高雄-屏東': {'geojson': "kaohsung_pingtung.geojson", 'center': [22.402317, 120.536198], 'station_csv': "station_kaoping.csv"},
    '屏東-台東': {'geojson': "pingtung_taitung.geojson", 'center': [22.781440, 120.834135], 'station_csv': "station_pingtait.csv"},
    '台東-花蓮': {'geojson': "taitung_hualien.geojson", 'center': [23.429920, 121.335207], 'station_csv': "station_taithua.csv"},
    '花蓮-宜蘭': {'geojson': "hualien_yilan.geojson", 'center': [24.228917, 121.532195], 'station_csv': "station_huayi.csv"},
    '宜蘭-台北': {'geojson': "yilan_taipei.geojson", 'center': [24.899394, 121.675311], 'station_csv': "station_yitaip.csv"},
}

# 檢查 session_state 中是否有 'selected_route'
if 'selected_route' in st.session_state:
    selected_route = st.session_state['selected_route']
    st.write(f"你在**上一頁**選擇的路段是：**{selected_route}**")
    st.header("這是你選擇路段的補給站")

    # 獲取當前路段的 GeoJSON 和 CSV 檔案路徑以及中心點
    route_info = section_data.get(selected_route)

    if route_info:
        geojson_file = route_info['geojson']
        station_csv_file = route_info['station_csv']
        center_coords = route_info['center']

        # 定義 GeoJSON 路線的樣式
        route_style = {
            "color": "red",      # 路線顏色
            "weight": 4,         # 路線粗細
            "opacity": 0.8,      # 路線透明度
            "fillColor": "none"  # 無填充色
        }

        # 讀取補給站資料
        try:
            # 讀取 CSV 檔
            station_df = pd.read_csv(station_csv_file)
            st.dataframe(station_df)

            # 初始化地圖並添加 GeoJSON 路線和補給站點
            m = leafmap.Map(center=center_coords, zoom=9, minimap_control=True)

            # 添加 GeoJSON 路線
            try:
                m.add_geojson(geojson_file, layer_name=selected_route, style=route_style)
            except FileNotFoundError:
                st.error(f"找不到 '{geojson_file}' 這個 GeoJSON 檔案。")
                st.info("請確認 GeoJSON 檔案與 Streamlit 腳本位於相同目錄，或提供正確的路徑。")

            # 添加補給站點
            # 關鍵點：x 和 y 參數為 "X" 和 "Y"
            if not station_df.empty and 'X' in station_df.columns and 'Y' in station_df.columns:
                m.add_points_from_xy(
                    station_df,
                    x="X",  # 經度欄位為 "X"
                    y="Y",  # 緯度欄位為 "Y"
                    popup=["路線","門市名稱","地址","X","Y"], # 可選：顯示補給站名稱、地址、電話等
                    tooltip="門市名稱", # 鼠標懸停時顯示名稱
                    color="blue", # 點的顏色
                    marker_cluster=True # 將附近的點聚類
                )
            elif station_df.empty:
                st.info(f"'{station_csv_file}' 中沒有補給站資料。")
            else:
                st.error("補給站 CSV 檔案中缺少 'X' 或 'Y' 欄位。")

            m.to_streamlit(height=700)

        except FileNotFoundError:
            st.error(f"找不到 '{station_csv_file}' 這個補給站 CSV 檔案，請確認檔案是否存在於專案根目錄。")
            st.info("請確認 CSV 檔案與 Streamlit 腳本位於相同目錄，或提供正確的路徑。")
        except Exception as e:
            st.error(f"讀取補給站資料或地圖渲染時發生錯誤：{e}")
            st.warning("請檢查 CSV 檔案格式和內容是否正確。")
    else:
        st.error(f"找不到 '{selected_route}' 路段的配置資訊。")

else:
    st.warning("請先回**選擇路段頁面**選擇路段！")
    if st.button("回選擇路段頁面"):
        st.switch_page("page01_test") # 導航回你的第一頁 (page01_test.py)
