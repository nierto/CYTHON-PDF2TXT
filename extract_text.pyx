# cython: language_level=3

import fitz  # PyMuPDF
from io import StringIO

def extract_text_from_pdf(pdf_path: str, txt_path: str):
    """
    Extracts text from a PDF file and saves it to a text file.

    :param pdf_path: Path to the PDF file.
    :param txt_path: Path where the extracted text will be saved.
    """
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Create a StringIO object to accumulate the extracted text
    extracted_text = StringIO()

    # Extract text from each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        extracted_text.write(text)

    # Close the document
    doc.close()

    # Save the extracted text to a file
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text.getvalue())

    # Clean up
    extracted_text.close()