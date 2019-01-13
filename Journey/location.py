import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd
import random


def location_select():
    location = pd.read_csv("location.csv")
    int_num = random.randrange(1741)
    msg.showinfo("目的地", "「" + location.iloc[int_num][0] + " " + location.iloc[int_num][1] + "」" + "に行ってらっしゃい！！")


base = tk.Tk()
base.title("Journey")
canvas = tk.Canvas(base, width=150, height=100, bd=0, highlightthickness=0)
canvas.pack()

btn_load = tk.Button(base, text="旅行", command=location_select)
btn_load.place(x=55, y=45)

base.mainloop()
