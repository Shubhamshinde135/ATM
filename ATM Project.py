import time

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='Bank'
)
mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM BankAtm')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Note = {'2000': 10, '500': 20, '200': 20, '100':40 }
MachineBalance = Note.get('2000') * 2000 + Note.get('500') * 500 + Note.get('200') * 200 + Note.get('100') * 100

a = Note['2000']
b = Note['500']
c = Note['200']
d = Note['100']

print("\n", "#" * 10, "Welcome to SBI ATM", "#" * 10, "\n")

def exitProgram():
    print('Logging Out...')
    time.sleep(1)
    exit()

def menu(CardNumber):
    print('\nPress 1 for MainMenu\nPress 2 for LogOut\n')
    Your_Option = int(input('Enter your option: '))
    if Your_Option == 1:
        mainMenu(CardNumber)
    if Your_Option == 2:
        exitProgram() 

def mainMenu(CardNumber):  # ATM Main Menu
    CardNumber = CardNumber
    print('''\n*  Select the option \n\n1. View account information
2. Change your pin\n3. Cash withdrawl\n4. Balance Transfer\n5. Log Out\n''')
    select = int(input("Select: "))
    if select <= 5:
        if select == 1:
            viewAccount(CardNumber)
        elif select == 2:
            ChangePin(CardNumber)
        elif select == 3:
            withdraw(CardNumber)
        elif select == 4:
            Transfer(CardNumber)
        elif select == 5:
            exitProgram()
    else:
        print("Please enter an integer (1-5)")
        mainMenu(CardNumber)

def viewAccount(CardNumber):
    '''View the complete account information'''
    mycursor.execute(f"SELECT * FROM BankAtm WHERE CardNumber={CardNumber}")
    myresult = mycursor.fetchall()
    result = [x for y in myresult for x in y]

    print('\nPersonal Information\n')
    print('#' * 40)
    print('\nName:', result[0])
    print('Card Number:', result[1])
    print('PIN:', result[2])
    print('Account Balance:', result[3], 'Rs')
    print('Account Number:', result[4], '\n')
    print('#' * 40)
    menu(CardNumber)

def ChangePin(CardNumber):
    User_Pin = int(input('Enter your pin: '))

    mycursor.execute(f"SELECT * FROM BankAtm where CardNumber={CardNumber}")
    myresult = mycursor.fetchone()

    pin = myresult[2]
    if User_Pin == pin:

        NewPin = int(input('Enter Four digit pin:'))
        pinlen = len(str(NewPin))

        if pinlen == 4 and NewPin != pin:
            mycursor.execute(f"UPDATE BankAtm SET PIN = {NewPin} WHERE CardNumber = {CardNumber}")
            mydb.commit()
            print('\nPin Updated successfully\n')
        else:
            print('Invalid input ')
            print('please try again')
        menu(CardNumber)

def Transfer(CardNumber):
    mycursor.execute(f"SELECT * FROM BankAtm WHERE CardNumber={CardNumber}")
    myresult = mycursor.fetchall()
    BankBalance = myresult[0][3]
    print('Account Balance:', BankBalance, 'Rs')

    Account_Number = int(input('Enter Account number to transfer amount:'))
    mycursor.execute("SELECT AccountNumber FROM BankAtm")
    myresult = mycursor.fetchall()
    account = [x for y in myresult for x in y]

    if Account_Number in account:

        Amount = int(input('Enter amount to transfer:'))
        mycursor.execute(f"SELECT * FROM BankAtm WHERE AccountNumber = {Account_Number}")
        myres = mycursor.fetchall()
        Recipient_Number = myres[0][4]
        Rec_BankBAlance = myres[0][3]

        if Amount <= BankBalance:
            if Account_Number == Recipient_Number:
                print('Transaaction Successful')
                UpdatedBalance = BankBalance - Amount
                UpBalance = Rec_BankBAlance + Amount
                mycursor.execute(f"UPDATE BankAtm SET BankBalance = {UpdatedBalance} WHERE CardNumber = {CardNumber}")
                mydb.commit()
                print('Balace after cash Transfer is:', UpdatedBalance, 'Rs')
                mycursor.execute(f"UPDATE BankAtm SET BankBalance = {UpBalance} WHERE AccountNumber = {Account_Number}")
                mydb.commit()
            else:
                print('Enter Valid Account number')
                menu(CardNumber)
        else:
            print('Your Account balance is low')
    else:
        print('\nplease enter valid account number\n')
    menu(CardNumber)

def withdraw(CardNumber):
    mycursor.execute(f"SELECT * FROM BankAtm WHERE CardNumber={CardNumber}")
    myresult = mycursor.fetchall()
    BankBalance = myresult[0][3]
    print('Account Balance:', BankBalance, 'Rs')
    withdraw_amount = int(input('Please enter amount to withdraw:'))
    p = (withdraw_amount) // 2000
    if p > a:
        p1 = a 
    else:
        p1 = p
    q = (withdraw_amount - (p1 * 2000)) // 500
    if q > b:
        q1 = b
    else:
        q1 = q    
    r = (withdraw_amount - (p1 * 2000 + q1 * 500)) // 200
    if r > c:
        r1 = c
    else:
        r1 = r    
    s = (withdraw_amount - (p1 * 2000 + q1 * 500 + r1 * 200)) // 100
    if s > d:
        s1 = 0
    else:
        s1 = s
    
    if withdraw_amount <= BankBalance :
        if s1 == s :
            if withdraw_amount == (p1 * 2000 + q1 * 500 + r1 * 200 + s1 * 100):
                                    
                pin = int(input('Enter Your ATM PIN: '))
                if pin == myresult[0][2]:
                    Note['2000'] = a - p1
                    Note['500'] = b - q1
                    Note['200'] = c - r1
                    Note['100'] = d - s1
                    print('Your Transaction successful')
                    UpdatedBalance = BankBalance - withdraw_amount
                    mycursor.execute(f"UPDATE BankAtm SET BankBalance = {UpdatedBalance} WHERE CardNumber = {CardNumber}")
                    mydb.commit()
                    print('Balace after cash withdraw is:', UpdatedBalance, 'Rs\n')
                    print(Note)
                else:
                    print('Enter valid pin')               
            else:
                print('Plese enter valid amount')
        else:
            print('Machine Balance is low')
    else:
        print('Your Account doesn\'t have sufficient Balance')
        print('Please Enter Valid amount')    
    menu(CardNumber)

def signIn():  # This function provides to sign in to your account.
    chances = 3
    print()
    CardNumber = int(input('Enter your AtmCard: '))
    while chances >= 0:
        print()
        User_Pin = int(input('Enter your PIN: '))
        mycursor.execute(f"SELECT * FROM BankAtm where CardNumber={CardNumber}")
        myresult = mycursor.fetchone()
        pin = myresult[2]
        name = myresult[0]
        if User_Pin == pin:
            print('\n Welcome to SBI ATM Mr', name)
            mainMenu(CardNumber)
        elif User_Pin != pin:
            chances -= 1
            print('Invalid Pin')
            print(f"You have {chances} chances left")
            print('Please Enter Valid PIN')
            if chances == 0:
                print('You crossing the number of chances')
                print('Due to security reason your card is Temporary block')
                break

while True:
    print("Sign In (enter '1')\nLogOut (enter '2')", '\n')
    question = int(input("Select: "))
    if question == 1:
        signIn()
        break
    elif question == 2:
        exitProgram()
    else:
        print('Invalid Keyword, Please Try Again.')
        
        
