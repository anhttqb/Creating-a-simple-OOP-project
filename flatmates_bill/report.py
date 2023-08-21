import os
import webbrowser
from filestack import Client

from fpdf import FPDF


class PdfReport:
    """Generating a pdf file that has data about the flatmates such as
    their names, their sharing bill amount, the period of the bill..."""

    def __init__(self, file_name):
        self.file_name = file_name

    def generate_pdf(self, flatmate1, flatmate2, bill):
        flatmate1_pay_amount = f"${flatmate1.pays(bill, flatmate2)}"
        flatmate2_pay_amount = f"${flatmate2.pays(bill, flatmate1)}"

        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image('flatmates_bill/other_files/house.png', w=40, h=40)

        # add a title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # add Period label and value
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and pay amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=f"{flatmate1.name}:", border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay_amount, border=0, ln=1)

        # Insert name and pay amount of the second flatmate
        pdf.cell(w=100, h=25, txt=f"{flatmate2.name}:", border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay_amount, border=0)

        # generating the result as a pdf file
        # change directory to other_files and generate and open the PDF
        # os.chdir("other_files")
        pdf.output(self.file_name)
        # webbrowser.open(self.file_name)

class FileSharer:
    """This class is responsible for uploading the file to the cloud"""

    def __init__(self, file_path, api_key='AOwdSvf4ESGOA5YVyC55Nz'):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        new_file_link = client.upload(filepath=self.file_path)
        return new_file_link.url


