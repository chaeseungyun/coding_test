# D20 | 3주차 스택 · 큐
# 접근: 스택에 아직 안떨어진 시점의 인덱스를 쌓는다. 한 칸씩 이동하다가 현재 값이 스택에서 꺼낸 인덱스의 값보다 작아지면 계산하고 이를 반복한다.
# 시간복잡도: O(n)
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 주식가격
#
# 초 단위로 기록된 주식 가격 배열 prices가 주어진다.
# prices[i]는 i초 시점의 가격이다. (i는 0부터 시작한다)
#
# 각 시점 i에 대해, 그 가격이 떨어지지 않은 기간이 몇 초인지 구해 배열로 반환하라.
#
# "떨어지지 않은 기간"은 다음을 따른다.
# - i초 이후 처음으로 prices[i]보다 작은 가격이 나오는 시점까지의 초 수다.
# - 끝까지 더 작은 가격이 없으면, 마지막 시점까지의 초 수다.
# - 가격이 같거나 오르는 것은 떨어진 것이 아니다.
# - 마지막 시점의 기간은 항상 0이다.
#
# 제한
# - prices 길이: 2 이상 100,000 이하
# - prices의 각 가격: 1 이상 10,000 이하인 자연수
#
# 입출력 예
#   [1, 2, 3, 2, 3]  -> [4, 3, 1, 1, 0]
#       (1은 끝까지 안 떨어짐 4초, 2도 끝까지 3초,
#        3은 바로 다음이 2라서 1초, 그다음 2는 끝까지 1초, 마지막은 0)
#   [1, 2, 3, 4]     -> [3, 2, 1, 0]
#       (계속 오르기만 해서 각자 끝까지의 초 수)
#   [4, 3, 2, 1]     -> [1, 1, 1, 0]
#       (바로 다음이 더 작아서 각각 1초)
# ------------------------------------------------------------

'''
def solution(prices: list[int]) -> list[int]:
    res = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i, len(prices) - 1): # 자기 자신에서 다음 칸까지 1초 걸림.
            if prices[j] >= prices[i]:
                res[i] += 1
            else:
                break
    return res
'''

def solution(prices: list[int]) -> list[int]:
    stack = []
    res = [0] * len(prices)

    for i in range(len(prices)):
        while stack:
            idx = stack[-1] # 마지막 인덱스
            if prices[idx] > prices[i]: # 현재값이 더 작으면
                res[idx] = i - idx
                stack.pop()
            else:
                break
        
        stack.append(i)
    
    if stack:
        for idx in stack:
            res[idx] = len(prices) - idx - 1
    
    return res



if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 2, 3], [4, 3, 1, 1, 0]),
        ([1, 2, 3, 4], [3, 2, 1, 0]),
        ([4, 3, 2, 1], [1, 1, 1, 0]),
        ([2, 2, 2, 2], [3, 2, 1, 0]),  # 같으면 떨어지지 않음
        ([1, 2], [1, 0]),
        ([3, 1], [1, 0]),
        ([5, 5, 4], [2, 1, 0]),  # 같은 가격 유지 후 하락
        ([1, 3, 2, 4], [3, 1, 1, 0]),
        ([5, 1, 5], [1, 1, 0]),  # 바로 떨어지고 다시 오름
        ([10, 10], [1, 0]),
    ]

    for args, expected in tests:
        got = solution(*args) if isinstance(args, tuple) else solution(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
