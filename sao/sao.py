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
random = 0
def output(n):#ここのｎが変わらんからこの方法では無理か？
    global random
    def key_event(e,n):
        global random
        if e.keysym == "Down":
            random = n.value
            print(random)#乱数表示

    def see_random():
        global random
        label1["text"] = random
        root.after(1,see_random)

    def see_n():
        label2["text"] = n.value
        root.after(1,see_n)

    root = tk.Tk()
    root.title("test")
    root.geometry("500x500")
    root.bind("<KeyPress>",lambda e:key_event(e,n))
    label1 = tk.Label(font=("Ubunt Mono",130))
    label2 = tk.Label(font=("Ubunt Mono",130))
    label1.pack()
    label2.pack()
    see_random()
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