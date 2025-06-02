import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import os
import base64 # Import base64 here, as it's used within the main logic

st.title("路段上的旅遊景點")

# Assuming 'option' is passed from the first page, e.g., via st.session_state
# For demonstration purposes, if 'option' is not yet set, default it to '台北-新竹'
if 'option' not in st.session_state:
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
        <img src="data
