
import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.title("路段上的旅遊景點")

if option == '台北-新竹'
    m = leafmap.Map(center=[121.182838, 24.949132], zoom=7, minimap_control=True)
    style = {"color": "red", "weight": 3, "opacity": 0.8}
    m.add_geojson(t_s, layer_name="台北-新竹", style=style)
    data = "play_ts.csv"
    m.add_points_from_xy(data, x="X", y="Y")

else if option == '新竹-台中'
        m = leafmap.Map(center=[120.740153, 24.462711], zoom=7, minimap_control=True)
        style = {"color": "orange", "weight": 3, "opacity": 0.8}
        m.add_geojson(s_tc, layer_name="新竹-台中", style=stlye)
        data = "play_stc.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '台中-嘉義'
        m = leafmap.Map(center=[120.292326, 23.809488], zoom=7, minimap_control=True)
        style = {"color": "purple", "weight": 3, "opacity": 0.8}
        m.add_geojson(tc_jia, layer_name="台中-嘉義", style=style)
        data = "play_tcjia.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '嘉義-高雄'
        m = leafmap.Map(center=[120.148435, 22.999866], zoom=7, minimap_control=True)
        style = {"color": "pink", "weight": 3, "opacity": 0.8}
        m.add_geojson(jia_kao, layer_name="嘉義-高雄", style=style)
        data = "play_jiakao.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '高雄-屏東'
        m = leafmap.Map(center=[120.536198, 22.402317], zoom=7, minimap_control=True)
        style = {"color": "yellow", "weight": 3, "opacity": 0.8}
        m.add_geojson(kao_ping, layer_name="高雄-屏東", style=style)
        data = "play_kaoping.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '屏東-台東'
        m = leafmap.Map(center=[120.834135, 22.781440], zoom=7, minimap_control=True)
        style = {"color": "blue", "weight": 3, "opacity": 0.8}
        m.add_geojson(ping_tait, layer_name="屏東-台東", style=syle)
        data = "play_pingtait.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '台東-花蓮'
        m = leafmap.Map(center=[121.335207, 23.429920], zoom=7, minimap_control=True)
        style = {"color": "grey", "weight": 3, "opacity": 0.8}
        m.add_geojson(tait_hua, layer_name="台東-花蓮", style=style)
        data = "play_taithua.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '花蓮-宜蘭'
        m = leafmap.Map(center=[121.532195, 24.228917], zoom=7, minimap_control=True)
        style = {"color": "black", "weight": 3, "opacity": 0.8}
        m.add_geojson(hua_yi, layer_name="花蓮-宜蘭", style=style)
        data = "play_huayi.csv"
        m.add_points_from_xy(data, x="X", y="Y")

else if option == '宜蘭-台北'
        m = leafmap.Map(center=[121.675311, 24.899394], zoom=7, minimap_control=True)
        style = {"color": "green", "weight": 3, "opacity": 0.8}
        m.add_geojson(yilan_taip, layer_name="宜蘭-台北", style=style)
        data = "play_yitaip.csv"
        m.add_points_from_xy(data, x="X", y="Y")

m.to_streamlit(height=700)
