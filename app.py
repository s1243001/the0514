import streamlit as st
from datetime import date

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




st.title("選擇日期區間")


# 初始化 session_state
#if 'start_date' not in st.session_state:
#    st.session_state['start_date'] = date(2024, 1, 1)
#if 'end_date' not in st.session_state:
#    st.session_state['end_date'] = date.today()

st.session_state['start_date'] = date(2024, 1, 1)
st.session_state['end_date'] = date.today()


# 日期選擇器
start_date = st.date_input(label = "選擇起始日期", value = st.session_state['start_date'], min_value = date(2018, 1, 1), max_value = date.today())
end_date = st.date_input(label = "選擇結束日期", value = st.session_state['end_date'], min_value = start_date, max_value = date.today())

# 儲存使用者選擇
st.session_state['start_date'] = start_date
st.session_state['end_date'] = end_date

st.success(f"目前選擇的日期區間為：{start_date} 到 {end_date}")


st.title("利用擴充器示範")

with st.expander("展示gif檔"):
    st.image("2sfca1500m.jpg")

with st.expander("播放mp4檔"):
    video_file = open("2sfca1500m.jpg", "rb")  # "rb"指的是讀取二進位檔案（圖片、影片）
    video_bytes = video_file.read()
    st.video(video_bytes)
    
