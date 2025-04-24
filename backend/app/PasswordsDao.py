from app.model import Passwords

from app.dao import BaseDao


class PasswordsDao(BaseDao):
    model = Passwords
