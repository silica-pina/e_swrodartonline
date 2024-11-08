import time
import random as rd
from multiprocessing import Process
import tkinter as tk

li = list(range(65260))
flg = 0

#ずっと動かすメイン抽選
def roulette(self):
    r = rd.randint(0,65259)
    for i in li[r:]:
        continue
    for i in li[:r]:
        continue

def key_event(e):
    if e.keysym == "Down":
        print("↓キーを押すと乱数取得する操作を書く")

#tkinterで状態や乱数、出玉などを表示する
def output(self):
    root = tk.Tk()
    root.title("test")
    root.geometry("500x500")
    root.bind("<KeyPress>",key_event)
    root.mainloop()

#プロセスを動かす
if __name__=="__main__":
    p1 = Process(target=roulette, args=(1,))
    p2 = Process(target=output, args=(2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()