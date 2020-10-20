# function

# def profile(name, age, *language):                      # 가변인수, 개수의 증감이 있을 경우에 활용가능
#     print("이름: {0}, 나이: {1}".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
#
# profile("kim", 18, "python", "java", "C", "JS", "React")
# profile("han", 37, "java", "js")

# 전역 / 지역 변수

# gun = 10
#
# def checkpoint(soldiers):
# #    gun = 15                        # 지역변수 = 함수 내에서만 활용되는 변수. 함수 밖의 변수와는 연동되지 않는다. 앞에 global같은게 없음
#     global gun                          # 전역변수 = 함수 밖의 변수도 그대로 가져와서 사용할 수 있게 global을 붙여준다
#     gun = gun - soldiers
#     print("(함수 내)남은 총 : {0}".format(gun))
#
#
# print("전체 총 : {0}".format(gun))
# checkpoint(3)
# print("남은 총: {0}".format(gun))


# 퀴즈
# 표준체중 : 각 키에 적당한 체중
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21
#
# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#       함수명 : std_weight
#       전달값 : 키(height), 성별(gender)
# ex) 키 ~~ 남자의 표준 체중은 ~~ 입니다.

def std_weight(height, gender):
    m = height / 100
    if gender == "남자":
        h = m*m*22
    elif gender == "여자":
        h = m*m*21
    else:
        pass
    return round(h, 2)


height = 160
gender = "남자"
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight(height, gender)))
