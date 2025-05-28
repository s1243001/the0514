import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.title("路段上的補給站們")

# 檢查是否有日期資訊
if 'option' in st.session_state:
    # 讀取資料
    df = pd.read_csv("station.csv")

    # 取得篩選條件
    route_station = st.session_state['option']
    
    # 篩選
    station_df = df[df['路線'] == route_station]

    st.write(f"你在*上一頁*選擇的路段是：{route1}")
    st.header("這是你選擇路段的補給站")
    st.dataframe(station_df)

    m = leafmap.Map(center = [42.5, -4.0], zoom = 7 , minimap_control=True)
    style = {
        "color": "red",  # Outline color
        "weight": 3,      # Line thickness
        "opacity": 0.5,     # Line transparency
        "fillColor": "none" # No fill color
    }
    if option == '台北-新竹'
        m = leafmap.Map(center=[121.182838, 24.949132], zoom=7, minimap_control=True)
        style = {"color": "red", "weight": 3, "opacity": 0.8}
        m.add_geojson(t_s, layer_name="台北-新竹", style=style)
        A = "station_ts.csv"
        m.add_points_from_xy(data, x="X", y="Y")

    else if option == '新竹-台中'
            m = leafmap.Map(center=[120.740153, 24.462711], zoom=7, minimap_control=True)
            style = {"color": "orange", "weight": 3, "opacity": 0.8}
            m.add_geojson(s_tc, layer_name="新竹-台中", style=stlye)
            B = "station_stc.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '台中-嘉義'
            m = leafmap.Map(center=[120.292326, 23.809488], zoom=7, minimap_control=True)
            style = {"color": "purple", "weight": 3, "opacity": 0.8}
            m.add_geojson(tc_jia, layer_name="台中-嘉義", style=style)
            C = "station_tcjia.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '嘉義-高雄'
            m = leafmap.Map(center=[120.148435, 22.999866], zoom=7, minimap_control=True)
            style = {"color": "pink", "weight": 3, "opacity": 0.8}
            m.add_geojson(jia_kao, layer_name="嘉義-高雄", style=style)
            D = "station_jiakao.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '高雄-屏東'
            m = leafmap.Map(center=[120.536198, 22.402317], zoom=7, minimap_control=True)
            style = {"color": "yellow", "weight": 3, "opacity": 0.8}
            m.add_geojson(kao_ping, layer_name="高雄-屏東", style=style)
            E = "station_kaoping.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '屏東-台東'
            m = leafmap.Map(center=[120.834135, 22.781440], zoom=7, minimap_control=True)
            style = {"color": "blue", "weight": 3, "opacity": 0.8}
            m.add_geojson(ping_tait, layer_name="屏東-台東", style=syle)
            F = "station_pingtait.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '台東-花蓮'
            m = leafmap.Map(center=[121.335207, 23.429920], zoom=7, minimap_control=True)
            style = {"color": "grey", "weight": 3, "opacity": 0.8}
            m.add_geojson(tait_hua, layer_name="台東-花蓮", style=style)
            G = "station_taithua.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '花蓮-宜蘭'
            m = leafmap.Map(center=[121.532195, 24.228917], zoom=7, minimap_control=True)
            style = {"color": "black", "weight": 3, "opacity": 0.8}
            m.add_geojson(hua_yi, layer_name="花蓮-宜蘭", style=style)
            H = "station_huayi.csv"
            m.add_points_from_xy(data, x="X", y="Y")

    else if option == '宜蘭-台北'
            m = leafmap.Map(center=[121.675311, 24.899394], zoom=7, minimap_control=True)
            style = {"color": "green", "weight": 3, "opacity": 0.8}
            m.add_geojson(yilan_taip, layer_name="宜蘭-台北", style=style)
            I = "station_yitaip.csv"
            m.add_points_from_xy(data, x="X", y="Y")
    
    
else:
    st.warning("請先回上一頁選擇路段！")
