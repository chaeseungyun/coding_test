# D02 보너스 | 1주차 구현 · 문자열
# 접근: 투포인터로 문자열을 찾아서 알맞은 숫자를 추가한다.
# 시간복잡도: O(n^2)
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 숫자 문자열과 영단어
#
# 숫자의 일부 자릿수가 영단어로 바뀐 문자열 s가 주어진다.
# s를 원래 숫자로 바꿔 정수로 반환하라.
#
# 영단어와 숫자의 대응은 다음과 같다.
#   zero  0
#   one   1
#   two   2
#   three 3
#   four  4
#   five  5
#   six   6
#   seven 7
#   eight 8
#   nine  9
#
# s에는 숫자(0-9)와 위 영단어가 섞여 있을 수 있다.
# 항상 올바른 숫자로 바꿀 수 있고, 맨 앞이 0인 경우는 없다.
# (숫자 0 자체는 가능하다.)
#
# 제한
# - s의 길이: 1 이상 50 이하
# - s는 숫자 또는 위 영단어만 포함한다
#
# 입출력 예
#   "one4seveneight"   -> 1478     (one, 4, seven, eight)
#   "23four5six7"      -> 234567   (2, 3, four, 5, six, 7)
#   "2three45sixseven" -> 234567   (2, three, 4, 5, six, seven)
#   "123"              -> 123      (영단어 없이 숫자만)
# ------------------------------------------------------------

def solution(s: str) -> int:
    res = ''
    n = len(s)
    num_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    start, end = 0, 1

    while start <= end and start < n and end <= n:
        flag = False
        cur_word = s[start:end]

        if cur_word in [str(i) for i in range(10)]: # 숫자면
            res += cur_word
            start += 1
            end += 1
            continue
        
        for word, v in num_map.items():
            if cur_word == word: # 완성된 글자면
                res += num_map[word]
                start = end - 1
                flag = True
                break
            elif cur_word in word: # 부분 글자면
                end += 1
                flag = True
                break

        if not flag: # 글자를 못찾으면
            start += 1

    return int(res)


if __name__ == "__main__":
    tests = [
        ("one4seveneight", 1478),
        ("23four5six7", 234567),
        ("2three45sixseven", 234567),
        ("123", 123),
        ("one", 1),                 # 영단어만 한 개
        ("zero", 0),                # 숫자 0
        ("nine9nine", 999),
        ("eightwo", 82),            # eight + two (eigh two 아님)
    ]

    for s, expected in tests:
        got = solution(s)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({s!r}) = {got!r} (expected {expected!r})")
