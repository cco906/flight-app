airport = ["TPE","NRT","KIX","ICN","SIN","CGK","BKK","SGN","BCN","DEL","HKG","HNL","LAX","MFM","MXP","PDX","SEA","SFO"]
while True:
    dep = input("請輸入出發地機場代碼(三碼大寫英文):").upper()
    if dep in airport:
        break  
    print("您所輸入的出發地機場代碼不在本航空公司的飛行城市內，請重新輸入！\n")
while True:
    arr = input("請輸入目的地機場代碼(三碼大寫英文):").upper()
    if arr not in airport:
        print("您所輸入的目的地機場代碼不在本航空公司的飛行城市內，請重新輸入！\n")
    elif arr == dep:  
        print("❌ 錯誤：目的地不能與出發地相同，請重新輸入！\n")
    else:
        break 
trip = (dep, arr)
print(f"\n成功建立旅程：從 {dep} 到 {arr}")

flights = [
    # ================= 亞洲航線 =================
    # 東京(成田) NRT
    {"flight": "TX100", "dep": "TPE", "arr": "NRT", "dep_t": "08:00", "arr_t": "11:40"},
    {"flight": "TX101", "dep": "NRT", "arr": "TPE", "dep_t": "13:25", "arr_t": "15:40"},
    {"flight": "TX102", "dep": "TPE", "arr": "NRT", "dep_t": "10:10", "arr_t": "13:50"},
    {"flight": "TX103", "dep": "NRT", "arr": "TPE", "dep_t": "15:20", "arr_t": "17:35"},
    {"flight": "TX104", "dep": "TPE", "arr": "NRT", "dep_t": "14:10", "arr_t": "17:50"},
    {"flight": "TX105", "dep": "NRT", "arr": "TPE", "dep_t": "19:20", "arr_t": "21:35"},
    # 大阪 KIX
    {"flight": "TX120", "dep": "TPE", "arr": "KIX", "dep_t": "07:55", "arr_t": "11:05"},
    {"flight": "TX121", "dep": "KIX", "arr": "TPE", "dep_t": "12:35", "arr_t": "14:15"},
    {"flight": "TX124", "dep": "TPE", "arr": "KIX", "dep_t": "13:50", "arr_t": "17:00"},
    {"flight": "TX125", "dep": "KIX", "arr": "TPE", "dep_t": "18:30", "arr_t": "20:10"},
    # 仁川 ICN
    {"flight": "TX300", "dep": "TPE", "arr": "ICN", "dep_t": "07:05", "arr_t": "10:10"},
    {"flight": "TX301", "dep": "ICN", "arr": "TPE", "dep_t": "11:10", "arr_t": "12:25"},
    {"flight": "TX302", "dep": "TPE", "arr": "ICN", "dep_t": "09:50", "arr_t": "12:55"},
    {"flight": "TX303", "dep": "ICN", "arr": "TPE", "dep_t": "13:55", "arr_t": "15:10"},
    {"flight": "TX306", "dep": "TPE", "arr": "ICN", "dep_t": "15:25", "arr_t": "18:30"},
    {"flight": "TX307", "dep": "ICN", "arr": "TPE", "dep_t": "19:30", "arr_t": "20:45"},
    # 新加坡 SIN
    {"flight": "TX500", "dep": "TPE", "arr": "SIN", "dep_t": "07:15", "arr_t": "11:25"},
    {"flight": "TX501", "dep": "SIN", "arr": "TPE", "dep_t": "12:55", "arr_t": "16:55"},
    {"flight": "TX502", "dep": "TPE", "arr": "SIN", "dep_t": "10:30", "arr_t": "14:40"},
    {"flight": "TX503", "dep": "SIN", "arr": "TPE", "dep_t": "16:10", "arr_t": "20:10"},
    {"flight": "TX508", "dep": "TPE", "arr": "SIN", "dep_t": "17:25", "arr_t": "21:35"},
    {"flight": "TX509", "dep": "SIN", "arr": "TPE", "dep_t": "01:05", "arr_t": "05:05"},
    # 雅加達 CGK
    {"flight": "TX520", "dep": "TPE", "arr": "CGK", "dep_t": "07:00", "arr_t": "10:45"},
    {"flight": "TX521", "dep": "CGK", "arr": "TPE", "dep_t": "12:15", "arr_t": "17:55"},
    # 曼谷 BKK
    {"flight": "TX530", "dep": "TPE", "arr": "BKK", "dep_t": "07:45", "arr_t": "10:10"},
    {"flight": "TX531", "dep": "BKK", "arr": "TPE", "dep_t": "11:40", "arr_t": "15:50"},
    {"flight": "TX532", "dep": "TPE", "arr": "BKK", "dep_t": "12:25", "arr_t": "14:50"},
    {"flight": "TX533", "dep": "BKK", "arr": "TPE", "dep_t": "16:20", "arr_t": "20:30"},
    # 胡志明市 SGN
    {"flight": "TX550", "dep": "TPE", "arr": "SGN", "dep_t": "06:45", "arr_t": "08:45"},
    {"flight": "TX551", "dep": "SGN", "arr": "TPE", "dep_t": "10:15", "arr_t": "14:10"},
    {"flight": "TX558", "dep": "TPE", "arr": "SGN", "dep_t": "20:45", "arr_t": "22:45"},
    {"flight": "TX559", "dep": "SGN", "arr": "TPE", "dep_t": "01:15", "arr_t": "05:10"},
    # 新德里 DEL
    {"flight": "TX590", "dep": "TPE", "arr": "DEL", "dep_t": "08:10", "arr_t": "11:25"},
    {"flight": "TX591", "dep": "DEL", "arr": "TPE", "dep_t": "13:25", "arr_t": "21:00"},
    # 香港 HKG
    {"flight": "TX700", "dep": "TPE", "arr": "HKG", "dep_t": "07:20", "arr_t": "08:50"},
    {"flight": "TX701", "dep": "HKG", "arr": "TPE", "dep_t": "09:50", "arr_t": "11:10"},
    {"flight": "TX702", "dep": "TPE", "arr": "HKG", "dep_t": "10:10", "arr_t": "11:40"},
    {"flight": "TX703", "dep": "HKG", "arr": "TPE", "dep_t": "12:40", "arr_t": "14:00"},
    {"flight": "TX704", "dep": "TPE", "arr": "HKG", "dep_t": "16:55", "arr_t": "18:25"},
    {"flight": "TX705", "dep": "HKG", "arr": "TPE", "dep_t": "19:25", "arr_t": "20:45"},
    {"flight": "TX706", "dep": "TPE", "arr": "HKG", "dep_t": "17:25", "arr_t": "18:55"},
    {"flight": "TX707", "dep": "HKG", "arr": "TPE", "dep_t": "20:10", "arr_t": "21:30"},
    {"flight": "TX708", "dep": "TPE", "arr": "HKG", "dep_t": "21:10", "arr_t": "22:40"},
    {"flight": "TX709", "dep": "HKG", "arr": "TPE", "dep_t": "06:55", "arr_t": "08:15"},
    # 澳門 MFM
    {"flight": "TX712", "dep": "TPE", "arr": "MFM", "dep_t": "15:25", "arr_t": "16:55"},
    {"flight": "TX713", "dep": "MFM", "arr": "TPE", "dep_t": "17:55", "arr_t": "19:20"},
    {"flight": "TX714", "dep": "TPE", "arr": "MFM", "dep_t": "18:15", "arr_t": "19:45"},
    {"flight": "TX715", "dep": "MFM", "arr": "TPE", "dep_t": "20:45", "arr_t": "22:10"},
    # ================= 美洲航線 =================
    # 洛杉磯 LAX
    {"flight": "TX1", "dep": "TPE", "arr": "LAX", "dep_t": "22:25", "arr_t": "19:10"},
    {"flight": "TX2", "dep": "LAX", "arr": "TPE", "dep_t": "00:25", "arr_t": "05:10"},
    {"flight": "TX3", "dep": "TPE", "arr": "LAX", "dep_t": "23:50", "arr_t": "20:35"},
    {"flight": "TX4", "dep": "LAX", "arr": "TPE", "dep_t": "00:05", "arr_t": "04:50"},
    {"flight": "TX5", "dep": "TPE", "arr": "LAX", "dep_t": "14:15", "arr_t": "11:00"},
    {"flight": "TX6", "dep": "LAX", "arr": "TPE", "dep_t": "13:30", "arr_t": "18:15"},
    # 舊金山 SFO
    {"flight": "TX11", "dep": "TPE", "arr": "SFO", "dep_t": "00:20", "arr_t": "20:30"},
    {"flight": "TX12", "dep": "SFO", "arr": "TPE", "dep_t": "00:45", "arr_t": "04:55"},
    # 西雅圖 SEA
    {"flight": "TX21", "dep": "TPE", "arr": "SEA", "dep_t": "00:10", "arr_t": "19:40"},
    {"flight": "TX22", "dep": "SEA", "arr": "TPE", "dep_t": "01:40", "arr_t": "05:05"},
    # 波特蘭 PDX
    {"flight": "TX25", "dep": "TPE", "arr": "PDX", "dep_t": "23:45", "arr_t": "19:20"},
    {"flight": "TX26", "dep": "PDX", "arr": "TPE", "dep_t": "00:50", "arr_t": "04:40"},
    # 檀香山 HNL
    {"flight": "TX29", "dep": "TPE", "arr": "HNL", "dep_t": "08:10", "arr_t": "22:55"},
    {"flight": "TX30", "dep": "HNL", "arr": "TPE", "dep_t": "00:55", "arr_t": "05:30"},
    # ================= 歐洲航線 =================
    # 巴塞隆納 BCN
    {"flight": "TX61", "dep": "TPE", "arr": "BCN", "dep_t": "23:30", "arr_t": "06:10"},
    {"flight": "TX62", "dep": "BCN", "arr": "TPE", "dep_t": "11:40", "arr_t": "05:00"},
    # 米蘭 MXP
    {"flight": "TX67", "dep": "TPE", "arr": "MXP", "dep_t": "23:30", "arr_t": "05:20"},
    {"flight": "TX68", "dep": "MXP", "arr": "TPE", "dep_t": "11:50", "arr_t": "04:25"},]
