# mortgage.py

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0
month_total = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month_total >= extra_payment_start_month and month_total <extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment
        month_total += 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        month_total += 1
    
print('Total paid', total_paid)
print('Month total', month_total)