import tkinter as tk
import tkinter.messagebox as msg

def cal():
    value_m = value_cm.get() / 100
    value_bmi = value_kg.get() / (value_m * value_m )
    msg.showinfo("BMI", "あなたのBMIは" + str(value_bmi) + "です！" )


# 表示画面の骨組み
base = tk.Tk()
base.title("BMI計算")
canvas = tk.Canvas(base, width=200, height=150, bd=0, highlightthickness=0)
canvas.pack()

# 値の保持
value_cm = tk.IntVar()
value_kg = tk.IntVar()

# 身長入力
l_height = tk.Label(base, text="身長（cm）")
l_height.place(x=30, y=30)
t_height = tk.Entry(base, textvariable=value_cm, justify="right", width=5)
t_height.place(x=100, y=30)

# 体重入力
l_weight = tk.Label(base, text="体重（kg）")
l_weight.place(x=30, y=70)
t_weight = tk.Entry(base, textvariable=value_kg, justify="right", width=5)
t_weight.place(x=100, y=70)

# 計算
btn_cal = tk.Button(base, text="計算", command=cal)
btn_cal.place(x=90, y=110)

base.mainloop()
