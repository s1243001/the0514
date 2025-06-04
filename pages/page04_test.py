import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import os
import base64 # Import base64 for image embedding

st.title(" 推薦的美食餐廳🍝")

# 從 session_state 讀取使用者選擇的路段
if 'selected_route' not in st.session_state:
    st.warning("請先回到第一頁選擇路段。")
    st.stop() # 如果沒有選擇路段，就停止程式執行

option = st.session_state['selected_route']

# Define base paths for your data and images
FOOD_CSV_FOLDER = "food_csv"
FOOD_PNG_FOLDER = "food_png"
GEOJSON_FOLDER = "." # Assuming geojson files are in the root directory or adjust as needed

# Function to load geojson (assuming they are in the root or a specified folder)
def load_geojson(filename):
    geojson_path = os.path.join(GEOJSON_FOLDER, filename)
    if os.path.exists(geojson_path):
        with open(geojson_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        st.error(f"GeoJSON file not found: {geojson_path}")
        return None

# Dictionary to hold road segment data for cleaner code (similar to page 3)
food_segments = {
    '台北-新竹': {
        'center': [24.949132, 121.182838], # Corrected lat/lon order
        'color': "red",
        'geojson_file': "taipei_hsinchu.geojson",
        'csv_file': "food_ts.csv",
        'markdown': """
        ###游記百年油飯
        
        「百年油飯」是整間店的精神、也是最為招牌的菜式，食材首選桃園在地圓糯米、嚴選香菇、臺灣溫體黑豬後腿肉、臺灣紅蔥頭、嚴選蝦米及蝦皮，加入自家熬製的雞油，糯米以杉木桶蒸熟帶出淡淡木香，再與其他食材一同用小火拌炒至收汁，米粒鹹香油潤、口感Q糯，推薦搭配秘製甜辣醬食用，香氣十足。
        https://today.line.me/tw/v2/article/gzv9Mjm

        <img src="data:image/png;base64,{food_ts1_base64}" width="500">

        ---

        ###關西牛肉捲餅
        
        「關西牛肉捲餅」是位於關西老街上的老字號小吃，手工現擀的餅皮吃起來特別酥脆，牛肉捲餅還加了滿滿滿的九層塔，香氣十足，捲餅裡面加了小黃瓜絲、九層塔、牛肉片、雞蛋，牛肉有事先醃漬過，吃起來有點偏鹹，用料還滿豐富的，而且分量很足，光吃１份就很有飽足感。
        https://supertaste.tvbs.com.tw/pack/345194

        <img src="data:image/png;base64,{food_ts2_base64}" width="500">

        ---

        ###廟口鴨香飯
        
        曾被許多知名美食節目報導，因此在用餐時段永遠大排長龍。鴨油淋得誠意十足，每口飯吃來香氣滿溢；經過燻烤的鴨肉讓香氣更上層樓。
        https://bobbyworld.tw/2024-01-01-2606/

        <img src="data:image/png;base64,{food_ts3_base64}" width="500">
        """,
        'images': ['food_ts1.jpg', 'food_ts2.jpg', 'food_ts3.jpg']
    },
    '新竹-台中': {
        'center': [24.462711, 120.740153],
        'color': "red", # Changed color for variety
        'geojson_file': "hsinchu_taichung.geojson",
        'csv_file': "food_stc.csv",
        'markdown': """
        ###（東北香粑粑）白沙屯美食
        
        東北香粑粑地點位於白沙屯拱天宮正後方、香客餐廳文物大樓旁的空地，是排隊的炸物點心攤，東北香粑粑的內餡以里肌肉、香蔥為主，外皮薄而酥脆，吃起來的味道也豐富且多汁，另外加上店家自行製作的辣醬，整體吃起來更加分。
        https://www.walkerland.com.tw/article/view/278481

        <img src="data:image/png;base64,{food_stc1_base64}" width="500">

        ---

        ###一品香水煎包專賣店
        
        一品香水煎包是知名的大甲小吃，首先是招牌的水煎包，外皮薄Q帶嚼勁，飽滿的瓠瓜內餡水嫩有口感，調味剛好不過重；再來是豬肉餡餅，外皮金黃微脆酥香，一口咬下內餡湯汁直接流出來，咀嚼中有淡淡的甜味與香氣；最後是韭菜包，同樣是薄脆帶Q的外皮，餡料主要為韭菜冬粉，韭菜口感鮮脆，微帶酥香的口感非常討喜。
        https://lyes.tw/33212128-%E4%B8%80%E5%93%81%E9%A6%99%E6%B0%B4%E7%85%8E%E5%8C%85/

        <img src="data:image/png;base64,{food_stc2_base64}" width="500">

        ---

        ###發愣吃VARMT - 勤美店
        
        這間店的人氣招牌「發愣辣拌麵」，裡頭配料有豆芽、蒜泥、青蔥、木耳、洋蔥丁、炙燒豬五花肉，搭配店家自製的蒜辣肉醬。麵條吃起來超Q彈，還帶著香辣及迷人蒜香味。
        https://supertaste.tvbs.com.tw/food/350835
        
        <img src="data:image/png;base64,{food_stc3_base64}" width="500">
        """,
        'images': ['food_stc1.jpg', 'food_stc2.jpg', 'food_stc3.jpg']
    },
    '台中-嘉義': {
        'center': [23.809488, 120.292326],
        'color': "red", # Changed color for variety
        'geojson_file': "taichung_jiayi.geojson",
        'csv_file': "food_tcjia.csv",
        'markdown': """
        ###阿添蛤仔麵
        
        吃彰化的蛤仔麵的特色是會將蛤仔去殼，因此是不用自己剝殼，此外重點的湯頭是清爽鮮甜的，麵的份量也是給的很足，丸子也很好吃。另外骨仔肉麵也是蠻多人推薦的，人氣一點都不輸給蛤仔麵，首先骨仔肉給的份量算是多的，吃起來肉質不乾柴，骨仔肉還帶有軟筋膜，吃起來略有咬勁而且很有層次感，Q軟Q軟的很不錯，重點是湯頭用的是大骨去熬的，喝起來很清甜，跟蛤仔湯頭那種清甜感略有不同。
        https://blaketravel.tw/blog/post/a-tian

        
        <img src="data:image/png;base64,{food_tcjia1_base64}" width="500">

        ---

        ###西螺 脆皮臭豆腐
        文字
        <img src="data:image/png;base64,{food_tcjia2_base64}" width="500">

        ---

        ###民主火雞肉飯
        
        火雞肉飯是嘉義最具代表性的小吃，到嘉義市總要吃１碗火雞肉飯才覺得不虛此行。位於東區民族路的「民主火雞肉飯」是嘉義雞肉飯的人氣霸主，無論平日還是假日人潮都沒停過，另外這家火雞肉飯除了觀光客喜歡，連在地人都會來吃。他們家的靈魂油蔥酥醬都是自己製作、不假他人之手，純正的火雞肉搭配香酥油蔥醬汁，鹹香撲鼻，超夠味！
        https://supertaste.tvbs.com.tw/pack/341122
        
        <img src="data:image/png;base64,{food_tcjia3_base64}" width="500">
        """,
        'images': ['food_tcjia1.jpg', 'food_tcjia2.jpg', 'food_tcjia3.jpg']
    },
    '嘉義-高雄': {
        'center': [22.999866, 120.148435],
        'color': "red", # Changed color for variety
        'geojson_file': "jiayi_kaohsung.geojson",
        'csv_file': "food_jiakao.csv",
        'markdown': """
        ###味泰豐香雞排
        
        本店有五花八門的現炸品項，有杏鮑菇、三角骨、馬鈴薯條、雞皮、百頁豆腐、銀絲卷、芋條粿、麥克雞塊、三角薯餅、魚板等，必點推薦第一名絕對是杏鮑菇，味泰豐的杏鮑菇跟別家鹹酥雞店或是夜市的很不一樣，會切成條狀之後再整條拿去炸，等炸好後，老闆娘才會幫你剪成小塊，外皮酥脆，裡頭杏鮑菇更加多汁。
        https://coffeelife2015.pixnet.net/blog/post/225515081
        
        <img src="data:image/png;base64,{food_jiakao1_base64}" width="500">

        ---

        ###城邊真味鱔魚意麵
        
        創立於1970年，至今已走過五十多個年頭，以鑊氣十足的炒鱔魚作為招牌，酸酸甜甜讓人回味。炒鱔魚意麵也是這裡的人氣菜色，跟炒鱔魚一樣，可選擇勾芡與否。另有生炒花枝與麻油腰花供應，後者鮮美可口，不妨一試。
        https://guide.michelin.com/tw/zh_TW/tainan-region/tainan/restaurant/eastern-castle-noodles
        
        <img src="data:image/png;base64,{food_jiakao2_base64}" width="500">

        ---

        ###Temperature Studio/溫度劑
        
        具十年高端餐飲經驗的主廚於2021年開設此店，只設六個座位，不設制式菜單，而是採用當季新鮮食材，糅合歐陸、日本與臺灣元素，製作出由前菜到甜品、溫度與層次堆疊的美食，並由主廚親自介紹菜色，期望為客人帶來充滿溫度的用餐體驗。推薦波特菇鑲肉，還有選用海水養殖虱目魚的魚肚飯。
        https://guide.michelin.com/tw/zh_TW/kaohsiung-region/kaohsiung/restaurant/temperature-studio

        <img src="data:image/png;base64,{food_jiakao3_base64}" width="500">
        """,
        'images': ['food_jiakao1.jpg', 'food_jiakao2.jpg', 'food_jiakao3.jpg']
    },
    '高雄-屏東': {
        'center': [22.402317, 120.536198],
        'color': "red", # Changed color for variety
        'geojson_file': "kaohsung_pingtung.geojson",
        'csv_file': "food_kaoping.csv",
        'markdown': """
        ###仁武烤鴨
        
        位於高雄仁武區的「仁武烤鴨」，​無論平日或假日，店門口總是滿滿的人潮。​店內不僅提供烤鴨料理，還有熱門必點的米血及店家手工自製超Q荷葉餅，搭配甜麵醬和蔥段，讓剛出爐的烤鴨美味更加升級。​烤鴨愛好者，絕對不能錯過這家高雄的烤鴨名店。招牌的「仁武烤鴨」的脆皮片鴨一上桌就香氣撲鼻，外皮烤得金黃酥脆，閃著誘人的油光，讓人還沒開動就口水直流。脆皮片鴨的鴨肉是整支鴨最肥美的地方，鮮嫩多汁，完全不乾柴，香氣迷人。
        https://vocus.cc/article/68033978fd8978000134adcc

        <img src="data:image/png;base64,{food_kaoping1_base64}" width="500">

        ---

        ###北港蔡三代筒仔米糕
        
        北港蔡三代筒仔米糕自1956年起屹立在鹽埕區，菜單內容樸實，就只有筒仔米糕、五種湯品及鐵蛋，卻因價廉物美成為高雄人的共同回憶。筒仔米糕選用陳放兩年的舊米製作，再於上桌前淋上滿滿的肉燥汁，糕身軟硬適中，佐以嫩薑同吃十分可口，叫人回味。富滋味的鐵蛋，和吸滿湯汁精華、香味濃郁的蒸蛋湯同樣值得一試。
        https://guide.michelin.com/tw/zh_TW/kaohsiung-region/kaohsiung/restaurant/bei-gang-tsai-rice-tube-yancheng

        <img src="data:image/png;base64,{food_kaoping2_base64}" width="500">

        ---

        ###王匠黑鮪魚生魚片&日本料理
        
        在漁市可說是賣生魚片的業者的一級戰區，而位於華僑市場228號攤的「王匠黑鮪魚生魚片&日本料理」卻有著獨樹一格的特色，充滿日式氛圍的外觀，氣派亮眼的攤位規模，生魚片品質絕佳，加上使用最新鮮的漁獲食材製作日式料理，早已成功擦亮「王匠」招牌，不僅節目報導採訪不斷，更是連外縣市遊客來到東港華僑市場都指名要吃這一攤。
        https://kenantravel.tw/wjsashimi/

        <img src="data:image/png;base64,{food_kaoping3_base64}" width="500">
        """,
        'images': ['food_kaoping1.jpg', 'food_kaoping2.jpg', 'food_kaoping3.jpg']
    },
    '屏東-台東': {
        'center': [22.781440, 120.834135],
        'color': "red", # Changed color for variety
        'geojson_file': "pingtung_taitung.geojson",
        'csv_file': "food_pingtait.csv",
        'markdown': """
        ###卑南豬血湯 侯記老店
        文字
        <img src="data:image/png;base64,{food_pingtait1_base64}" width="500">

        ---

        ###某一家
        文字
        <img src="data:image/png;base64,{food_pingtait2_base64}" width="500">
        """,
        'images': ['food_pingtait1.jpg', 'food_pingtait2.jpg']
    },
    '台東-花蓮': {
        'center': [23.429920, 121.335207],
        'color': "red", # Changed color for variety
        'geojson_file': "taitung_hualien.geojson",
        'csv_file': "food_taithua.csv",
        'markdown': """
        ###全美行
        文字
        <img src="data:image/png;base64,{food_taithua1_base64}" width="500">

        ---

        ###某一家
        文字
        <img src="data:image/png;base64,{food_taithua2_base64}" width="500">
        """,
        'images': ['food_taithua1.jpg', 'food_taithua2.jpg']
    },
    '花蓮-宜蘭': {
        'center': [24.228917, 121.532195],
        'color': "red", # Changed color for variety
        'geojson_file': "hualien_yilan.geojson",
        'csv_file': "food_huayi.csv",
        'markdown': """
        ###液香扁食
        文字
        <img src="data:image/png;base64,{food_huayi1_base64}" width="500">

        ---

        ###羅東碳烤燒餅餅店
        文字
        <img src="data:image/png;base64,{food_huayi2_base64}" width="500">
        """,
        'images': ['food_huayi1.jpg', 'food_huayi2.jpg']
    },
    '宜蘭-台北': {
        'center': [24.899394, 121.675311],
        'color': "red", # Changed color for variety
        'geojson_file': "yilan_taipei.geojson",
        'csv_file': "food_yitaip.csv",
        'markdown': """
        ###十分溜哥燒烤雞翅包飯
        文字
        <img src="data:image/png;base64,{food_yitaip1_base64}" width="500">

        ---

        ###羅東碳烤燒餅餅店
        文字
        <img src="data:image/png;base64,{food_yitaip2_base64}" width="500">
        """,
        'images': ['food_yitaip1.jpg', 'food_yitaip2.jpg']
    }
}

# --- Main logic to display map and information ---

if option in food_segments:
    segment_info = food_segments[option]

    # Initialize map
    # Note: Corrected center order to [latitude, longitude]
    m = leafmap.Map(center=segment_info['center'], zoom=7, minimap_control=True)
    style = {"color": segment_info['color'], "weight": 3, "opacity": 0.8}

    # Add GeoJSON
    geojson_data = load_geojson(segment_info['geojson_file'])
    if geojson_data:
        m.add_geojson(geojson_data, layer_name=option, style=style)

    # Add points from CSV
    csv_path = os.path.join(FOOD_CSV_FOLDER, segment_info['csv_file'])
    if os.path.exists(csv_path):
        m.add_points_from_xy(csv_path, x="X", y="Y")
    else:
        st.error(f"CSV file not found: {csv_path}")

    # Display map
    m.to_streamlit(height=700)

    # Prepare markdown with images
    image_placeholders = {}
    for img_file in segment_info['images']:
        img_path = os.path.join(FOOD_PNG_FOLDER, img_file)
        if os.path.exists(img_path):
            with open(img_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                # Extract filename without extension for placeholder name
                placeholder_name = os.path.splitext(img_file)[0] + '_base64'
                image_placeholders[placeholder_name] = encoded_string
        else:
            st.warning(f"Image file not found: {img_path}. Placeholder will be empty.")
            # Even if not found, add to dictionary to prevent KeyError
            placeholder_name = os.path.splitext(img_file)[0] + '_base64'
            image_placeholders[placeholder_name] = "" # Empty string if image not found

    # Format the markdown string with the base64 encoded images
    formatted_markdown = segment_info['markdown'].format(**image_placeholders)
    st.markdown(formatted_markdown, unsafe_allow_html=True)

else:
    # 如果 selected_route 不在 food_segments 字典中，提示使用者
    st.write("所選路段無資料顯示。請回到第一頁重新選擇。")
