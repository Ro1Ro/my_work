#################################==Как этим пользоваться?==#################################
'''
    1. Выбираем шифр (Цезаря/Виженера).
    2. Что делаем?(Шифруем/Дешифруем).
    3. Введите в первую строку ваш текст:
        --- Знаки препинания (".", ",", "!", "?").
        --- Цифры.
        --- Пробелы.
        Допустимы, но их перевод НЕ будет осуществлен.
        Вы можете одновременно ввести текст на латинице и кирилице (Покупайте bitcoinы).
    4. Введите код по которому нужно зашифровать/дешифровать текст.
        Шифр Цезаря:
            Код:
            --- Допустимы лишь числа от 1 до 33 (Включительно).
        Шифр Виженера:
            Код:
            --- Допустимы лишь символы кирилицы и/или латиницы
    5. Нажмите кнопку "==Защифровать=="/"==Дешифровать=="
    Прим.
        Если результат не виден, то откройте программу в полноэкранном режиме.
'''
#################################==Импорт библеотек(0IB1^0IB2)==#################################

from tkinter import *
print("0IB1&1")

from tkinter import messagebox as mb
print("0IB2&1")

#################################==Функция перевода Цезарь(0FNZE)==#################################

def trans_cezari(a, b):
    
    letters_eng_up = ["A", "B", "C", "D", "E",
                  "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O",
                  "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y",
                  "Z"]

    letters_eng_down = ["a", "b", "c", "d", "e",
                      "f", "g", "h", "i", "j",
                      "k", "l", "m", "n", "o",
                      "p", "q", "r", "s", "t",
                      "u", "v", "w", "x", "y",
                      "z"]

    letters_rus_up = ['А', 'Б', 'В', 'Г', 'Д',
                     'Е', 'Ё', 'Ж', 'З', 'И',
                     'Й', 'К', 'Л', 'М', 'Н',
                     'О', 'П', 'Р', 'С', 'Т',
                     'У', 'Ф', 'Х', 'Ц', 'Ч',
                     'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
                     'Э', 'Ю', 'Я']

    letters_rus_down = ['а', 'б', 'в', 'г', 'д',
                       'е', 'ё', 'ж', 'з', 'и',
                       'й', 'к', 'л', 'м', 'н',
                       'о', 'п', 'р', 'с', 'т',
                       'у', 'ф', 'х', 'ц', 'ч',
                       'ш', 'щ', 'ъ', 'ы', 'ь',
                       'э', 'ю', 'я']
    print("0FNZELETT1")
    
    c = []
    
    for i in a:
        if (i in letters_eng_up):
            c.append(letters_eng_up[(letters_eng_up.index(i)+b)%len(letters_eng_up)])
        elif (i in letters_eng_down):
            c.append(letters_eng_down[(letters_eng_down.index(i)+b)%len(letters_eng_down)])
        elif (i in letters_rus_up):
            c.append(letters_rus_up[(letters_rus_up.index(i)+b)%len(letters_rus_up)])
        elif (i in letters_rus_down):
            c.append(letters_rus_down[(letters_rus_down.index(i)+b)%len(letters_rus_down)])        
        else:
            c.append(i)
            
    print("0FNZERET1&"+''.join(c))
    return "".join(c)

#################################==Функция перевода Виженер(0FNVIZH)==#################################

