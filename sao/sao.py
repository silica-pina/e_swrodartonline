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
cnt = 0
def output(n):#ここのｎが変わらんからこの方法では無理か？
    global random
    def key_event(e,n):
        global random,cnt
        if e.keysym == "Down":
            random = n.value
            print(random)#乱数表示
            cnt += 1
            label4["text"] = cnt

    def see_random():
        global random
        label1["text"] = random
        root.after(1,see_random)

    def see_n():
        label2["text"] = n.value
        root.after(1,see_n)

    def judge():
        global random,cnt
        if random % 204 == 0 and random % 2 == 0:
            label3["text"] = "確変"
        elif random % 204 == 0 and random % 2 == 1:
            label3["text"] = "時短"
        else:
            label3["text"] = "ハズレ"
        root.after(1,judge)

    root = tk.Tk()
    root.title("test")
    root.geometry("500x700")
    root.bind("<KeyPress>",lambda e:key_event(e,n))
    label1 = tk.Label(font=("Ubunt Mono",110))
    label2 = tk.Label(font=("Ubunt Mono",110))
    label3 = tk.Label(font=("Ubunt Mono",110))
    label4 = tk.Label(font=("Ubunt Mono",80))
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    see_random()
    see_n()
    judge()
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