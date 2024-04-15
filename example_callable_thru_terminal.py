import os
import sys
import extract_text

version = "0.0.1"

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <path_to_pdf> <output_folder>")
        sys.exit(1)
        
    if sys.argv[1] == "--version" or sys.argv[1] == "-v"  :
        print("extract_pdf_txt version: %s\n", version)
    
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
         print(f"""
        +-------------------------------------------------------------------+
        |                            About This Tool                        |
        +-------------------------------------------------------------------+
        | Author: Nierto                                                    |
        | Version: {version}                                                |
        |                                                                   |
        | Description:                                                      |
        | This simply takes a pdf file and outputs its text in a txt file   |
        | effectively. Designed for ease of use in UNIX-like environments.  |
        | I used the Fitz python module, it works like a charm              |
        |                                                                   |
        | Usage:                                                            |
        | $ extract_pdf_txt.py [options]                                    |
        |                                                                   |
        | Options:                                                          |
        |   -h, --help        Display this help message and exit.           |
        |   -v, --version     Show program's version number and exit.       |
        |   -e, --extract     extract text from pdf into .txt file          |
        |                                                                   |
        | Example:                                                          |
        | $ extract_pdf_txt.py --v                                          |
        |                                                                   |
        | Report bugs to: dev@nierto.com                                    | 
        +-------------------------------------------------------------------+
        """)  
          
    if sys.argv[1] == "--extract" or sys.argv[1] == "-e":
        pdf_path = sys.argv[2]
        output_folder = sys.argv[3]
        if not os.path.exists(pdf_path):
            print("The specified PDF file does not exist.")
            sys.exit(1)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        pdf_filename = os.path.basename(pdf_path)
        base_name, _ = os.path.splitext(pdf_filename)
        txt_filename = base_name + ".txt"
        txt_path = os.path.join(output_folder, txt_filename)
        print("Output text file will be saved as:", txt_path)
        # call to cython func here.
        extract_text.extract_text_from_pdf(pdf_path, txt_path)
        print(f"Text has been extracted from {pdf_path} and saved to {txt_path}.")
    else:
        print('Type "python extract_pdf_txt.py -h" for more information')

    if __name__ == "__main__":
    main()
