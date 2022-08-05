def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges