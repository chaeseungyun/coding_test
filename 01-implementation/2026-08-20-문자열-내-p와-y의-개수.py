# D01 | 1주차 구현 · 문자열
# 접근: 순차적으로 순회하며 지정한 문자의 개수를 찾음
# 시간복잡도: O(2n) == O(n)
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 문자열 내 p와 y의 개수
#
# 대문자와 소문자가 섞인 문자열 s가 주어진다.
# s 안의 'p' 개수와 'y' 개수가 같으면 True, 다르면 False를 반환하라.
# 'p'와 'y'가 둘 다 하나도 없으면 True.
# 개수를 셀 때 대소문자는 구분하지 않는다. (P == p, Y == y)
#
# 제한
# - s의 길이: 1 이상 50 이하
# - s는 알파벳만 포함한다
#
# 입출력 예
#   "pPoooyY"  -> True    (p 2개, y 2개)
#   "Pyy"      -> False   (p 1개, y 2개)
# ------------------------------------------------------------

def solution(s: str) -> bool:
    s = s.lower()
    
    pCount = s.count('p')
    yCount = s.count('y')

    return pCount == yCount

if __name__ == "__main__":
    tests = [
        ("pPoooyY", True),
        ("Pyy", False),
        ("abc", True),       # p, y 둘 다 없음
        ("P", False),
        ("yY", False),       # p 0개, y 2개
        ("PpYy", True),
    ]

    for s, expected in tests:
        got = solution(s)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({s!r}) = {got!r} (expected {expected!r})")
