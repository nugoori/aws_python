class UserInfo:

    # cls변수( 클래스변수 == static )
    adminUser = {
        "username": "root",
        "password": "1q2w3e4r"
    }

    def __init__(self):
        self.adminUser = {
            "username": "user1",
            "password": "1234"
        }

    @classmethod
    def showAdinUser(cls):
        print("[showAdminUser]")
        print(cls.adminUser)

class User:
    # init에 멤버변수를 작성
    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print("그냥 실행할 수 있는 메소드")

if __name__ == "__main__":
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(UserInfo.adminUser)

    userInfo.showAdinUser()
    UserInfo.showAdinUser()

    User.showUserClassInfo()