class StudentRepository:

    def __init__(self):
        self.studentList = [] # list()

    def add(self, student):
        self.studentList.append(student)
        print("학생을 추가하였습니다.")

    def findStudentByName(self, name):
        for student in self.studentList:
            if student.name == name:
                return student
        return None

# 오버라이딩
def marine():
    pass

def main():
    from Student import Student # import만 하면 모듈만 받아오게 되므로 그걸 참조하여 안의 요소들을 사용해야 한다
    # from: 모듈파일 import: 모듈내부의 클래스, 함수, 변수
    sr = StudentRepository()
    sr.add(Student("김준일", 30))
    sr.add(Student("김준이", 31))
    sr.add(Student("김준삼", 32))
    sr.add(Student("김준사", 33))

    print(sr.studentList)

    print(sr.findStudentByName("김준일"))

main()

print("학생 저장소 모듈", __name__)




