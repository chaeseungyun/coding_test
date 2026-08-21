# D02 | 1주차 구현 · 문자열
# 접근: 홀수, 짝수를 구분하고 가운데 인덱스를 구해서 슬라이싱
# 시간복잡도: O(1)
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 가운데 글자 가져오기
#
# 문자열 s가 주어진다. s의 가운데 글자를 반환하라.
# 길이가 홀수이면 가운데 한 글자만 반환한다.
# 길이가 짝수이면 가운데 두 글자를 반환한다.
#
# 제한
# - s의 길이: 1 이상 100 이하
# - s는 알파벳만 포함한다
#
# 입출력 예
#   "abcde"  -> "c"     (길이 5, 가운데 한 글자)
#   "qwer"   -> "we"    (길이 4, 가운데 두 글자)
# ------------------------------------------------------------

def solution(s: str) -> str:
    length = len(s)

    if length % 2 == 0:
        mid = length // 2
        return s[mid - 1:mid + 1]
    
    return s[length // 2]


if __name__ == "__main__":
    tests = [
        ("abcde", "c"),
        ("qwer", "we"),
        ("a", "a"),           # 길이 1
        ("ab", "ab"),         # 길이 2
        ("xyz", "y"),         # 홀수, 가운데 한 글자
        ("abcd", "bc"),       # 짝수, 가운데 두 글자
    ]

    for s, expected in tests:
        got = solution(s)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({s!r}) = {got!r} (expected {expected!r})")