def time_to_mins(t_str):
    hours, mins = t_str.split(":")
    return int(hours) * 60 + int(mins)
def get_flight_options(d_code, a_code, flights):
    """取得指定航段的所有方案（包含直飛與過濾排序後的轉機）"""
    options = []
    directs = [f for f in flights if f["dep"] == d_code and f["arr"] == a_code]
    for d in directs:
        options.append({"type": "direct", "data": d})
    if len(directs) == 0:
        transfers = []
        leg1_list = [f for f in flights if f["dep"] == d_code and f["arr"] == "TPE"]
        leg2_list = [f for f in flights if f["dep"] == "TPE" and f["arr"] == a_code]
        for f1 in leg1_list:
            for f2 in leg2_list:
                arr1_mins = time_to_mins(f1["arr_t"])
                dep2_mins = time_to_mins(f2["dep_t"])
                wait_time = dep2_mins - arr1_mins
                if wait_time < 60:
                    wait_time += 1440
                if 60 <= wait_time <= 1440:
                    wait_h = wait_time // 60
                    wait_m = wait_time % 60
                    transfers.append({"leg1": f1,"leg2": f2,"wait_time": wait_time,"wait_text": f"{wait_h} 小時 {wait_m} 分鐘",})
        transfers.sort(key=lambda x: x["wait_time"])
        for t in transfers:
            options.append({"type": "transfer", "data": t})
    return options
