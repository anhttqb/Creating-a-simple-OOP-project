class Bill:
    """Object that contains data of a bill, such as its amount or
    time period"""

    def __init__(self, bill_amount, period):
        self.amount = bill_amount
        self.period = period


class Flatmate:
    '''Object that includes information of flatmates such as their names.
    how many days they actually lived in house, how much money they had to pay..'''

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill_amount, flatmate_2):
        total_stayed_days = self.days_in_house + flatmate_2.days_in_house
        bill_amount_per_day = bill_amount.amount / total_stayed_days
        money_to_pay = bill_amount_per_day * self.days_in_house
        return round(money_to_pay, 2)
