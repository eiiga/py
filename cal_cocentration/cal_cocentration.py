import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd

#計算して値をメッセージボックスで返す
def result():
    pesticide = (int_total.get() * int_concentration.get()) / 100
    if pesticide > 0:
        msg.showinfo('結果', '農薬を' + str(pesticide) + 'g用意してください')
        df = pd.DataFrame([[str(int_total.get()), str(int_concentration.get()), str(pesticide)]],
                          columns=['total', 'concentration', 'pesticide'])
        df.to_csv("data.csv", mode='a', header=False)
    else:
        msg.showinfo('結果', '入力値を確認してください')

def show():
    sh = pd.read_csv("data.csv", names=['mL', '%', 'g'], usecols=[1, 2, 3])
    root = tk.Tk()
    root.title("計算履歴")
    root_canvas = tk.Canvas(root, width=250, height=150, bd=0, highlightthickness=0)
    l_show = tk.Label(root, text=sh).pack()
    root_canvas.pack()


#ウィンドウの設定
base = tk.Tk()
base.title("濃度計算")
canvas = tk.Canvas(base, width=250, height=150, bd=0, highlightthickness=0)
canvas.pack()

#入力値を保持
int_total = tk.IntVar()
int_concentration = tk.IntVar()

#全量
l_total_water = tk.Label(base, text="全量")
l_total_water.place(x=0, y=30)
tx_total_water = tk.Entry(base, textvariable=int_total)
tx_total_water.place(x=50, y=30)
l_ml = tk.Label(base, text="ml")
l_ml.place(x=180, y=30)

#濃度
l_concentration = tk.Label(base, text="濃度")
l_concentration.place(x=0, y=60)
tx_concentration = tk.Entry(base, textvariable=int_concentration)
tx_concentration.place(x=50, y=60)
l_par = tk.Label(base, text="%")
l_par.place(x=180, y=60)

#計算ボタンの生成
btn_cal = tk.Button(base, text="計算", command=result)
btn_cal.place(x=90, y=90)

btn_show = tk.Button(base, text="履歴", command=show)
btn_show.place(x=90, y=120)

base.mainloop()



