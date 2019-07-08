from tkinter import Tk, Label, Frame, Button, Entry, Canvas, PhotoImage, Listbox
import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import ttk
import os
import os.path
import urllib.request
import urllib.parse
import urllib.error
import ssl
import ast
import json
import os
from urllib.request import Request, urlopen
import datetime
import requests 

 

def load_json():
    file = open('stocks.json', 'r')
    people = json.loads(file.read())            
    file.close() 
    return people
def load_todo():
    file = open('todo.json', 'r')
    p = json.loads(file.read())
    file.close()
    return p
def dump_json(p):
    file = open('stocks.json', 'w')
    file.write(json.dumps(p, indent = 8))
    file.close()
def dump_todo(p):
    file = open('todo.json','w')
    file.write(json.dumps(p,indent=1))
    file.close()
def loadTable():
    stocks = []
    stocks = load_json()   
    for i in listbox.get_children():
        listbox.delete(i)
    for s in stocks:
        listbox.insert('', '0', values=(str(s['Symbol']),str(s['Price']),str(s['Open']),str(s['PE']),str(s['EPS']),str(s['Close']),str(s['Volume']),str(s['Div/Yield'])))
def loadTodo():
    todos = []
    todos = load_todo()
    listbox3.delete('0','end')
    for s in todos:
        listbox3.insert(0,s['Todo'] + '   -   Due: ' + s['Date'])
def addStock():
    stock = []
    stocks = {
        'Symbol':str(stock_symbol['text']),
        'Price':str(stock_price['text']),
        'Open':str(stock_open['text']),
        'PE':str(stock_high['text']),
        'EPS':str(stock_low['text']),
        'Close':str(stock_close['text']),
        'Volume':str(stock_volume['text']),
        'Div/Yield':str(stock_adj_close['text'])
    }
    file = open('stocks.json', 'r')
    ok = file.read()
    if ok != '[]' and ok == '':
        dump_json(stock)          
    stock = load_json()           
    stock.append(stocks)
    dump_json(stock)
    loadTable()
def addToDo():
    todo = []
    todos = {
        'Todo':str(todo_input.get().upper()),
        'Date':str(todo2_input.get())
    }
    file = open('todo.json','r')
    ok = file.read()
    if ok != '[]' and ok == '':
        dump_todo(todo)          
    todo = load_todo()           
    todo.append(todos)
    dump_todo(todo)
    todo_input.delete(0,'end')
    todo2_input.delete(0,'end')
    loadTodo()             
