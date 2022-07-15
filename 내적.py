import numpy as np

def solution(a, b):
    a = np.array(a)
    b = np.array(b)
    answer = int(np.dot(a,b))
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges