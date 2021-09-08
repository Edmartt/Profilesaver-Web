from werkzeug.security import check_password_hash, generate_password_hash


class User:
    id: int
    username: str
    email: str
    password: str

    def __init__(self, username: str, password: str, email=None, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self) -> None:
        raise AttributeError('Forbidden access')

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