def findStock():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'https://finance.yahoo.com/quote/' + stock_symbol_input.get().upper() + '?p=' + stock_symbol_input.get().upper()
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    html = soup.prettify('utf-8')
    company_json={}
    other_details = {}
    for span in soup.findAll('span',
                         attrs={'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'
                         }):
        company_json['PRESENT_VALUE'] = span.text.strip()
    for div in soup.findAll('div', attrs={'class': 'D(ib) Va(t)'}):
        for span in div.findAll('span', recursive=False):
            company_json['PRESENT_GROWTH'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'PREV_CLOSE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['PREV_CLOSE'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'OPEN-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['OPEN'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'BID-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['BID'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'ASK-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['ASK'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'DAYS_RANGE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['DAYS_RANGE'] = span.text.strip()
    for td in soup.findAll('td',
                       attrs={'data-test': 'FIFTY_TWO_WK_RANGE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['FIFTY_TWO_WK_RANGE'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'TD_VOLUME-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['TD_VOLUME'] = span.text.strip()
    for td in soup.findAll('td',
                       attrs={'data-test': 'AVERAGE_VOLUME_3MONTH-value'
                       }):
        for span in td.findAll('span', recursive=False):
            other_details['AVERAGE_VOLUME_3MONTH'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'MARKET_CAP-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['MARKET_CAP'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'BETA_3Y-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['BETA_3Y'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'PE_RATIO-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['PE_RATIO'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'EPS_RATIO-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['EPS_RATIO'] = span.text.strip()
    for td in soup.findAll('td', attrs={'data-test': 'EARNINGS_DATE-value'
                       }):
        other_details['EARNINGS_DATE'] = []
        for span in td.findAll('span', recursive=False):
            other_details['EARNINGS_DATE'].append(span.text.strip())
    for td in soup.findAll('td',
                       attrs={'data-test': 'DIVIDEND_AND_YIELD-value'}):
        other_details['DIVIDEND_AND_YIELD'] = td.text.strip()
    for td in soup.findAll('td',
                       attrs={'data-test': 'EX_DIVIDEND_DATE-value'}):
        for span in td.findAll('span', recursive=False):
            other_details['EX_DIVIDEND_DATE'] = span.text.strip()
    for td in soup.findAll('td',
                       attrs={'data-test': 'ONE_YEAR_TARGET_PRICE-value'
                       }):
        for span in td.findAll('span', recursive=False):
            other_details['ONE_YEAR_TARGET_PRICE'] = span.text.strip()

    stock_symbol.config(text=str(stock_symbol_input.get().upper()))
    stock_price.config(text="$" + str(company_json["PRESENT_VALUE"]))
    stock_open.config(text= "$" + str(other_details["OPEN"]))
    stock_high.config(text=str(other_details["PE_RATIO"]))
    stock_low.config(text=str(other_details["EPS_RATIO"]))
    stock_close.config(text="$" + str(other_details["PREV_CLOSE"]))
    stock_volume.config(text=str(other_details["TD_VOLUME"]))
    stock_adj_close.config(text=str(other_details["DIVIDEND_AND_YIELD"]))
def findTrendStock():
    url = 'https://finance.yahoo.com/trending-tickers'

    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
 
    the_table = soup.find(class_='yfinlist-table')
    the_tds = the_table.find_all('tr')
    total_list = []
    game_list = []

    for element in the_tds:
        if element.find('a'):
            contents = element.find('a').contents[0]
        elif element.find('span'):
            contents = element.find('span').contents[0]
        else:
            contents=element.contents[0]

        contents = str(contents)
        contents = contents.replace('\n',"")
        game_list.append(contents)

    for m in game_list:
        listbox1.insert(0,m)
def findNews():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    now = datetime.datetime.now()
    now = now.strftime('%A, %B %d, %Y  %I:%M %p')

    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")

    scripts = soup.find_all('script')
    for script in scripts:
        if 'preloadedData' in script.text:
            jsonStr = script.text
            jsonStr = jsonStr.split('=', 1)[1].strip()
            jsonStr = jsonStr.rsplit(';', 1)[0]
            jsonObj = json.loads(jsonStr)

    print ('%s\nHeadlines\n%s\n' %(url, now))
    count = 1
    for ele, v in jsonObj['initialState'].items():
        try:
            if v['headline'] and v['__typename'] == 'PromotionalProperties':
                print('Headline %s: %s' %(count, v['headline']))
                listbox2.insert(0,'%s - %s' %(count, v['headline']))

                count += 1
        except:
            continue
def deleteToDo():
    myData = load_todo()
    for a in myData:
        if a['Todo'] == todo_input.get().upper():
            myData.remove(a)
    dump_todo(myData)
    todo_input.delete(0,'end')
    loadTodo() 

root = Tk()
root.geometry("1250x1000")
root.title("STOCK-IT")
root.resizable(width="FALSE", height="FALSE")

root.grid_columnconfigure(0, weight=400)
root.grid_columnconfigure(1, weight=600)
root.grid_columnconfigure(2, weight=600)  

left_frame = Frame(root, width=250,height=520)
right_frame=Frame(root, width=500,height=420)
bottom_frame=Frame(root,width=400,height=420)
x_frame = Frame(root,  width=400,height = 420)
y_frame = Frame(root , width=400, height = 420)

left_frame.grid(column=0,row=0,sticky="w")
right_frame.grid(column=1,row=0, sticky="ne")
bottom_frame.grid(column=2, row=1, sticky="e")
x_frame.grid(column=1,row=1,sticky="nw")
y_frame.grid(column=0,row=1,sticky="nw")

stock_header = ['Symbol','Date','High','Low','Open','Close','Volume','Adj Close']
label_stock_symbol = Label(left_frame, text='Stock: ',font='Montserrat 14')
label_stock_price = Label(left_frame, text='Price: ',font='Montserrat 14')
label_stock_open = Label(left_frame, text='Open: ',font='Montserrat 14')
label_stock_high = Label(left_frame, text='PE: ',font='Montserrat 14')
label_stock_low = Label(left_frame,text='EPS: ', font='Montserrat 14')
label_stock_close = Label(left_frame,text='Close: ', font='Montserrat 14')
label_stock_volume = Label(left_frame, text='Volume: ',font='Montserrat 14')
label_stock_adj = Label(left_frame, text='Div/Yield: ',font='Montserrat 14')

label_stock_symbol.grid(column=0,row=0, sticky='w')
label_stock_price.grid(column=0,row=1,sticky='w')
label_stock_open.grid(column=0,row=2,sticky='w')
label_stock_high.grid(column=0,row=3,sticky='w')
label_stock_low.grid(column=0,row=4, sticky='w')
label_stock_close.grid(column=0,row=5, sticky='w')
label_stock_volume.grid(column=0,row=6, sticky='w')
label_stock_adj.grid(column=0,row=7, sticky='w')
 
stock_symbol = Label(left_frame,text="--", font='Montserrat 14')
stock_symbol.grid(column=1,row=0)
stock_price = Label(left_frame,text="--", font='Montserrat 14')
stock_price.grid(column=1,row=1)
stock_open = Label(left_frame,text="--", font='Montserrat 14')
stock_open.grid(column=1,row=2)
stock_high = Label(left_frame,text="--", font='Montserrat 14')
stock_high.grid(column=1,row=3)
stock_low = Label(left_frame,text="--", font='Montserrat 14')
stock_low.grid(column=1,row=4)
stock_close = Label(left_frame,text="--", font='Montserrat 14')
stock_close.grid(column=1,row=5)
stock_volume = Label(left_frame, text="--",font='Montserrat 14')
stock_volume.grid(column=1, row=6)
stock_adj_close = Label(left_frame,text="--", font='Montserrat 14')
stock_adj_close.grid(column=1, row=7)
stock_symbol_input = Entry(left_frame,width=10)
stock_symbol_input.grid(column=0,row=8,sticky="w")



submit_button = Button(left_frame,text='Search',width=10, command=findStock)
submit_button.grid(column=0,row=9,sticky="w")
add_submit_button = Button(left_frame,text='Add', width=10, command=addStock)
add_submit_button.grid(column=0,row=10,sticky="w")
trend_button = Button(left_frame,text='Trending', width=10, command=findTrendStock)
trend_button.grid(column=0,row=11,sticky="w")
news_button = Button(left_frame, text="News", width=10, command=findNews)
news_button.grid(column=0,row=12,sticky="w")

list_label = Label(right_frame, text="My Stocks", font='Montserrat 14')
list_label.grid(column=0,row=0,sticky="w")
listbox = ttk.Treeview(right_frame,columns=stock_header,show="headings",height=20)
listbox.grid(column=0,row=1, sticky="w")

asdf = Label(y_frame,text="")
asdf.grid(column=0,row=0,sticky="e")
trend_label = Label(y_frame, text="Trending Stocks", font='Montserrat 14')
trend_label.grid(column=0,row=1,sticky="e")
listbox1=Listbox(y_frame,width=20,height=25)
listbox1.grid(column=0,row=2,sticky="nw")

asdff = Label(x_frame,text="")
asdff.grid(column=0,row=0,sticky="w")
news_label = Label(x_frame, text="Todays News Headline", font='Monstserrat 14')
news_label.grid(column=0,row=1,sticky="w")
listbox2 = Listbox(x_frame,height=25,width=75)
listbox2.grid(column=0,row=2,sticky="nw")

asdfff = Label(bottom_frame,text="")
asdfff.grid(column=0,row=0,sticky="w")
todo_list_label = Label(bottom_frame,text="To-Do List", font='Monstserrat 14')
todo_list_label.grid(column=0,row=1,sticky="w")
listbox3 = Listbox(bottom_frame,height=20,width=40)
listbox3.grid(column=0,row=2,sticky="w")

todo_label = Label(bottom_frame,text="Task: ")
todo_label.grid(column=0,row=3,sticky="w")
todo_input = Entry(bottom_frame,width=40)
todo_input.grid(column=0,row=4,sticky="w")
todo_label = Label(bottom_frame,text="Date: ")
todo_label.grid(column=0,row=5,sticky="w")
todo2_input = Entry(bottom_frame,width=20)
todo2_input.grid(column=0,row=6,sticky="w")

todo_button = Button(bottom_frame, text="Add", width=10, command=addToDo)
todo_button.grid(column=0,row=7,sticky="w")

todo_delete_button=Button(bottom_frame,text="Done", width=10, command=deleteToDo)
todo_delete_button.grid(column=0,row=8,sticky="w")

for col in stock_header:
    listbox.column(col,width=80)

if os.path.exists('stocks.json'):
    file = open('stocks.json', 'r')
    ok = file.read()
    if ok != '':
        loadTable()
else:
    file=open('stocks.json','w') 


if os.path.exists('todo.json'):
    file = open('todo.json', 'r')
    ok = file.read()
    if ok != '':
        loadTodo()
else:
    file=open('todo.json','w') 

root.mainloop()

 