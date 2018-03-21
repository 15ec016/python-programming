# Python Program to Reverse a Number using While loop
 
Num = int(input("Please Enter any Num: "))
Reverse = 0
while(Num > 0):
    Reminder = Num %10
    Reverse = (Reverse *10) + Reminder
    Num = Num //10
 
print("\n Reverse of entered number is = %d" %Reverse)
