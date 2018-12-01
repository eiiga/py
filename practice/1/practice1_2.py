
# トランプのマークを格納
mark = ["スペード", "ハート", "ダイヤ", "クラブ"]

# トランプの数字を格納　↓ここから↓
trump = []

for i in range(52):
    num = (i + 1) % 13
    # 1の時はA（エース）を格納
    if num == 1:
        card = "A"
        trump.append(card)
    # 11の時はJ（ジャック）を格納
    elif num == 11:
        card = "J"
        trump.append(card)
    # 12の時はQ（クイーン）を格納
    elif num == 12:
        card = "Q"
        trump.append(card)
    # 13の時はK（キング）を格納
    elif num == 0:
        card = "K"
        trump.append(card)
    else:
        trump.append(str(num))
# トランプの数字を格納　↑ここまで↑

index = 1

# トランプの数だけループさせる
for k in trump:
    # １〜13はスペード
    if index <= 13:
        print(str(index) + "：" + mark[0] + "　" + k)
        index += 1
    # 14〜26はハート
    elif 13 < index <= 26:
        print(str(index) + "：" + mark[1] + "　" + k)
        index += 1
    # 27〜39はダイヤ
    elif 26 < index <= 39:
        print(str(index) + "：" + mark[2] + "　" + k)
        index += 1
    # 40〜53はクラブ
    elif 39 < index <= 52:
        print(str(index) + "：" + mark[3] + "　" + k)
        index += 1
