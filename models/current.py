from models.account import Account 
class Current(Account):
    def __init__(self, name, balance,wesite_url,pin_number, pivilege,registration_number):
        super().__init__( name, balance,pin_number, privilege)
        self.company_name=company_name
        self.registration_number=registration_number
        self.website_url=website_url