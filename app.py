import streamlit as st

# 1. 設定網頁標題與圖示
st.set_page_config(
    page_title="TX 航空航班查詢系統", page_icon="✈️", layout="centered"
)

st.title("✈️ TX 航空航班查詢系統")
st.write(
    "請選擇您的出發地與目的地，系統將自動為您搜尋直飛與經台北 (TPE)"
    " 轉機的來回組合。"
)

# 2. 支援機場清單
airport = [
    "TPE",
    "NRT",
    "KIX",
    "ICN",
    "SIN",
    "CGK",
    "BKK",
    "SGN",
    "BCN",
    "DEL",
    "HKG",
    "HNL",
    "LAX",
    "MFM",
    "MXP",
    "PDX",
    "SEA",
    "SFO",
]

# 3. TX 航空航班總表
flights = [
    # 亞洲航線
    {
        "flight": "TX100",
        "dep": "TPE",
        "arr": "NRT",
        "dep_t": "08:00",
        "arr_t": "11:40",
    },
    {
        "flight": "TX101",
        "dep": "NRT",
        "arr": "TPE",
        "dep_t": "13:25",
        "arr_t": "15:40",
    },
    {
        "flight": "TX102",
        "dep": "TPE",
        "arr": "NRT",
        "dep_t": "10:10",
        "arr_t": "13:50",
    },
    {
        "flight": "TX103",
        "dep": "NRT",
        "arr": "TPE",
        "dep_t": "15:20",
        "arr_t": "17:35",
    },
    {
        "flight": "TX104",
        "dep": "TPE",
        "arr": "NRT",
        "dep_t": "14:10",
        "arr_t": "17:50",
    },
    {
        "flight": "TX105",
        "dep": "NRT",
        "arr": "TPE",
        "dep_t": "19:20",
        "arr_t": "21:35",
    },
    {
        "flight": "TX120",
        "dep": "TPE",
        "arr": "KIX",
        "dep_t": "07:55",
        "arr_t": "11:05",
    },
    {
        "flight": "TX121",
        "dep": "KIX",
        "arr": "TPE",
        "dep_t": "12:35",
        "arr_t": "14:15",
    },
    {
        "flight": "TX124",
        "dep": "TPE",
        "arr": "KIX",
        "dep_t": "13:50",
        "arr_t": "17:00",
    },
    {
        "flight": "TX125",
        "dep": "KIX",
        "arr": "TPE",
        "dep_t": "18:30",
        "arr_t": "20:10",
    },
    {
        "flight": "TX300",
        "dep": "TPE",
        "arr": "ICN",
        "dep_t": "07:05",
        "arr_t": "10:10",
    },
    {
        "flight": "TX301",
        "dep": "ICN",
        "arr": "TPE",
        "dep_t": "11:10",
        "arr_t": "12:25",
    },
    {
        "flight": "TX302",
        "dep": "TPE",
        "arr": "ICN",
        "dep_t": "09:50",
        "arr_t": "12:55",
    },
    {
        "flight": "TX303",
        "dep": "ICN",
        "arr": "TPE",
        "dep_t": "13:55",
        "arr_t": "15:10",
    },
    {
        "flight": "TX306",
        "dep": "TPE",
        "arr": "ICN",
        "dep_t": "15:25",
        "arr_t": "18:30",
    },
    {
        "flight": "TX307",
        "dep": "ICN",
        "arr": "TPE",
        "dep_t": "19:30",
        "arr_t": "20:45",
    },
    {
        "flight": "TX500",
        "dep": "TPE",
        "arr": "SIN",
        "dep_t": "07:15",
        "arr_t": "11:25",
    },
    {
        "flight": "TX501",
        "dep": "SIN",
        "arr": "TPE",
        "dep_t": "12:55",
        "arr_t": "16:55",
    },
    {
        "flight": "TX502",
        "dep": "TPE",
        "arr": "SIN",
        "dep_t": "10:30",
        "arr_t": "14:40",
    },
    {
        "flight": "TX503",
        "dep": "SIN",
        "arr": "TPE",
        "dep_t": "16:10",
        "arr_t": "20:10",
    },
    {
        "flight": "TX508",
        "dep": "TPE",
        "arr": "SIN",
        "dep_t": "17:25",
        "arr_t": "21:35",
    },
    {
        "flight": "TX509",
        "dep": "SIN",
        "arr": "TPE",
        "dep_t": "01:05",
        "arr_t": "05:05",
    },
    {
        "flight": "TX520",
        "dep": "TPE",
        "arr": "CGK",
        "dep_t": "07:00",
        "arr_t": "10:45",
    },
    {
        "flight": "TX521",
        "dep": "CGK",
        "arr": "TPE",
        "dep_t": "12:15",
        "arr_t": "17:55",
    },
    {
        "flight": "TX530",
        "dep": "TPE",
        "arr": "BKK",
        "dep_t": "07:45",
        "arr_t": "10:10",
    },
    {
        "flight": "TX531",
        "dep": "BKK",
        "arr": "TPE",
        "dep_t": "11:40",
        "arr_t": "15:50",
    },
    {
        "flight": "TX532",
        "dep": "TPE",
        "arr": "BKK",
        "dep_t": "12:25",
        "arr_t": "14:50",
    },
    {
        "flight": "TX533",
        "dep": "BKK",
        "arr": "TPE",
        "dep_t": "16:20",
        "arr_t": "20:30",
    },
    {
        "flight": "TX550",
        "dep": "TPE",
        "arr": "SGN",
        "dep_t": "06:45",
        "arr_t": "08:45",
    },
    {
        "flight": "TX551",
        "dep": "SGN",
        "arr": "TPE",
        "dep_t": "10:15",
        "arr_t": "14:10",
    },
    {
        "flight": "TX590",
        "dep": "TPE",
        "arr": "DEL",
        "dep_t": "08:10",
        "arr_t": "11:25",
    },
    {
        "flight": "TX591",
        "dep": "DEL",
        "arr": "TPE",
        "dep_t": "13:25",
        "arr_t": "21:00",
    },
    {
        "flight": "TX700",
        "dep": "TPE",
        "arr": "HKG",
        "dep_t": "07:20",
        "arr_t": "08:50",
    },
    {
        "flight": "TX701",
        "dep": "HKG",
        "arr": "TPE",
        "dep_t": "09:50",
        "arr_t": "11:10",
    },
    {
        "flight": "TX702",
        "dep": "TPE",
        "arr": "HKG",
        "dep_t": "10:10",
        "arr_t": "11:40",
    },
    {
        "flight": "TX703",
        "dep": "HKG",
        "arr": "TPE",
        "dep_t": "12:40",
        "arr_t": "14:00",
    },
    {
        "flight": "TX704",
        "dep": "TPE",
        "arr": "HKG",
        "dep_t": "16:55",
        "arr_t": "18:25",
    },
    {
        "flight": "TX705",
        "dep": "HKG",
        "arr": "TPE",
        "dep_t": "19:25",
        "arr_t": "20:45",
    },
    {
        "flight": "TX706",
        "dep": "TPE",
        "arr": "HKG",
        "dep_t": "17:25",
        "arr_t": "18:55",
    },
    {
        "flight": "TX707",
        "dep": "HKG",
        "arr": "TPE",
        "dep_t": "20:10",
        "arr_t": "21:30",
    },
    {
        "flight": "TX708",
        "dep": "TPE",
        "arr": "HKG",
        "dep_t": "21:10",
        "arr_t": "22:40",
    },
    {
        "flight": "TX709",
        "dep": "HKG",
        "arr": "TPE",
        "dep_t": "06:55",
        "arr_t": "08:15",
    },
    {
        "flight": "TX712",
        "dep": "TPE",
        "arr": "MFM",
        "dep_t": "15:25",
        "arr_t": "16:55",
    },
    {
        "flight": "TX713",
        "dep": "MFM",
        "arr": "TPE",
        "dep_t": "17:55",
        "arr_t": "19:20",
    },
    {
        "flight": "TX714",
        "dep": "TPE",
        "arr": "MFM",
        "dep_t": "18:15",
        "arr_t": "19:45",
    },
    {
        "flight": "TX715",
        "dep": "MFM",
        "arr": "TPE",
        "dep_t": "20:45",
        "arr_t": "22:10",
    },
    # 美洲航線
    {
        "flight": "TX1",
        "dep": "TPE",
        "arr": "LAX",
        "dep_t": "22:25",
        "arr_t": "19:10",
    },
    {
        "flight": "TX2",
        "dep": "LAX",
        "arr": "TPE",
        "dep_t": "00:25",
        "arr_t": "05:10",
    },
    {
        "flight": "TX3",
        "dep": "TPE",
        "arr": "LAX",
        "dep_t": "23:50",
        "arr_t": "20:35",
    },
    {
        "flight": "TX4",
        "dep": "LAX",
        "arr": "TPE",
        "dep_t": "00:05",
        "arr_t": "04:50",
    },
    {
        "flight": "TX5",
        "dep": "TPE",
        "arr": "LAX",
        "dep_t": "14:15",
        "arr_t": "11:00",
    },
    {
        "flight": "TX6",
        "dep": "LAX",
        "arr": "TPE",
        "dep_t": "13:30",
        "arr_t": "18:15",
    },
    {
        "flight": "TX11",
        "dep": "TPE",
        "arr": "SFO",
        "dep_t": "00:20",
        "arr_t": "20:30",
    },
    {
        "flight": "TX12",
        "dep": "SFO",
        "arr": "TPE",
        "dep_t": "00:45",
        "arr_t": "04:55",
    },
    {
        "flight": "TX13",
        "dep": "TPE",
        "arr": "SFO",
        "dep_t": "21:20",
        "arr_t": "17:30",
    },
    {
        "flight": "TX14",
        "dep": "SFO",
        "arr": "TPE",
        "dep_t": "00:15",
        "arr_t": "04:25",
    },
    {
        "flight": "TX21",
        "dep": "TPE",
        "arr": "SEA",
        "dep_t": "00:10",
        "arr_t": "19:40",
    },
    {
        "flight": "TX22",
        "dep": "SEA",
        "arr": "TPE",
        "dep_t": "01:40",
        "arr_t": "05:05",
    },
    {
        "flight": "TX25",
        "dep": "TPE",
        "arr": "PDX",
        "dep_t": "23:45",
        "arr_t": "19:20",
    },
    {
        "flight": "TX26",
        "dep": "PDX",
        "arr": "TPE",
        "dep_t": "00:50",
        "arr_t": "04:40",
    },
    {
        "flight": "TX29",
        "dep": "TPE",
        "arr": "HNL",
        "dep_t": "17:10",
        "arr_t": "07:55",
    },
    {
        "flight": "TX30",
        "dep": "HNL",
        "arr": "TPE",
        "dep_t": "10:10",
        "arr_t": "14:45",
    },
    # 歐洲航線
    {
        "flight": "TX61",
        "dep": "TPE",
        "arr": "BCN",
        "dep_t": "23:30",
        "arr_t": "06:10",
    },
    {
        "flight": "TX62",
        "dep": "BCN",
        "arr": "TPE",
        "dep_t": "11:40",
        "arr_t": "05:00",
    },
    {
        "flight": "TX67",
        "dep": "TPE",
        "arr": "MXP",
        "dep_t": "23:30",
        "arr_t": "05:20",
    },
    {
        "flight": "TX68",
        "dep": "MXP",
        "arr": "TPE",
        "dep_t": "11:50",
        "arr_t": "04:25",
    },
]


