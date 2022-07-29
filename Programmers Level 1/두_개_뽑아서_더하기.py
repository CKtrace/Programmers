def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for u in range(i+1, len(numbers)):
            if numbers[i] + numbers[u] not in answer:
                answer.append(numbers[i]+numbers[u])
    answer.sort()
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
