from tkinter import *
from tkinter import ttk
import mysql.connector
import pandas as pd


tableHeaders = []
tableData = []
# Change the settings here foc connection
database = "sakila"
table = "sales_by_film_category"
host = "localhost"
user = "studentadmin"
password = "8989"
# Do Not Change code below it

def get_DB(conn):
    fetch_headers = "SHOW databases;"
    cursor = conn.cursor()
    cursor.execute(fetch_headers)
    res = cursor.fetchall()
    ret = []
    for i in res:
        ret.append(i[0])
    return ret

def get_tables(database):
    try:
        conn = mysql.connector.connect(host = host, database = database,user = user,password = password)
        cursor = conn.cursor()
        query = "show tables;"
        cursor.execute(query)
        res = cursor.fetchall()
        ret = []
        for i in res:
            ret.append(i[0])
        # print(ret)
        return ret
    except mysql.connector.Error as err:
        print("Error : ",err)
    finally:
        conn.close()
        print("Get Table Connection Closed")

def print_all(database=database,table=table):
    try:
        conn = mysql.connector.connect(host = host, database = database,user = user,password = password)
        fetch_headers = "SHOW columns FROM "+table+";"
        cursor = conn.cursor()
        cursor.execute(fetch_headers)
        res = cursor.fetchall()
        tableHeaders = []
        for i in res:
            tableHeaders.append(i[0])
        tableHeaders = [str(x).upper() for x in tableHeaders]
        print(tableHeaders)
        fetch_all = "select *  FROM "+table+";"
        cursor.execute(fetch_all)
        res = cursor.fetchall()
        print("Total Records : ",len(res))
        global tableData
        tableData = pd.DataFrame(data=res,columns=tableHeaders)
        # print(a)
        tableData.to_csv('./records.csv',index=False)
        return tableHeaders,tableData
    except mysql.connector.Error as err:
        print("Error : ",err)
    finally:
        conn.close()
        print("Print All Connection Closed")

def db_insert(conn,a,b):
    query = "insert into teacher (name,subject_id) values (\"{}\",\"{}\")".format(a,b)
    print(query)
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE teacher AUTO_INCREMENT=1")
    cursor.execute(query)
    conn.commit()

def db_delete(conn,my_id):
    cursor = conn.cursor()
    for i in my_id:
        query = "delete from teacher where id = {};".format(i)
        print(query)
        cursor = conn.cursor()
        cursor.execute(query)
    conn.commit()

def get_all_tables():
    for i in tot_db:
        print("-"*30)
        get_tables(i)

def widget():
    
    def dbChanged(*args):
        database = dbValue.get()
        tbCombo['values']=get_tables(database=database)
    
    def tbChanged(*args):
        table = tbValue.get()
        database = dbValue.get()
        global tableData,tableHeaders
        tableHeaders,tableData=print_all(database,table)
        tableHeaders = tuple(["ID"])+tuple(tableHeaders)
        
    
    def PrintTree():
        win = Toplevel(root)
        tree = ttk.Treeview(win, height=100, columns=tableHeaders, selectmode='browse')

            # Place the tree in the remaining space in the grid
        tree.pack(fill='x')
        # Define that we want to show the heading row
        tree['show'] = 'headings'

        # Assign the heading and column options
        i = 1
        for col in tableHeaders:
            num = f'#{i}' # Format string to produce incrementing numbers
            tree.heading(num, text=col)
            tree.column(num,width=100)
            i += 1

        # Create new treeview items and place them in the treeview
        # We get the values to add by cycling through the student
        # data list
        for info in tableData.to_records():
            num = f'#{i}'
            tree.insert('', 'end', values=[str(x) for x in info])
            i += 1
        
    root = Tk()
    root.title("Data Base Viewer")
    root.geometry("700x100")
    root.title("Widget Example")
    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.grid(column=0, row=0, sticky=(N, W, E, S),padx=10,pady=10)


    # Start of layout
    dbValue = StringVar()
    dbCombo = ttk.Combobox(frame, textvariable=dbValue)
    dbLabel = ttk.Label(frame, text="Select Database : ")
    dbLabel.grid(column=1, row=0, sticky=(W, E,N,S),padx=10,pady=10)
    dbCombo['values'] = tot_db
    dbCombo.grid(column=2, row=0, sticky=(W, E,N,S),padx=10,pady=10)
    dbCombo.bind('<<ComboboxSelected>>', dbChanged)

    tbLabel = ttk.Label(frame,text="Select Table ")
    tbLabel.grid(column=3, row=0, sticky=(W, E,N,S),padx=10,pady=10)
    tbValue = StringVar()
    tbCombo = ttk.Combobox(frame,textvariable=tbValue)
    tbCombo.grid(column=4,row=0,sticky=(W, E,N,S),padx=10,pady=10)
    tbCombo.bind('<<ComboboxSelected>>', tbChanged)

    showButton = ttk.Button(root, text='Show Database', command=PrintTree)
    showButton.grid(column=5, row=0)

    


    root.mainloop()

def set_conn():
    try:
        global globalconn
        globalconn = mysql.connector.connect(host = host, database = database,user = user,password = password)
        global tot_db
        tot_db = get_DB(globalconn)
        widget()
    except mysql.connector.Error as err:
        print("Error : ",err)
    finally:
        # dconn.close()
        print("Connection Closed")
        globalconn.close()

set_conn()
# get_all_tables()
