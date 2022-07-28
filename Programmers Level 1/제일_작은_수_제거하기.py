def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        l = min(arr)
        arr.remove(l)
        return arr
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges