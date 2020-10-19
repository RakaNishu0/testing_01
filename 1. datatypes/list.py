# List

subway = [10, 20, 30]       # 문자열도 가능, 혼합도 가능
print(subway)
print(subway.index(10))     # 10 이라는 데이터가 리스트 내의 몇번째에 위치하고 있는가?

subway.append(50)           # 50 을 리스트의 가장 뒤에 추가
print(subway)

subway.insert(3, 40)        # 3번째 자리에 40 을 삽입
print(subway)

print(subway.pop())         # 리스트의 가장 뒤에 있는 데이터를 출력하고, 리스트에서 빼버린다.
print(subway)               # pop()으로 빼고 남은 리스트를 확인

print(subway.count(50))         # 문자열과 동일한 방식. 해당 데이터가 몇개 있는지 출력

subway.sort()               # sort() 오름차순으로 정렬
print(subway)
subway.reverse()            # reverse() 내림차순으로 정렬
print(subway)
# subway.clear()              # clear() 리스트의 내용을 모두 삭제
# print(subway)

station = ['강매', '수색', '디엠씨']
subway.extend(station)      # extend() 리스트 확장(합치기)
print(subway)
