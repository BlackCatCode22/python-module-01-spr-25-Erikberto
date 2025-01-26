#Chapter 3 exercise 3
#eS 1/25/25
#CIT-95 spring25
#Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error message. If the score is between 0.0 and 1.0 print a grade using the following table:
# >=0.9 A       Enter score:0.95
# >=0.8 B       A
# >=0.7 C       Enter score: perfect
# >=0.6 D       Bad score
# <=0.6 F       Enter score: 10.0
#               Bad score
#               Enter score: 0.75
#               C
#               Enter score: 0.5
#               F
print()
score = input('Enter score: ')
score_entered= float(score)
try:
    if score_entered >= 0.9 and score_entered <= 1.0:
        grade = 'A'
    if score_entered >= 0.8 and score_entered < 0.9:
        grade = 'B'
    if score_entered >= 0.7 and  score_entered < 0.8:
        grade = 'C'
    if score_entered >= 0.6 and  score_entered < 0.7:
        grade = 'D'
    if score_entered <= 0.6:
        grade = 'F'
    print('Grade:',grade)
except:
    print('Please enter a valid score number.')
