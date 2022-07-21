def solution(numbers):
    answer = 0
    for i in range(10) :
        if i not in numbers :
            answer += i
    return answer

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges