import os,openpyxl,tkinter
from tkinter import ttk,messagebox

def enter_data():
        number = number_entry.get()
        name = name_entry.get()
        arrival = arrival_entry.get()
        quantity = quantity_entry.get()
        receiving = receiving_entry.get()
        date_write = date_write_entry.get()
        reason = reason_entry.get()
        note = note_entry.get()
        if number and name:            
            filepath = "File.xlsx"           
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["№", "Наименование", "S/N", "Количество", "Дата Поступление","Дата Списание", "Причина Списани", "Примечание"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([number, name, arrival, quantity, receiving, 
                          date_write, reason, note])
            workbook.save(filepath)                
        else:
            tkinter.messagebox.showwarning(message="Укажите Номер и Наименование ")
            return enter_data

window = tkinter.Tk()
window.title("Neftek Operating")
frame = tkinter.Frame(window)
frame.pack()

user_info_frame =tkinter.LabelFrame(frame, text="Окно Добавление")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

number = tkinter.Label(user_info_frame, text="№")
number.grid(row=0, column=0)
number_entry = tkinter.Entry(user_info_frame)
number_entry.grid(row=1, column=0)

name = tkinter.Label(user_info_frame, text="Наименование")
name.grid(row=0, column=1)
name_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row=1, column=1)

arrival = tkinter.Label(user_info_frame, text="S/N")
arrival.grid(row=0, column=2)
arrival_entry = tkinter.Entry(user_info_frame)
arrival_entry.grid(row=1, column=2)

quantity = tkinter.Label(user_info_frame, text="Количество")
quantity.grid(row=0, column=3)
quantity_entry = tkinter.Entry(user_info_frame)
quantity_entry.grid(row=1, column=3)

receiving = tkinter.Label(user_info_frame, text="Дата Поступление")
receiving.grid(row=0, column=4)
receiving_entry = tkinter.Entry(user_info_frame)
receiving_entry.grid(row=1, column=4)

date_write = tkinter.Label(user_info_frame, text="Дата Списание")
date_write.grid(row=0, column=5)
date_write_entry = tkinter.Entry(user_info_frame)
date_write_entry.grid(row=1, column=5)

reason = tkinter.Label(user_info_frame, text="Причина Списание")
reason.grid(row=0, column=6)
reason_entry = tkinter.Entry(user_info_frame)
reason_entry.grid(row=1, column=6)

note = tkinter.Label(user_info_frame, text="Примечание")
note.grid(row=0, column=7)
note_entry = tkinter.Entry(user_info_frame)
note_entry.grid(row=1, column=7)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, padx=20, pady=10)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = tkinter.Button(frame, text="Записать в Excel", command= enter_data)
button.grid(row=3, column=0, padx=20, pady=10)
 
window.mainloop()