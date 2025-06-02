import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import os # Import the os module for path manipulation

st.title("路段上的旅遊景點")

# Assuming 'option' is passed from the first page, e.g., via st.session_state
# For demonstration purposes, if 'option' is not yet set, default it to '台北-新竹'
if 'option' not in st.session_state:
    # This is a placeholder for testing. In a real multi-page app,
    # 'option' should be set on the previous page.
    st.session_state.option = '台北-新竹'

option = st.session_state.option

# Define base paths for your data and images
PLAY_CSV_FOLDER = "play_csv"
PLAY_PNG_FOLDER = "play_png"
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

# Dictionary to hold road segment data for cleaner code
road_segments = {
    '台北-新竹': {
        'center': [24.949132, 121.182838], # Corrected lat/lon order for Leafmap center
        'color': "red",
        'geojson_file': "taipei_hsinchu.geojson", # Assuming geojson files have .geojson extension
        'csv_file': "play_ts.csv",
        'markdown': """
        ###大溪老街
        文字
        <img src="data:image/png;base64,{ts1_base64}" width="500">

        ---

        ###新竹17公里海岸風景區
        文字
        <img src="data:image/png;base64,{ts2_base64}" width="500">
        """,
        'images': ['ts1.jpg', 'ts2.jpg'] # Assuming images are .jpg
    },
    '新竹-台中': {
        'center': [24.462711, 120.740153],
        'color': "orange",
        'geojson_file': "hsinchu_taichung.geojson",
        'csv_file': "play_stc.csv",
        'markdown': """
        ###白沙屯拱天宮
        文字
        <img src="data:image/png;base64,{stc1_base64}" width="500">

        ---

        ###大甲鎮瀾宮
        文字
        <img src="data:image/png;base64,{stc2_base64}" width="500">

        ---

        ###國立自然科學博物館
        文字
        <img src="data:image/png;base64,{stc3_base64}" width="500">
        """,
        'images': ['stc1.jpg', 'stc2.jpg', 'stc3.jpg']
    },
    '台中-嘉義': {
        'center': [23.809488, 120.292326],
        'color': "purple",
        'geojson_file': "taichung_jiayi.geojson",
        'csv_file': "play_tcjia.csv",
        'markdown': """
        ###八卦山大佛風景區
        文字
        <img src="data:image/png;base64,{tcjia1_base64}" width="500">

        ---

        ###員林神社鳥居
        文字
        <img src="data:image/png;base64,{tcjia2_base64}" width="500">

        ---

        ###嘉義北門驛
        文字
        <img src="data:image/png;base64,{tcjia3_base64}" width="500">
        """,
        'images': ['tcjia1.jpg', 'tcjia2.jpg', 'tcjia3.jpg']
    },
    '嘉義-高雄': {
        'center': [22.999866, 120.148435],
        'color': "pink",
        'geojson_file': "jiayi_kaohsung.geojson",
        'csv_file': "play_jiakao.csv",
        'markdown': """
        ###嘉義縣科學教育中心-太空教育館
        文字
        <img src="data:image/png;base64,{jiakao1_base64}" width="500">

        ---

        ###臺南孔廟
        文字
        <img src="data:image/png;base64,{jiakao2_base64}" width="500">

        ---

        ###K.A.T 橋仔頭糖廠藝術村
        文字
        <img src="data:image/png;base64,{jiakao3_base64}" width="500">
        """,
        'images': ['jiakao1.jpg', 'jiakao2.jpg', 'jiakao3.jpg']
    },
    '高雄-屏東': {
        'center': [22.402317, 120.536198],
        'color': "yellow",
        'geojson_file': "kaohsung_pingtung.geojson",
        'csv_file': "play_kaoping.csv",
        'markdown': """
        ###龍虎塔
        文字
        <img src="data:image/png;base64,{kaoping1_base64}" width="500">

        ---

        ###大鵬灣國家風景區
        文字
        <img src="data:image/png;base64,{kaoping2_base64}" width="500">

        ---

        ###國立海洋生物博物館
        文字
        <img src="data:image/png;base64,{kaoping3_base64}" width="500">
        """,
        'images': ['kaoping1.jpg', 'kaoping2.jpg', 'kaoping3.jpg']
    },
    '屏東-台東': {
        'center': [22.781440, 120.834135],
        'color': "blue",
        'geojson_file': "pingtung_taitung.geojson",
        'csv_file': "play_pingtait.csv",
        'markdown': """
        ###壽卡鐵馬驛站
        文字
        <img src="data:image/png;base64,{pingtait1_base64}" width="500">

        ---

        ###多良車站
        文字
        <img src="data:image/png;base64,{pingtait2_base64}" width="500">

        ---

        ###國立臺灣史前文化博物館
        文字
        <img src="data:image/png;base64,{pingtait3_base64}" width="500">
        """,
        'images': ['pingtait1.jpg', 'pingtait2.jpg', 'pingtait3.jpg']
    },
    '台東-花蓮': {
        'center': [23.429920, 121.335207],
        'color': "grey",
        'geojson_file': "taitung_hualien.geojson",
        'csv_file': "play_taithua.csv",
        'markdown': """
        ###鹿野高台
        文字
        <img src="data:image/png;base64,{taithua1_base64}" width="500">

        ---

        ###臺東池上錦新三號道路 伯朗大道
        文字
        <img src="data:image/png;base64,{taithua2_base64}" width="500">
        """,
        'images': ['taithua1.jpg', 'taithua2.jpg']
    },
    '花蓮-宜蘭': {
        'center': [24.228917, 121.532195],
        'color': "black",
        'geojson_file': "hualien_yilan.geojson",
        'csv_file': "play_huayi.csv",
        'markdown': """
        ###鯉魚潭風景遊憩區
        文字
        <img src="data:image/png;base64,{huayi1_base64}" width="500">

        ---

        ###七星潭
        文字
        <img src="data:image/png;base64,{huayi2_base64}" width="500">

        ---

        ###清水斷崖
        文字
        <img src="data:image/png;base64,{huayi3_base64}" width="500">
        """,
        'images': ['huayi1.jpg', 'huayi2.jpg', 'huayi3.jpg']
    },
    '宜蘭-台北': {
        'center': [24.899394, 121.675311],
        'color': "green",
        'geojson_file': "yilan_taipei.geojson",
        'csv_file': "play_yitaip.csv",
        'markdown': """
        ###福隆舊草嶺隧道
        文字
        <img src="data:image/png;base64,{yitaip1_base64}" width="500">

        ---

        ###十分老街
        文字
        <img src="data:image/png;base64,{yitaip2_base64}" width="500">
        """,
        'images': ['yitaip1.jpg', 'yitaip2.jpg']
    }
}

