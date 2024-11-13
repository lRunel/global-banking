class AccountRepository:
    account  = []
    account_counter = 1000

    # method to generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter
    
    # Method to save Account
    @classmethod
    def save_account(cls,account):
        cls.account.append(account)

    # method to get all accounts
    def get_all_accounts(self):
        return self.account