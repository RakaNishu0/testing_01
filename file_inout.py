# file open and write(overwrite)
# score_file = open("score.txt", "w", encoding="utf8")
# print("math : 0", file=score_file)
# print("engl : 10", file=score_file)
# score_file.close()                  # 파일을 오픈한 후에는 반드시 닫아줄 것
#
# # write by append
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("science : 100")
# score_file.write("\ncode : 100")
# score_file.close()
#
# # read file all
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()
#
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())    # line 별로 읽고 커서는 다음 줄로 이동
# score_file.close()

# read and contain in list
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()      # readline = 1 line / readlines = every lines
# for line in lines:
#     print(line, end="")
# score_file.close()


# write with dictionary...??
score_file = open("score.txt", "a", encoding="utf8")
profile = {"name":"part", "age":40, "hobby":["drunk", "golf", "youtube"]}
score_file.write(profile)
score_file.close()
# TypeError: write() argument must be str, not dict
