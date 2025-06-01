import streamlit as st
import leafmap.foliumap as leafmap

st.title("選擇你的路段")

# 定義所有路段
sections = [
    '台北-新竹', '新竹-台中', '台中-嘉義', '嘉義-高雄',
    '高雄-屏東', '屏東-台東', '台東-花蓮', '花蓮-宜蘭', '宜蘭-台北'
]

# 定義每個路段的 GeoJSON 檔案名、中心點和圖片路徑
# 如果沒有圖片，可以將 'image_path' 設為 None 或不包含該鍵
section_data = {
    '台北-新竹': {'geojson': "taipei_hsinchu.geojson", 'center': [24.949132, 121.182838], 'image': 'taiphsin_ele.png'},
    '新竹-台中': {'geojson': "hsinchu_taichung.geojson", 'center': [24.462711, 120.740153], 'image': 'hsintaic_ele.png'},
    '台中-嘉義': {'geojson': "taichung_jiayi.geojson", 'center': [23.809488, 120.292326], 'image': 'taicjia_ele.png'},
    '嘉義-高雄': {'geojson': "jiayi_kaohsung.geojson", 'center': [22.999866, 120.148435], 'image': 'jiakao_ele.png'},
    '高雄-屏東': {'geojson': "kaohsung_pingtung.geojson", 'center': [22.402317, 120.536198], 'image': 'kaoping_ele.png'},
    '屏東-台東': {'geojson': "pingtung_taitung.geojson", 'center': [22.781440, 120.834135], 'image': 'pingtait_ele.png'},
    '台東-花蓮': {'geojson': "taitung_huaien.geojson", 'center': [23.429920, 121.335207], 'image': 'taithua_ele.png'},
    '花蓮-宜蘭': {'geojson': "hualien_yilan.geojson", 'center': [24.228917, 121.532195], 'image': 'huayi_ele.png'},
    '宜蘭-台北': {'geojson': "yilan_taipei.geojson", 'center': [24.899394, 121.675311], 'image': 'yitaip_ele.png'},
}

option = st.selectbox(
    '選擇你的路段',
    sections
)
st.write(f'你選擇的路段：**{option}**') # 使用 st.write 更彈性，且能顯示 Markdown

# 定義 GeoJSON 路線的樣式
style = {
    "color": "red",      # 路線顏色
    "weight": 3,         # 路線粗細
    "opacity": 0.7,      # 路線透明度
    "fillColor": "none"  # 無填充色
}

# 根據選擇的路段顯示圖片和地圖
if option in section_data:
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
    m = leafmap.Map(center=center_coords, zoom=9, minimap_control=True) # 將 zoom 調高一些，更清楚地圖

    # 添加 GeoJSON 路線
    try:
        m.add_geojson(geojson_file, layer_name=option, style=style)
    except FileNotFoundError:
        st.error(f"找不到 '{geojson_file}' 這個 GeoJSON 檔案，請確認檔案是否存在。")
        st.info("請確認 GeoJSON 檔案與 Streamlit 腳本位於相同目錄，或提供正確的路徑。")

    # 顯示地圖
    m.to_streamlit(height=700)
else:
    st.info("請從上方下拉選單中選擇一個路段來顯示其地圖和資訊。")
