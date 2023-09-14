from userManagement.controller.UserController import UserController
from userManagement.repository.UserRepository import pd
from userManagement.entity.User import User

class UserView:

    @staticmethod
    def register():
        # 모듈을 불러올 때 코드 상 위치를 주의 해야 함( 사용 되는 곳에서 만 사용 하는게 좋을 수도? )
        print("[사용자 등록 화면]")
        username = input("사용자 이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        response = UserController.registerUser(User(
            # User객체의 builder pattern이 필요가 없음
            username=username,
            password=password,
            name=name,
            email=email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 추가하던 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요")

    @staticmethod
    def ShowAllUser():
        # print("[사용자 전체 조회]")
        # print(pd.DataFrame(UserRepository.getUsersAll()))

        ###
        response = UserController.getAllUser()
        if bool(response.body):
            print(pd.DataFrame(response.body))
        else:
            print("조회 할 데이터가 없습니다.")

        if not response.__dict__.get("body"):
            print("데이터를 가져오던 중 오류가 발생하였습니다")
        print()

    @staticmethod
    def ShowUserByUsername():
        print("[특정 사용자 정보]")
        username = input("찾으실 사용자 이름을 입력하세요 >>> ")

        response = UserController.getUserByUsername(username)
        if bool(response.body):
            print(pd.Series(response.body))
        else:
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def updateUser():
        print("[ 사용자 정보 수정 ]")
        response = UserController.getAllUser()
        if not bool(response.body):
            print("수정할 사용자 정보를 조회 할 수 없습니다")
            return
        df = pd.DataFrame(response.body)
        print(df)
        userId = input("수정할 사용자 ID를 입력하세요 >>>")
        index = df.index[df["userId"] == int(userId)].values[0] # loc(=location) .index[조건] / .values : list로 변환
        print(index)
        print(df.iloc[index]) # iloc : indexLocation > 한개면 series로 return
        user = UserView.showUpdateMenu(response.body[index])
        if not bool(user):
            print("수정을 취소하였습니다.")
            return

        response = UserController.updateUser(user)
        if(bool(response.body)):
            print("===== << 수정 완료 >> =====")

    # put : data가 공백으로 날아오면 공백으로 update가 됨
    # patch : data가 공백으로 날아오면 이전 데이터 유지
    @staticmethod
    def showUpdateMenu(oldUser):
        newUser = oldUser.copy()
        
        while True:
            print("-" * 30)
            df = pd.DataFrame([oldUser, newUser], index=["수정 전", "수정 후"])
            print(df)
            print("-" * 30)
            print("1. password 수정")
            print("2. name 수정")
            print("3. email 수정")
            print("s. 저장")
            print("c. 취소")
            select = input("메뉴 선택 >>>")

            if select == "c":
                return None
            elif select == "s":
                return newUser
            elif select == "1":
                password = input("비밀번호 입력 >>>")

                if not UserView.isValid(oldUser.get("password"), password):
                    continue

                checkPassword = input("비밀번호 확인 >>>")
                if checkPassword != password:
                    print("비밀번호가 일치하지 않습니다.")
                    continue
                newUser["password"] = password

            elif select == "2":
                name = input("이름 입력 >>>")

                if not UserView.isValid(oldUser.get("name"), name):
                    continue

                newUser["name"] = name
            elif select == "3":
                email = input("이메일 입력 >>>")

                if not UserView.isValid(oldUser.get("email"), email):
                    continue

                newUser["email"] = email
            else:
                print("선택한 번호는 등록되지 않은 번호입니다.")
                print()

        return False

    @staticmethod
    def isValid(oldValue, value):
        if not bool(value):
            print("공백일 수 없습니다.")
            return False
        elif oldValue == value:
            print("기존의 비밀번호와 동일합니다.")
            return False

        return True

    @staticmethod
    def delete():
        print("")
        response = UserController.getAllUser()
        if not bool(response.body):
            print("삭제할 사용자 정보를 조회 할 수 없습니다")
            return
        df = pd.DataFrame(response.body)
        print(df)
        userId = input("수정할 사용자 ID를 입력하세요 >>>")
        index = df.index[df["userId"] == int(userId)].values[0]
        print(index)
        # print(df.iloc[index])
        # deleteMenu로 빼야 할 부분
        # userController에서 매개변수로 넘길 user를 받으면 삭제는되지만 'ResponseEntity' object has no attribute 'get'
        user = UserController.deleteUserByUserId(response.body[index])

        if userId == user:
            UserController.deleteUserByUserId(user)
            print("선택한 사용자 정보를 삭제하였습니다.")






