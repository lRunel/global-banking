from repositories.account_repositary import AccountRepository
class Account:
    def __init__(self,account_number,name,balance,privilege):
        self.account_number=AccountRepository.generate_account_number()
        self.name=name
        self.balance =balance
        self.privilege=privilege
        self.is_active=True 
        self.closed_date=None

        