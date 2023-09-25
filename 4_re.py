# 주민등록번호
# 901111-1111111

# e-mail address
# dydiddl@naver.com

# 차량번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1

# 일정한 형태가 정해져 있는 것

import re
# abcd, book, desk 이런형태로 4글자
# ca?e 만 기억이 남
# care, cafe, case, cave
# 검사 방법 1 : caae, cabe, cace, ...
p = re.compile("ca.e") 
# . (ca.e): 하나의 문자 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작을 의미 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)

# print(m.group()) # 매치되지 않으면 에러가 발생

#     # m = p.match("caffe")
#     print(m.group()) # 매치되지 않으면 에러가 발생

def print_match(m):
    if m :
        print('m.group():', m.group()) # 일치하는 문자열 반환
        print('m.string:', m.string) # 입력받은 문자열 반환
        print('m.start():', m.start()) # 일치하는 문자열의 시작 index
        print('m.end():', m.end()) # 일치하는 문자열의 끝 index
        print('m.span()', m.span()) # 일치하는 문자열의 시작 / 끝 index
        
    else :
        print('매칭되지 않음')

# m = p.match('careless') # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search('good care') # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall('good care cafe') # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile('원하는 형태')
# 2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 "리스트" 형태로 반환
# w3school 사이트에서 공부 할 수 있음 , python re