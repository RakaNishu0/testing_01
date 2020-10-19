# if 조건:
#     실행 명령문

# weather = input("날씨는 어떤가요? ")
# if weather == "비":
#     print("우산 필수")
# elif weather == "미세먼지":
#     print("마스크 써라")
# else:
#     print("Let's go")

temp = int(input("오늘 온도는 몇도입니까? "))
if 30 <= temp:
    print("너무 덥다 에어컨 좀")
elif 10 <= temp < 30:
    print("적당하네")
elif 0 <= temp < 10:
    print("춥다...")
else:
    print("얼어 죽겠다!")
