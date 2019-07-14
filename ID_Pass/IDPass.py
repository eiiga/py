import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import tkinter.messagebox as msg

def top():
    def finish():
        base.destroy()

    def goto_insert():
        base.destroy()
        new_insert()

    def search_all():
        df = pd.read_csv("IDPass.csv")
        # df_exact = df[df['Item'] == String_search_data.get()]
        tree.delete(*tree.get_children())
        for i in range(len(df)):
            tree.insert("", "end", values=(df.iloc[i][0], df.iloc[i][1], df.iloc[i][2]))

    def search_id_pass():
        try:
            df = pd.read_csv("IDPass.csv")
            df_exact = df[df['Item'] == String_search_data.get()]
            tx_String_ID.delete(0, tk.END)
            tx_String_Pass.delete(0, tk.END)
            tx_String_ID.insert(tk.END, df_exact.iloc[0][1])
            tx_String_Pass.insert(tk.END, df_exact.iloc[0][2])
        except:
            msg.showinfo("お知らせ", "データがありません")

    # ウィンドウの設定
    base = tk.Tk()
    base.title("ID・Pass検索")
    canvas = tk.Canvas(base, width=550, height=500, bd=0, highlightthickness=0)
    canvas.pack()

    # タイトルラベル
    l_title = tk.Label(base, text="ID・Pass検索")
    l_title.place(x=200, y=30)

    #入力値を保持
    String_search_data = tk.StringVar()

    #検索フォーム
    tx_String_search_data = tk.Entry(base, textvariable=String_search_data)
    tx_String_search_data.place(x=140, y=60)
    btn_search_data = tk.Button(base, text="検索", command=search_id_pass)
    btn_search_data.place(x=350, y=65)

    # 検索結果フォーム
    tx_String_ID = tk.Entry(base)
    tx_String_ID.place(x=30, y=120)
    tx_String_Pass = tk.Entry(base)
    tx_String_Pass.place(x=250, y=120)

    # 全件検索
    btn_search_all = tk.Button(base, text="全件検索", command=search_all)
    btn_search_all.place(x=220, y=180)

    # Treeviewの設定
    tree = ttk.Treeview(base, columns=(0, 1, 2))
    tree["show"] = "headings"
    tree.column(0, width=100)
    tree.column(1, width=200)
    tree.column(2, width=200)
    tree.heading(0, text='項目')
    tree.heading(1, text='ID')
    tree.heading(2, text='Pass')
    tree.place(x=10, y=220)

    # 新規作成ボタン
    btn_insert = tk.Button(base, text="新規", command=goto_insert)
    btn_insert.place(x=100, y=450)

    # 終了ボタン
    btn_finish = tk.Button(base, text="終了", command=finish)
    btn_finish.place(x=350, y=450)

    base.mainloop()

def new_insert():
    def finish():
        base.destroy()

    def goto_top():
        base.destroy()
        top()

    def value_insert():
        df = pd.DataFrame([String_insert_koumoku.get(), String_insert_ID.get(), String_insert_pass.get()])
        df.to_csv("IDPass.csv")
        msg.showinfo("お知らせ", "新規追加が完了しました")

    base = tk.Tk()
    base.title("ID・Pass検索")
    canvas = tk.Canvas(base, width=500, height=500, bd=0, highlightthickness=0)
    canvas.pack()

    # タイトルラベル
    l_title = tk.Label(base, text="新規作成")
    l_title.place(x=200, y=30)

    #入力値を保持
    String_insert_koumoku = tk.StringVar()
    String_insert_ID = tk.StringVar()
    String_insert_pass = tk.StringVar()

    #検索フォーム
    tx_String_insert_koumoku = tk.Entry(base, textvariable=String_insert_koumoku)
    tx_String_insert_koumoku.place(x=140, y=60)
    tx_String_insert_ID = tk.Entry(base, textvariable=String_insert_ID)
    tx_String_insert_ID.place(x=140, y=90)
    tx_String_insert_pass = tk.Entry(base, textvariable=String_insert_pass)
    tx_String_insert_pass.place(x=140, y=120)
    btn_insert_data = tk.Button(base, text="新規追加", command=value_insert)
    btn_insert_data.place(x=200, y=150)

    # 戻るボタン
    btn_insert = tk.Button(base, text="戻る", command=goto_top)
    btn_insert.place(x=100, y=450)

    # 終了ボタン
    btn_finish = tk.Button(base, text="終了", command=finish)
    btn_finish.place(x=350, y=450)

    base.mainloop()

top()
