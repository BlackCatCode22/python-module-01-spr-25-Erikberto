#Chapter 3 exercise 1
#eS 1/25/25
#CIT-95 spring25
#Rewrite your pay computation to give employee 1.5 times the hourly rate for hours worked over 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475
print()
hours = input('Enter hours worked: ')
hours_worked = float(hours)
regular_pay = 10
overtime_pay =regular_pay*1.5
if hours_worked <= 40:
    pay = hours_worked*regular_pay
if hours_worked > 40:
    pay = ((hours_worked-40)*overtime_pay)+(40*regular_pay)
print('Your pay is: $', pay)

