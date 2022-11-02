def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]:
            answer += 1
            del burger[-4:]
    return answer

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges