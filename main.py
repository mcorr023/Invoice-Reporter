from tkinter import ttk
import tkinter as tk
import invoiceReporter
import pdfConverter
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('icon.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select PDF file", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a PDF file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        pdf_report = invoiceReporter.report(pdfConverter.importReport(file), pdfConverter.importInvoices(file))

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, pdf_report)
        text_box.tag_configure("left", justify="left")
        text_box.tag_add("left", 1.0, "end")
        text_box.grid(column=1, row=3)

        scrollbar = ttk.Scrollbar(root, orient='vertical', command = text_box.yview)
        scrollbar.grid(row=3, column=3, sticky=tk.NS)
        text_box['yscrollcommand'] = scrollbar.set

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()

        
