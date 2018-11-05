import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd

def result():
    sh_exp = pd.read_csv("exp.csv", header=None, index_col=None)
    sh_level = pd.read_csv("level.csv", header=None, index_col=None)
    int_total_exp = int_exp.get() + int(sh_exp.iloc[0][0])
    sh_level.iloc[0][0] = sh_level.iloc[0][0].astype('int')
    int_max_exp = sh_level.iloc[0][0] * 5
    if int_total_exp >= int_max_exp:
        msg.showinfo("お知らせ", "レベルアップ！！")
        int_remains = int_total_exp - int_max_exp
        df_exp = pd.DataFrame([[str(int_remains)]])
        df_exp.to_csv("exp.csv", index=False, header=False)
        int_level = sh_level.iloc[0][0] + 1
        df_level = pd.DataFrame([[str(int_level)]])
        df_level.to_csv("level.csv", index=False, header=False)
    else:
        int_rest_exp = int_max_exp - int_total_exp
        msg.showinfo("お知らせ", "次のレベルまで" + str(int_rest_exp))
        df_exp = pd.DataFrame([[str(int_total_exp)]])
        df_exp.to_csv("exp.csv", index=False, header=False)

def load():
    sh_level = pd.read_csv("level.csv", header=None, index_col=None)
    l_level_num = tk.Label(base, text=str(sh_level.iloc[0][0]))
    l_level_num.place(x=100, y=30)


#ウィンドウの設定
base = tk.Tk()
base.title("Level")
canvas = tk.Canvas(base, width=250, height=150, bd=0, highlightthickness=0)
canvas.pack()

#初期値
l_name = tk.Label(base, text="エイ")
l_name.place(x=30, y=30)
l_level = tk.Label(base, text="Lv.：")
l_level.place(x=70, y=30)

#入力値を保持
int_exp = tk.IntVar()

#経験値
l_exp = tk.Label(base, text="経験値")
l_exp.place(x=0, y=60)
tx_exp = tk.Entry(base, textvariable=int_exp)
tx_exp.place(x=50, y=60)
btn_exp = tk.Button(base, text="セーブ", command=result)
btn_exp.place(x=150, y=90)

#ロード
btn_load = tk.Button(base, text="ロード", command=load)
btn_load.place(x=90, y=90)

base.mainloop()
