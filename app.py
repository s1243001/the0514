import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide", page_title="自行車環島Go！Go！")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io), [GEE](https://earthengine.google.com/), 
    [geemap](https://leafmap.org) and [leafmap](https://leafmap.org). 
    """
)

st.header("Instructions")

markdown = """
1. You can use it as a template for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python file.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)




m = leafmap.Map(center = [42.5, -4.0], zoom = 7 , minimap_control=True)
style = {
    "color": "red",  # Outline color
    "weight": 1.5,      # Line thickness
    "opacity": 0.5,     # Line transparency
    "fillColor": "none" # No fill color
}
route1 = "route1.geojson"
m.add_geojson(route1, layer_name="route1",style=style)
m.to_streamlit(height=700)

option = st.selectbox(
    '選擇你的路線',
    ['台北-新竹','新竹-台中','台中-嘉義','嘉義-高雄','高雄-屏東','屏東-台東','台東-花蓮','花蓮-宜蘭','宜蘭-台北'])
st.text(f'你的答案：{option}')

with st.expander("展示gif檔"):
    st.image("2sfca1500m.jpg")

with st.expander("播放mp4檔"):
    video_file = open("2sfca1500m.jpg", "rb")  # "rb"指的是讀取二進位檔案（圖片、影片）
    video_bytes = video_file.read()
    st.video(video_bytes)
    
