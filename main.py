import tkinter
import datetime
from tkinter import *





master = Tk() # anayüz
master.title("Gün Sayar by Krinzy")

simdi = datetime.datetime.now()

canvas = Canvas(master, height=400, width=750)
canvas.pack()

frame_ust = Frame(master, bg='#2f4f4f')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.795, relheight=0.1)

frame_yan = Frame(master, bg='#2f4f4f')
frame_yan.place(relx=0.388, rely=0.20, relwidth=0.23, relheight=0.7)

sinavtipitext = Label(frame_ust, bg='#2f4f4f', text="Olay Tipi", font="Verdaba 12 bold")
sinavtipitext.pack()

sinavtipi = StringVar(frame_ust)
sinavtipi.set("\t")
Yks = str("YKS")
Lgs = str("LGS")
Tatil = str("TATIL")
Secim = str("SECIM")
sinavtipiacilma = OptionMenu(frame_ust, sinavtipi, Yks, Lgs, Secim, Tatil)
sinavtipiacilma.pack(padx=250, pady=1, side=LEFT)

olaytarihi = ""

def update_cevaptext():
    global olaytarihi
    sinavtipiacilma_value = sinavtipi.get()
    if sinavtipiacilma_value == "YKS":
        olaytarihi = "" #simdi + timedelta(days=10)
    cevaptext.config(text=olaytarihi)


    if sinavtipiacilma_value == "LGS":
        olaytarihi = "" #simdi + timedelta(days=10)
    cevaptext.config(text=olaytarihi)

    if sinavtipiacilma_value == "TATIL":
        olaytarihi = "" #simdi + timedelta(days=10)
    cevaptext.config(text=olaytarihi)

    if sinavtipiacilma_value == "SECIM":
        olaytarihi = "AKP GELİYO" #simdi + timedelta(days=10)
    cevaptext.config(text=olaytarihi)


cevaptext = Label(frame_yan, bg='#2f4f4f', text=olaytarihi, font="Verdana 12 bold")
cevaptext.pack()

bilgi = Label(frame_yan, bg='#2f4f4f', text="ÖĞRENİM AMAÇLI.", font="Verdana 12 bold")
bilgi.pack(padx=0, pady=1, side=BOTTOM)

button = Button(frame_yan, text="Güncelle", command=update_cevaptext)
button.pack()

master.mainloop()