import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.title("路段上的旅遊景點")

if option == '台北-新竹'
    m = leafmap.Map(center=[121.182838, 24.949132], zoom=7, minimap_control=True)
    style = {"color": "red", "weight": 3, "opacity": 0.8}
    m.add_geojson(t_s, layer_name="台北-新竹", style=style)
    food1 = "food_ts.csv"
    m.add_points_from_xy(food1, x="X", y="Y")
    st.markdown("""
        ###游記百年油飯

        文字
        
        <img == "food_ts1">

        ---

        ###關西牛肉捲餅

        文字

        <img == "food_ts2">

        ---

        ###廟口鴨香飯

        文字

        <img == "food_ts3">
        """)

else if option == '新竹-台中'
        m = leafmap.Map(center=[120.740153, 24.462711], zoom=7, minimap_control=True)
        style = {"color": "orange", "weight": 3, "opacity": 0.8}
        m.add_geojson(s_tc, layer_name="新竹-台中", style=stlye)
        food2 = "food_stc.csv"
        m.add_points_from_xy(food2, x="X", y="Y")
        st.markdown("""
        ###（東北香粑粑）白沙屯美食

        文字
        
        <img == "food_stc1">

        ---

        ###一品香水煎包專賣店

        文字

        <img == "food_stc2">

        ---

        ###南瓜屋魔女露露的廚房

        文字

        <img == "food_stc3">
        """)

else if option == '台中-嘉義'
        m = leafmap.Map(center=[120.292326, 23.809488], zoom=7, minimap_control=True)
        style = {"color": "purple", "weight": 3, "opacity": 0.8}
        m.add_geojson(tc_jia, layer_name="台中-嘉義", style=style)
        food3 = "food_tcjia.csv"
        m.add_points_from_xy(food3, x="X", y="Y")
        st.markdown("""
        ###阿添蛤仔麵

        文字
        
        <img == "food_tcjia1">

        ---

        ###西螺 脆皮臭豆腐

        文字

        <img == "food_tcjia2">

        ---

        ###民主火雞肉飯

        文字

        <img == "food_tcjia3">
        """)

else if option == '嘉義-高雄'
        m = leafmap.Map(center=[120.148435, 22.999866], zoom=7, minimap_control=True)
        style = {"color": "pink", "weight": 3, "opacity": 0.8}
        m.add_geojson(jia_kao, layer_name="嘉義-高雄", style=style)
        food4 = "food_jiakao.csv"
        m.add_points_from_xy(food4, x="X", y="Y")
        st.markdown("""
        ###味泰豐香雞排

        文字
        
        <img == "food_jiakao1">

        ---

        ###城邊真味鱔魚意麵

        文字

        <img == "food_jiakao2">

        ---

        ###Temperature Studio/溫度劑

        文字

        <img == "food_jiakao3">
        """)

else if option == '高雄-屏東'
        m = leafmap.Map(center=[120.536198, 22.402317], zoom=7, minimap_control=True)
        style = {"color": "yellow", "weight": 3, "opacity": 0.8}
        m.add_geojson(kao_ping, layer_name="高雄-屏東", style=style)
        food5 = "food_kaoping.csv"
        m.add_points_from_xy(food5, x="X", y="Y")
        st.markdown("""
        ###仁武烤鴨

        文字
        
        <img == "food_kaoping1">

        ---

        ###北港蔡三代筒仔米糕

        文字

        <img == "food_kaoping2">

        ---

        ###王匠黑鮪魚生魚片&日本料理

        文字

        <img == "food_kaoping3">
        """)

else if option == '屏東-台東'
        m = leafmap.Map(center=[120.834135, 22.781440], zoom=7, minimap_control=True)
        style = {"color": "blue", "weight": 3, "opacity": 0.8}
        m.add_geojson(ping_tait, layer_name="屏東-台東", style=syle)
        food6 = "food_pingtait.csv"
        m.add_points_from_xy(food6, x="X", y="Y")
        st.markdown("""
        ###卑南豬血湯 侯記老店

        文字
        
        <img == "food_pingtait1">

        ---

        ###某一家

        文字

        <img == "food_pingtait2">
        """)

else if option == '台東-花蓮'
        m = leafmap.Map(center=[121.335207, 23.429920], zoom=7, minimap_control=True)
        style = {"color": "grey", "weight": 3, "opacity": 0.8}
        m.add_geojson(tait_hua, layer_name="台東-花蓮", style=style)
        food7 = "food_taithua.csv"
        m.add_points_from_xy(food7, x="X", y="Y")
        st.markdown("""
        ###全美行

        文字
        
        <img == "food_taithua1">

        ---

        ###某一家

        文字

        <img == "food_taithua2">
        """)


else if option == '花蓮-宜蘭'
        m = leafmap.Map(center=[121.532195, 24.228917], zoom=7, minimap_control=True)
        style = {"color": "black", "weight": 3, "opacity": 0.8}
        m.add_geojson(hua_yi, layer_name="花蓮-宜蘭", style=style)
        food8 = "food_huayi.csv"
        m.add_points_from_xy(food8, x="X", y="Y")
        st.markdown("""
        ###液香扁食

        文字
        
        <img == "food_huayi1">

        ---

        ###羅東碳烤燒餅餅店

        文字

        <img == "food_huayi2">
        """)

else if option == '宜蘭-台北'
        m = leafmap.Map(center=[121.675311, 24.899394], zoom=7, minimap_control=True)
        style = {"color": "green", "weight": 3, "opacity": 0.8}
        m.add_geojson(yilan_taip, layer_name="宜蘭-台北", style=style)
        food9 = "food_yitaip.csv"
        m.add_points_from_xy(food9, x="X", y="Y")
        st.markdown("""
        ###十分溜哥燒烤雞翅包飯

        文字
        
        <img == "food_yitaip1">

        ---

        ###羅東碳烤燒餅餅店

        文字

        <img == "food_yitaip2">
        """)


m.to_streamlit(height=700)
