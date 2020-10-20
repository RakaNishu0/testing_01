# print( sep= )
# print("Python", "java", "C", sep=" vs ")    # sep= 파라미터. 문자열 사이의 출력에 대해 지정할 수 있다.

# print( end= )             # end= 한 줄을 end=의 값으로 표기하고 다음 줄로 넘어가지 않는다

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# scores = {"math":10, "lang":30, "science":100}
# for subject, score in scores.items():
#     print(subject, score)
# #
# scores = {"math":10, "lang":30, "science":100}
# for subject, score in scores.items():
#     print(subject.ljust(10), str(score).rjust(8), sep=";")
# # ljust(x) = x만큼 공간을 확보하고 왼쪽 정렬
# # rjust(x) = x만큼 공간을 확보하고 오른쪽 정렬
# #
# for num in range(1, 21):
#     print("standby : "+str(num).zfill(3))
# # zfill(x) = x자리수 만큼 표시를 하고, 공백은 0으로 채운다. 1 = 001


# Standard input

# answer = input("Input value :")
# print(type(answer))         # input() 으로 받는 값은 '무조건' str()이다.


# output format
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(300))
# 양수 = + / 음수 = -
print("{0: >+5}".format(400))
print("{0: >+5}".format(-500))
# 왼쪽 정렬을 하고, 빈칸은 _ 로 채움
print("{0:_<+7}".format(700))
# 3자리마다 , 를 찍어주기
print("{0:,}".format(1000000000000000))
# 3자리마다 , 를 찍어주기, +/- 기호 붙이기
print("{0:+,}".format(-10000000000))
# 3자리마다 , 를 찍어주기, +/- 기호 붙이기, 공간 확보 + 빈공간은 * 로 채우기
print("{0:*>+30,}".format(-10000000000))
# 소수점 출력
print("{0:f}".format(4/3))
# 소수점 특정 자리수까지만 출력
print("{0:.2f}".format(4/3))        # 3번째 자리에서 반올림해서 2자리까지만 출력
