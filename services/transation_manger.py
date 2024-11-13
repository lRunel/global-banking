import datetime
class TransactionManagers:
    transaction_log = []

    @staticmethod
    def get_current_timestamp():
        return datetime.datetime.now()

    @classmethod
    def log_transactions(
        cls, account_number, amount, transaction_type, to_account_number=None
    ):
        transaction_record = {
            "account_number": account_number,
            "amount": amount,
            "transaction_type": transaction_type,
            "date": cls.get_current_timestamp(),
            "to-account_number": to_account_number,
        }
        cls.transaction_log.append(transaction_record)