def trans_vizhener(a, b, per):
    
    key_num = []
    
    letters_eng_up = ["A", "B", "C", "D", "E",
                      "F", "G", "H", "I", "J",
                      "K", "L", "M", "N", "O",
                      "P", "Q", "R", "S", "T",
                      "U", "V", "W", "X", "Y",
                      "Z"]

    letters_eng_down = ["a", "b", "c", "d", "e",
                      "f", "g", "h", "i", "j",
                      "k", "l", "m", "n", "o",
                      "p", "q", "r", "s", "t",
                      "u", "v", "w", "x", "y",
                      "z"]

    letters_rus_up = ['А', 'Б', 'В', 'Г', 'Д',
                     'Е', 'Ё', 'Ж', 'З', 'И',
                     'Й', 'К', 'Л', 'М', 'Н',
                     'О', 'П', 'Р', 'С', 'Т',
                     'У', 'Ф', 'Х', 'Ц', 'Ч',
                     'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
                     'Э', 'Ю', 'Я']

    letters_rus_down = ['а', 'б', 'в', 'г', 'д',
                        'е', 'ё', 'ж', 'з', 'и',
                        'й', 'к', 'л', 'м', 'н',
                        'о', 'п', 'р', 'с', 'т',
                        'у', 'ф', 'х', 'ц', 'ч',
                        'ш', 'щ', 'ъ', 'ы', 'ь',
                        'э', 'ю', 'я']
    
    print("0FNVIZHLETT1")
    
    for i in b:
        if (i in letters_eng_up):
            key_num.append(letters_eng_up.index(i)+1)
        if (i in letters_eng_down):
            key_num.append(letters_eng_down.index(i)+1)
        if (i in letters_rus_up):
            key_num.append(letters_rus_up.index(i)+1)
        if (i in letters_rus_down):
            key_num.append(letters_rus_down.index(i)+1)
            
    num = 0
    
    print("0FNVIZHKEY1")
    
    c = []
    
    for i in a:
        if (i in letters_eng_up) and per == 0:
            c.append(letters_eng_up[(letters_eng_up.index(i)+key_num[num%len(key_num)])%len(letters_eng_up)])
            num+=1
        elif (i in letters_eng_down) and per == 0:
            c.append(letters_eng_down[(letters_eng_down.index(i)+key_num[num%len(key_num)])%len(letters_eng_down)])
            num+=1
        elif (i in letters_rus_up) and per == 0:
            c.append(letters_rus_up[(letters_rus_up.index(i)+key_num[num%len(key_num)])%len(letters_rus_up)])
            num+=1
        elif (i in letters_rus_down) and per == 0:
            c.append(letters_rus_down[(letters_rus_down.index(i)+key_num[num%len(key_num)])%len(letters_rus_down)])
            num+=1
        elif (i in letters_eng_up) and per == 1:
            c.append(letters_eng_up[(letters_eng_up.index(i)-key_num[num%len(key_num)])%len(letters_eng_up)])
            num+=1
        elif (i in letters_eng_down) and per == 1:
            c.append(letters_eng_down[(letters_eng_down.index(i)-key_num[num%len(key_num)])%len(letters_eng_down)])
            num+=1
        elif (i in letters_rus_up) and per == 1:
            c.append(letters_rus_up[(letters_rus_up.index(i)-key_num[num%len(key_num)])%len(letters_rus_up)])
            num+=1
        elif (i in letters_rus_down) and per == 1:
            c.append(letters_rus_down[(letters_rus_down.index(i)-key_num[num%len(key_num)])%len(letters_rus_down)])
            num+=1
        else:
            c.append(i)
            
    print("0FNVIZHRET1&"+"".join(c))
    return "".join(c)

#################################==Запуск tkinter==#################################
    
def start():
    
    global root
    
    def menu_0():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Цезарь или Виженер')
        
        cezari_but = Button(root, text = "====Шифр Цезаря====", command = menu_cezari_0)
        cezari_but.place(relx = 0.12, rely = 0.25)
        
        vizhner_but = Button(root, text = "===Шифр Виженера===", command = menu_vizhner_0)
        vizhner_but.place(relx = 0.12, rely = 0.50)
        
        print("0FNMENU1")
        root.mainloop()
        
#################################==Цезарь==#################################

    def menu_cezari_0():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Цезарь')
        
        shifrovat_cezari = Button(root, text = "===Шифровать===", command = menu_cezari_0_0)
        shifrovat_cezari.place(relx = 0.20, rely = 0.20)
        
        deshifrovat_cezari = Button(root, text = "==Дешифровать==", command = menu_cezari_0_1)
        deshifrovat_cezari.place(relx = 0.21, rely = 0.45)
        
        m = Button(root, text = "=Вернуться в меню=", command = menu_0)
        m.place(relx = 0.20, rely = 0.70)
        
        print("0FNMENUCEZ1")
        root.mainloop()
        
    def menu_cezari_0_0():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Цезарь Шифровать')
        
        text_z = StringVar()
        key_z = StringVar()
        
        text_label = Label(text="Введите текст:")
        text_label.place(relx = 0.20, rely = 0.10)
        text = Entry(root, textvariable = text_z)
        text.place(relx = 0.20, rely = 0.20)
        
        key_label = Label(text="Введите ключ:")
        key_label.place(relx = 0.20, rely = 0.30)
        key = Entry(root, textvariable = key_z)
        key.place(relx = 0.20, rely = 0.40)
        
        
        end = Button(root, text = "=Зашифровать=", command = lambda: re(text_z.get(), key_z.get(), 0, 0))
        end.place(relx = 0.05, rely = 0.80)
        
        m = Button(root, text = "=В меню=", command = menu_0)
        m.place(relx = 0.60, rely = 0.80)
        
        print("0FNMENUCEZ1&0")
        root.mainloop()
        
        
    def menu_cezari_0_1():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Цезарь Дешифровать')
        
        text_z = StringVar()
        key_z = StringVar()
        
        text_label = Label(text="Введите текст:")
        text_label.place(relx = 0.20, rely = 0.10)
        text = Entry(root, textvariable = text_z)
        text.place(relx = 0.20, rely = 0.20)
        
        key_label = Label(text="Введите ключ:")
        key_label.place(relx = 0.20, rely = 0.30)
        key = Entry(root, textvariable = key_z)
        key.place(relx = 0.20, rely = 0.40)    

        end = Button(root, text = "=Дешифровать=", command = lambda: re(text_z.get(), key_z.get(), 1, 0))
        end.place(relx = 0.05, rely = 0.80)
        
        m = Button(root, text = "=В меню=", command = menu_0)
        m.place(relx = 0.60, rely = 0.80)
        
        print("0FNMENUCEZ1&1")
        root.mainloop()
        
    
