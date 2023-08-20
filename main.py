from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, FloatField, IntegerField
from flask import Flask, render_template, request
from flatmates_bill.flat_infor import Bill, Flatmate
from flatmates_bill.report import PdfReport, FileSharer

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        # When rendering template, make sure to pass the correct arguments in order to avoid errors in html files
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = billform.days_in_house1.data

        name2 = billform.name2.data
        days_in_house2 = billform.days_in_house2.data

        the_bill = Bill(bill_amount=amount, period=period)
        flatmate1 = Flatmate(name1, days_in_house1)
        flatmate2 = Flatmate(name2, days_in_house2)

        pdf_report = PdfReport(file_name=f"{the_bill.period}.pdf")
        pdf_report.generate_pdf(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

        file_sharer = FileSharer(file_path=pdf_report.file_name)

        return render_template("bill_form_page.html", name1=flatmate1.name, result=True,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1),
                               billform=billform, pdf_url=file_sharer.share())


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = billform.days_in_house1.data

        name2 = billform.name2.data
        days_in_house2 = billform.days_in_house2.data

        the_bill = Bill(bill_amount=amount, period=period)
        flatmate1 = Flatmate(name1, days_in_house1)
        flatmate2 = Flatmate(name2, days_in_house2)

        return render_template("results.html", name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):  # not a page
    amount = FloatField(label="Bill Amount: ", default=100)
    period = StringField(label="Bill Period: ", default="August 2023")

    name1 = StringField(label="Name: ", default="Tom")
    days_in_house1 = IntegerField(label="Days in the house: ", default=20)

    name2 = StringField(label="Name: ", default='Angela')
    days_in_house2 = IntegerField(label="Days in the house: ", default=15)

    submit_button = SubmitField(label="Calculate")



app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page')) # Make sure that the url is the same as in the 'action' field in the corresponding html file
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
