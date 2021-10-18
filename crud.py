#pip install mysql-connector-python
import tkinter as tk
from tkinter import ttk
import mysql.connector
 
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="3240160", database="refrid", port=3308)
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM new_table")
        records = mycursor.fetchall()
        #print(records)
 
        for i, (id,stname, course,fee,de, gt) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee, de, gt))
            mysqldb.close()
 
 
root = tk.Tk()
root.title("Student Records")
label = tk.Label(root, text="Student Records", font=("Arial",30)).grid(row=0, columnspan=3)
 
cols = ('id', 'stname', 'course','fee', 'toto', 'teta')
listBox = ttk.Treeview(root, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
show()
root.mainloop()