#################################==Виженера==#################################

    def menu_vizhner_0():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Виженер')
        
        shifrovat_vizhner = Button(root, text = "===Шифровать===", command = menu_vizhner_0_0)
        shifrovat_vizhner.place(relx = 0.20, rely = 0.20)
        
        deshifrovat_vizhner = Button(root, text = "==Дешифровать==", command = menu_vizhner_0_1)
        deshifrovat_vizhner.place(relx = 0.21, rely = 0.45)
        
        m = Button(root, text = "=Вернуться в меню=", command = menu_0)
        m.place(relx = 0.20, rely = 0.70)
        
        print("0FNMENUVIZH1")
        root.mainloop()
        
    def menu_vizhner_0_0():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Виженера Шифровать')
        
        text_z = StringVar()
        key_z = StringVar()
        
        text_label = Label(text="Введите текст:")
        text_label.place(relx = 0.20, rely = 0.10)
        text = Entry(root, textvariable = text_z)
        text.place(relx = 0.20, rely = 0.20)
        
        key_label = Label(text="Введите ключ:")
        key_label.place(relx = 0.20, rely = 0.30)
        key = Entry(root, textvariable = key_z)
        key.place(relx = 0.20, rely = 0.40)
        
        end = Button(root, text = "=Зашифровать=", command = lambda: re(text_z.get(), key_z.get(), 0, 1))
        end.place(relx = 0.05, rely = 0.80)
        
        m = Button(root, text = "=В меню=", command = menu_0)
        m.place(relx = 0.60, rely = 0.80)
        
        print("0FNMENUVIZH1&0")
        root.mainloop()
        
    def menu_vizhner_0_1():
        
        global root
        root.destroy()
        root = Tk()
        root.title('Виженера Дешифровать')
        
        text_z = StringVar()
        key_z = StringVar()

        text_label = Label(text="Введите текст:")
        text_label.place(relx = 0.20, rely = 0.10)
        text = Entry(root, textvariable = text_z)
        text.place(relx = 0.20, rely = 0.20)
        
        key_label = Label(text="Введите ключ:")
        key_label.place(relx = 0.20, rely = 0.30)
        key = Entry(root, textvariable = key_z)
        key.place(relx = 0.20, rely = 0.40)
        
        end = Button(root, text = "=Дешифровать=", command = lambda: re(text_z.get(), key_z.get(), 1, 1))
        end.place(relx = 0.05, rely = 0.80)
        
        m = Button(root, text = "=В меню=", command = menu_0)
        m.place(relx = 0.60, rely = 0.80)
        
        print("0FNMENUVIZH1&1")
        root.mainloop()
        
