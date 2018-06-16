import tkinter as tk
import tkinter.messagebox as msg

#計算
def cal():
    #変換前が㎡
    if int_unit_land_before.get() == 0:
        if int_unit_land_after.get() == 0:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            int_result = int_num.get() * 0.01
            msg.showinfo('結果', str(int_result) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            int_result = int_num.get() * 0.0001
            msg.showinfo('結果', str(int_result) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            int_result = int_num.get() * 0.33
            msg.showinfo('結果', str(int_result) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            int_result = int_num.get() / 666
            msg.showinfo('結果', str(int_result) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            int_result = int_num.get() / 999
            msg.showinfo('結果', str(int_result) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            int_result = int_num.get() / 9999
            msg.showinfo('結果', str(int_result) + kind_of_land[6])

    # 変換前がa
    if int_unit_land_before.get() == 1:
        if int_unit_land_after.get() == 0:
            int_result = int_num.get() * 100
            msg.showinfo('結果', str(int_result) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            int_result = int_num.get() / 100
            msg.showinfo('結果', str(int_result) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            int_result = int_num.get() * 30
            msg.showinfo('結果', str(int_result) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            int_result = int_num.get() / 6.6
            msg.showinfo('結果', str(int_result) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            int_result = int_num.get() / 9.9
            msg.showinfo('結果', str(int_result) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            int_result = int_num.get() / 99
            msg.showinfo('結果', str(int_result) + kind_of_land[6])

    # 変換前がha
    if int_unit_land_before.get() == 2:
        if int_unit_land_after.get() == 0:
            int_result = int_num.get() * 10000
            msg.showinfo('結果', str(int_result) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            int_result = int_num.get() * 100
            msg.showinfo('結果', str(int_result) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            int_result = int_num.get() * 3000
            msg.showinfo('結果', str(int_result) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            int_result = int_num.get() / 16
            msg.showinfo('結果', str(int_result) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            int_result = int_num.get() / 0.1
            msg.showinfo('結果', str(int_result) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            int_result = int_num.get() / 0.01
            msg.showinfo('結果', str(int_result) + kind_of_land[6])

    # 変換前が坪
    if int_unit_land_before.get() == 3:
        if int_unit_land_after.get() == 0:
            int_result = int_num.get() * 3.3
            msg.showinfo('結果', str(int_result) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            int_result = int_num.get() / 30
            msg.showinfo('結果', str(int_result) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            int_result = int_num.get() / 3000
            msg.showinfo('結果', str(int_result) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            int_result = int_num.get() / 200
            msg.showinfo('結果', str(int_result) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            int_result = int_num.get() / 300
            msg.showinfo('結果', str(int_result) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            int_result = int_num.get() / 3000
            msg.showinfo('結果', str(int_result) + kind_of_land[6])

    # 変換前が畝
    if int_unit_land_before.get() == 4:
        if int_unit_land_after.get() == 0:
            int_result = int_num.get() * 666
            msg.showinfo('結果', str(int_result) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            int_result = int_num.get() * 6.6
            msg.showinfo('結果', str(int_result) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            int_result = int_num.get() * 16
            msg.showinfo('結果', str(int_result) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            int_result = int_num.get() * 200
            msg.showinfo('結果', str(int_result) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            int_result = int_num.get() * 0.66
            msg.showinfo('結果', str(int_result) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            int_result = int_num.get() * 0.067
            msg.showinfo('結果', str(int_result) + kind_of_land[6])

    # 変換前が反
    if int_unit_land_before.get() == 5:
        if int_unit_land_after.get() == 0:
            int_result = int_num.get() * 999
            msg.showinfo('結果', str(int_result) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            int_result = int_num.get() * 9.99
            msg.showinfo('結果', str(int_result) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            int_result = int_num.get() * 0.099
            msg.showinfo('結果', str(int_result) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            int_result = int_num.get() * 300
            msg.showinfo('結果', str(int_result) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            int_result = int_num.get() * 1.67
            msg.showinfo('結果', str(int_result) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            int_result = int_num.get() * 0.1
            msg.showinfo('結果', str(int_result) + kind_of_land[6])

    # 変換前が町歩
    if int_unit_land_before.get() == 6:
        if int_unit_land_after.get() == 0:
            int_result = int_num.get() * 9999
            msg.showinfo('結果', str(int_result) + kind_of_land[0])
        elif int_unit_land_after.get() == 1:
            int_result = int_num.get() * 99.99
            msg.showinfo('結果', str(int_result) + kind_of_land[1])
        elif int_unit_land_after.get() == 2:
            int_result = int_num.get() * 0.99
            msg.showinfo('結果', str(int_result) + kind_of_land[2])
        elif int_unit_land_after.get() == 3:
            int_result = int_num.get() * 3000
            msg.showinfo('結果', str(int_result) + kind_of_land[3])
        elif int_unit_land_after.get() == 4:
            int_result = int_num.get() * 16.7
            msg.showinfo('結果', str(int_result) + kind_of_land[4])
        elif int_unit_land_after.get() == 5:
            int_result = int_num.get() * 16.7
            msg.showinfo('結果', str(int_result) + kind_of_land[5])
        elif int_unit_land_after.get() == 6:
            msg.showinfo('結果', str(int_num.get()) + kind_of_land[6])

#画面作成
root = tk.Tk()
root.title("面積変換アプリ")
canvas = tk.Canvas(root, width=400, height=280, bd=0, highlightthickness=0)
canvas.pack()

#辞書型で単位を格納
kind_of_land = {0: '㎡', 1: 'a', 2: 'ha', 3: '坪', 4: '畝', 5: '反', 6: '町歩'}

#入力値の保持
int_num = tk.IntVar()
int_unit_land_before = tk.IntVar()
int_unit_land_after = tk.IntVar()

#テキストボックスの作成
tx_num = tk.Entry(root, textvariable=int_num)
tx_num.place(x=140, y=30)

#変換前ラベル
l_before = tk.Label(root, text='変換前')
l_before.place(x=20, y=60)

#変換前ラジオボタン
b_rd1 = tk.Radiobutton(root, text=kind_of_land[0], variable=int_unit_land_before, value=0)
b_rd1.place(x=20, y=90)
b_rd1 = tk.Radiobutton(root, text=kind_of_land[1], variable=int_unit_land_before, value=1)
b_rd1.place(x=70, y=90)
b_rd2 = tk.Radiobutton(root, text=kind_of_land[2], variable=int_unit_land_before, value=2)
b_rd2.place(x=120, y=90)
b_rd3 = tk.Radiobutton(root, text=kind_of_land[3], variable=int_unit_land_before, value=3)
b_rd3.place(x=170, y=90)
b_rd4 = tk.Radiobutton(root, text=kind_of_land[4], variable=int_unit_land_before, value=4)
b_rd4.place(x=220, y=90)
b_rd5 = tk.Radiobutton(root, text=kind_of_land[5], variable=int_unit_land_before, value=5)
b_rd5.place(x=270, y=90)
b_rd6 = tk.Radiobutton(root, text=kind_of_land[6], variable=int_unit_land_before, value=6)
b_rd6.place(x=320, y=90)

#変換後ラベル
l_after = tk.Label(root, text='変換後')
l_after.place(x=20, y=120)

#変換後ラジオボタン
a_rd1 = tk.Radiobutton(root, text=kind_of_land[0], variable=int_unit_land_after, value=0)
a_rd1.place(x=20, y=150)
a_rd1 = tk.Radiobutton(root, text=kind_of_land[1], variable=int_unit_land_after, value=1)
a_rd1.place(x=70, y=150)
a_rd2 = tk.Radiobutton(root, text=kind_of_land[2], variable=int_unit_land_after, value=2)
a_rd2.place(x=120, y=150)
a_rd3 = tk.Radiobutton(root, text=kind_of_land[3], variable=int_unit_land_after, value=3)
a_rd3.place(x=170, y=150)
a_rd4 = tk.Radiobutton(root, text=kind_of_land[4], variable=int_unit_land_after, value=4)
a_rd4.place(x=220, y=150)
a_rd5 = tk.Radiobutton(root, text=kind_of_land[5], variable=int_unit_land_after, value=5)
a_rd5.place(x=270, y=150)
a_rd6 = tk.Radiobutton(root, text=kind_of_land[6], variable=int_unit_land_after, value=6)
a_rd6.place(x=320, y=150)

#計算ボタン
btn_cal = tk.Button(root, text='計算', command=cal)
btn_cal.place(x=180, y=200)

root.mainloop()
