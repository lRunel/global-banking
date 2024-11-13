from services.account_manager import AccountManager
from services.transation_manger import TransactionManagers
from repositories.account_repositary import AccountRepository
class AccountUI:
    def start(self):
        while True:
            print('\nWelcome to Global Digital Bank')
            print('\nSelect an option')
            print('1. Open Account')
            print('2. Close Account')
            print('3. Withdraw Funds')
            print('4. Deposit Funds')
            print('5. Transfer Funds')
            print('9. Exit')
            #option = int(input('\nEnter your option: '))
            choice = int(input('Enter your choice: '))

            if choice == 1:
                self.open_account()
            elif choice == 2:
                self.close_account()
            elif choice == 3:
                self.withdraw_funds()
            elif choice == 4:
                self.deposit_funds()
            elif choice == 5:
                self.transfer_funds()
            elif choice == 9:
                break
            else:
                print('Invalid choice. Please try again')
    def open_account(self):
        account_type = input('Enter account type (savings/current): ').strip().lower()
        name = input('Enter your name: ')
        amount = float(input('Enter initial deposit amount: '))
        pin_number = input('Enter your pin number: ')
        privilege = input('Enter account privilege (PREMIUM/GOLD/SILVER): ').strip().upper()
        if account_type == "savings":
            date_of_birth = input("Enter the date of birth(YYYY-MM-DD) : ")
            gender = input("Enter gender (M/F) : ")
            account = AccountManager().open_account(
            account_type,
            name=name,
            balance=amount,
            date_of_birth=date_of_birth,
            gender=gender,
            pin_number=pin_number,
            privilege=privilege,
            )

        elif account_type == "current":
            registration_number = input("Enter your registrtion number : ")
            website_url = input("Enter your website URL")
            account = AccountManager().open_account(
                account_type,
                name=name,
                balance=amount,
                registration_number=registration_number,
                website_url=website_url,
                pin_number=pin_number,
                privilege=privilege,
            )
        
        else:
            print("Invalid account type. Please try again")
            return
        print(account_type.capitalize(),"Account opened successfully. Account Number : ",account.account_number)

    def close_account(self):
        account_number=int(input("Enter the Account number : "))
        account=next((acc for acc in AccountRepository.account if acc.account_number == account_number),None)

        if account:
            try:
                AccountManager().close_account(account)
                print("Account closed successfully")
            except Exception as e:
                print("Error : ",e)
        
        else:
            print("Account Not Found. Please try again ")
        



    def withdraw_funds(self):
        account_number=int(input("Enter the Account number : "))
        amount=float(input("Enter amount to Withdraw : "))
        pin_number=input("Enter the pin number : ")
        account=next((acc for acc in AccountRepository.account if acc.account_number == account_number),None)
        
        if account:
            try:
                AccountManager().withdraw(account)
                print("Account withdrawn successfully")
            except Exception as e:
                print("Error : ",e)
        
        else:
            print("not enough fund. Please try again ")
    def deposit_funds(self):
        account_number=int(input("Enter the Account number : "))
        amount=float(input("Enter amount to deposited : "))
        account=next((acc for acc in AccountRepository.account if acc.account_number == account_number),None)
        
        if account:
            try:
                AccountManager().deposit(account,amount)
                print("amount deposited successfully")
            except Exception as e:
                print("Error : ",e)
        
        else:
            print("Account Not Found. Please try again ")

    def transfer_funds(self):
        sender_account_number=int(input("enter sender "))
        reciever_account_number=int(input("enter reciever "))
        pin_number=int(input("enter your pin number"))
        amount=float(input("Enter amount to Withdraw : "))
        sender_account=next((acc for acc in AccountRepository.account if acc.account_number == sender_account_number),None)
        reciever_account=next((acc for acc in AccountRepository.account if acc.account_number == reciever_account_number),None)
        if reciever_account and  sender_account:
            try:
                AccountManager().transfer(sender_account,reciever_account,amount,pin_number)
                print("amount deposited successfully")
            except Exception as e:
                print("Error : ",e)
        
        else:
            print("Account Not Found. Please try again ")