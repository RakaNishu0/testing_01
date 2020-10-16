# 랜덤 함수

# from random import *        # 랜덤 모듈을 불러오기
#
# print(random())             # 0.0 ~ 1.0 사이의 랜덤한 값을 1개 출력하는 함수
# print(int(random() * 10))        # 0.0 ~ 1.0 사이의 값에 10을 곱하고 그 값을 '정수'로 변환
# print(randrange(1, 45))      # 첫 인수와 두번째 인수 "미만"의 정수값을 랜덤으로 1개 출력하는 함수
#
# day = randint(4, 28)        # 첫번째 인수와 두번째 인수 "이하"의 정수(int)값을 랜덤으로 1개 출력하는 함수
# print("모임 일자는 " + str(day)+"일입니다.")
#

# 문자열의 슬라이스
# jumin = "861230-1234567"
#
# print('성별 :' + jumin[7])            # 7번째의 문자열을 출력
# print('year :' + jumin[0:2])        # 0 번째부터 2번째 앞까지의 문자열을 출력
# print('month :' + jumin[2:4])        # 2 번째부터 4번째 앞가지의 문자열을 출력
# print('y-m-d :' + jumin[:6])        # 처음부터 6번째 앞까지(0~5)의 문자열을 출력
# print('num :' + jumin[7:])          # 7번째 부터 끝까지의 문자열을 출력
# print('num- :' + jumin[-7:])        # 뒤에서부터 숫자를 세어 7번째 자리부터 끝까지 출력


# 문자열 처리 함수
console = "Xbox is Amazing"
print(console.lower())                      # lower() 모든 문자열을 소문자로
print(console.upper())                      # upper() 모든 문자열을 대문자로
print(console[0].isupper())                 # isupper() 해당 문자가 대문자인가? T or F
print(len(console))                         # len() 문자열의 길이
print(console.replace("Xbox", "PS5"))       # replace() 문자열을 찾아서 치환. replace(타겟, 치환)

index = console.index("A")                  # index() 몇번째 자리에 해당 문자가 위치해 있는지 찾아줌
print(index)
print(console.find("a"))                    # find() 몇번재 자리에 해당 문자가 있는지 찾아줌
print(console.find('PS5'))                  # find() 는 index()와 달리, 결과가 없어도 에러를 뱉지 않고 -1 을 반환하면서 프로그램을 종료시키지는 않는다.
print(console.index('PS5'))                 # index() 는 찾을 수 없는 문자열인 경우 Error 를 반환하며 프로그램을 강제 종료한다.
