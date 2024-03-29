# numpy_study :
# 고성능(대량)의 수치 계산을 위한 라이브러리
# 벡터, 행렬 연산에 사용

import numpy as np

numArray1 = [1,2,3,4,5]
numArray2 = [6,7,8,9,10]

numArray3 = []
for i in range(len(numArray1)):
    numArray3.append(numArray1[i] + numArray2[i])

print(numArray3)

npArray1 = np.array(numArray1)
npArray2 = np.array(numArray2)
npArray3 = npArray1 * npArray2

print(npArray1)
print(npArray2)
print(npArray3)

npDoubleArray1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
npDoubleArray2 = np.array([[11,12,13,14,15], [16,17,18,19,20]])
print(npDoubleArray1)
print(npDoubleArray2)
print(npDoubleArray1 + npDoubleArray2)

print(npArray1.shape)
print(npDoubleArray1.shape)


npArray4 = np.arange(1,11) # 배열의 범위를 지정하여 생성
print(npArray4)

npArray5 = np.zeros(10)
print(npArray5)
npArray6 = np.zeros_like(npDoubleArray1)
print(npArray6)
npArray7 = np.ones(10)
print(npArray7)
npArray8 = np.ones_like(npDoubleArray1)
print(npArray8)
npArray9 = np.full((5, ), 5) #(행, 열)
print(npArray9)

print(npArray9 * 2)