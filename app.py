import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide", page_title="自行車環島Go！Go！")

st.title("歡迎來到台灣自行車環島旅行指南")
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
    
