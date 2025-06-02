
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
    markdown = """
    ###大溪老街
    
        文字
        <ts1.jpg>
        
        ---

    ###新竹17公里海岸風景區

       文字
       <ts2.jpg>
    """
    st.markdown(markdown, unsafe_allow_html=True)

else if option == '新竹-台中'
        m = leafmap.Map(center=[120.740153, 24.462711], zoom=7, minimap_control=True)
        style = {"color": "orange", "weight": 3, "opacity": 0.8}
        m.add_geojson(s_tc, layer_name="新竹-台中", style=stlye)
        data = "play_stc.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###白沙屯拱天宮
    
        文字
        <stc1.jpg>
        
        ---

        ###大甲鎮瀾宮

        文字
        <stc2.jpg>

        ---

        ###國立自然科學博物館

        文字
        <stc3.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)


else if option == '台中-嘉義'
        m = leafmap.Map(center=[120.292326, 23.809488], zoom=7, minimap_control=True)
        style = {"color": "purple", "weight": 3, "opacity": 0.8}
        m.add_geojson(tc_jia, layer_name="台中-嘉義", style=style)
        data = "play_tcjia.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###八卦山大佛風景區
    
        文字
        <tcjia1.jpg>
        
        ---

        ###員林神社鳥居

        文字
        <tcjia2.jpg>

        ---

        ###嘉義北門驛

        文字
        <tcjia3.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

else if option == '嘉義-高雄'
        m = leafmap.Map(center=[120.148435, 22.999866], zoom=7, minimap_control=True)
        style = {"color": "pink", "weight": 3, "opacity": 0.8}
        m.add_geojson(jia_kao, layer_name="嘉義-高雄", style=style)
        data = "play_jiakao.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###嘉義縣科學教育中心-太空教育館
    
        文字
        <jiakao1.jpg>
        
        ---

        ###臺南孔廟

        文字
        <jiakao2.jpg>

        ---

        ###K.A.T 橋仔頭糖廠藝術村

        文字
        <jiakao3.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

else if option == '高雄-屏東'
        m = leafmap.Map(center=[120.536198, 22.402317], zoom=7, minimap_control=True)
        style = {"color": "yellow", "weight": 3, "opacity": 0.8}
        m.add_geojson(kao_ping, layer_name="高雄-屏東", style=style)
        data = "play_kaoping.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###龍虎塔
    
        文字
        <kaoping1.jpg>
        
        ---

        ###大鵬灣國家風景區

        文字
        <kaoping2.jpg>

        ---

        ###國立海洋生物博物館

        文字
        <kaoping3.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

else if option == '屏東-台東'
        m = leafmap.Map(center=[120.834135, 22.781440], zoom=7, minimap_control=True)
        style = {"color": "blue", "weight": 3, "opacity": 0.8}
        m.add_geojson(ping_tait, layer_name="屏東-台東", style=syle)
        data = "play_pingtait.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###壽卡鐵馬驛站
    
        文字
        <pingtait1.jpg>
        
        ---

        ###多良車站

        文字
        <pingtait2.jpg>

        ---

        ###國立臺灣史前文化博物館

        文字
        <pingtait3.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

else if option == '台東-花蓮'
        m = leafmap.Map(center=[121.335207, 23.429920], zoom=7, minimap_control=True)
        style = {"color": "grey", "weight": 3, "opacity": 0.8}
        m.add_geojson(tait_hua, layer_name="台東-花蓮", style=style)
        data = "play_taithua.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###鹿野高台
    
        文字
        <taithua1.jpg>
        
        ---

        ###臺東池上錦新三號道路 伯朗大道

        文字
        <taithua2.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

else if option == '花蓮-宜蘭'
        m = leafmap.Map(center=[121.532195, 24.228917], zoom=7, minimap_control=True)
        style = {"color": "black", "weight": 3, "opacity": 0.8}
        m.add_geojson(hua_yi, layer_name="花蓮-宜蘭", style=style)
        data = "play_huayi.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###鯉魚潭風景遊憩區
    
        文字
        <huayi1.jpg>
        
        ---

        ###七星潭

        文字
        <huayi2.jpg>

        ---

        ###清水斷崖

        文字
        <huayi3.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

else if option == '宜蘭-台北'
        m = leafmap.Map(center=[121.675311, 24.899394], zoom=7, minimap_control=True)
        style = {"color": "green", "weight": 3, "opacity": 0.8}
        m.add_geojson(yilan_taip, layer_name="宜蘭-台北", style=style)
        data = "play_yitaip.csv"
        m.add_points_from_xy(data, x="X", y="Y")
        markdown = """
        ###福隆舊草嶺隧道
    
        文字
        <yitaip1.jpg>
        
        ---

        ###十分老街

        文字
        <yitaip2.jpg>
        """
        st.markdown(markdown, unsafe_allow_html=True)

m.to_streamlit(height=700)
