# SET
# 집합. 중복이 안되고 순서가 없다. 출력 시 입력되어 있는 순서를 보장하지 않는다.

myset = {1, 2, 3, 3, 3}         # 중복되는 3은 1개만 표시된다.
print(myset)

# 집합의 논리연산
java = {"kim", "jeong", "yo", "park"}
python = set(["jo", "park"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가 & 삭제하기
python.add("kim")
python.remove("jo")
print(python)
