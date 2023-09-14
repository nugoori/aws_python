import pandas as pd
import numpy as np

#####[ Series ] #####
a = pd.Series({"a": 1, "b": 2, "c": 3})
print(a)
print(a.index)

a = np.array([1,2,3,4])
b = pd.Series(a)
print(b)
print(b.index.values) # Series타입에서의 key값 type=object> values로 값 가져오기 가능

#####[ dataFrame ] #####
a = {"a": [1,2,3, 0], "b": [4,5,6, 0], "c": [7,8,9, 0], "d": [10, 11, 12, 0]}
b = pd.Series(a)
# c = pd.DataFrame(a, index=["a", "b", "c"])
c = pd.DataFrame(a, index=a.keys())
print(b)
print(c)
print(c.index.values)
print(c.columns)

a = pd.DataFrame({"a": (1,2), "b":1, "c":3}) #
print(a)
a.index = ["x", "y"]
a.columns= ["i", "j", "k"]
print()
print(a)
print()
print(a.loc[a["j"] == 1]) # loc 에는 조건을 넣을 수도 있음
print()
print(a.iloc[0])

a = {"a": [1,2,3], "b": [4,5,6], "c": [7,8,9], "d": [10, 11, 12]}
b = pd.DataFrame(a)
print()
print(b.describe())

print()
print(b.sum())
print(b.sum(axis=1)) # axis=1 : sum함수의 방향?을 바꿈
print(b.min())
print(b.max())
print(b.mean()) # 평균
print(b.std(), b.var()) # * 표준편차, 분산




