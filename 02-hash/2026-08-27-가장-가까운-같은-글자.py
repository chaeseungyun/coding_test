# D08 보너스 | 2주차 해시
# 접근: 글자별 등장한 마지막 인덱스를 dict에 저장, 갱신. 
# 시간복잡도: O(n)
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 가장 가까운 같은 글자
#
# 문자열 s가 주어진다. 각 위치의 글자에 대해,
# 자기보다 앞에 나온 같은 글자 중 가장 가까운 것과의 거리를 구하라.
# 앞에 같은 글자가 한 번도 없으면 -1이다.
#
# 거리는 (현재 인덱스) - (앞에 나온 같은 글자의 인덱스) 이다.
# 결과는 s와 같은 길이의 정수 리스트로 반환하라.
#
# 제한
# - s의 길이: 1 이상 10,000 이하
# - s는 영문 소문자만 포함한다
#
# 입출력 예
#   "banana" -> [-1, -1, -1, 2, 2, 2]
#     b: 앞에 없음
#     a: 앞에 없음
#     n: 앞에 없음
#     a: 앞에서 가장 가까운 a는 2칸 앞
#     n: 앞에서 가장 가까운 n은 2칸 앞
#     a: 앞에서 가장 가까운 a는 2칸 앞
#   "foobar" -> [-1, -1, 1, -1, -1, -1]
#     세 번째 o만 바로 앞 o와 1칸 차이, 나머지는 앞에 같은 글자 없음
# ------------------------------------------------------------

# O(n^2)
def solution(s: str) -> list[int]:

    res = [-1] * len(s)
    
    for i in range(len(s)):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                res[i] = i - j
                break
    
    return res

# O(n)
def solutionByHash(s: str) -> list[int]:
    res = []
    d = {}

    for i, w in enumerate(s):
        if w in d:
            res.append(i - d[w])
        else:
            res.append(-1)
        d[w] = i
    
    return res

if __name__ == "__main__":
    tests = [
        ("banana", [-1, -1, -1, 2, 2, 2]),
        ("foobar", [-1, -1, 1, -1, -1, -1]),
        ("a", [-1]),                         # 한 글자
        ("aa", [-1, 1]),                     # 같은 글자 연속
        ("abc", [-1, -1, -1]),               # 전부 다른 글자
        ("aaaa", [-1, 1, 1, 1]),             # 전부 같은 글자
        ("abba", [-1, -1, 1, 3]),            # 떨어진 같은 글자
        ("z", [-1]),                         # 한 글자 (다른 문자)
    ]

    for args, expected in tests:
        got = solutionByHash(*args) if isinstance(args, tuple) else solutionByHash(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
