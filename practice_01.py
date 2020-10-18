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
# console = "Xbox is Amazing"
# print(console.lower())                      # lower() 모든 문자열을 소문자로
# print(console.upper())                      # upper() 모든 문자열을 대문자로
# print(console[0].isupper())                 # isupper() 해당 문자가 대문자인가? T or F
# print(len(console))                         # len() 문자열의 길이
# print(console.replace("Xbox", "PS5"))       # replace() 문자열을 찾아서 치환. replace(타겟, 치환)
# print(console.count("i"))                   # count() 문자열에서 해당 문자가 몇번 나타났는지를 출력
#
# index = console.index("A")                  # index() 몇번째 자리에 해당 문자가 위치해 있는지 찾아줌
# print(index)
# print(console.find("a"))                    # find() 몇번재 자리에 해당 문자가 있는지 찾아줌
# print(console.find('PS5'))                  # find() 는 index()와 달리, 결과가 없어도 에러를 뱉지 않고 -1 을 반환하면서 프로그램을 종료시키지는 않는다.
# # print(console.index('PS5'))                 # index() 는 찾을 수 없는 문자열인 경우 Error 를 반환하며 프로그램을 강제 종료한다.
#
# # 문자열 포맷
# a = 10
# s = "yoda"
# b = "A"
# print("Me is %d years old" % a)             # %d = 정수(int)
# print("Me is %s" % s)                           # %s = 문자열(string), 하지만 정수도 정상적으로 받는다.
# print("Me is %s years old" % a)
# print("Apple is starting %c" % b)               # %c = 문자(character) 1개만
# print("I love %s and %s color" % ("Red", "Blue"))   # 여러개를 사용할 경우에는 그 수만큼 사용하고 ()안에 넣어줌
#
# print("Me is {} years old".format(15))          # {} 사용하는 대입변수 사용
# print("I love {} and {} color".format("Red", "Blue"))   # 마찬가지로 복수개의 대입 사용 가능
# print("I love {1} and {0} color".format("Red", "Blue")) # {}안에 숫자 표시는 index의 순서로, 자료형의 순서와 별개로 지정하여 출력할 수 있다.
#
# print("I am {age} years and love {color} color".format(age = 17, color="Red"))  # {}안의 변수를 format() 안에서 지정할 수 있다.
#
# age = 18
# color = "Blue"
# print('Me is {age} years and love {color} color')       # f 함수?를 사용하지 않음
# print(f'Me is {age} years and love {color} color')      # f 함수?를 사용해서 문자열 안에 변수를 적용가능
#


# 탈출문자
# print("백문이 불여일견\n백견이 불여일타")                     # \n = 줄바꿈
# print("\", \'")                                         # \", \' = 따옴표 기호로 사용하기
# print("\\")                                             # \\ = \ 역슬래시 기호로 사용하기
# print("Re Born\rRed")                                   # \r = 커서를 맨 앞으로 이동하여 뒤의 문자열을 쓰기
# print("a\tb")                                           # \t = tab (4 spaces)
# print("aabbcc\b")                                       # \b = backspace (1글자 삭제)

# 퀴즈
# 사이트별로 비밀번호를 만드는 프로그램을 작성
# 규칙1 : https:// 부분은 제외
# 규칙2 : 처음 만나는 . 이후의 부분은 제외
# 규칙3 : 남은 글자 처음 3자리 + 남은 글자 갯수 + 글자 내 'e'의 갯수 + ! 로 구성하기

domain = "https://youtube.com"

# print(domain.find(":")+3)
# print(domain.find("."))

base = domain[domain.find(":")+3:domain.find(".")]
# print(base)
r1 = base[:3]
r2 = len(base)
r3 = base.count('e')

print(f"{domain}'s password is... \"{r1}{r2}{r3}!\"")
