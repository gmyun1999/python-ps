
"""
두번째 과제는 주어진 집합의 원소들의 중복 합으로 주어진 숫자를 만드는 방법을 찾는 문제입니다.
입력은 집합의 원소의 개수, 집합의 각 원소, 최종적으로 만들고 싶은 숫자 입니다.
EX) {4,7,10,5} 로 12를 만드는 경우 입력은 4 4 7 10 5 12 입니다.
이 경우 출력은 7 5 또는 4 4 4가 되어야 합니다. 만들 수 없는 경우에는 "Impossible" 을 출력합니다.
주의: 시험 문제에서와는 다르게 각 원소들을 여러번 사용할 수 있습니다. 따라서 implicit order를 다시 설계해야 합니다.
Optional: 위와 같은 출력 형태 대신에 7(1) 5(1) 또는 4(3)의 형태로 출력하기 위해 결과를 후 가공하는 과정을 연습해 보시는 것도 좋습니다.
제출은 소스코드만 하시면 됩니다.
입력 부분을 포함하는 완전한 소스코드를 제출하십시오.
"""

"""
--------------------------------------------------------------------
단 이코드는 주어진 원소들과 최종적으로 만들숫자가 양의정수라는 가정하에 만들어졌음
--------------------------------------------------------------------
"""


# dp_lst 를 [0,0]으로 초기화
# dp_lst[i][1]에서 1은 사용된 element
# dp_lst[i][0] +dp_lst[i][1] = target
def make_combination(elements, target):
    dp_lst = [[0 for _ in range(2)] for _ in
              range(target + 1)]

    # elements 를 더했을 때 나올수 있는 값을 1부터 target 까지 조사
    for sums_of_elements in range(1, target + 1):
        for element in elements:
            if sums_of_elements < element:
                dp_lst[sums_of_elements] = [-1, -1]
            elif dp_lst[sums_of_elements - element][1] > -1:  # element 를 뺀값이 존재 하는 경우
                dp_lst[sums_of_elements] = [sums_of_elements - element, element]
                break
            else:
                dp_lst[sums_of_elements] = [-1, -1]

    result = []
    sum_of_elements = target

    # target 부터 sums_of_elements 가 0까지 역추적
    while sum_of_elements > 0:
        if dp_lst[sum_of_elements][1] == -1:
            break

        result.append(dp_lst[sum_of_elements][1])
        sum_of_elements = dp_lst[sum_of_elements][0]

    return result


def main():
    input_lst = list(map(int, input().split()))
    num_elements = input_lst[0]
    elements = input_lst[1:num_elements + 1]
    target = input_lst[num_elements + 1]

    combination = make_combination(elements, target)

    if combination:
        print(" ".join(map(str, combination)))
    else:
        print("impossible")


if __name__ == "__main__":
    main()
