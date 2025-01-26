#Chapter 3 exercise 2
#eS 1/25/25
#CIT-95 spring25
#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing
#a message and exiting the program.
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

print()
hours = input('Enter hours worked: ')
try:
    hours_worked = float(hours)
    regular_pay = 10
    overtime_pay = regular_pay*1.5
    if hours_worked <= 40:
        pay = hours_worked*regular_pay
    if hours_worked > 40:
        pay = ((hours_worked-40)*overtime_pay)+(40*regular_pay)
    print('Your pay is:', pay)
except:
    print('Error, please enter a numeric input.')