def solution(array, commands):
    ist = []
    for i in range(len(commands)):
        num1 = commands[i][0] - 1
        num2 = commands[i][1]
        num3 = commands[i][2] - 1
        new_list = sorted(array[num1:num2])
        ist.append(new_list[num3])
    return ist
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges