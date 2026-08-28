# D09 | 2주차 해시
# 접근: "같은 이름이 참가 명단에 더 많이 있으면" 그 이름 중 한 명이 완주하지 못한 것이다. dict 로 빈도수 계산하고 키가 없거나 값이 크면 반환
# 시간복잡도: O(n)
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 완주하지 못한 선수
#
# 마라톤에 참가한 선수 명단 participant와, 완주한 선수 명단 completion이 주어진다.
# 참가자는 단 한 명만 완주하지 못했다. 그 선수의 이름을 반환하라.
#
# 동명이인이 있을 수 있다. 같은 이름이 여러 명이면 각각 다른 사람이다.
# 따라서 "같은 이름이 참가 명단에 더 많이 있으면" 그 이름 중 한 명이 완주하지 못한 것이다.
#
# 제한
# - participant 길이: 1 이상 100,000 이하
# - completion 길이: participant 길이 - 1
# - 이름은 알파벳 소문자만, 길이 1 이상 20 이하
# - 완주하지 못한 선수는 항상 한 명이다
#
# 입출력 예
#   ["leo", "kiki", "eden"], ["eden", "kiki"]
#       -> "leo"       (leo만 완주 명단에 없음)
#   ["marina", "josipa", "nikola", "vinko", "filipa"],
#   ["josipa", "filipa", "marina", "nikola"]
#       -> "vinko"     (vinko만 빠짐)
#   ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
#       -> "mislav"    (mislav가 두 명 참가, 한 명만 완주)
# ------------------------------------------------------------

def solution(participant: list[str], completion: list[str]) -> str:
    def makeDict(arr):
        d = {}
        for item in arr:
            c = d.get(item, 0)
            d[item] = c + 1
        return d
    
    dParticipant = makeDict(participant)
    dCompletion = makeDict(completion)

    for name, freq in dParticipant.items():
        target = dCompletion.get(name, 0)
        if not target:
            return name
        
        if target < freq:
            return name
    
    return ''

if __name__ == "__main__":
    tests = [
        ((["leo", "kiki", "eden"], ["eden", "kiki"]), "leo"),
        (
            (
                ["marina", "josipa", "nikola", "vinko", "filipa"],
                ["josipa", "filipa", "marina", "nikola"],
            ),
            "vinko",
        ),
        ((["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]), "mislav"),
        ((["a"], []), "a"),  # 참가 1명, 완주 0명
        ((["ana", "ana"], ["ana"]), "ana"),  # 동명이인만 있는 경우
        ((["kim", "lee", "park"], ["lee", "park"]), "kim"),  # 맨 앞이 미완주
        ((["kim", "lee", "park"], ["kim", "lee"]), "park"),  # 맨 뒤가 미완주
        ((["a", "b", "a", "c", "a"], ["a", "c", "b", "a"]), "a"),  # 같은 이름 3명 중 1명 미완주
    ]

    for args, expected in tests:
        got = solution(*args) if isinstance(args, tuple) else solution(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
