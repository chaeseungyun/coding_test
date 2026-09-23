# D34 | 5주차 완전탐색 · 백트래킹
# 접근:
# 시간복잡도:
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 모음사전
#
# 사전에 알파벳 모음 A, E, I, O, U만을 사용해 만들 수 있는
# 길이 1 이상 5 이하의 모든 단어가 수록되어 있다.
#
# 단어는 사전 순(알파벳 순)으로 정렬되어 있다.
# 같은 접두어면 더 짧은 단어가 앞에 온다.
# 첫 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA",
# "AAAAE", ... 이며 마지막 단어는 "UUUUU"다.
#
# 앞부분만 나열하면 아래와 같다.
#
#   1. A
#   2. AA
#   3. AAA
#   4. AAAA
#   5. AAAAA
#   6. AAAAE
#   7. AAAAI
#   8. AAAAO
#   9. AAAAU
#  10. AAAE
#     ...
#
# 단어 word가 주어질 때, 사전에서 몇 번째인지 반환하라.
# 번호는 1부터 센다.
#
# 제한
# - word의 길이: 1 이상 5 이하
# - word는 'A', 'E', 'I', 'O', 'U'만 포함한다
#
# 입출력 예
#   "AAAAE"  -> 6      (AAAAA 다음이 AAAAE)
#   "AAAE"   -> 10     (AAAA + 모음 5개를 지난 다음이 AAAE)
#   "I"      -> 1563   (A, E로 시작하는 단어를 모두 지난 뒤 첫 단어)
#   "EIO"    -> 1189
# ------------------------------------------------------------

def solution(word: str) -> int:
    words = ['A', 'E', 'I', 'O', 'U']
    count = 0
    sentence = []
    found = False

    def dfs(target):
        nonlocal count
        nonlocal found

        if "".join(sentence) == target:
            found = True
            return

        for word in words:
            if len(sentence) < 5:
                count += 1
                sentence.append(word)
                dfs(target)
                sentence.pop()
                if found:
                    return
    
    dfs(word)
    return count


if __name__ == "__main__":
    tests = [
        ("AAAAE", 6),
        ("AAAE", 10),
        ("I", 1563),
        ("EIO", 1189),
        ("A", 1),
        ("AA", 2),
        ("AAAAA", 5),
        ("E", 782),
        ("U", 3125),
        ("UUUUU", 3905),
    ]

    for args, expected in tests:
        got = solution(*args) if isinstance(args, tuple) else solution(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
