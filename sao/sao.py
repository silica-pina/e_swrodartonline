import time
import random as rd
from multiprocessing import Process, Value
import tkinter as tk
import time
import pygame

#音源
pFlash = "pフラ.mp3"


#乱数
li = list(range(64620))
flg = 0

#ずっと動かすメイン抽選
def roulette(n):
    r = rd.randint(0,64619)
    while True:
        for i in li[r:]:
            n.value = i
        for i in li[:r]:
            n.value = i


#tkinterで状態や乱数、出玉などを表示する
random = 1
cnt = 0
flg = 0 #状態を表す 0:通常、1：ST、2：時短、3：cタイム経由時短
now = 0 #現在の差玉
ren = 0 #連荘数
def output(n):
    global random,cnt
    def key_event(e,n):
        global random,cnt,flg
        if e.keysym == "Down":
            random = n.value
            cnt += 1
            label4["text"] = "回転数：" + str(cnt)
            if flg == 0:
                label7["text"] = "通常"
                normal()
            elif flg == 1:
                label7["text"] = "ST中"
                rush()
            elif flg == 2:
                label7["text"] = "時短中"
                timeSaving()
            elif flg == 3:
                label7["text"] = "cタイム時短中"
                c_timeSaving()

    #サウンド
    pygame.mixer.init()
    beep = pygame.mixer.Sound(pFlash)  # Sound に変える
    def sound(mp3):
        beep.play()

    #自分が引いた乱数を表示
    def see_random():
        global random
        label1["text"] = random
        root.after(1,see_random)

    #抽選機の乱数を表示
    def see_n():
        label2["text"] = n.value
        root.after(1,see_n)

    def normal(): #通常
        global random,cnt,flg,now,ren,pFlash
        if random % 319 == 0 and (random/319)%2 == 0:
            sound(pFlash)
            flg = 1
            now += 410
            cnt = 0
            ren += 1
            label3["text"] = "ST"
            label5["text"] = "差玉：" + str(now)
            label8["text"] = "連荘数：" + str(ren)
        elif random % 319 == 0 and (random/319)%2 == 1:
            flg = 2
            now += 410
            cnt = 0
            ren += 1
            label3["text"] = "時短"
            label5["text"] = "差玉：" + str(now)
            label8["text"] = "連荘数：" + str(ren)
        else:
            now -= 15
            label3["text"] = "ハズレ"
            label5["text"] = "差玉：" + str(now)

    def rush():#ST
        global random,cnt,flg,now,ren,pFlash
        if cnt <= 159:
            if random % 98 == 0 or random == 30 or random == 64600: #足りない2つの当たりを適当に追加
                now += 1380
                cnt = 0
                ren += 1
                sound(pFlash)
                label3["text"] = "当たり"
                label5["text"] = "差玉：" + str(now)
                label8["text"] = "連荘数：" + str(ren)
            else:
                label3["text"] = "ハズレ"
                label6["text"] = "残り:" + str(159-cnt)
        else:
            if random % 3 == 0:
                flg = 3
                cnt = 0
                now -= 35 #電サポ減少込み
                label3["text"] = "cタイム当選"
                label5["text"] = "差玉：" + str(now)
            else:
                flg = 0
                ren = 0
                now -= 15
                label3["text"] = "cタイム非当選"
                label5["text"] = "差玉：" + str(now)
                label8["text"] = "連荘数：" + str(ren)

    def timeSaving(): #時短
        global random,cnt,flg,now,ren,pFlash
        if cnt <= 104:
            if random % 319 == 0:
                flg = 1
                cnt = 0
                ren += 1
                now += 1380
                sound(pFlash)
                label3["text"] = "ST"
                label5["text"] = "差玉：" + str(now)
                label8["text"] = "連荘数：" + str(ren)
            else:
                label3["text"] = "ハズレ"
                label6["text"] = "残り:" + str(104-cnt)
        else:
            flg = 0
            ren = 0
            label8["text"] = "連荘数：" + str(ren)

    def c_timeSaving(): #cタイム経由時短
        global random,cnt,flg,now,ren,pFlash
        if cnt <= 115:
            if random % 319 == 0:
                flg = 1
                cnt = 0
                ren += 1
                now += 1380
                sound(pFlash)
                label3["text"] = "ST"
                label5["text"] = "差玉：" + str(now)
                label8["text"] = "連荘数：" + str(ren)
            else:
                label3["text"] = "ハズレ"
                label6["text"] = "残り:" + str(115-cnt)
        else:
            flg = 0
            ren = 0
            label8["text"] = "連荘数：" + str(ren)

    root = tk.Tk()
    root.title("eSwordArtOnline ↓キーで抽選")
    root.geometry("800x1000")
    root.bind("<KeyPress>",lambda e:key_event(e,n))
    label1 = tk.Label(font=("Ubunt Mono",100))
    label2 = tk.Label(font=("Ubunt Mono",100))
    label3 = tk.Label(font=("Ubunt Mono",100))
    label4 = tk.Label(font=("Ubunt Mono",80)) #回転数
    label5 = tk.Label(font=("Ubunt Mono",80)) #差玉
    label6 = tk.Label(font=("Ubunt Mono",80)) #STや時短の残り回転数
    label7 = tk.Label(font=("Ubunt Mono",80)) #状態
    label8 = tk.Label(font=("Ubunt Mono",80)) #連荘数
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    label6.pack()
    label7.pack()
    label8.pack()
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