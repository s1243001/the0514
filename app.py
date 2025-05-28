import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide", page_title="自行車環島Go！Go！")

st.title("歡迎來到台灣自行車環島旅行指南")
st.markdown(
    """
    自行車環島是被喻為台灣人一定要做的三件事其中之一；環島顧名思義就是繞台灣一圈，其路線五花八門、可長可短，因此選用最熱門的環島路線「環1」作為例子。這條路線起點為台北市的松山車站，途中經過埤塘、鄉村，穿越山脈以及河谷既是一場身心挑戰，也是文化與自然的體驗。今天，無論是出於對達成身為台灣人的成就，還是文化探索或運動等目的，都能在名為「環1」的這條道路上，看到許多人踏上這段富有意義的旅程，感受台灣各個地方的美麗之處。
    """
)

st.header("Instructions")

markdown = """
1. 選擇你的環島路段
2. 查看你路線上的補給站
3. 推薦的景點介紹
4. 推薦的美食餐廳
"""

st.markdown(markdown)

st.header("自行車環島一號線路線圖")

m = leafmap.Map(center = [42.5, -4.0], zoom = 7 , minimap_control=True)
style = {
    "color": "red",  # Outline color
    "weight": 3,      # Line thickness
    "opacity": 0.5,     # Line transparency
    "fillColor": "none" # No fill color
}
route1 = "route1.geojson"
m.add_geojson(route1, layer_name="route1",style=style)
m.to_streamlit(height=700)
    
