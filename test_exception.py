# exception
# Error 가 발생하는 상황을 어떻게 처리할 것인가?

# num1 = int(input("1st number : "))
# num2 = int(input("2nd number : "))
# print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# ValueError: invalid literal for int() with base 10: '삼'   <- ValueError 가 발생하면서 프로그램 종료.

# try:                                            # try & except = 에러 발생하면 except로 보내며, 종료시키지 않는다
#     num1 = int(input("1st number : "))
#     num2 = int(input("2nd number : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("Error! Please insert int()")         # ValueError 에 대한 반응
# except ZeroDivisionError as err:
#     print(err, "Cannot divide by 0")            # ZeroDivisionError 에 대한 반응
# except  Exception as err:
#     print(err)                                  # 그 외 모든 에러에 대한 반응


# try:
#     num1 = int(input("1st number : "))
#     num2 = int(input("2nd number : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError                        # raise = 지정한 Error로 우회시킨다.
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("Wrong value. insert 1 digit")

# User Custom Error Exception:
# class BigNumErr(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
#
# try:
#     num1 = int(input("1st number : "))
#     num2 = int(input("2nd number : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumErr("input : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("Wrong value. insert 1 digit")
# except BigNumErr as err:
#     print("Too Big Number. insert 1 digit")
#     print(err)


# finally. = try문 내에서 거의 마지막에 실행. 중간에 에러가 있든 없든 실행이 되는 구문.



# 퀴즈
# 자동주문 프로그램을 작성하시오
# 조건 1 : 1보다 작거나, 숫자가 아닌 값 = ValueError "잘못된 값을 입력하였습니다."
# 조건 2 : 치킨량은 총 10마리. 소진시 사용자정의 에러 [SoldOutError] 출력 후 종료
# "재고가 소진되어 더이상 주문을 받지 않습니다."

# [코드예문] - 수정해서 완성하시오
chicken = 10
waiting = 1         # 홀 안에는 만석. 대기번호 1번부터 시작


class SoldOutError(Exception):
    pass


while(True):
    print("[남은치킨]: {0} 마리".format(chicken))
    try:                           # try: 구문을 while 보다 위에 두면 에러처리 후 while 이 반복되지 않는다.
        order = int(input("치킨을 몇마리 주문하겠는가? : "))
        if order > chicken:         # 남은 치킨보다 주문량이 많으면
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError                # 1보다 작은 수에 대해선 ValueError 로 우회시킨다
        else:
            print("[대기번호 {0}]: {1} 마리 주문이 접수되었다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:                    # chicken 재고가 0이 되면
            raise SoldOutError              # SoldOutError 로 우회시킨다

    except ValueError:
        print("잘못된 값을 입력함")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문이 불가합니다.")
        break                               # 프로그램 종료
