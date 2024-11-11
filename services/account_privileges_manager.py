from models.privileges import Privilege
class AccountPrivilegeManager:
    Privilege={'PREMIUM':100000,
    'GOLD':50000,
    'SILVER':25000
    }
    @classmethod
    def get_transfer_limit(cls,privilege):
        return