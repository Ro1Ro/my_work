#######################интерфейс##################
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import ttk

root = Tk()
root.title("weathernofty")
city = "moskva"
def start():
    global root
    root.destroy()

def sett():
    global root, city, g
    def callback(*arg):
        global city
        city = str(var.get())
    root.destroy()
    root = Tk()
    root.title("Setting")
    chose_t = Label(root, text = "Выберите город")
    towns = ("vladimir", "moskva")
    var = StringVar()
    combobox = ttk.Combobox(values=towns, textvariable = var, state="readonly")
    chose_t.pack()
    combobox.pack()
    var.trace("w", callback)
    #тайминги уведомлений
    #сколько висит уведомлялка
img = ImageTk.PhotoImage(Image.open("icon.png"))
panel = Label(root, image = img)
start_but = Button(root, text = "Start", command = start)
setting_but = Button(root, text = "Setting", command = sett)

panel.pack()
start_but.pack()
setting_but.pack()

root.mainloop()
######################парсинг######################
from bs4 import BeautifulSoup as bs
import requests
import datetime
def time_of_day():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 5:
        b = 0
        tim_day = "Ночь"
    elif hour < 12:
        b = 1
        tim_day = "Утро"
    elif hour < 17:
        b = 2
        tim_day = "День"
    else:
        b = 3
        tim_day = "Вечер"
    return b, tim_day
def parser():
    current_time = datetime.datetime.now()
    day = current_time.day
    
    date = current_time
    date = str(date)[:10]

    moun = ["", "january", "february", "march",
            "april", "may", "june", "july", "august",
            "september", "october", "november", "december"]
    m_n = date[6:-3]
    url = f"https://pogoda.mail.ru/prognoz/{city}/{date[-2:]}-{moun[int(date[6:-3])]}/"
    r = requests.get(url)
    soup = bs(r.content, "html.parser")

    allinfo = soup.findAll('div', class_="day day_period")
  
    b, tim_day = time_of_day()
    text1 = []
    text = ""
    text2 = []

    for i in allinfo[b]:
        texi = i.text
        if len(texi)>1:
            texi = texi.replace("\n", "")
            texi = texi.strip()
            texi = ' '.join(texi.split())
            print("|", texi, "|")
            text1.append(texi)
    for i in range(1, 8):
        if i == 2:
            text0 = text1[i].split()
            print(text0)
            text2.append(text0[0]+", "+text0[1]+" "+text0[2]+" "+text0[3])
        else:
            text2.append(text1[i])
    title_noft = date+" " + tim_day
    text = f"Температура: {text2[0]} Давление: {text2[2]} \nНа улице {text2[1]} \nВлажность воздуха: {text2[-1]} \nСкорость ветра:  {text2[4]}"
    return title_noft, text
###################################Уведомления################################
import time
from plyer import notification
def p():
    print(11)
if __name__ == "__main__":
    while True:
        title_noft, text = parser()
        notification.notify(title = title_noft, message = text, timeout = 10)
        time.sleep(360)
