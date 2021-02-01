# mortgage.py

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0

for i in range(12):
    principal = principal * (1+rate/12) - payment - 1000
    total_paid = total_paid + payment

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
print('Total paid', total_paid)
