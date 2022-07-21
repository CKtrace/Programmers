from collections import Counter

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges