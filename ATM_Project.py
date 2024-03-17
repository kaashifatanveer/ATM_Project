# ATM_Project
#This project is a simple ATM simulator implemented in Python. It allows users to perform basic ATM operations such as checking their balance, depositing money, withdrawing funds and changing password.

def withdraw():
    amount=int(input("Enter the amount you want to withdraw: "))
    pin=int(input("Enter your unique pin: "))
    if(pin!=pins[i]):
        print("Wrong PIN entered!")
        exit()
    else:
        if(balance[i]<amount):
            print("Insufficient amount!!")
        if(balance[i]>amount):
            print("Collect amount")
            print("Want to see your balance? (Y/N):")
            balcheck=input("Enter (Y/N): ")
            if(balcheck=='Y'):
                print("Your balance amount is: ",balance[i]-amount)
            if(balcheck=='N'):
                print("Thank you for banking with us!")


def deposit():
    amount=int(input("Enter the amount you want to deposit: "))
    pin=int(input("Enter your unic pin: "))
    if(pin!=pins[i]):
        print("Wrong PIN entered!")
        exit()
    else:
        balance[i]+=amount
        print("Want to see your balance? (Y/N)")
        balcheck=input("Enter (Y/N): ")
        if(balcheck=='Y'):
            print("Your balance amount is: ",balance[i])
        else:
            print("Thank you for banking with us!")


def checkbalance():
    pin=int(input("Enter your unique pin: "))
    if(pin!=pins[i]):
        print("Wrong PIN entered!")
        exit()
    else:
        print("The balance is: ",balance[i])
        print("Thank You!")
def changepwd():
    currentpwd=input("Enter your current password: ")
    if(currentpwd!=passcode[i]):
        print("Current password you entered is wrong!")
    else:
        newpwd=input("Enter your new password: ")
        confirmpwd=input("Re-enter your new password: ")
        if(newpwd!= confirmpwd):
            print("Passwords doesnt match")
        else:
            passcode[i]=confirmpwd
            print("Password changed successfully")

def ATM():
    pass_code=input("Enter the Password: ")
    flag=0
    if(pass_code!=passcode[i]):
        print("Wrong Password, 2 attempts left")
        pass_code=input("Enter the Password: ")
        if(pass_code!=passcode[i]):
            print("Wrong Password, 1 attempt left")
            pass_code=input("Enter the Password: ")
            if(pass_code!=passcode[i]):
                print("Wrong Password Entered, Account Blocked!!")
            else:
                flag=1
        else:
            flag=1
    else:
        flag=1

    if(flag==0):
        print("END")
    else:
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Check Balance")
        print("4.Change Password")
        choice=int(input("Enter Your Choice:"))
       
        while(1):
                if(choice==1):
                    withdraw()
                    break
                elif(choice==2):
                    deposit()
                    break
                elif(choice==3):
                    checkbalance()
                    break
                elif(choice==4):
                    changepwd()
                    break
                else:
                    print("Enter the valid choice!!")
                    break
    
user=["Tanveer","Sonia","Praneetha","Yashu"]
passcode=["tannu26","sony04","pranee17","yashu01"]
pins=[1111,2222,3333,4444]
balance=[15000,2400,350000,42000]
username=input("Enter Your Username: ")
if(username in user):
    i=user.index(username)
else:
    print("User doesn't exist!")
    print("END")
    exit()
ATM()
