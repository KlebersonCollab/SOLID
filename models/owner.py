from models.developer import Developer
from models.developer import Developer
from models.user import User


class Owner(User, Developer):
    def __init__(self, username, email):
        super().__init__(username, email)
        
    @staticmethod
    def member():
        return ['username 1','username 2','team 1']