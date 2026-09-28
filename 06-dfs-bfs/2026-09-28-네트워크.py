# D40 | 6주차 DFS · BFS
# 접근: 네트워크 한 그룹을 dfs로 찾아낸 후 그룹 수를 계산한다.
# 시간복잡도: O(n^2)
# 막힌 지점: (없으면 "없음") 
# 1. 재귀 방식의 dfs 적용 시 recursion depth 에러가 떠서 bfs로 변경
# 2. 미로 탐색과 같이 접근 했었는데 양방향 그래프라는 사실을 간과했다.
# (0, 2)는 0번 컴퓨터와 2번 컴퓨터가 연결되어 있다는거지 격자에서 연결된 지점이 아니다.
# 그래서 인접 그래프를 이용한 그래프 탐색으로 변경하고 탐색은 dfs로 코드를 간결하게 작성할 수 있어서 dfs로 진행했다.
# 3. graph를 그릴 때 (i, j) 쌍을 넣어야 하는데 computers[i][j]를 graph[i]에 append 해서 오답이 났었다.
# 소요 시간: 35분
# ------------------------------------------------------------
# 문제: 네트워크
#
# 컴퓨터 n대가 있고, 번호는 0부터 n - 1까지다.
# 두 컴퓨터가 직접 연결되어 있거나 다른 컴퓨터를 거쳐 연결되어 있으면
# 같은 네트워크에 속한다. 다른 컴퓨터와 연결되지 않은 컴퓨터도
# 혼자 하나의 네트워크를 이룬다.
# 전체 네트워크의 개수를 반환하라.
#
# computers는 n행 n열의 정수 리스트다.
# computers[i][j]가 1이면 i번과 j번 컴퓨터가 직접 연결되어 있고,
# 0이면 직접 연결되어 있지 않다. 연결은 양방향이다.
# computers[i][i]는 항상 1이다.
#
# 제한
# - 1 <= n <= 200
# - computers의 행과 열 크기는 모두 n
# - 모든 원소는 0 또는 1
# - computers[i][j] == computers[j][i]
#
# 입출력 예
#   n=3, computers=[[1,1,0], [1,1,0], [0,0,1]] -> 2
#       (0번과 1번이 한 네트워크, 2번이 별도 네트워크)
#   n=3, computers=[[1,1,0], [1,1,1], [0,1,1]] -> 1
#       (0번과 2번도 1번을 거쳐 연결되므로 모두 같은 네트워크)
#   n=1, computers=[[1]] -> 1
#       (컴퓨터 한 대만 있어도 하나의 네트워크)
# ------------------------------------------------------------

from collections import defaultdict

def solution(n: int, computers: list[list[int]]) -> int:
    visited = [0 for _ in range(n)]
    graph = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)

    def dfs(k):
        visited[k] = 1
        for v in graph[k]:
            if not visited[v]:
                dfs(v)
    
    count = 0
    
    for k in range(n):
        if not visited[k]:
            dfs(k)
            count += 1
    
    return count


if __name__ == "__main__":
    tests = [
        ((3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2),
        ((3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1),
        ((1, [[1]]), 1),
        ((4, [[1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1]]), 2),
        ((5, [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0],
              [1, 1, 1, 0, 0], [0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1]]), 3),
        ((200, [[int(i == j) for j in range(200)] for i in range(200)]), 200),
        ((200, [[1] * 200 for _ in range(200)]), 1),
    ]

    names = [
        "기본 예제 · 네트워크 2개",
        "간접 연결 · 네트워크 1개",
        "컴퓨터 1대",
        "번호가 떨어진 컴퓨터끼리 연결",
        "연결된 그룹과 독립 컴퓨터",
        "200대 · 모두 독립",
        "200대 · 모두 연결",
    ]
    passed = 0
    failed = []
    print("네트워크 채점")
    print("-" * 60)

    for i, (args, expected) in enumerate(tests, start=1):
        label = f"{i:02d}. {names[i - 1]} (n={args[0]})"
        try:
            got = solution(*args)
        except Exception as error:
            failed.append(i)
            print(f"[ERROR] {label}")
            print(f"        {type(error).__name__}: {error}")
            continue

        if got == expected:
            passed += 1
            print(f"[PASS]  {label}")
        else:
            failed.append(i)
            print(f"[FAIL]  {label}")
            print(f"        기대값: {expected!r} | 실제값: {got!r}")

    print("-" * 60)
    print(f"결과: {len(tests)}개 중 {passed}개 통과 / {len(failed)}개 실패")
    if failed:
        print("실패 케이스: " + ", ".join(f"{i:02d}" for i in failed))
