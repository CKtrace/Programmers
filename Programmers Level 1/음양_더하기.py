def solution(absolutes, signs):
    x = 0
    for i in signs:
        if i == False:
            a = absolutes[x]
            absolutes[x] = -(a)
        x +=1
    return sum(absolutes)

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges