import time
import random as rd
from multiprocessing import Process, Value
import tkinter as tk
import time

li = list(range(65260))
flg = 0

#ずっと動かすメイン抽選
def roulette(n):
    r = rd.randint(0,65259)
    while True:
        for i in li[r:]:
            n.value = i
        for i in li[:r]:
            n.value = i


#tkinterで状態や乱数、出玉などを表示する
def output(n):#ここのｎが変わらんからこの方法では無理か？
    def key_event(e,n):
        if e.keysym == "Down":
            print(n.value)#乱数表示

    def see_n():
        label["text"] = n.value
        root.after(1,see_n)

    root = tk.Tk()
    root.title("test")
    root.geometry("500x500")
    root.bind("<KeyPress>",lambda e:key_event(e,n))
    label = tk.Label(font=("Ubunt Mono",160))
    label.pack()
    see_n()
    root.mainloop()

#プロセスを動かす
if __name__=="__main__":
    n = Value("i",0) #iはintを表す
    p1 = Process(target=roulette, args=(n,))
    p2 = Process(target=output, args=(n,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()