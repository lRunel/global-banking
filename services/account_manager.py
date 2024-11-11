from models.savings import Savings
from models.current import Current
from repositories.account_repositary import AccountRepository
from exception.exceptions import AccountNotActiveExeption
from exception.exceptions import InvlidPinException
from exception.exceptions import InsufficientFundsException
from services.transation_manger import TransactionManagers

class AccountManager:
    def open_accoint(self,account_type,**kwargs):
        if account_type=='savings':
            new_account= Savings(**kwargs)
        elif account_type == 'current':
            new_account = Current
        else:
            raise ValueError('Invalid account type')
        AccountRepository.save_account(new_account)
        return new_account
    def check_acccout_active(self,account):
        if not account.is_active:
            raise AccountNotActiveExeption('Account is not Active')
    def validate_pin(self,account,pin_number):
        if account.pin_number != pin_number:
            raise InvlidPinException('Invail Pin')
    def withdraw(self,account,amount,pin_number):
        self.check_acccout_active(account)
        self.validate_pin(account,pin_number)
        if account.balace < amount:
            raise InsufficientFundsException('Insufficient funds')
        account.balance -= amount
        TransactionManagers.log_transaction(account.account_number,amount,'withdraw')
    def deposit(self,account,amount):
        self.check_acccout_active(account)

        account.balance +=amount
        TransactionManagers.log_transactions(account.account_number,amount)
    def transfer(self, from_account, to_account, amount, pin_number):
     self.check_account_active(from_account)
     self.check_account_active(to_account)
     self.validate_pin(from_account, pin_number)

     if from_account.balance < amount:
        raise InsufficientFundsException('Insufficient funds')

     limit = AccountPrivilegesManager.get_transfer_limit(from_account.privilege)
     if amount > limit:
        raise TransferLimitExceededException('Transfer limit exceeded')

     from_account.balance -= amount
     to_account.balance += amount
     TransactionManager.log_transaction(from_account.account_number, amount, 'transfer', to_account.account_number)

