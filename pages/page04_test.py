import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np
import os # 導入 os 模組用於路徑操作

st.title("路段上的美食")

# 定義檔案夾的路徑
FOOD_CSV_DIR = "food_csv"
FOOD_PNG_DIR = "food_png"

# 假設 'option' 變數在 Streamlit 應用程式的其他地方定義，例如透過 st.selectbox
# 這裡為了示範，我們定義一個 'option' 的佔位符
# 你應該用你應用程式中實際設定 'option' 變數的方式來替換這裡。
option = st.selectbox(
    "選擇一個旅遊路線",
    (
        "台北-新竹",
        "新竹-台中",
        "台中-嘉義",
        "嘉義-高雄",
        "高雄-屏東",
        "屏東-台東",
        "台東-花蓮",
        "花蓮-宜蘭",
        "宜蘭-台北",
    ),
)


# --- 第四頁的邏輯 (與你現有的結構相似) ---

if option == "台北-新竹":
    m = leafmap.Map(center=[121.182838, 24.949132], zoom=7, minimap_control=True)
    style = {"color": "red", "weight": 3, "opacity": 0.8}
    m.add_geojson(t_s, layer_name="台北-新竹", style=style)
    # 使用 os.path.join 組合 CSV 檔案的路徑
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_ts.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###游記百年油飯")
    st.write("文字")
    # 使用 st.image 顯示圖片，並使用 os.path.join 組合圖片的路徑
    st.image(os.path.join(FOOD_PNG_DIR, "food_ts1.jpg"))
    st.markdown("---")
    st.markdown("###關西牛肉捲餅")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_ts2.jpg"))
    st.markdown("---")
    st.markdown("###廟口鴨香飯")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_ts3.jpg"))


elif option == "新竹-台中":
    m = leafmap.Map(center=[120.740153, 24.462711], zoom=7, minimap_control=True)
    style = {"color": "orange", "weight": 3, "opacity": 0.8}
    # 修正 'stlye' 為 'style'
    m.add_geojson(s_tc, layer_name="新竹-台中", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_stc.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###（東北香粑粑）白沙屯美食")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_stc1.jpg"))
    st.markdown("---")
    st.markdown("###一品香水煎包專賣店")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_stc2.jpg"))
    st.markdown("---")
    st.markdown("###南瓜屋魔女露露的廚房")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_stc3.jpg"))


elif option == "台中-嘉義":
    m = leafmap.Map(center=[120.292326, 23.809488], zoom=7, minimap_control=True)
    style = {"color": "purple", "weight": 3, "opacity": 0.8}
    m.add_geojson(tc_jia, layer_name="台中-嘉義", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_tcjia.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###阿添蛤仔麵")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_tcjia1.jpg"))
    st.markdown("---")
    st.markdown("###西螺 脆皮臭豆腐")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_tcjia2.jpg"))
    st.markdown("---")
    st.markdown("###民主火雞肉飯")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_tcjia3.jpg"))


elif option == "嘉義-高雄":
    m = leafmap.Map(center=[120.148435, 22.999866], zoom=7, minimap_control=True)
    style = {"color": "pink", "weight": 3, "opacity": 0.8}
    m.add_geojson(jia_kao, layer_name="嘉義-高雄", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_jiakao.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###味泰豐香雞排")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_jiakao1.jpg"))
    st.markdown("---")
    st.markdown("###城邊真味鱔魚意麵")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_jiakao2.jpg"))
    st.markdown("---")
    st.markdown("###Temperature Studio/溫度劑")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_jiakao3.jpg"))


elif option == "高雄-屏東":
    m = leafmap.Map(center=[120.536198, 22.402317], zoom=7, minimap_control=True)
    style = {"color": "yellow", "weight": 3, "opacity": 0.8}
    m.add_geojson(kao_ping, layer_name="高雄-屏東", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_kaoping.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###仁武烤鴨")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_kaoping1.jpg"))
    st.markdown("---")
    st.markdown("###北港蔡三代筒仔米糕")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_kaoping2.jpg"))
    st.markdown("---")
    st.markdown("###王匠黑鮪魚生魚片&日本料理")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_kaoping3.jpg"))


elif option == "屏東-台東":
    m = leafmap.Map(center=[120.834135, 22.781440], zoom=7, minimap_control=True)
    style = {"color": "blue", "weight": 3, "opacity": 0.8}
    # 修正 'syle' 為 'style'
    m.add_geojson(ping_tait, layer_name="屏東-台東", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_pingtait.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###卑南豬血湯 侯記老店")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_pingtait1.jpg"))
    st.markdown("---")
    st.markdown("###某一家")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_pingtait2.jpg"))


elif option == "台東-花蓮":
    m = leafmap.Map(center=[121.335207, 23.429920], zoom=7, minimap_control=True)
    style = {"color": "grey", "weight": 3, "opacity": 0.8}
    m.add_geojson(tait_hua, layer_name="台東-花蓮", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_taithua.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###全美行")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_taithua1.jpg"))
    st.markdown("---")
    st.markdown("###某一家")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_taithua2.jpg"))


elif option == "花蓮-宜蘭":
    m = leafmap.Map(center=[121.532195, 24.228917], zoom=7, minimap_control=True)
    style = {"color": "black", "weight": 3, "opacity": 0.8}
    m.add_geojson(hua_yi, layer_name="花蓮-宜蘭", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_huayi.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###液香扁食")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_huayi1.jpg"))
    st.markdown("---")
    st.markdown("###羅東碳烤燒餅餅店")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_huayi2.jpg"))


elif option == "宜蘭-台北":
    m = leafmap.Map(center=[121.675311, 24.899394], zoom=7, minimap_control=True)
    style = {"color": "green", "weight": 3, "opacity": 0.8}
    m.add_geojson(yilan_taip, layer_name="宜蘭-台北", style=style)
    food_csv_path = os.path.join(FOOD_CSV_DIR, "food_yitaip.csv")
    m.add_points_from_xy(food_csv_path, x="X", y="Y")
    st.markdown("###十分溜哥燒烤雞翅包飯")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_yitaip1.jpg"))
    st.markdown("---")
    st.markdown("###羅東碳烤燒餅餅店")
    st.write("文字")
    st.image(os.path.join(FOOD_PNG_DIR, "food_yitaip2.jpg"))


# 顯示地圖
m.to_streamlit(height=700)
