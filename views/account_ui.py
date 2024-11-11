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
            option = int(input('\nEnter your option: '))
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

        def close_account(self):
            pass

        def withdraw_funds(self):
            pass

        def deposit_funds(self):
            pass
