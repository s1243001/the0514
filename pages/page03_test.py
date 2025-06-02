import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="路段上的旅遊景點",
    page_icon="🗺️",
    layout="wide"
)

st.title("路段上的旅遊景點")

# Define attraction data for each route
# This dictionary holds GeoJSON path, map center, attraction CSV path,
# and a list of dictionaries for each attraction's details (title, text, image path).
# Coordinates are [latitude, longitude]
attraction_data = {
    '台北-新竹': {
        'geojson': "geojson/taipei_hsinchu.geojson",
        'center': [24.949132, 121.182838],
        'attraction_csv': "play_csv/play_ts.csv",
        'attractions': [
            {"title": "大溪老街", "text": "這裡是大溪老街的介紹文字。", "image_path": "play_png/ts1.png"},
            {"title": "新竹17公里海岸風景區", "text": "這裡有新竹17公里海岸風景區的介紹文字。", "image_path": "play_png/ts2.png"},
        ]
    },
    '新竹-台中': {
        'geojson': "geojson/hsinchu_taichung.geojson",
        'center': [24.462711, 120.740153],
        'attraction_csv': "play_csv/play_stc.csv",
        'attractions': [
            {"title": "白沙屯拱天宮", "text": "這裡是白沙屯拱天宮的介紹文字。", "image_path": "play_png/stc1.png"},
            {"title": "大甲鎮瀾宮", "text": "這裡是大甲鎮瀾宮的介紹文字。", "image_path": "play_png/stc2.png"},
            {"title": "國立自然科學博物館", "text": "這裡有國立自然科學博物館的介紹文字。", "image_path": "play_png/stc3.png"},
        ]
    },
    '台中-嘉義': {
        'geojson': "geojson/taichung_jiayi.geojson",
        'center': [23.809488, 120.292326],
        'attraction_csv': "play_csv/play_tcjia.csv",
        'attractions': [
            {"title": "八卦山大佛風景區", "text": "這裡有八卦山大佛風景區的介紹文字。", "image_path": "play_png/tcjia1.png"},
            {"title": "員林神社鳥居", "text": "這裡有員林神社鳥居的介紹文字。", "image_path": "play_png/tcjia2.png"},
            {"title": "嘉義北門驛", "text": "這裡有嘉義北門驛的介紹文字。", "image_path": "play_png/tcjia3.png"},
        ]
    },
    '嘉義-高雄': {
        'geojson': "geojson/jiayi_kaohsung.geojson",
        'center': [22.999866, 120.148435],
        'attraction_csv': "play_csv/play_jiakao.csv",
        'attractions': [
            {"title": "嘉義縣科學教育中心-太空教育館", "text": "這裡有嘉義縣科學教育中心-太空教育館的介紹文字。", "image_path": "play_png/jiakao1.png"},
            {"title": "臺南孔廟", "text": "這裡有臺南孔廟的介紹文字。", "image_path": "play_png/jiakao2.png"},
            {"title": "K.A.T 橋仔頭糖廠藝術村", "text": "這裡有K.A.T 橋仔頭糖廠藝術村的介紹文字。", "image_path": "play_png/jiakao3.png"},
        ]
    },
    '高雄-屏東': {
        'geojson': "geojson/kaohsung_pingtung.geojson",
        'center': [22.402317, 120.536198],
        'attraction_csv': "play_csv/play_kaoping.csv",
        'attractions': [
            {"title": "龍虎塔", "text": "這裡有龍虎塔的介紹文字。", "image_path": "play_png/kaoping1.png"},
            {"title": "大鵬灣國家風景區", "text": "這裡有大鵬灣國家風景區的介紹文字。", "image_path": "play_png/kaoping2.png"},
            {"title": "國立海洋生物博物館", "text": "這裡有國立海洋生物博物館的介紹文字。", "image_path": "play_png/kaoping3.png"},
        ]
    },
    '屏東-台東': {
        'geojson': "geojson/pingtung_taitung.geojson",
        'center': [22.781440, 120.834135],
        'attraction_csv': "play_csv/play_pingtait.csv",
        'attractions': [
            {"title": "壽卡鐵馬驛站", "text": "這裡有壽卡鐵馬驛站的介紹文字。", "image_path": "play_png/pingtait1.png"},
            {"title": "多良車站", "text": "這裡有多良車站的介紹文字。", "image_path": "play_png/pingtait2.png"},
            {"title": "國立臺灣史前文化博物館", "text": "這裡有國立臺灣史前文化博物館的介紹文字。", "image_path": "play_png/pingtait3.png"},
        ]
    },
    '台東-花蓮': {
        'geojson': "geojson/taitung_huaien.geojson", # Taitung_Hualien.geojson
        'center': [23.429920, 121.335207],
        'attraction_csv': "play_csv/play_taithua.csv", # play_taitung_hualien.csv
        'attractions': [
            {"title": "鹿野高台", "text": "這裡是鹿野高台的介紹文字。", "image_path": "play_png/taithua1.png"}, # tait_hua1.png
            {"title": "臺東池上錦新三號道路 伯朗大道", "text": "這裡有臺東池上錦新三號道路 伯朗大道的介紹文字。", "image_path": "play_png/taithua2.png"}, # tait_hua2.png
        ]
    },
    '花蓮-宜蘭': {
        'geojson': "geojson/hualien_yilan.geojson",
        'center': [24.228917, 121.532195],
        'attraction_csv': "play_csv/play_huayi.csv",
        'attractions': [
            {"title": "鯉魚潭風景遊憩區", "text": "這裡有鯉魚潭風景遊憩區的介紹文字。", "image_path": "play_png/huayi1.png"},
            {"title": "七星潭", "text": "這裡有七星潭的介紹文字。", "image_path": "play_png/huayi2.png"},
            {"title": "清水斷崖", "text": "這裡有清水斷崖的介紹文字。", "image_path": "play_png/huayi3.png"},
        ]
    },
    '宜蘭-台北': {
        'geojson': "geojson/yilan_taipei.geojson",
        'center': [24.899394, 121.675311],
        'attraction_csv': "play_csv/play_yitaip.csv",
        'attractions': [
            {"title": "福隆舊草嶺隧道", "text": "這裡是福隆舊草嶺隧道的介紹文字。", "image_path": "play_png/yitaip1.png"},
            {"title": "十分老街", "text": "這裡有十分老街的介紹文字。", "image_path": "play_png/yitaip2.png"},
        ]
    },
}

