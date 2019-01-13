import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd
import random

# 市町村情報をcsvファイルから読み込み結果を出力
def location_select():
    location = pd.read_csv("location.csv")
    int_num = random.randrange(1741)
    msg.showinfo("目的地", "「" + location.iloc[int_num][0] + " " + location.iloc[int_num][1] + "」" + "に行ってらっしゃい！！")

# ウィンドウの生成
base = tk.Tk()
base.title("Journey")
canvas = tk.Canvas(base, width=150, height=100, bd=0, highlightthickness=0)
canvas.pack()

# ボタンの生成（クリックしてlocation_selectを呼び出す）
btn_load = tk.Button(base, text="旅行", command=location_select)
btn_load.place(x=55, y=45)

base.mainloop()
