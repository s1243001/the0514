import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import os
import base64 # Import base64 for image embedding

st.title(" 推薦的美食餐廳🍝")

# 從 session_state 讀取使用者選擇的路段
if 'selected_route' not in st.session_state:
    st.warning("請先回到第一頁選擇路段。")
    st.stop() # 如果沒有選擇路段，就停止程式執行

option = st.session_state['selected_route']

# Define base paths for your data and images
FOOD_CSV_FOLDER = "food_csv"
FOOD_PNG_FOLDER = "food_png"
GEOJSON_FOLDER = "." # Assuming geojson files are in the root directory or adjust as needed

# Function to load geojson (assuming they are in the root or a specified folder)
def load_geojson(filename):
    geojson_path = os.path.join(GEOJSON_FOLDER, filename)
    if os.path.exists(geojson_path):
        with open(geojson_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        st.error(f"GeoJSON file not found: {geojson_path}")
        return None

# Dictionary to hold road segment data for cleaner code (similar to page 3)
food_segments = {
    '台北-新竹': {
        'center': [24.949132, 121.182838], # Corrected lat/lon order
        'color': "red",
        'geojson_file': "taipei_hsinchu.geojson",
        'csv_file': "food_ts.csv",
        'markdown': """
        ###游記百年油飯
        文字
        <img src="data:image/png;base64,{food_ts1_base64}" width="500">

        ---

        ###關西牛肉捲餅
        文字
        <img src="data:image/png;base64,{food_ts2_base64}" width="500">

        ---

        ###廟口鴨香飯
        文字
        <img src="data:image/png;base64,{food_ts3_base64}" width="500">
        """,
        'images': ['food_ts1.jpg', 'food_ts2.jpg', 'food_ts3.jpg']
    },
    '新竹-台中': {
        'center': [24.462711, 120.740153],
        'color': "red", # Changed color for variety
        'geojson_file': "hsinchu_taichung.geojson",
        'csv_file': "food_stc.csv",
        'markdown': """
        ###（東北香粑粑）白沙屯美食
        文字
        <img src="data:image/png;base64,{food_stc1_base64}" width="500">

        ---

        ###一品香水煎包專賣店
        文字
        <img src="data:image/png;base64,{food_stc2_base64}" width="500">

        ---

        ###發愣吃VARMT - 勤美店
        文字
        <img src="data:image/png;base64,{food_stc3_base64}" width="500">
        """,
        'images': ['food_stc1.jpg', 'food_stc2.jpg', 'food_stc3.jpg']
    },
    '台中-嘉義': {
        'center': [23.809488, 120.292326],
        'color': "red", # Changed color for variety
        'geojson_file': "taichung_jiayi.geojson",
        'csv_file': "food_tcjia.csv",
        'markdown': """
        ###阿添蛤仔麵
        文字
        <img src="data:image/png;base64,{food_tcjia1_base64}" width="500">

        ---

        ###西螺 脆皮臭豆腐
        文字
        <img src="data:image/png;base64,{food_tcjia2_base64}" width="500">

        ---

        ###民主火雞肉飯
        文字
        <img src="data:image/png;base64,{food_tcjia3_base64}" width="500">
        """,
        'images': ['food_tcjia1.jpg', 'food_tcjia2.jpg', 'food_tcjia3.jpg']
    },
    '嘉義-高雄': {
        'center': [22.999866, 120.148435],
        'color': "red", # Changed color for variety
        'geojson_file': "jiayi_kaohsung.geojson",
        'csv_file': "food_jiakao.csv",
        'markdown': """
        ###味泰豐香雞排
        文字
        <img src="data:image/png;base64,{food_jiakao1_base64}" width="500">

        ---

        ###城邊真味鱔魚意麵
        文字
        <img src="data:image/png;base64,{food_jiakao2_base64}" width="500">

        ---

        ###Temperature Studio/溫度劑
        文字
        <img src="data:image/png;base64,{food_jiakao3_base64}" width="500">
        """,
        'images': ['food_jiakao1.jpg', 'food_jiakao2.jpg', 'food_jiakao3.jpg']
    },
    '高雄-屏東': {
        'center': [22.402317, 120.536198],
        'color': "red", # Changed color for variety
        'geojson_file': "kaohsung_pingtung.geojson",
        'csv_file': "food_kaoping.csv",
        'markdown': """
        ###仁武烤鴨
        文字
        <img src="data:image/png;base64,{food_kaoping1_base64}" width="500">

        ---

        ###北港蔡三代筒仔米糕
        文字
        <img src="data:image/png;base64,{food_kaoping2_base64}" width="500">

        ---

        ###王匠黑鮪魚生魚片&日本料理
        文字
        <img src="data:image/png;base64,{food_kaoping3_base64}" width="500">
        """,
        'images': ['food_kaoping1.jpg', 'food_kaoping2.jpg', 'food_kaoping3.jpg']
    },
    '屏東-台東': {
        'center': [22.781440, 120.834135],
        'color': "red", # Changed color for variety
        'geojson_file': "pingtung_taitung.geojson",
        'csv_file': "food_pingtait.csv",
        'markdown': """
        ###卑南豬血湯 侯記老店
        文字
        <img src="data:image/png;base64,{food_pingtait1_base64}" width="500">

        ---

        ###某一家
        文字
        <img src="data:image/png;base64,{food_pingtait2_base64}" width="500">
        """,
        'images': ['food_pingtait1.jpg', 'food_pingtait2.jpg']
    },
    '台東-花蓮': {
        'center': [23.429920, 121.335207],
        'color': "red", # Changed color for variety
        'geojson_file': "taitung_hualien.geojson",
        'csv_file': "food_taithua.csv",
        'markdown': """
        ###全美行
        文字
        <img src="data:image/png;base64,{food_taithua1_base64}" width="500">

        ---

        ###某一家
        文字
        <img src="data:image/png;base64,{food_taithua2_base64}" width="500">
        """,
        'images': ['food_taithua1.jpg', 'food_taithua2.jpg']
    },
    '花蓮-宜蘭': {
        'center': [24.228917, 121.532195],
        'color': "red", # Changed color for variety
        'geojson_file': "hualien_yilan.geojson",
        'csv_file': "food_huayi.csv",
        'markdown': """
        ###液香扁食
        文字
        <img src="data:image/png;base64,{food_huayi1_base64}" width="500">

        ---

        ###羅東碳烤燒餅餅店
        文字
        <img src="data:image/png;base64,{food_huayi2_base64}" width="500">
        """,
        'images': ['food_huayi1.jpg', 'food_huayi2.jpg']
    },
    '宜蘭-台北': {
        'center': [24.899394, 121.675311],
        'color': "red", # Changed color for variety
        'geojson_file': "yilan_taipei.geojson",
        'csv_file': "food_yitaip.csv",
        'markdown': """
        ###十分溜哥燒烤雞翅包飯
        文字
        <img src="data:image/png;base64,{food_yitaip1_base64}" width="500">

        ---

        ###羅東碳烤燒餅餅店
        文字
        <img src="data:image/png;base64,{food_yitaip2_base64}" width="500">
        """,
        'images': ['food_yitaip1.jpg', 'food_yitaip2.jpg']
    }
}

# --- Main logic to display map and information ---

if option in food_segments:
    segment_info = food_segments[option]

    # Initialize map
    # Note: Corrected center order to [latitude, longitude]
    m = leafmap.Map(center=segment_info['center'], zoom=7, minimap_control=True)
    style = {"color": segment_info['color'], "weight": 3, "opacity": 0.8}

    # Add GeoJSON
    geojson_data = load_geojson(segment_info['geojson_file'])
    if geojson_data:
        m.add_geojson(geojson_data, layer_name=option, style=style)

    # Add points from CSV
    csv_path = os.path.join(FOOD_CSV_FOLDER, segment_info['csv_file'])
    if os.path.exists(csv_path):
        m.add_points_from_xy(csv_path, x="X", y="Y")
    else:
        st.error(f"CSV file not found: {csv_path}")

    # Display map
    m.to_streamlit(height=700)

    # Prepare markdown with images
    image_placeholders = {}
    for img_file in segment_info['images']:
        img_path = os.path.join(FOOD_PNG_FOLDER, img_file)
        if os.path.exists(img_path):
            with open(img_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                # Extract filename without extension for placeholder name
                placeholder_name = os.path.splitext(img_file)[0] + '_base64'
                image_placeholders[placeholder_name] = encoded_string
        else:
            st.warning(f"Image file not found: {img_path}. Placeholder will be empty.")
            # Even if not found, add to dictionary to prevent KeyError
            placeholder_name = os.path.splitext(img_file)[0] + '_base64'
            image_placeholders[placeholder_name] = "" # Empty string if image not found

    # Format the markdown string with the base64 encoded images
    formatted_markdown = segment_info['markdown'].format(**image_placeholders)
    st.markdown(formatted_markdown, unsafe_allow_html=True)

else:
    # 如果 selected_route 不在 food_segments 字典中，提示使用者
    st.write("所選路段無資料顯示。請回到第一頁重新選擇。")
