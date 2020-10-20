# Pickle
import pickle

# profile_file = open("profile.pickle", "wb")     # wb = binary 로 쓰기
# profile = {"name":"part", "age":40, "hobby":["drunk", "golf", "youtube"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

# 보통 file 쓰기를 하면 리스트/딕셔너리/튜플 등의 자료형을 쓸 수가 없다. (문자/숫자만 가능)
# pickle 의 경우에는 이를 가능하게 해준다는 것. 단 바이너리로 쓰기 때문에 pickle로 읽어야 한다.
