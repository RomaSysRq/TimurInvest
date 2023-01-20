import tkinter
from tkinter import *
from tkinter import Menu
from PIL import Image, ImageTk
import pickledb
db = pickledb.load('text.db', True)
amount = db.get('amount')
window = Tk()
window.title("Тимур Инвестиции 1.0")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.configure(bg='#34b4eb')
window.geometry("1000x500")
ico = Image.open('icon.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
def exit():
    window.destroy()
def add():
    amount = db.get('amount')
    money = db.get(cardnum)
    if money >= 13:
        amount = amount + 1
        money = money - 13
        money1['text'] = str(money) + ' руб.'
    else:
        window.destroy()
    if amount == 0:
        amount = 0
        print(2312)
        db.set('amount', amount)
        window.destroy()
    trade_amount['text'] = str(amount)
    money1['text'] = str(money) + ' руб.'
    db.set('amount', amount)
def minus():
    amount = db.get('amount')
    money = db.get(cardnum)
    amount = amount - 1
    if amount < 0:
        amount = 0
        print(2312)
        db.set('amount', amount)
        window.destroy()
    money = money + 14
    trade_amount['text'] = str(amount)
    money1['text'] = str(money) + ' руб.'
    db.set('amount', amount)
def add1():
    try:
        money = db.get(cardnum)
    except:
        money1['text'] = 'Нету карты'
    money = money + 1
    db.set(cardnum, money)
    money1['text'] = str(money) + ' руб.'
def minus1():
    money = db.get(cardnum)
    money = money - 1
    if money == 0:
        money = 0
        window.destroy()
    db.set(cardnum, money)
    money1['text'] = str(money) + ' руб.'
def cardadd():
    s = card1.get(1.0, END)
    if not db.get(s):
        db.set(str(s), 0)
    global cardnum
    cardnum = str(s)
    money = db.get(cardnum)
    money1['text'] = str(money) + ' руб.'
    


frame_center = Frame()
hello = Label(text='Здравствуйте!', fg='white', bg='red', font="Courier 20")
frame_card = Frame(bg='green')
card_ot = Label(frame_card, text=' ', fg='white', bg='green')
card = Label(frame_card, text='Номер карты', fg='white', bg='green')
card1 = Text(frame_card, height=1, width=16)
card5 = Label(frame_card, text='Срок', fg='white', bg='green')
card2 = Text(frame_card, height=1, width=4)
card4 = Label(frame_card, text='CVV', fg='white', bg='green')
card3 = Text(frame_card, height=1, width=3)
test = Button(frame_card, text='Привязать', bg='#4e5052', fg='white', command=cardadd)
vix = Button(frame_center,text='Выход', bg='#4e5052', fg='white', command=exit)
frame_trade = Frame(bg='yellow')
trade_kir_label = Label(frame_trade, text='Курс',bg='yellow')
trade_kir = Label(frame_trade, text='12~14 руб.',bg='#4e5052', fg='white')
trade_buy = Button(frame_trade, text='Купить',bg='green', fg='white', command=add)
trade_sell = Button(frame_trade, text='Продать',bg='red', fg='white', command=minus)
trade_amount_label = Label(frame_trade, text='Кол-во',bg='yellow')
trade_amount = Label(frame_trade, text='0',bg='#4e5052', fg='white')
money_label = Label(frame_center, text='Добавить деньги')
money1 = Label(frame_center, text='0',bg='#4e5052', fg='white')
money_plus = Button(frame_center, text='Добавить 1',bg='green', fg='white', command=add1)
money_minus = Button(frame_center, text='Снять 1',bg='red', fg='white', command=minus1)





hello.pack()
frame_center.pack(side=BOTTOM)
money_label.pack()
money1.pack()
money_plus.pack(anchor='w', padx=20, side=LEFT)
money_minus.pack(anchor='e', padx=20, side=RIGHT)
frame_card.pack(side=LEFT, anchor='w')
card_ot.pack(anchor='w', padx=20,pady=10)
card.pack(anchor='w', padx=20)
card1.pack(anchor='w', padx=20)
card5.pack(anchor='w', padx=20)
card2.pack(anchor='w', padx=20)
card4.pack(anchor='w', padx=20)
card3.pack(anchor='w', padx=20)
test.pack(anchor='w',pady=20, padx=20)
vix.pack(ipadx=10, ipady=10)
frame_trade.pack(side=RIGHT)
trade_kir_label.pack(anchor='center', padx=20,pady=10)
trade_kir.pack(pady=5)
trade_buy.pack(anchor='w', padx=20, side=LEFT)
trade_sell.pack(anchor='e', padx=20, side=RIGHT)
trade_amount_label.pack(padx=20)
trade_amount.pack(padx=20)

money1['text'] = '0 руб.'
trade_amount['text'] = str(amount)
window.mainloop()
