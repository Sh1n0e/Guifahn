from tkinter import messagebox
import sqlite3
from tkinter import *

def load_equipment():
    conn = sqlite3.connect('Plants.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Equipment")
    data = c.fetchall()
    row = data[0]
    print(row[1])
    return data

def set_data():
    data = load_equipment()
    row = data[var_recordset_index.get()]
    var_equipment_id.set(row[0])
    var_quantity.set(row[2])
    var_name.set(row[1])

def next():
    print("Here is the next item")
    var_recordset_index.set(var_recordset_index.get()+1)
    set_data()

def prev():
    print("Here is the previous item")
    var_recordset_index.set(var_recordset_index.get() - 1)
    set_data()

def insert():
    var_equipment_id.set("")
    var_name.set("")
    var_quantity.set("")
    print("INSERT")
    equipment = [var_name.get(), var_quantity.get()]
    insert_query = "INSERT INTO equipment VALUES (null,?,?)"
    conn = sqlite3.connect('Plants.db')
    c = conn.cursor()
    c.execute(insert_query, equipment)
    conn.commit()

def delete():
    MsgBox = messagebox.askquestion('DELETE RECORD',
                                    'Are you sure you want to delete the current record? This cannot be undone.',
                                    icon='warning')
    if MsgBox == 'yes':
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        delete_query = "DELETE FROM equipment WHERE equipment_id=" + str(var_equipment_id.get())
        print(delete_query)
        c.execute(delete_query)
        conn.commit()
        set_data()
        print("DELETED")

def update():
	print("UPDATE")
	equipment = [var_name.get(), var_quantity.get(), var_equipment_id.get()]
	update_query = "UPDATE equipment SET type=? , quantity=? WHERE equipment_id=?"
	conn = sqlite3.connect('Plants.db')
	c = conn.cursor()
	c.execute(update_query, equipment)
	conn.commit()
	set_data()

def new_window():
    second_window = Toplevel(root)
    second_window.title("NEW WINDOW")
    second_window.geometry("200x200")
    btn_back = Button(second_window, text="BACK", command=lambda: second_window.destroy())
    btn_back.pack()


root = Tk()
root.geometry("500x500")
root.title("Hello World GUI")

var_recordset_index = IntVar()
var_recordset_index.set(0)

var_recordset_index = IntVar()
var_recordset_index.set(0)

Equipment_window_label = Label(root, text="Garden system: Equipment")
Equipment_window_label.grid(row =0 ,column =1 )

var_equipment_id = StringVar(root)
var_name = StringVar(root)
var_quantity = StringVar(root)

equipment_id = Label(root, text="Equipment ID:")
equipment_id.grid(row=1, column =0)
equipment_id_entry = Entry(root)
entry_equipment_id = Entry(root, textvariable = var_equipment_id)
entry_equipment_id.grid(row=1, column=1)

name = Label(root, text="Name:")
name.grid(row=2, column =0 )
name_entry = Entry(root)
entry_name = Entry(root, textvariable = var_name)
entry_name.grid(row=2, column=1)

quantity = Label(root, text="Quantity:")
quantity.grid(row=3, column=0)
quantity_entry = Entry(root)
entry_quantity = Entry(root, textvariable = var_quantity)
entry_quantity.grid(row=3, column=1)

load_equipment_btn = Button(root, text = "load equipment", command = load_equipment)
load_equipment_btn.grid(row=6, column=1)

next_btn = Button(root, text=">", command = next)
next_btn.grid(row=5, column=2)

prev_btn = Button(root, text="<", command = prev)
prev_btn.grid(row=5, column=0)

insert_btn = Button(root, text="Insert data", command = insert)
insert_btn.grid(row=2, column=2)

delete_btn = Button(root, text = "Delete entry", command = delete)
delete_btn.grid(row=6, column=2)

update_btn = Button(root, text = "Update entry", command = update)
update_btn.grid(row=6,column=0)

new_btn = Button(root, text = "New Window", command = new_window)
new_btn.grid(row=7,column=1)

set_data()
root.mainloop()
