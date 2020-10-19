# Change data type

menu = {"커피", "우유", "쥬스", "홍차"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))



# 퀴즈
# rule 1 : 댓글은 20명, 1 ~ 20
# rule 2 : 무작위 추첨, 중복 불가
# rule 3 : random 모듈의 shuffle, sample 활용

# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

from random import *
# i = 1
# lst = []
# while i <= 20:            # while 을 사용하면 만들 수는 있지만, 5줄이나 필요함
#     lst.append(i)
#     i += 1
lst = range(1, 21)          # range() 를 이용하여 1 ~ 20 까지의 숫자를 생성.
print(type(lst))            # 단, range() 함수로 생성된 숫자의 타입은 range타입 (=/=리스트)

# print(lst)
lst = list(lst)             # lst 변수를 list 타입으로 변경
shuffle(lst)                # shuffle 함수는 range 데이터타입으로는 사용할 수 없다.

# chicken = sample(lst, 1)
# coffee = sample(lst, 3)
winner = sample(lst, 4)     # 4명의 당첨자를 샘플링 추출

print("-- 당첨 축하 --")
print("치킨 당첨자 : {}".format(winner[0]))
print("커피 당첨자 : {}".format(winner[1:]))
print("-- 축하 축하 --")
