import datetime, calendar

balance = 5000
interest_rate = 13 * .01
monthly_payment = 500

today = datetime.date.today()

days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# print(days_in_current_month)
# print(today.day)
days_till_end_current_month = days_in_current_month-today.day
# print(days_till_end_current_month)

start_date = today + datetime.timedelta(days_till_end_current_month + 1)
# print(start_date)

end_date = start_date

while balance > 0:
    monthly_int_charge = (interest_rate/12) * balance
    balance += monthly_int_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    # balance = 0 if balance < 0 else round(balance, 2)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    # print(days_till_end_current_month)
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
    # end_date = end_date + datetime.timedelta(days_in_current_month)

    print(end_date, balance)