# D41 | 6주차 DFS · BFS
# 접근: 현재 글자에서 최종 글자로 가는 경로들을 BFS를 통해 최단 경로를 계산한다.
# 시간복잡도: O(n^2 * L)
# 막힌 지점: (없으면 "없음") 없음
#
# ------------------------------------------------------------
# 문제: 단어 변환
#
# 시작 단어 begin을 목표 단어 target으로 바꾸려고 한다.
# 한 번에 알파벳 한 글자만 바꿀 수 있다.
# 바꾼 직후의 단어는 words 안에 있어야 한다.
# words에 없는 단어는 중간에 쓸 수 없다.
#
# begin에서 target이 될 때까지 필요한 최소 변경 횟수를 반환하라.
# 규칙을 지켜 target에 도착할 수 없으면 0을 반환하라.
# begin 자체는 횟수에 포함하지 않는다. 글자를 바꿀 때마다 1이다.
#
# 두 단어는 길이가 같다.
# 같은 위치끼리 비교했을 때 다른 글자가 정확히 하나인 단어로만 한 번에 바꿀 수 있다.
#
# 제한
# - begin, target, words의 각 단어는 알파벳 소문자만 포함한다
# - 단어 길이: 3 이상 10 이하. 문제에 등장하는 단어의 길이는 모두 같다
# - words 길이: 3 이상 50 이하. 서로 같은 단어는 없다
# - begin과 target은 서로 다르다
# - begin은 words에 들어 있을 수도 있고, 없을 수도 있다
#
# 입출력 예
#   ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])  -> 4
#       (hit-hot-dot-dog-cog. 한 글자씩 4번)
#   ("hit", "cog", ["hot", "dot", "dog", "lot", "log"])  -> 0
#       (cog가 words에 없어 도착할 수 없다)
#   ("hit", "hot", ["hot", "dot", "dog"])  -> 1
#       (hit와 hot은 두 번째 글자만 다르다)
#   ("hit", "cog", ["hot", "dot", "lot", "cog"])  -> 0
#       (cog는 words에 있지만, 한 글자만 다른 단어가 이어지지 않는다)
#   ("aaa", "abc", ["aab", "abb", "abc", "aac", "acc"])  -> 2
#       (aaa-aac-abc가 2번. aaa-aab-abb-abc는 3번)
#   ("log", "cog", ["dog", "lot", "cog"])  -> 1
#       (log와 cog는 첫 글자만 다르다)
#   ("hit", "cog", ["hit", "hot", "dot", "dog", "lot", "log", "cog"])  -> 4
#       (begin이 words에 있어도 시작 횟수는 0. 최단은 그대로 4번)
#   ("aaaaaaaaaa", "aaaaaaaabc", ["aaaaaaaaab", "aaaaaaaabb", "aaaaaaaabc"])  -> 3
#       (끝에서부터 한 글자씩만 바뀌어 3번)
# ------------------------------------------------------------

from collections import deque

def solution(begin: str, target: str, words: list[str]) -> int:
    '''
    한 글자만 바뀌었는지, 그 글자가 바꿀 수 있는 단어인지 확인해야 함.
    target은 words 안에 있어야 함.

    1. 현재 단어와 words의 글자를 하나씩 비교하며 한 글자만 바뀐게 있는지 확인한다. 이러면 words에 있는 단어만 사용 가능하다.
    2. 가능한 words를 사용하여 1번을 반복한다.
    
    최소 횟수를 구해야하므로 bfs가 적절할 것 같다.
    '''
    # 규칙을 지킬 수 없음
    if target not in words:
        return 0

    def compareWithOne(before, after):
        count = 0

        for i in range(len(before)):
            if before[i] != after[i]:
                count += 1
                if count > 1:
                    return False
        return count == 1
    
    queue = deque()
    queue.append((begin, 0))
    visited = set()

    while queue:
        cur, depth = queue.popleft()
        if cur == target:
            return depth

        for word in words:
            if word not in visited and compareWithOne(cur, word):
                queue.append((word, depth + 1))
                visited.add(word)
    
    return 0



if __name__ == "__main__":
    tests = [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
        (("hit", "hot", ["hot", "dot", "dog"]), 1),
        (("hit", "cog", ["hot", "dot", "lot", "cog"]), 0),
        (("aaa", "abc", ["aab", "abb", "abc", "aac", "acc"]), 2),
        (("log", "cog", ["dog", "lot", "cog"]), 1),
        (("hit", "cog", ["hit", "hot", "dot", "dog", "lot", "log", "cog"]), 4),
        (("aaaaaaaaaa", "aaaaaaaabc", ["aaaaaaaaab", "aaaaaaaabb", "aaaaaaaabc"]), 3),
    ]

    for args, expected in tests:
        got = solution(*args) if isinstance(args, tuple) else solution(args)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] solution({args!r}) = {got!r} (expected {expected!r})")
