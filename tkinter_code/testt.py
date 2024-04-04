import os
import openpyxl
import tkinter as tk
from tkinter import messagebox

def enter_data(number_entry, name_entry, arrival_entry, quantity_entry, receiving_entry, date_write_entry, reason_entry, note_entry):
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
            heading = ["№", "Наименование", "S/N", "Количество", "Дата Поступление", "Дата Списание", "Причина Списание", "Примечание"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([number, name, arrival, quantity, receiving, date_write, reason, note])
        workbook.save(filepath)
    else:
        messagebox.showwarning(message="Укажите Номер и Наименование")

window = tk.Tk()
window.title("Neftek Operating")

frame = tk.Frame(window)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="Окно Добавление")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

labels = ["№", "Наименование", "S/N", "Количество", "Дата Поступление", "Дата Списание", "Причина Списание", "Примечание"]
entries = [tk.Entry(user_info_frame) for _ in labels]

for index, label in enumerate(labels):
    tk.Label(user_info_frame, text=label).grid(row=0, column=index)
    entries[index].grid(row=1, column=index)

courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1, column=0, padx=20, pady=10)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = tk.Button(frame, text="Записать в Excel", command=lambda: enter_data(*entries))
button.grid(row=2, column=0, padx=20, pady=10)

window.mainloop()
