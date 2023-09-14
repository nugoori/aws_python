import pandas as pd
import numpy as np

##### [ CSV 파일 불러오기 ] #####
data = pd.read_csv("books_data.csv", encoding="euc-kr") # encoding 주의, 기본 encoding은 UTF-8 // 한글-> cp949?
print(data)
print(data.columns)
print()
print(data.loc[data["도서명"] == "퇴사 후 독립출판 책만들기"])

# 일반 excel을 바로 불러오는 csv 라이브러리
import csv
f = open("books_data.csv", "r") # encoding 종류? 적용 가능
csvData = csv.reader(f)
i = 0
for data in csvData:
    if i < 10:
        print(data)
    else:
        break
    i += 1