# 4. 時間運算函式
def time_to_mins(t_str):
    hours, mins = t_str.split(":")
    return int(hours) * 60 + int(mins)


def get_flight_options(d_code, a_code, flights):
    options = []
    directs = [f for f in flights if f["dep"] == d_code and f["arr"] == a_code]
    for d in directs:
        options.append({"type": "direct", "data": d})

    if len(directs) == 0:
        transfers = []
        leg1_list = [
            f for f in flights if f["dep"] == d_code and f["arr"] == "TPE"
        ]
        leg2_list = [
            f for f in flights if f["dep"] == "TPE" and f["arr"] == a_code
        ]

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
                    transfers.append(
                        {
                            "leg1": f1,
                            "leg2": f2,
                            "wait_time": wait_time,
                            "wait_text": f"{wait_h} 小時 {wait_m} 分鐘",
                        }
                    )

        transfers.sort(key=lambda x: x["wait_time"])
        for t in transfers:
            options.append({"type": "transfer", "data": t})

    return options


# 5. 網頁介面元件 (UI)
col1, col2 = st.columns(2)
with col1:
    dep = st.selectbox("請選擇【出發地】", airport, index=1)
with col2:
    arr = st.selectbox("請選擇【目的地】", airport, index=8)

if dep == arr:
    st.error("❌ 目的地不能與出發地相同！")
