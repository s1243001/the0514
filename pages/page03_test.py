import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import os
import base64 # Import base64 here, as it's used within the main logic

st.title("推薦的景點介紹🏖️")

# 從 session_state 讀取使用者選擇的路段
# 注意：這裡的鍵是 'selected_route'，與第一頁儲存的鍵一致
if 'selected_route' not in st.session_state:
    st.warning("請先回到第一頁選擇路段。")
    st.stop() # 如果沒有選擇路段，就停止程式執行

option = st.session_state['selected_route']

# Define base paths for your data and images
PLAY_CSV_FOLDER = "play_csv"
PLAY_PNG_FOLDER = "play_png"
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

# Dictionary to hold road segment data for cleaner code
road_segments = {
    '台北-新竹': {
        'center': [24.949132, 121.182838], # Corrected lat/lon order for Leafmap center
        'color': "red",
        'geojson_file': "taipei_hsinchu.geojson", # Assuming geojson files have .geojson extension
        'csv_file': "play_ts.csv",
        'markdown': """
        ###大溪老街
        
        大溪是桃園最早發展的地方，在清領時期就透過大漢溪與大陸進行貿易，造就了許多商號與商賈。日治大正時代因流行巴洛克建築風格，因此各商號融合巴洛克式繁飾主義和閩南傳統裝飾圖案，包括希臘山頭、羅馬柱子和中式的魚、蝙蝠等祈求吉慶的圖案混合，形成一種大溪專有的特色。
        https://travel.tycg.gov.tw/zh-tw/travel/attraction/414

        <img src="data:image/png;base64,{ts1_base64}" width="500">

        ---

        ###新竹17公里海岸風景區
        
        新竹十七公里海岸線擁有「北台灣最美自行車道」的美稱！從南寮漁港一路沿著海岸線騎乘自行車，途中經過「魚鱗天梯」、「看海公園」等，一路到「香山沙丘」無一不是美景，非常適合在這連綿的自行車道邊賞景邊細細漫遊。
        https://www.welcometw.com/%E6%96%B0%E7%AB%B9%E6%99%AF%E9%BB%9E/

        <img src="data:image/png;base64,{ts2_base64}" width="500">
        """,
        'images': ['ts1.jpg', 'ts2.jpg'] # Assuming images are .jpg
    },
    '新竹-台中': {
        'center': [24.462711, 120.740153],
        'color': "red",
        'geojson_file': "hsinchu_taichung.geojson",
        'csv_file': "play_stc.csv",
        'markdown': """
        ###白沙屯拱天宮
        
        敬奉主神為媽祖的白沙屯拱天宮位在苗栗縣通霄鎮白東里白沙屯聚落，是當地居民的信仰中心。白沙屯媽祖集開基、鎮殿、進香為一身，媽祖神像獨特的特色為軟身四肢可活動，早期白沙屯先民因海上捕漁艱苦與危險，便奉祀軟身天上聖母，以祈求平安。另外每年以步行方式前往北港朝天宮進香是白沙屯一年一度的宗教節慶盛事，被列入台灣宗教百景之一，媽祖鑾轎因為轎頂覆蓋一層粉紅色薄帆布，有時行進非常快速，被信徒暱稱為「粉紅超跑」或是「粉紅法拉利」。

        <img src="data:image/png;base64,{stc1_base64}" width="500">

        ---

        ###大甲鎮瀾宮
        
        大甲區鎮瀾宮據說是清雍正8年（西元1730年）自湄洲天后祖廟恭請媽祖神像來臺。每年農曆三月初「遶境進香」場面浩大，追隨的信眾無數，各地廟宇均有迎媽祖的慶祝活動。大甲區鎮瀾宮媽祖繞境進香相傳已有數百年的歷史，主要是為了增添神像的靈氣。每次進香的人數之龐大，規模之壯觀，受到海內外的學術界和大眾傳播界的重視與研究。
        https://travel.taichung.gov.tw/zh-tw/attractions/intro/609

        <img src="data:image/png;base64,{stc2_base64}" width="500">

        ---

        ###國立自然科學博物館
        
        國立自然科學博物館創立於1986年，是全臺首座將自然科學生活化的博物館，亦是一處可以實地動手操作學習的知識殿堂！本館展示呈現多樣性，包括：太空劇場、科學中心、生命科學廳、地球環境廳、人類文化廳、植物園等，內容豐富且深具教育意義。
        https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=2191

        <img src="data:image/png;base64,{stc3_base64}" width="500">
        """,
        'images': ['stc1.jpg', 'stc2.jpg', 'stc3.jpg']
    },
    '台中-嘉義': {
        'center': [23.809488, 120.292326],
        'color': "red",
        'geojson_file': "taichung_jiayi.geojson",
        'csv_file': "play_tcjia.csv",
        'markdown': """
        ###八卦山大佛風景區
        
        八卦山大佛盤座在八卦山頭，低目慈眉看照著彰化，總讓快要接近彰化市和在地人熟悉地仰望，已超越宗教，成為彰化縣的重要地標，更吸引絡繹不絕的遊客，是彰化必訪勝地。
　      法相莊嚴肅穆的大佛竣工於1961年，曾是台灣十大熱門旅遊景點，被納入遠足、畢旅行程，從南到北，幾乎人人都有張和大佛合影紀念照片，交織許多記憶，增加歷史的厚度。
　      八卦山大佛風景區逾半世紀逐步形成，除了莊嚴的釋迦摩尼佛像，周邊還有豐富的遊憩資源，進入大佛風景區，首入眼簾是巍峨牌樓、連接「參佛道」，階梯盡頭似是一片天空點綴樹木，而兩旁卅二尊觀音法雕石像，引領執拾而上、沉澱心靈，走著走著，當視覺往右往挪移，乍見22公尺高的巨大釋迦牟尼佛盤坐蓮花座，讓人不由得歡喜讚嘆，大佛之大，也曾是亞洲第一。

        <img src="data:image/png;base64,{tcjia1_base64}" width="500">

        ---

        ###員林神社鳥居
        
        員林神社建於昭和6年（1931），是日治時期員林郡的神社之一。員林神社的祀神有造化三神（大國魂命、少彥名命、大己貴命）及北白川宮能久親王。員林神社共有三道鳥居，由參拜道通往本殿，神社參拜道上的鳥居，已改為傳統廟宇的牌坊造型。參拜道兩旁仍保留石燈籠、銅馬、及獅座。民國49年員林神社本殿遭拆毀，改為浩然台，一樓為涼亭，二樓做為忠烈祠，內部供奉「明延平郡王靈位」、「國軍陣亡將士靈位」及「國民革命先烈靈位」。
        https://tourism.chcg.gov.tw/AttractionsContent.aspx?id=119&chk=e7c911d7-3f45-4179-823d-9075e40cd13e

        <img src="data:image/png;base64,{tcjia2_base64}" width="500">

        ---

        ###嘉義北門驛
        
        北門驛興建於明治43年(1910)，最早是阿里山森林鐵路的起點車站，也是阿里山鐵路的貨運集散地，還有阿里山鐵路沿線的民生物資都是由此運上山，因此其地位相當重要。 到了民國62年（1973），因應阿里山轉型觀光景點的熱潮，阿里山森林鐵路嶄新的北門新車站落成啟用，取代了木造老車站「北門驛」，繼續搭載觀光客上阿里山。不過至民國71年（1982）阿里山公路正式通車，阿里山森林鐵路的搭乘盛況自此不再，北門驛周遭區域漸沒落。如今阿里山鐵路已不再運送木材了，北門驛見證伐木時代阿里山林業的繁榮興盛，因而被嘉義市政府指定為古蹟，並成為攝影愛好者及民眾休閒娛樂的好去處。 
        https://www.chiayi.gov.tw/News_Content.aspx?n=512&s=216167

        <img src="data:image/png;base64,{tcjia3_base64}" width="500">
        """,
        'images': ['tcjia1.jpg', 'tcjia2.jpg', 'tcjia3.jpg']
    },
    '嘉義-高雄': {
        'center': [22.999866, 120.148435],
        'color': "red",
        'geojson_file': "jiayi_kaohsung.geojson",
        'csv_file': "play_jiakao.csv",
        'markdown': """
        ###嘉油鐵馬道
        
        嘉油鐵馬道係為利用閒置的中油舊鐵道修築，於嘉義市世賢路四段中油廠區旁設為起點，途經美源、光路、獅子、紅瓦厝里等四里，以及嘉義水上鄉三和、下寮、回歸等三村。到達北回歸線站天文廣場，全長3500公尺，規劃成為自行車專用道暨景觀綠廊步道，以增進嘉義市的休閒與觀光資源。
        https://travel.chiayi.gov.tw/ChiayiTrendStore/TravelInformation/C000005/1/1f75b820-6671-41b3-a860-c47207b8a150
        
        <img src="data:image/png;base64,{jiakao1_base64}" width="500">

        ---

        ###臺南孔廟
        
        「全臺首學」臺灣的第一座孔子廟——臺南孔子廟創建於明永曆19年（1665年），當時稱為「先師聖廟」，至今已有三百多年的歷史，由島上第一個漢人政權鄭氏王朝所創立，為的是在臺開辦教育，培養為國效命的人才。清領時期亦延續功能，為臺灣官辦的最高學府「臺灣府學」所在地。直到今日，孔廟依然是讀書人的聖廟，有著崇高的地位。
        https://www.twtainan.net/zh-tw/attractions/detail/800/

        <img src="data:image/png;base64,{jiakao2_base64}" width="500">

        ---

        ###K.A.T 橋仔頭糖廠藝術村
        
        位於高雄橋頭的橋仔頭糖廠建立於1901年，是臺灣第一個現代工業區。2001年，由橋仔頭文史協會與一群藝術家，將此歷史工業遺址轉化為文化保存聚落，並且展開第一期的「橋仔頭糖廠藝術村」之藝術家駐村計畫。2008年開始以文化資產、環境教育、常民美學、藝術典藏為主要方向，持續推動藝術家駐村的計畫。這裡不只提供藝術家住宿空間和工作室，每季也舉辦不同主題的活動。
        https://artres.moc.gov.tw/zh/database/twContent/5516100de3fd476aacd82deb328eef25

        <img src="data:image/png;base64,{jiakao3_base64}" width="500">
        """,
        'images': ['jiakao1.jpg', 'jiakao2.jpg', 'jiakao3.jpg']
    },
    '高雄-屏東': {
        'center': [22.402317, 120.536198],
        'color': "red",
        'geojson_file': "kaohsung_pingtung.geojson",
        'csv_file': "play_kaoping.csv",
        'markdown': """
        ###龍虎塔
        
        坐落於高雄市左營區蓮池潭畔的龍虎塔興建於1976年，其具唐宋風格，磚石結構，樓閣式、七層，塔高31.6米。塔身每面刻火焰狀紋飾券門，外觀造型生動明亮，內部刻畫浮雕更別樹一格，龍塔內畫有中國的二十四孝子插圖，及代表罪惡之人死後入地獄時會遭受十殿閻王審判罰刑圖；虎塔則畫有十二賢士及代表天堂極樂世界的玉皇大帝三十六宮圖。
        https://vacation.eztravel.com.tw/sight/plc0000096264/dragon-and-tiger-pagodas-%E9%BE%8D%E8%99%8E%E5%A1%94

        <img src="data:image/png;base64,{kaoping1_base64}" width="500">

        ---

        ###大鵬灣國家風景區
        
        大鵬灣是臺灣最大的內灣，區內海域之動植物資源豐富，本區特有的紅樹林－海茄苳及濱海植物如馬鞍藤、土沈香、苦林盤等；動物景觀以鳥類、魚類及軟甲類為主，出現的鳥種計有九十五種，包括候鳥、過境鳥等，魚類有石斑等，另外活動於溼地的招潮蟹尤具特色。 
        https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=484

        <img src="data:image/png;base64,{kaoping2_base64}" width="500">

        ---

        ###國立海洋生物博物館
        
        屏東海生館被列為米其林綠色指南三星級必遊景點，更曾被旅遊網站評選為「亞洲排名第四、中港台第一名」的水族館。兼具旅遊與教育的意義，致力於推廣海洋保育、帶領民眾認識海洋生態。擁有三大展示館：台灣水域館、珊瑚王國館、世界水域館，呈現多樣性的海洋生態，打造出許多知名網美景點；館內更有白鯨、企鵝、海豹等明星生物，陪你遨遊海生館。還有每日定時定點餵食解說、觸摸池等現場活動，讓民眾更認識海洋世界的奧妙之處。
        https://www.taiwan.net.tw/m1.aspx?sNo=0001122&id=2242

        <img src="data:image/png;base64,{kaoping3_base64}" width="500">
        """,
        'images': ['kaoping1.jpg', 'kaoping2.jpg', 'kaoping3.jpg']
    },
    '屏東-台東': {
        'center': [22.781440, 120.834135],
        'color': "red",
        'geojson_file': "pingtung_taitung.geojson",
        'csv_file': "play_pingtait.csv",
        'markdown': """
        ###壽卡鐵馬驛站
        
        壽卡鐵馬驛站為南迴公路的最高點，原為199線道山路通行之檢查哨。近年單車運動盛行，許多騎士前來挑戰南迴公路長達21公里的上坡，壽卡驛站如燈塔立於至高點，象徵騎士完成艱困挑戰。
        https://twhwmuseum.thb.gov.tw/tw/cp-1320-8074-3139c-7.html

        <img src="data:image/png;base64,{pingtait1_base64}" width="500">

        ---

        ###多良車站
        
        多良車站被譽為全臺灣最美的車站，因其坐擁美麗的海景，迎面駛來的是緩慢前行的火車，轟隆隆的聲響與藍色海洋、蓊鬱山林，自然和諧的融合在一起。
        https://www.taiwan.net.tw/m1.aspx?sNo=0042331&uid=25011&keystring=

        <img src="data:image/png;base64,{pingtait2_base64}" width="500">

        ---

        ###國立臺灣史前文化博物館
        
        臺灣史前文化博物館，源自於卑南文化遺址的發現。博物館擁有世界級建築設計與豐富的展品，並規劃了親近宜人的戶外場域，摩艾石像以及館外綿延的草坪地景等深受旅客喜愛的特色造景。內部常設展分為三個主要展廳：「臺灣史前史廳」呈現百年來的考古發現，引導探索臺灣史前歷史；「南島廳」以南島族群視角介紹大洋文化，並連結世界文化互動；「臺灣自然史廳」透過誕生、冰期、新世代等三個展示室展示不同時期的臺灣自然歷史。「探索館」則是俱備舒適的軟硬體設備，空間中也設置許多原住民族藝術家創作的藝術作品，以公共設施結合圖畫或是透過繪本、遊戲和展示引導親子了解史前文化與原住民議題。
        https://tour.taitung.gov.tw/zh-tw/attraction/details/309

        <img src="data:image/png;base64,{pingtait3_base64}" width="500">
        """,
        'images': ['pingtait1.jpg', 'pingtait2.jpg', 'pingtait3.jpg']
    },
    '台東-花蓮': {
        'center': [23.429920, 121.335207],
        'color': "red",
        'geojson_file': "taitung_hualien.geojson",
        'csv_file': "play_taithua.csv",
        'markdown': """
        ###鹿野高台
        
        鹿野高台擁有絕佳視野，能夠一覽整個高台地區與卑南溪谷底的田野景色，也是臺灣東部一處優良的天然空域活動場地。每當6月至8月時，正是鹿野高台進行熱氣球活動的好時機，搭乘緩緩升空起飛的熱氣球，徜徉在花東縱谷的美景之中，親身體驗熱氣球起飛的這一份躍動。
        每逢暑假期間，盛大舉辦的臺灣國際熱氣球嘉年華以及光雕音樂會，都吸引來自世界各地的旅人前來參加，熱氣球繫留體驗、熱氣球自由飛行表演、絢麗燦爛的光雕音樂會，或是曙光光雕音樂會等活動，讓人永生難忘。

        <img src="data:image/png;base64,{taithua1_base64}" width="500">

        ---

        ###臺東池上錦新三號道路 伯朗大道
        
        在臺東池上鄉的田間道路上，兩旁是隨風搖曳的稻浪，因拍攝伯朗咖啡的廣告而大受歡迎，被稱為「伯朗大道」。而在伯朗大道的中間，有一條蜿蜒曲折的小路，是知名藝人曾來這兒騎單車拍攝廣告的地方，兩邊一望無際的綠色稻田隨風搖曳，被譽為是一條「翠綠的天堂之路」。
        https://www.erv-nsa.gov.tw/zh-tw/attractions/detail/197

        <img src="data:image/png;base64,{taithua2_base64}" width="500">
        """,
        'images': ['taithua1.jpg', 'taithua2.jpg']
    },
    '花蓮-宜蘭': {
        'center': [24.228917, 121.532195],
        'color': "red",
        'geojson_file': "hualien_yilan.geojson",
        'csv_file': "play_huayi.csv",
        'markdown': """
        ###鯉魚潭風景遊憩區
        
        鯉魚潭位於花蓮縣壽豐鄉，是花蓮縣境內最大的內陸湖泊，潭面呈南北長東西窄的橢圓形，面積因四季水量榮枯而互有消長，並因潭東的鯉魚山而得名。旅客可在此露營、野餐、遊湖。天候佳時，潭東的鯉魚山會聚集飛行傘活動愛好者，駕馭鮮麗的飛行傘翱翔於山巔水湄間，平添山光水色。
        https://www.taiwan.net.tw/m1.aspx?sNo=0001124&id=3

        <img src="data:image/png;base64,{huayi1_base64}" width="500">

        ---

        ###七星潭
        
        七星潭富有詩意的名稱，據說是位於花蓮師範學院和花蓮機場一帶，早年有零星湖泊散佈，後來因建設需要而填實。現在一般稱七星潭，是指美崙工業區和花蓮機場以北的地區，有斷層形成的海峽與優美的弧形海灣，具有豐富的自然人文景觀。在七星潭，可以遠眺清水斷崖，夜間還可以欣賞新城和崇德地區的燈火，區內更有許多景點，提供休憩和知性之旅。
        七星潭風景區以自行車道為動脈，從花蓮市南濱公園、經花蓮港、四八高地到七星潭風景區，長達21公里的旅程有不同的風光。花蓮縣政府更興建了石雕園區、賞星廣場、觀日樓、兒童遊樂場等休憩設施，在漁場附近還有海生態的解說牌，也利用防風林區闢建海濱植物園區，動植物生態非常豐富，來一趟知性之旅絕對不虛此行。
        https://www.taiwan.net.tw/m1.aspx?sNo=0001124&id=9488

        <img src="data:image/png;base64,{huayi2_base64}" width="500">

        ---

        ###清水斷崖
        
        清水斷崖，位於和平和崇德之間，是臺灣東岸的一大奇景，更是臺灣八大景之一。清水斷崖高一千多公尺，以極近90度的角度緊臨太平洋，公路綿延20多公里，蜿蜒曲折，一邊是懸崖峭壁，一邊是茫茫大海，形勢險峻，氣象萬千，令人膽戰心驚，嘆為觀止。而在蘇花公路的崇德隧道旁，有步道通往兩個觀景臺，可將太平洋及清水斷崖的山光水色盡入眼簾。途中更有北方澳、南方澳及烏石鼻等多個風景點讓你選擇。
        https://www.taiwan.net.tw/m1.aspx?sNo=0001124&id=2228

        <img src="data:image/png;base64,{huayi3_base64}" width="500">
        """,
        'images': ['huayi1.jpg', 'huayi2.jpg', 'huayi3.jpg']
    },
    '宜蘭-台北': {
        'center': [24.899394, 121.675311],
        'color': "red",
        'geojson_file': "yilan_taipei.geojson",
        'csv_file': "play_yitaip.csv",
        'markdown': """
        ###福隆舊草嶺隧道
        
        全長2,167公尺的「舊草嶺隧道」，昔日從福隆通往石城，早期宜蘭往返臺北交通因地形險峻，令往來行旅苦不堪言。日治時代進行鐵路舖設，興建工程中以穿越草嶺山脈之草嶺隧道最為艱困危險，隧道於西元1924年2月貫通。後因單線通車不敷使用，於民國75年（西元1986年）另建新草嶺隧道，舊隧道遂封閉閒置近20年。東北角風管處在歷經多年努力下，於民國97年（西元2008年）8月10日正式開放，為北台灣第一條以鐵路隧道改建而成的鐵馬隧道，更是獲得國際「明日旅業大獎WTTC」及臺灣十大自行車經典路線的獎項肯定，遊客可以騎乘自行車體驗它的原始風貌。
        https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=A12-00050
        
        <img src="data:image/png;base64,{yitaip1_base64}" width="500">

        ---

        ###十分老街
        
        新北市平溪區的十分，堪稱開發最早，也是規模最大的聚落，一條因開採煤礦而興建的鐵路支線「平溪線」，沿著基隆河河谷蜿蜒，在採礦落沒的匆匆歲月洗禮後，串起了十分、平溪、菁桐等幾個饒富風味的老街，這裡的主要特色在於老街和火車鐵軌是相連的，可以體驗「火車門前過」的新奇感受，以及走在鐵軌旁逛街的趣味，也是很多電影、偶像劇取景的知名景點。
        https://www.travel.taipei/zh-tw/attraction/details/300
        
        <img src="data:image/png;base64,{yitaip2_base64}" width="500">
        """,
        'images': ['yitaip1.jpg', 'yitaip2.jpg']
    }
}

# --- Main logic to display map and information ---

if option in road_segments:
    segment_info = road_segments[option]

    # Initialize map
    m = leafmap.Map(center=segment_info['center'], zoom=7, minimap_control=True)
    style = {"color": segment_info['color'], "weight": 3, "opacity": 0.8}

    # Add GeoJSON
    geojson_data = load_geojson(segment_info['geojson_file'])
    if geojson_data:
        m.add_geojson(geojson_data, layer_name=option, style=style)

    # Add points from CSV
    csv_path = os.path.join(PLAY_CSV_FOLDER, segment_info['csv_file'])
    if os.path.exists(csv_path):
        m.add_points_from_xy(csv_path, x="X", y="Y")
    else:
        st.error(f"CSV file not found: {csv_path}")

    # Display map
    m.to_streamlit(height=700)

    # Prepare markdown with images
    image_placeholders = {}
    for img_file in segment_info['images']:
        img_path = os.path.join(PLAY_PNG_FOLDER, img_file)
        if os.path.exists(img_path):
            with open(img_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                # Here is the fix: Extract filename without extension
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
    # 如果 selected_route 不在 road_segments 字典中，提示使用者
    st.write("所選路段無資料顯示。請回到第一頁重新選擇。")