#################################==Проверка введеных символов==#################################
    def re(a, b, per, shiphr):
        
        letters_eng_up = ["A", "B", "C", "D", "E",
                      "F", "G", "H", "I", "J",
                      "K", "L", "M", "N", "O",
                      "P", "Q", "R", "S", "T",
                      "U", "V", "W", "X", "Y",
                      "Z"]

        letters_eng_down = ["a", "b", "c", "d", "e",
                        "f", "g", "h", "i", "j",
                        "k", "l", "m", "n", "o",
                        "p", "q", "r", "s", "t",
                        "u", "v", "w", "x", "y",
                        "z"]

        letters_rus_up = ['А', 'Б', 'В', 'Г', 'Д',
                             'Е', 'Ё', 'Ж', 'З', 'И',
                             'Й', 'К', 'Л', 'М', 'Н',
                             'О', 'П', 'Р', 'С', 'Т',
                             'У', 'Ф', 'Х', 'Ц', 'Ч',
                             'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
                             'Э', 'Ю', 'Я']

        letters_rus_down = ['а', 'б', 'в', 'г', 'д',
                                'е', 'ё', 'ж', 'з', 'и',
                                'й', 'к', 'л', 'м', 'н',
                                'о', 'п', 'р', 'с', 'т',
                                'у', 'ф', 'х', 'ц', 'ч',
                                'ш', 'щ', 'ъ', 'ы', 'ь',
                                'э', 'ю', 'я']
        c = 1
        for i in a:
            
            if 97 <= ord(i) <= 122 or 1072 <= ord(i) <= 1103 or ord(i) == 32 or ord(i) in [ord("."), ord(","), ord("!"), ord("?")] or ord("A") <= ord(i) <= ord("Z") or ord("А") <= ord(i) <= ord("Я") or ord("0") <= ord(i) <= ord("9"):
                continue
            else:
                msg = f'Неверный символ в первой строке, повторите ввод текста({i}) \n (Допустимые символы: ".", ",", "!", "?", а также все символы кирилицы, латиницы и цифр)'
                mb.showwarning(f"Ошибка: IN00SYM1{i}", msg)
                c = 0
                break
            
        if len(b) in [1, 2] and shiphr == 0:
            
            for i in b:
                
                if ord('0') <= ord(i) <= ord('9'):
                    continue
                else:
                    msg = 'Неверный код. \n (Можно ввести лишь цифры)'
                    mb.showwarning("Ошибка: IN1COD2SYMCEZ", msg)
                    c = 0
                    break
                
            else:
                
                if 1 <= int(b) <= 33:
                    pass
                else:
                    msg = 'Неверный код. \n (Допустимые числа от 1 до 33)'
                    mb.showwarning("Ошибка: IN2COD2NUMCEZ", msg)
                    c = 0
            
        else:

            if shiphr == 0:
                msg = 'Неверный код. \n (Допустимые числа от 1 до 33)'
                mb.showwarning("Ошибка: IN2COD2LENCEZ", msg)
                c = 0
            elif shiphr == 1:
                
                for i in b:
                    
                    if i in letters_eng_up or i in letters_eng_down or i in letters_rus_down or i in letters_rus_up:
                        c = 1
                    else:
                        msg = 'Неверный код. \n (Недопустимый символ)'
                        mb.showwarning("Ошибка: IN2COD2VIZHERRSYM&IN2COD2VIZHNUM", msg)
                        c = 0
                        
                if len(b) == 0:
                    
                    msg = 'Неверный код. \n (Пустой ввод)'
                    mb.showwarning("Ошибка: IN2COD2VIZHNONE", msg)
                    c = 0
                    
        if c == 1 and per == 0 and shiphr == 0:
            l = trans_cezari(a, int(b))
            result_label = Label(text="Результат:")
            result_label.place(relx = 0.20, rely = 0.50)
            res_label = Label(text = " "*500, font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            res_label = Label(text = l, fg = "red", font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            print("0FNMENUCEZTRANS1")
            
        elif c == 1 and per == 1 and shiphr == 0:
            l = trans_cezari(a, -int(b))
            result_label = Label(text="Результат:")
            result_label.place(relx = 0.20, rely = 0.50)
            res_label = Label(text = " "*500, font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            res_label = Label(text = l, fg = "red", font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            print("0FNMENUCEZTRANS2")
            
        elif c == 1 and per == 0 and shiphr == 1:
            l = trans_vizhener(a, b, per)
            result_label = Label(text="Результат:")
            result_label.place(relx = 0.20, rely = 0.50)
            res_label = Label(text = " "*500, font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            res_label = Label(text = l, fg = "red", font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            print("0FNMENUVIZHTRANS1")
            
        elif c == 1 and per == 1 and shiphr == 1:
            l = trans_vizhener(a, b, per)
            result_label = Label(text="Результат:")
            result_label.place(relx = 0.20, rely = 0.50)
            res_label = Label(text = " "*500, font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            res_label = Label(text = l, fg = "red", font = "Arial 14")
            res_label.place(relx = 0.20, rely = 0.60)
            print("0FNMENUVIZHTRANS2")

#################################==Стартовая Точка==#################################
    
    root = Tk()
    root.title('Цезарь или Виженер')
    
    cezari_but = Button(root, text = "====Шифр Цезаря====", command = menu_cezari_0)
    cezari_but.place(relx = 0.12, rely = 0.25)
    
    vizhner_but = Button(root, text = "===Шифр Виженера===", command = menu_vizhner_0)
    vizhner_but.place(relx = 0.12, rely = 0.50)
    
    print("0FNMENU0")
    
    root.mainloop()
    
start()


