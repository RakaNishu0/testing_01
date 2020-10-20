import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# open() & close() 의 과정이 필요 없다.

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("Learning Python...")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# with 를 사용하면 훨씬 간단하고 편리하게 파일 입출력을 처리할 수 있다.



# 퀴즈
# 매주 1회 보고서를 작성한다. 보고서 폼은 다음과 같다.
#
# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
#
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# i = 1
# while i < 51:
# while i < 5:
for i in range(1, 5):
    with open(f"{i}w_rpt.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"- {i} 주차 주간보고 -")
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무요약 :")
        # i += 1
