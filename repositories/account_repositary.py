class AccountRepository:
    #Class attribute here
    account=[]
    accou_counter = 1000
    #Methhod to generate a new account number 
    @classmethod
    def generate_account_number(cls):
        cls.account_counter  += 1
        return cls.accou_counter