else:
    out_opts = get_flight_options(dep, arr, flights)
    in_opts = get_flight_options(arr, dep, flights)

    st.markdown("---")
    st.subheader(f"🛫 去程搜尋結果 ({dep} ➔ {arr})")

    out_labels = []
    for opt in out_opts:
        if opt["type"] == "direct":
            f = opt["data"]
            out_labels.append(
                f"【直飛】{f['flight']} ({f['dep_t']} - {f['arr_t']})"
            )
        else:
            t = opt["data"]
            l1, l2 = t["leg1"], t["leg2"]
            out_labels.append(
                f"【轉機 - 等待 {t['wait_text']}】{l1['flight']} ({l1['dep_t']} - {l1['arr_t']})"
                f" ➔ {l2['flight']} ({l2['dep_t']} - {l2['arr_t']})"
            )

    sel_out_idx = (
        st.radio("請選擇去程航班：", range(len(out_labels)), format_func=lambda x: out_labels[x])
        if out_labels
        else None
    )

    st.markdown("---")
    st.subheader(f"🛬 回程搜尋結果 ({arr} ➔ {dep})")

    in_labels = []
    for opt in in_opts:
        if opt["type"] == "direct":
            f = opt["data"]
            in_labels.append(
                f"【直飛】{f['flight']} ({f['dep_t']} - {f['arr_t']})"
            )
        else:
            t = opt["data"]
            l1, l2 = t["leg1"], t["leg2"]
            in_labels.append(
                f"【轉機 - 等待 {t['wait_text']}】{l1['flight']} ({l1['dep_t']} - {l1['arr_t']})"
                f" ➔ {l2['flight']} ({l2['dep_t']} - {l2['arr_t']})"
            )

    sel_in_idx = (
        st.radio("請選擇回程航班：", range(len(in_labels)), format_func=lambda x: in_labels[x])
        if in_labels
        else None
    )

    if sel_out_idx is not None and sel_in_idx is not None:
        st.markdown("---")
        st.success("🎉 行程預訂確認單")

        c1, c2 = st.columns(2)
        with c1:
            st.info(f"**去程：{dep} ➔ {arr}**\n\n{out_labels[sel_out_idx]}")
        with c2:
            st.info(f"**回程：{arr} ➔ {dep}**\n\n{in_labels[sel_in_idx]}")
