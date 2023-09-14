# python 시각화 모듈
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [2,3,4,5]
plt.plot(x,y)
plt.show()
plt.bar(x,y)
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111) # 그래프의 틀

x2 = np.array(x)
y2 = np.array([4,5,1,2])

x3 = np.array([2,3,4,6])
y3 = np.array([1,4,2,7])

x4 = np.array([1,2,4,6])
y4 = np.array([2,4,3,6])

axes.plot(x,y, color="red", linestyle="dashed", marker="^")
axes.plot(x2,y2, color="k", linestyle="dotted", marker="o")
plt.show()

figure = plt.figure()
axes1 = figure.add_subplot(221) # 1행 2열에서 1열
axes1.plot(x,y)
axes2 = figure.add_subplot(222) # 1행 2열에서 2열
axes2.plot(x2,y2)
axes3 = figure.add_subplot(223)
axes3.plot(x3,y3)
axes4 = figure.add_subplot(224)
axes4.bar(x4,y4)
plt.show()


figure = plt.figure()
axes = figure.add_subplot(111)

axes.bar(x,y)
axes.bar(x2,y2)
plt.show()

figure = plt.figure()
axes1 = figure.add_subplot(111)
axes2 = axes1.twinx() # 그래프 곂치기
axes1.bar(x, y, color="blue", label="bar")
axes2.plot(x2, y2, color="red", label="plot")
plt.show()

# 폰트 찾기
from  matplotlib import font_manager, rc
# font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# for font in font_list:
#     print(font)
# 한글 폰트 적용하기
rc("font", family="D2Coding")
# 점 그래프 scatter
figure = plt.figure()
axes = figure.add_subplot(111)

x = [1,2,3,4]
y = [2,4,6,8]
x2 = [1,1,3,4]
y2 = [6,2,4,6]

axes.scatter(x,y)
axes.scatter(x2,y2)
plt.title("제목")
plt.xlabel("x축 이름")
plt.ylabel("y축 이름")
plt.show()

# 원형 그래프
figure = plt.figure()
axes = figure.add_subplot(111)

label = ["축구", "농구", "야구", "배구"]
data = [10, 20, 5, 30]

axes.pie(data, labels=label)
# plt.show()

# img 파일로 저장
plt.savefig("test")