# Check if 'selected_route' is in session_state (meaning user came from the first page)
if 'selected_route' in st.session_state:
    selected_route = st.session_state['selected_route']
    st.write(f"你在**上一頁**選擇的路段是：**{selected_route}**")
    st.header("探索這個路段的熱門景點！")

    # Get data for the selected route
    route_info = attraction_data.get(selected_route)

    if route_info:
        geojson_file = route_info['geojson']
        attraction_csv_file = route_info['attraction_csv']
        center_coords = route_info['center']
        attractions_list = route_info['attractions']

        # Define GeoJSON route style
        route_style = {
            "color": "red",
            "weight": 4,
            "opacity": 0.8,
            "fillColor": "none"
        }

        # Initialize Leafmap
        m = leafmap.Map(center=center_coords, zoom=9, minimap_control=True)

        # Add GeoJSON route
        try:
            m.add_geojson(geojson_file, layer_name=selected_route, style=route_style)
        except FileNotFoundError:
            st.error(f"找不到 '{geojson_file}' 這個 GeoJSON 檔案。")
            st.info("請確認 GeoJSON 檔案位於 'geojson/' 子目錄中，或提供正確的路徑。")

        # Read and add attraction points from CSV
        try:
            attraction_df = pd.read_csv(attraction_csv_file)
            st.dataframe(attraction_df) # Display the DataFrame for verification

            # Ensure CSV has 'X' (longitude) and 'Y' (latitude) columns
            if not attraction_df.empty and 'X' in attraction_df.columns and 'Y' in attraction_df.columns:
                m.add_points_from_xy(
                    attraction_df,
                    x="X",  # Longitude column
                    y="Y",  # Latitude column
                    popup=["名稱", "地址"], # Customize based on your CSV columns
                    tooltip="名稱",
                    color="green", # Change color for attractions
                    marker_cluster=True
                )
            elif attraction_df.empty:
                st.info(f"'{attraction_csv_file}' 中沒有景點資料。")
            else:
                st.error("景點 CSV 檔案中缺少 'X' 或 'Y' 欄位。")

        except FileNotFoundError:
            st.error(f"找不到 '{attraction_csv_file}' 這個景點 CSV 檔案，請確認檔案是否存在。")
            st.info("請確認 CSV 檔案位於 'play_csv/' 子目錄中，或提供正確的路徑。")
        except Exception as e:
            st.error(f"讀取景點資料或地圖渲染時發生錯誤：{e}")
            st.warning("請檢查景點 CSV 檔案格式和內容是否正確。")

        # Display the map
        m.to_streamlit(height=600) # Adjust height as needed

        st.markdown("---")
        st.subheader("景點介紹")
        # Display attractions details (text and images)
        for attraction in attractions_list:
            st.markdown(f"### {attraction['title']}")
            st.write(attraction['text'])
            if attraction['image_path']:
                try:
                    st.image(attraction['image_path'], caption=attraction['title'], use_container_width=True)
                except FileNotFoundError:
                    st.warning(f"找不到 '{attraction['image_path']}' 這張景點圖片，請確認檔案是否存在。")
            st.markdown("---") # Separator for each attraction

    else:
        st.error(f"找不到 '{selected_route}' 路段的景點配置資訊。")

else:
    st.warning("請先回**選擇路段頁面**選擇路段！")
    if st.button("回選擇路段頁面"):
        st.switch_page("page01_test") # Navigate back to your main page
