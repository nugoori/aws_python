class Student:
    # 생성자 ****
    # self == this -> 자신의 주소(생성된 객체의 주소)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # toString()
    def __str__(self):
        return f"Student[name: {self.name}, age: {self.age}]"

    def setName(self, name):
        self.name = name

    print("학생 모듈", __name__)


def main():
    # new 키워드가 필요가 없음
    s1 = Student("김준일", 30)
    print(s1.name)
main()