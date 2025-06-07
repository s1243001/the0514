import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
National Changhua University of Education
<https://www.ncue.edu.tw/>
"""

st.sidebar.title("About Our From")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("🫂關於我們的網站")


markdown = """
感謝您使用台灣自行車環島一號線旅遊網！<br>  
抱歉由於期末時間緊迫，目前尚未實現更多語言選項及其他功能<br>  
如果您在環島的旅途中，發現令人印象深刻的景色或是山珍海味，歡迎將美食店家與景點資訊分享給我們<br>  
您的建議有助於我們在日後更新中提供更好的使用者體驗<br>  

---

**享受台灣自行車旅行的美好，祝你有個難忘的旅程！**

---
"""
st.markdown(markdown, unsafe_allow_html=True)

st.title("☎️ 聯絡資訊")
markdown2 = """📧 **Email**  
- Wu: [apord67@gmail.com](mailto:apord67@gmail.com)  
- Wang: [wang940125@gmail.com](mailto:wang940125@gmail.com)  


🌍 **Resources**  
- Streamlit Map Template: [GitHub Repository](https://github.com/s1243001/the0514/tree/main)
- 台灣騎跡全國自行車單一總入口網: [website](https://taiwanbike.tw/bikeRoute/search)
- 交通部觀光署環島旅遊指南: [website](https://www.taiwan.net.tw/att/files/%E8%87%AA%E8%A1%8C%E8%BB%8A%E7%92%B0%E5%B3%B6%E6%8C%87%E5%8D%97.pdf)
- Attraction & Food Recommendation: (景點、食物參考網站以至於介紹後方)

---

<span style="color: grey;">最近更新日期: 2025/06/07 上午12:00</span>



"""

st.markdown(markdown2, unsafe_allow_html=True)



