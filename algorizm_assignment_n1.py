# 이번 과제는 주어진 식을 계산하여 결과를 출력하는 프로그램입니다.
# 조건 1: 식은 한 자리 숫자, +, *로만 구성되어 있습니다.
# Ex) 4+3*2+2
#    주의: 빼기나 나누기를 포함하는 경우, 한 자리 이상의 수에 대한 처리, 공백문자에 대한 처리 등이 포함되는 경우 copy로 간주하고, 변명의 여지가 없습니다.
# 조건 2: 반드시 recursion을 사용하는 divide and conquer로 구현합니다. 이외의 방식은 역시 copy로 간주됩니다.
# 조건 3: 식을 문자열 (언어에 따라 다르지만, c++: std::string, java: String 등)로 받고,
# 추가로 계산의 대상이 되는 첫번째 글자의 index, 마지막 글자의 index+1을 입력으로 받아 계산결과(integer)를 return하는 함수의 형태로 구현합니다.
# Ex) c++: int calc(const std::string& str, int s, int e
# Java: int calc(String str, int s, int e)
# 조건 4: 계산 결과는 통상적인 덧셈과 곱셈의 순서에 맞에 계산되어야 합니다.
# Ex) 4+3*2+2 의 결과는 12
# 주의: 제출은 직접 작성한 source code만 합니다. (cpp, hpp, h, java, py, kt, cs, 등)
# 주의: jupyter notebook file은 source code가 아니므로 제출 대상이 아닙니다.
# Hint:
# 입력된 범위의 크기가 1이면 문자 - '0' 과 같은 방식으로 문자를 숫자로 변환하여 return하고,
# 그보다 크면 범위 내에서 +를 찾고 +를 기준으로 좌우의 계산 결과(recursive call)을 더하여 return하고,
# +가 없으면 범위 내에서 *를 찾고 *를 기준으로 좌우의 계산 결과(recursive call)을 곱하여 return 하면 됩니다.
# 매우 주의: 단순한 compile error, 입출력 관련 문제 외 알고리즘을 구현하는 부분에서는 참고자료(web page, 기계학습기술을 이용한 장치 등)는 열람하지 마십시오.
#     이와 같은 행위나 (어떤 경우든) 다른 사람(인공지능 포함)이 작성한 코드를 활용하는 경우는 부정행위에 속합니다.
#     거의 모든 경우에 판별할 수 있으며 확인된 경우 이유 여하를 막론하고 F학점이 부여될 예정입니다.


def calc(lst, left, right):
    lf_result = lst[left]
    rt_result = lst[right - 1]
    op = left + 1
    if right - left > 3:
        op = left + 1
        for j in range(left + 1, right - 1, 2):
            if lst[j] == "+":
                op = j
                break
        lf_result = calc(lst, left, op)
        rt_result = calc(lst, op + 1, right)
    if right - left == 1:
        return lst[left]
    if lst[op] == "+":
        return lf_result + rt_result
    else:
        return lf_result * rt_result


arr = list(input())
n = len(arr)
for i in range(n):
    if i % 2 == 0:
        arr[i] = int(arr[i])

print(calc(arr, 0, n))
