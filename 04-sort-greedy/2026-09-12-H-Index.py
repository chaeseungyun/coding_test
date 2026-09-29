# D24 | 4주차 정렬 · 그리디
# 접근: 0 ~ 가장 많이 인용된 횟수를 탐색하며 h의 최댓값을 찾는다. 오름차순으로 정렬하고 h가 들어갈 자리를 찾는다.
# 시간복잡도: O(n * m)
# 막힌 지점: (없으면 "없음") 문제를 이해하는데 오래 걸렸다. 논문이 h번 이상 인용되어야 하며 그 개수를 구할 때 h-index라는 이름때문에 내가 정의한 h를 인덱스로 착각하는 등 오류가 있었음.
# 소요 시간: 25분
# ------------------------------------------------------------
# 문제: H-Index
#
# 어떤 과학자가 발표한 논문별 인용 횟수 배열 citations가 주어진다.
# citations[i]는 i번째 논문이 인용된 횟수이다.
#
# 이 과학자의 H-Index를 구하라.
#
# H-Index는 다음을 만족하는 h의 최댓값이다.
# - 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이다.
# - 나머지 논문은 h번 이하로 인용되었다.
#
# 제한
# - citations의 길이(논문 수 n): 1 이상 1,000 이하
# - citations의 각 값: 0 이상 10,000 이하인 정수
#
# 입출력 예
#   [3, 0, 6, 1, 5]  -> 3
#       (5편 중 3편 이상 인용된 논문이 3편(3, 6, 5)이고
#        나머지 2편(0, 1)은 3번 이하)
#   [1, 3, 5, 7, 9]  -> 3
#       (3번 이상 인용된 논문이 4편이라 h=3은 되고,
#        4번 이상 인용된 논문은 3편뿐이라 h=4는 안 된다)
#   [0, 0, 0]        -> 0
#       (한 번도 인용되지 않아 h=0)
# ------------------------------------------------------------


def solution(citations: list[int]) -> int:
    high = max(citations)
    citations.sort()
    result = 0

    for idx, item in enumerate(citations): # item: 논문의 인용 횟수
        for h in range(high + 1): # h: h-index
            if h <= item and len(citations) - idx >= h: # h번 이상 인용된 item 찾기. 리스트 길이 - 그 논문의 인덱스로 h보다 많거나 같게 인용됐는지 확인
                result = max(h, result) # 가장 큰 h-index

    return result

if __name__ == "__main__":
    tests = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 5, 7, 9], 3),
        ([0, 0, 0], 0),
        ([0], 0),
        ([1], 1),
        ([10], 1),           # 논문 수보다 큰 h는 불가
        ([10, 10, 10], 3),
        ([2, 2], 2),
        ([1, 1, 1], 1),
        ([0, 1], 1),
        ([0, 1, 2], 1),
        ([1, 2, 3, 4, 5], 3),
        ([5, 5, 5, 5], 4),
        ([4, 4, 4], 3),
        ([0, 0, 1, 1], 1),
    ]

    for args, expected in tests:
        got = solution(*args) if isinstance(args, tuple) else solution(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