# --- Main logic to display map and information ---

if option in road_segments:
    segment_info = road_segments[option]

    # Initialize map
    m = leafmap.Map(center=segment_info['center'], zoom=7, minimap_control=True)
    style = {"color": segment_info['color'], "weight": 3, "opacity": 0.8}

    # Add GeoJSON
    geojson_data = load_geojson(segment_info['geojson_file'])
    if geojson_data:
        m.add_geojson(geojson_data, layer_name=option, style=style)

    # Add points from CSV
    csv_path = os.path.join(PLAY_CSV_FOLDER, segment_info['csv_file'])
    if os.path.exists(csv_path):
        m.add_points_from_xy(csv_path, x="X", y="Y")
    else:
        st.error(f"CSV file not found: {csv_path}")

    # Display map
    m.to_streamlit(height=700)

    # Prepare markdown with images
    # Read image files and convert to base64 for embedding in markdown
    import base64

    image_placeholders = {}
    for img_file in segment_info['images']:
        img_path = os.path.join(PLAY_PNG_FOLDER, img_file)
        if os.path.exists(img_path):
            with open(img_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                # Create a placeholder name like {ts1_base64}
                placeholder_name = img_file.replace('.', '_') + '_base64'
                image_placeholders[placeholder_name] = encoded_string
        else:
            st.warning(f"Image file not found: {img_path}. Placeholder will be empty.")
            placeholder_name = img_file.replace('.', '_') + '_base64'
            image_placeholders[placeholder_name] = "" # Empty string if image not found

    # Format the markdown string with the base64 encoded images
    formatted_markdown = segment_info['markdown'].format(**image_placeholders)
    st.markdown(formatted_markdown, unsafe_allow_html=True)

else:
    st.write("請在第一頁選擇一個路段以顯示詳細資訊。")
