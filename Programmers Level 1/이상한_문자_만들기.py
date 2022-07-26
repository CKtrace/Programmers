def solution(s):
    rk = ''
    list = s.split(" ")
    for i in list:
        for j in range(len(i)):
            if j % 2 == 0:
                rk += i[j].upper()
            else:
                rk += i[j].lower()
        rk += " "
    return rk[0:-1]
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges