# for

# for waiting in range(10):
#     print("대기번호 : {}".format(waiting))

# starbucks = ["ironMan", "Thor", "Groot", "Yoda"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))


# while
# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{0}, 커피 레디. {1}번 남았다".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("버렸다")

# customer = "IronMan"
# i = 1
# while True:                                   # 조건이 True인 동안에 반복하는 것이므로, 이는 무한반복문이 된다.
#     print("{0}, Ready. Called {1} times".format(customer, i))
#     i += 1


# continue & break

# absent = [2, 5]
# no_book = [8]
# for student in range(1, 11):
#     if student in absent:
#         continue                            # 이하 문장을 수행하지 않고, for 문을 다시 시작하게 한다.
#     elif student in no_book:
#         print("{0}, break it".format(student))
#         break                               # 이하 문장이 무엇이 오든 반복문을 끝낸다.
#     print("{0}, read it".format(student))
#
# # for 문의 활용
#
# student = [1, 2, 3, 4, 5]
# student = [i+10 for i in student]           # student 리스트의 내용마다 10을 더한 값을 i로 해서 다시 만든다
# print(student)
#
# students = ["ironman", "thor", "hulk"]
# # students = [len(i) for i in students]     # students의 값을 i에 넣고, i의 길이를 출력하여 리스트로 만든다.
# # print(students)
# students = [i.upper() for i in students]    # students의 값을 i에 넣고, 대문자로 변환하여 리스트로 만든다.
# print(students)


# 퀴즈
# 50명의 승객을 매칭할 수 있다. 다음의 조건을 만족할 수 있는 총 탑승 승객 수를 구하라
# 조건 1 : 운행 소요시간은 5분 ~ 50분 랜덤
# 조건 2 : 소요시간 5분 ~ 15분 사이인 승객만 매칭해야 한다.

from random import *

i = 0
# passenger = list(range(1, 51))
# for matching in passenger:
for pasngr in range(1, 51):
    tf_time = randrange(5, 51)
    if 5 <= tf_time <= 15:
        i += 1
        print(f"[O] {pasngr}번째, (소요시간 : {tf_time}분)")
    else:
        print(f"[ ] {pasngr}번째, (소요시간 : {tf_time}분)")

print(f"총 탑승 가능 : {i}명")
