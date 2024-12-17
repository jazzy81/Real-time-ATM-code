import mysql.connector
from datetime import datetime,timedelta  #relativedelta
import time


class Atm:

    def __init__(self):
       self.pin = ""
       self.card_no = ""
       self.db_connection()
       self.GUI()  #  graphic user interface
    
    def db_connection(self):
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jazzyjh@123M",
            database="atm_data")
            self.mycursor =  self.mydb.cursor()
             


    def GUI(self):
         
        user_input =  int(input("""Hii, How may I help you?
                        1. Enter 1 to create pin!
                        2. enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance 
                        5. Enter 5 to exit"""))
    
        if user_input == 1:
            self.create_pin()
        elif user_input == 2 :
            self.deposite()
        elif user_input == 3 :
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        else:
            print("Have a Good Day")

      
    


    def create_pin(self):
        verify = self.check_pin()
        if verify:
            if not self.expiry_check():
             print("Unable to create PIN. Please contact the bank for card renewal.")
             self.GUI()
             return
             

            while True:
                try:
                    temp_pin = int(input("Enter the new PIN you want to reset Here: "))
                except ValueError:
                    print("Invalid PIN format. Please enter numeric PIN.")
                    continue
                
                
                if not (len(str(temp_pin)) == 4):
                    print("Invalid input. Please try again. PIN must be 4 digits.")
                    continue
                
                
                self.pin = str(temp_pin)
                break
            
           
            self.mycursor.execute("UPDATE card_details SET pin_no = %s WHERE card_no = %s", (self.pin, self.card_no))
            self.mydb.commit()
            print("PIN set successfully")
        else:
            print("Sorry,Frist open an account!!!")
            time.sleep(10)
        self.GUI()

    


    def check_pin(self):
        
        while True:
            self.card_no = input("Enter your 16-digit card number here: ")
            if not (self.card_no.isdigit() and len(self.card_no) == 16):
                print("Invalid input. Please try again.")
                continue 
            break

     
        attempts = 0

        while attempts < 3:
           
            try:
                temp_pin = int(input("Enter Your PIN Here: "))
            except ValueError:
                print("Invalid PIN format. Please enter numeric PIN.")
                continue
            
            self.mycursor.execute("SELECT * FROM card_details WHERE card_no=%s AND pin_no=%s", (self.card_no, temp_pin))
            account_holder = self.mycursor.fetchone()
            if account_holder:
                print("PIN verified")
                print("Proceed")
                return True 
            else:
                attempts += 1  
                print(f"You have {3 - attempts} attempt(s) left out of 3.")
               
        print("3 incorrect PIN attempts. Your account is blocked for 1 minute.")
        time.sleep(10)  
        self.GUI()

    
    

    def expiry_check(self):
        
        self.mycursor.execute("SELECT issue_date FROM card_details WHERE card_no = %s", (self.card_no,))
        issue_date = self.mycursor.fetchone()[0]
        issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
        temp_expiry_date = issue_date + timedelta(days=60)  #relativedelta(years=3)
    
        if datetime.now() > temp_expiry_date:
          print("Your card has expired.")
          return False

        print("Card is still valid.")
        return True

                           
                
    def deposite(self):
        verify = self.check_pin()
        if verify:
         while True:
            try:
                amount = int(input("Enter the amount you want to deposite"))
                if amount <= 0:
                    print("Amount must be greater than 0")
                    continue
                break  
            except ValueError:
                    print("Invalid format. Please enter numeric characters.")
                   
        self.balance = amount
        self.mycursor.execute("UPDATE card_details SET balance = balance + %s WHERE card_no = %s", (self.balance, self.card_no))

        self.mydb.commit()
        print("deposit successful")
        self.GUI()

    def withdraw(self):

        verify = self.check_pin()
                
        if verify:
         while True:
            try:
                amount = int(input("Enter the amount you want to withdrawal"))
                if amount <= 0:
                    print("Amount must be greater than 0")
                    continue
                break  
            except ValueError:
                    print("Invalid format. Please enter numeric characters.")
        self.mycursor.execute("SELECT * FROM card_details WHERE card_no=%s",(self.card_no,))
        self.balance= int(self.mycursor.fetchone()[6])
        if amount <= self.balance:
            self.balance = amount
            self.mycursor.execute("UPDATE card_details SET balance = balance - %s WHERE card_no = %s", (self.balance, self.card_no))
            self.mydb.commit()
            print("Operation successful")
        else:
            print("insufficient Balance")  
        self.GUI()

    def check_balance(self):
                verify = self.check_pin()
                if verify:
                   self.mycursor.execute("SELECT * FROM card_details WHERE card_no=%s",(self.card_no,))
                   self.balance = self.mycursor.fetchone()
                   print(self.balance[6])
                self.GUI()
                
sbi = Atm()            
                            


            

            










        

