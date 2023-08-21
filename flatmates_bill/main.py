from flat_infor import Bill, Flatmate
from report import PdfReport, FileSharer

# Implementing input values from user
money_amount = float(input("Hey user, enter how much the bill cost: $"))
period = input("What's the bill period? E.g. August 2023: ")

name1 = input("What is your name? ").capitalize()
days_in_house_person1 = int(input(f"How many days did {name1} stay in the flat? "))

name2 = input("What is the name of the other flatmate? ").capitalize()
days_in_house_person2 = int(input(f"How many days did {name2} stay in the flat? "))

bill = Bill(bill_amount=money_amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house_person1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house_person2)

print(f"{flatmate1.name} pays: ${flatmate1.pays(bill_amount=bill, flatmate_2=flatmate2)}")
print(f"{flatmate2.name} pays: ${flatmate2.pays(bill_amount=bill, flatmate_2=flatmate1)}")

pdf_report = PdfReport(file_name=f"{bill.period}.pdf")
pdf_report.generate_pdf(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)

file_sharer = FileSharer(file_path=pdf_report.file_name)
print(file_sharer.share())
