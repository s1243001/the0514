# page01_test.py (你的第一頁)

import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(
    page_title="選擇你的環島路段🛣️/看看路線起伏⛰️",
    page_icon="🗺️",
    layout="wide"
)

st.title("選擇你的路段")

# 定義所有路段的 GeoJSON 檔案名、中心點和圖片路徑
# 注意：這裡的中心點座標是 [緯度, 經度]
section_data = {
    '台北-新竹': {'geojson': "geojson/taipei_hsinchu.geojson", 'center': [24.949132, 121.182838], 'image': 'taihsin_ele.png'},
    '新竹-台中': {'geojson': "geojson/hsinchu_taichung.geojson", 'center': [24.462711, 120.740153], 'image': 'hsintaic_ele.png'},
    '台中-嘉義': {'geojson': "geojson/taichung_jiayi.geojson", 'center': [23.809488, 120.292326], 'image': 'taicjia_ele.png'},
    '嘉義-高雄': {'geojson': "geojson/jiayi_kaohsung.geojson", 'center': [22.999866, 120.148435], 'image': 'jiakao_ele.png'},
    '高雄-屏東': {'geojson': "geojson/kaohsung_pingtung.geojson", 'center': [22.402317, 120.536198], 'image': 'kaoping_ele.png'},
    '屏東-台東': {'geojson': "geojson/pingtung_taitung.geojson", 'center': [22.781440, 120.834135], 'image': 'pingtait_ele.png'},
    '台東-花蓮': {'geojson': "geojson/taitung_huaien.geojson", 'center': [23.429920, 121.335207], 'image': 'taithua_ele.png'},
    '花蓮-宜蘭': {'geojson': "geojson/hualien_yilan.geojson", 'center': [24.228917, 121.532195], 'image': 'huayi_ele.png'},
    '宜蘭-台北': {'geojson': "geojson/yilan_taipei.geojson", 'center': [24.899394, 121.675311], 'image': 'yitaip_ele.png'},
}

# 從字典中獲取路段列表
sections = list(section_data.keys())

# 下拉選單讓使用者選擇路段
option = st.selectbox(
    '選擇你的路段',
    sections
)
st.write(f'你選擇的路段：**{option}**')

# 定義 GeoJSON 路線的預設樣式
route_style = {
    "color": "red",
    "weight": 3,
    "opacity": 0.7,
    "fillColor": "none"
}

# 根據選擇的路段顯示圖片和地圖
if option: # 確保有選擇的路段
    data = section_data[option]
    geojson_file = data['geojson']
    center_coords = data['center']
    image_path = data.get('image') # 使用 .get() 避免沒有 'image' 鍵時報錯

    # 顯示圖片 (如果存在)
    if image_path:
        try:
            st.image(image_path, caption=f'{option} 路段示意圖', use_container_width=True)
        except FileNotFoundError:
            st.warning(f"找不到 '{image_path}' 這張圖片，請確認檔案是否存在。")

    # 創建 Leafmap 地圖
    m = leafmap.Map(center=center_coords, zoom=9, minimap_control=True)

    # 添加 GeoJSON 路線
    try:
        m.add_geojson(geojson_file, layer_name=option, style=route_style)
    except FileNotFoundError:
        st.error(f"找不到 '{geojson_file}' 這個 GeoJSON 檔案，請確認檔案是否存在。")
        st.info("請確認 GeoJSON 檔案位於 'geojson/' 子目錄中，或提供正確的路徑。")

    # 顯示地圖
    m.to_streamlit(height=700)

    # 將選擇的路段儲存到 session_state，以便第二頁讀取
    st.session_state['selected_route'] = option

    # 添加一個按鈕導航到第二頁
    st.markdown("---")
    st.write("想看看這個路段的補給站嗎？")
    if st.button("查看補給站地圖"):
        # ***關鍵修改點：導航到 "pages/Station_Map"***
        st.switch_page("pages/Station_Map") # 注意：不需要 .py 副檔名
else:
    st.info("請從上方下拉選單中選擇一個路段來顯示其地圖和資訊。")
