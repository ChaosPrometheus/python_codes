import os
import openpyxl
import tkinter as tk
from tkinter import messagebox

def enter_data(number_entry, name_entry, arrival_entry, quantity_entry, receiving_entry, date_write_entry, reason_entry, note_entry):
    # Get data from user input
    number = number_entry.get()
    name = name_entry.get()
    arrival = arrival_entry.get()
    quantity = quantity_entry.get()
    receiving = receiving_entry.get()
    date_write = date_write_entry.get()
    reason = reason_entry.get()
    note = note_entry.get()

    # Check if number and name are provided
    if number and name:
        filepath = "File.xlsx"
        
        # Create a new Excel file if it doesn't exist
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["№", "Наименование", "S/N", "Количество", "Дата Поступление", "Дата Списание", "Причина Списание", "Примечание"]
            sheet.append(heading)
            workbook.save(filepath)
        
        # Load the existing workbook and add the data
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([number, name, arrival, quantity, receiving, date_write, reason, note])
        workbook.save(filepath)
    else:
        messagebox.showwarning(message="Укажите Номер и Наименование")

# Create the main window
window = tk.Tk()
window.title("Neftek Operating")

# Create a frame
frame = tk.Frame(window)
frame.pack()

# Create a label frame for user input
user_info_frame = tk.LabelFrame(frame, text="Окно Добавление")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Define labels and entry fields
labels = ["№", "Наименование", "S/N", "Количество", "Дата Поступление", "Дата Списание", "Причина Списание", "Примечание"]
entries = [tk.Entry(user_info_frame) for _ in labels]

for index, label in enumerate(labels):
    tk.Label(user_info_frame, text=label).grid(row=0, column=index)
    entries[index].grid(row=1, column=index)

# Create a label frame for buttons
courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1, column=0, padx=20, pady=10)

# Adjust padding for widgets in both frames
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Create the "Записать в Excel" button
button = tk.Button(frame, text="Записать в Excel", command=lambda: enter_data(*entries))
button.grid(row=2, column=0, padx=20, pady=10)

# Start the main GUI loop
window.mainloop()