def user_select_option(options, leg_title):
    """讓使用者挑選航班的互動函式"""
    if not options:
        print(f"❌ {leg_title} 無可用航班！")
        return None
    print(f"\n==================== {leg_title} 方案選擇 ====================")
    for idx, opt in enumerate(options, 1):
        if opt["type"] == "direct":
            f = opt["data"]
            print(f" [{idx}] 【直飛】班號：{f['flight']} | 起飛時間：{f['dep_t']} |"f" 抵達時間：{f['arr_t']}")
        else:
            t = opt["data"]
            l1, l2 = t["leg1"], t["leg2"]
            print(f" [{idx}] 【經 TPE 轉機】第一段 ({l1['flight']}):"f" {l1['dep_t']}~{l1['arr_t']} ➔ 等待 {t['wait_text']} ➔"f" 第二段 ({l2['flight']}): {l2['dep_t']}~{l2['arr_t']}")
    while True:
        try:
            choice = int(input(f"\n請輸入您想選擇的 {leg_title} 編號 (1~{len(options)}): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            print(f"⚠️ 請輸入有效的範圍數字 (1~{len(options)})！")
        except ValueError:
            print("⚠️ 請輸入數字編號！")
outbound_opts = get_flight_options(dep, arr, flights)
inbound_opts = get_flight_options(arr, dep, flights)
selected_outbound = user_select_option(outbound_opts, f"去程 ({dep} ➔ {arr})")
selected_inbound = user_select_option(inbound_opts, f"回程 ({arr} ➔ {dep})")
print("\n" + "=" * 60)
print("🎉 您的預訂行程確認單")
print("=" * 60)
def print_choice_detail(choice_obj, title):
    print(f"📌 【{title}】")
    if not choice_obj:
        print("   未選擇航班")
        return
    if choice_obj["type"] == "direct":
        f = choice_obj["data"]
        print(f"   類型：直飛航班\n   班號：{f['flight']}\n  "f" 時間：{f['dep_t']} 起飛 ➔ {f['arr_t']} 抵達")
    else:
        t = choice_obj["data"]
        l1, l2 = t["leg1"], t["leg2"]
        print(f"   類型：經台北 (TPE) 轉機（轉機等待 {t['wait_text']}）")
        print(f"   • 第一段：{l1['flight']} ({l1['dep']} ➔ TPE) |"f" {l1['dep_t']}~{l1['arr_t']}")
        print(f"   • 第二段：{l2['flight']} (TPE ➔ {l2['arr']}) |"f" {l2['dep_t']}~{l2['arr_t']}")
print_choice_detail(selected_outbound, f"去程：{dep} ➔ {arr}")
print("-" * 60)
print_choice_detail(selected_inbound, f"回程：{arr} ➔ {dep}")
print("=" * 60)
print("祝您旅途愉快！✈️")