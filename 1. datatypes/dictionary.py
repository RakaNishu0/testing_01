# dictionary

cabinet = {3:"choi", 100:"yo33yo"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5])               # 잘못된 키를 요구하면 프로그램이 바로 종료된다
print(cabinet.get(5))           # get() 을 이용하면 None 을 출력하고 프로그램은 이어진다.

print(3 in cabinet)             # True or False 로 확인할 수도 있다
print(4 in cabinet)

cabinet[50] = "kim"                 # 50 이라는 키(key)에 "kim"의 값을 추가
cabinet[3] = "jeong"                # 3 이라는 키에 이미 있던 값을 지우고 "jeong"의 값을 추가
print(cabinet)

del cabinet[3]                      # 3 이라는 키를 삭제
print(cabinet)

print(cabinet.keys())               # key 만 출력
print(cabinet.values())             # value 만 출력
print(cabinet.items())              # 모두 출력

cabinet.clear()                     # 내용 모두 삭제
print(cabinet)