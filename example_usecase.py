import os
import tkinter as tk
from tkinter import filedialog
import extract_text

# Initialize Tkinter root widget
root = tk.Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

# Show an "Open" dialog box and return the path to the selected file
pdf_path = filedialog.askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF files", "*.pdf")])

# Check if a file was selected
if not pdf_path:
    print("No file selected.")
else:
    print("Selected file:", pdf_path)
    
# Show a dialog box for choosing an output directory
output_folder = filedialog.askdirectory(
    title="Select Output Folder")

# Check if a folder was selected
if not output_folder:
    print("No folder selected.")
else:
    print("Selected output folder:", output_folder)
    
if output_folder:
    # Extract the base name of the PDF file (without extension) to use for the text file
    pdf_filename = os.path.basename(pdf_path)
    base_name, _ = os.path.splitext(pdf_filename)
    txt_filename = base_name + ".txt"
    txt_path = os.path.join(output_folder, txt_filename)
    print("Output text file will be saved as:", txt_path)

# Assuming extract_text.pyx contains a function named extract_text_from_pdf
# that extracts text from a PDF file and saves it to a text file.

if pdf_path and output_folder:
    # Call your Cython function here
    extract_text.extract_text_from_pdf(pdf_path, txt_path)
    print(f"Text has been extracted from {pdf_path} and saved to {txt_path}.")
