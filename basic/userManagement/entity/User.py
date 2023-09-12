class User:

    def __init__(self, userId=None, username=None, password=None, name=None, email=None):
        self.userId = userId
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __str__(self):
        # """ """를 사용할 때에는 들여쓰기를 조심 해야함
        return f"""[User]
userId: {self.userId}
username: {self.username}
password: {self.password}
name: {self.name}
email: {self.email}
"""