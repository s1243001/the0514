import streamlit as st
import ee
from google.oauth2 import service_account
import geemap.foliumap as geemap

# 從 Streamlit Secrets 讀取 GEE 服務帳戶金鑰 JSON
service_account_info = st.secrets["GEE_SERVICE_ACCOUNT"]

# 使用 google-auth 進行 GEE 授權
credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=["https://www.googleapis.com/auth/earthengine"]
)

# 初始化 GEE
ee.Initialize(credentials)


###############################################
st.set_page_config(layout="wide")
st.title("🌍 使用服務帳戶連接 GEE 的 Streamlit App")


my_Map = geemap.Map()
my_point = ee.Geometry.Point([120.5583462887228, 24.081653403304525])
my_image = (
    ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
    .filterBounds(my_point)
    .filterDate('2021-01-01', '2022-01-01')
    .sort('CLOUDY_PIXEL_PERCENTAGE')
    .first()
    .select('B.*')
)

vis_params = {'min': 100, 'max': 3500, 'bands': ['B8', 'B4', 'B3']}




training001 = my_image.sample(
    **{
        'region': my_image.geometry(),  # 若不指定，則預設為影像my_image的幾何範圍。
        'scale': 30,
        'numPixels': 5000,
        'seed': 0,
        'geometries': True,  # 設為False表示取樣輸出的點將忽略其幾何屬性(即所屬網格的中心點)，無法作為圖層顯示，可節省記憶體。
    }
)




n_clusters = 10
clusterer_KMeans = ee.Clusterer.wekaKMeans(nClusters=n_clusters).train(training001)


result001 = my_image.cluster(clusterer_KMeans)

legend_dict2 = {
    'zero': '#ab0000',
    'one': '#1c5f2c',
    'two': '#d99282',
    'three': '#466b9f',
    'four': '#ab6c28',
    'five': '#3cb371',
    'six': '#ffff00',
    'seven':'#d8bfd8'
}
palette = list(legend_dict2.values())
vis_params_002 = {'min': 0, 'max': 7, 'palette': palette}




my_Map = geemap.Map(center=[24.081653403304525, 120.5583462887228], zoom=10)

left_layer = geemap.ee_tile_layer(my_Image.randomVisualizer(), {}, 'original land cover')
right_layer = geemap.ee_tile_layer(result001.randomVisualizer(), {}, 'wekaKMeans classified land cover')


my_Map.split_map(left_layer, right_layer)
my_Map.add_legend(title='Land Cover Type', legend_dict=legend_dict2, position='bottomright')


my_Map.to_streamlit(height=600)
