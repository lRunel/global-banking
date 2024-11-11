class Account:
    def __init__(self,account_number,name,balance,isactive,privilege):
        self.account_number=account_number
        self.name=name
        self.balance =balance
        self.isactive=isactive
        self.privilege=privilege
        self.is_active=True 
        self.closed_date=None

        