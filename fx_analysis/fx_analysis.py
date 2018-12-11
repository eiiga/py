import numpy as np
from sklearn import linear_model
import tkinter as tk
import tkinter.messagebox as msg


def analysis():
    x = np.array([[112.68], [113.408], [113.727], [113.996], [113.649], [114.484], [113.892], [113.758], [113.178],
                 [112.973], [112.271], [112.135],[112.161], [111.78], [112.294], [112.69], [112.189], [112.537],
                 [112.819], [112.42], [112.148], [112.382], [111.869], [112.347], [113.087], [112.933], [112.648]])

    y = np.array([113.407, 113.624, 113.999, 113.649, 114.484, 113.893, 113.675, 113.179, 112.973, 112.274, 112.149,
                  112.21, 111.782, 112.294, 112.691, 112.189, 112.537, 112.82, 112.418, 112.157, 112.381, 111.814, 112.347,
                  113.086, 112.933, 112.652, 113.214])

    lr = linear_model.LinearRegression()

    lr.fit(x, y)

    # 係数(0.78)
    # print(lr.coef_)
    a = 0.78381451

    # 切片24.4
    # print(lr.intercept_)
    b = 24.4

    num = int_fx_num.get()

    result = a * float(num) + b

    msg.showinfo("お知らせ", result)


# ウィンドウの設定
base = tk.Tk()
base.title("FX-analysis")
canvas = tk.Canvas(base, width=250, height=150, bd=0, highlightthickness=0)
canvas.pack()

# 初期値
l_name = tk.Label(base, text="値を入力して下さい。")
l_name.place(x=60, y=30)

# 入力値を保持
int_fx_num = tk.IntVar()

# 値
tx_exp = tk.Entry(base, textvariable=int_fx_num)
tx_exp.place(x=30, y=60)
btn_exp = tk.Button(base, text="解析", command=analysis)
btn_exp.place(x=100, y=90)

base.mainloop()
