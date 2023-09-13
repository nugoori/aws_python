from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
import pandas as pd

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        try:
                        # db 연결
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor) # .cursor의 종류?지정, 기본 타입은 튜플
            sql = """
            insert into user_tb
            values(0, %s, %s, %s, %s)
            """
            # %s : setString / %~
            # db에 저장 # cursor (= java: preparedstatement) sql문을 실행해주는? 반복을 돌면서 %s에 순서대로 대입?
            insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
            connection.commit()
            return insertCount
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def getUsersAll():
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select 
                user_id as userId,
                username,
                password,
                name,
                email 
            from user_tb        
            """
            cursor.execute(sql)
            rs = cursor.fetchall() # fetchone : 제일 위의 column한 줄을 가져옴
            return rs
        except Exception as e:
            print(e)
            return None
        # Series : dict 타입 하나만 넣어 줘야함
        # df = pd.DataFrame(data)
        # df = pd.DataFrame(userList) # list형식에 key value만 맞춰져 있다먼 pandas가 자동으로 변형해 줌
        # print(df)

    @staticmethod
    def selectUserByUsername(username = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
                select
                    user_id as userId,
                    username,
                    password,
                    name,
                    email
                from
                    user_tb
                where
                    username = %s
            """
            #     f"" username = '{username}' ""
            cursor.execute(sql, username)
            rs = cursor.fetchone()
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def updateUser(user=None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor) # .cursor의 종류?지정, 기본 타입은 튜플
            sql = """
            insert into user_tb
            set
                password = %s,
                name = %s,
                emai; = %s
            where
                user_id = %s
            """
            insertCount = cursor.execute(sql,
                        (user.get("password"), user.get("name"), user.get("email"), user.get("userId")))
            connection.commit()
            return insertCount

        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def deleteUser(user=None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)  # .cursor의 종류?지정, 기본 타입은 튜플
            sql = """
                delete
                from user_tb
                where
                    user_id = %s
            """
            insertCount = cursor.execute(sql, user.get("userId"))
            connection.commit()
            return insertCount

        except Exception as e:
            print(e)
            return 0