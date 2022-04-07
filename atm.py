

#-------------------------------------------------------------------------Bank of sagar-------------------------------------------------------------#
#SBI ATM DETELS
#0.67.5 --version
#Builder name = Isparsh kesharwani
#This project is complete.





import time

print("please insert your Card")

time.sleep(3)

#Data server

password=8835

#Data server complete

pin=int(input("enter your pin "))

if pin==password:

 print ('''
       5 == current
       6 == cried
       7 == saving
       '''
       )

option=int(input("please enter your choise"))

#Data server#

card=7

#Data server complete#

if card==option:

 balance=1000000

time.sleep(2)

if pin==password:
    print ('''
        1 == balance
        2 == withdraw balance
        3 == deposit money
        4 == pay money
        8 == mini statement
        '''
        )

    try:
         option=int(input("please enter your choise "))
    except:
           print("please enter valid option")

    if option==1:
        print (f"your current balance is {balance}")

    if option==2:

        withdraw_amount=int(input("please enter withdraw amount"))

        balance=balance-withdraw_amount

        print (f"{withdraw_amount} is debited form your account")

        print (f"your current balance is {balance}")
    if option==3:

        deposit_amount=int(input("please enter deposit amount "))

        balance=balance+deposit_amount

        print(f"{deposit_amount} is credited to your account")

        print (f"your update balance is {balance} ")
    if option==4:

        pay_amount=int(input("please enter pay amount "))

        balance=balance-pay_amount

        account_number=int(input("please enter card number "))

        #Data server

        number=7746069776

        #Data server is complet

        while number==account_number:

         print(f"{pay_amount} is debited form your account")

         print(f"your update balance is {balance} ")

if option==8:

        print (f"your transaction is 2")

        print (f"your 1st transaction = Debit = ATM = 11.7 rs  ")

        print (f"your 2st transaction = Debit = Text = 5.9 rs")

        balance=balance-11.7

        balance=balance-5.9

        print (f"your current balance is  {balance}")

else:
    print("thanks for cooming")


