
# 1〜12月まで英語でリスト型に格納
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", \
         "December"]

# リストの要素数を確認
# print(len(month))

index = 1

# ループ処理を行い、リストの中身を表示させる
for i in month:
    print(str(index) + "月：" + i)
    index += 1

