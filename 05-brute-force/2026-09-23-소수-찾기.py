# D35 | 5주차 완전탐색 · 백트래킹
# 접근: 완전 탐색으로 만들 수 있는 숫자들을 하나씩 만들면서 소수를 판별한다. 완전 탐색으로 백트래킹을 활용한다.
# 시간복잡도: 생성 O(n·n!) + 판별 O(|S|·√M)
# 막힌 지점: (없으면 "없음")
# 50분 소요
# ------------------------------------------------------------
# 문제: 소수 찾기
#
# 한 자리 숫자가 적힌 종이 조각이 흩어져 있다.
# 조각에 적힌 숫자를 이어 붙이면 여러 자리 수를 만들 수 있다.
# 조각은 문자열 numbers로 주어진다. numbers[i]가 조각 하나의 숫자다.
#
# 조각의 일부 또는 전부를 골라, 순서를 바꿔 수를 만든다.
# 각 조각은 한 수 안에서 최대 한 번만 쓴다.
# 고르지 않은 조각은 버려도 된다.
# 앞자리가 0인 수는 그 0을 뺀 값과 같은 수로 본다.
# 같은 값이 여러 방식으로 나와도 한 번만 센다.
#
# 이렇게 만들 수 있는 수 가운데 소수가 몇 개인지 반환하라.
# 1과 0은 소수가 아니다. 한 자리 소수(2, 3, 5, 7)는 센다.
#
# 제한
# - numbers의 길이: 1 이상 7 이하
# - numbers는 '0'~'9'만 포함한다
# - 같은 숫자가 여러 조각에 있을 수 있다
#
# 입출력 예
#   "17"   -> 3    (7, 17, 71. 1은 소수가 아님)
#   "011"  -> 2    (11, 101. 011은 11과 같고, 1·0·10은 소수가 아님)
#   "2"    -> 1    (2 하나)
#   "1"    -> 0    (1은 소수가 아님)
#   "0"    -> 0
#   "11"   -> 1    (만들 수 있는 값은 1, 11. 소수인 것은 11뿐)
# ------------------------------------------------------------

def solution(numbers: str) -> int:
    count = 0
    counted = set()
    used = [0] * len(numbers)

    def isPrimeNumber(s: str): # 소수 계산
        if not s:
            return False

        target = int(s)

        if target <= 1:
            return False

        if target % 2 == 0:
            return target == 2 
        
        i = 3
        while i * i <= target:
            if target % i == 0:
                return False
            i += 2

        return True
    
    def dfs(cur: str):
        nonlocal count
        if cur:
            counted.add(int(cur))
        for i in range(len(numbers)):
            nextWord = cur + numbers[i]
            if not used[i]:
                used[i] = 1
                dfs(nextWord)
                used[i] = 0
    
    dfs("")

    for num in counted:
        if isPrimeNumber(num):
            count += 1

    return count

if __name__ == "__main__":
    tests = [
        ("17", 3),
        ("011", 2),
        ("2", 1),
        ("1", 0),
        ("0", 0),
        ("11", 1),
        ("23", 3),     # 2, 3, 23 (32는 소수 아님)
        ("000", 0),    # 0만 만들 수 있음
    ]

    for args, expected in tests:
        got = solution(*args) if isinstance(args, tuple) else solution(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
