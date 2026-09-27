# S01 | 1주차 SELECT · 한 테이블
# 접근:
# 시간복잡도:
# 막힌 지점: (없으면 "없음")
#
# ------------------------------------------------------------
# 문제: 연락처 없는 휴면 회원
#
# 회원 테이블 members에서 아래 조건을 모두 만족하는 회원을 조회하는
# SELECT 문을 작성하라.
#
# 1. status가 'DORMANT'이다.
# 2. phone이 NULL이다.
#    빈 문자열 ''은 NULL이 아니다. 전화번호가 있는 것으로 보고 제외한다.
# 3. joined_on이 '2024-01-01'보다 이전이다. 그날은 포함하지 않는다.
#    joined_on은 'YYYY-MM-DD' 문자열이다.
# 4. grade가 'VIP' 또는 'GOLD'이다.
#    비교는 대소문자를 구분한다. 'vip', 'gold'는 해당하지 않는다.
#
# 결과 컬럼은 아래 순서대로만 반환한다.
#   member_id, name, grade, joined_on
#
# 정렬은 joined_on 오름차순이고, 같은 날짜면 member_id 오름차순이다.
#
# members
# - member_id  정수, 기본키
# - name       문자열, NULL 아님
# - status     문자열, NULL 아님
# - phone      문자열, NULL 가능
# - grade      문자열, NULL 아님
# - joined_on  문자열 'YYYY-MM-DD', NULL 아님
#
# 제한
# - 행은 0개 이상 1,000개 이하
# - solution()은 SELECT 문 하나인 문자열을 반환한다
# - 채점 방언은 SQLite다. 이 문제에서는 표준 SELECT만으로 충분하다
#
# 입출력 예
#   members
#     (1, 이서준, DORMANT, NULL,       VIP,    2022-05-01)
#     (2, 최하늘, DORMANT, 01012345678, VIP,    2021-03-03)
#     (3, 김다은, DORMANT, NULL,       GOLD,   2023-11-02)
#     (4, 한소희, DORMANT, NULL,       GOLD,   2024-01-01)
#     (5, 정우성, DORMANT, NULL,       SILVER, 2020-08-08)
#     (6, 박민재, ACTIVE,  NULL,       VIP,    2020-01-01)
#   -> [(1, '이서준', 'VIP', '2022-05-01'),
#       (3, '김다은', 'GOLD', '2023-11-02')]
#       (최하늘은 전화번호가 있어 제외, 한소희는 가입일이 기준 당일,
#        정우성은 등급이 SILVER, 박민재는 ACTIVE.
#        남은 두 명은 가입일이 빠른 이서준이 먼저)
#
#   members
#     (10, 가가, DORMANT, NULL, VIP,  2023-01-01)
#     (8,  다다, DORMANT, NULL, VIP,  2023-01-02)
#     (7,  나나, DORMANT, NULL, GOLD, 2023-01-01)
#   -> [(7, '나나', 'GOLD', '2023-01-01'),
#       (10, '가가', 'VIP', '2023-01-01'),
#       (8, '다다', 'VIP', '2023-01-02')]
#       (같은 가입일이면 member_id가 작은 나나가 가가보다 앞)
#
#   members
#     (1, 공백전화, DORMANT, '',   VIP,  2020-01-01)
#     (2, 활동회원, ACTIVE,  NULL, GOLD, 2019-05-05)
#     (3, 당일가입, DORMANT, NULL, VIP,  2024-01-01)
#     (4, 전날가입, DORMANT, NULL, GOLD, 2023-12-31)
#   -> [(4, '전날가입', 'GOLD', '2023-12-31')]
#       (빈 문자열 전화, ACTIVE, 기준 당일 가입은 제외.
#        전날은 기준보다 이전이므로 포함)
# ------------------------------------------------------------

import sqlite3


SCHEMA = """
CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    phone TEXT,
    grade TEXT NOT NULL,
    joined_on TEXT NOT NULL
);
"""


def solution() -> str:
    ...


def run(rows):
    sql = solution()
    if not isinstance(sql, str):
        raise TypeError("solution()은 SELECT 문 문자열을 반환해야 한다")

    conn = sqlite3.connect(":memory:")
    try:
        conn.executescript(SCHEMA)
        conn.executemany(
            "INSERT INTO members "
            "(member_id, name, status, phone, grade, joined_on) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            rows,
        )
        return list(conn.execute(sql))
    finally:
        conn.close()


if __name__ == "__main__":
    tests = [
        (
            [
                (1, "이서준", "DORMANT", None, "VIP", "2022-05-01"),
                (2, "최하늘", "DORMANT", "01012345678", "VIP", "2021-03-03"),
                (3, "김다은", "DORMANT", None, "GOLD", "2023-11-02"),
                (4, "한소희", "DORMANT", None, "GOLD", "2024-01-01"),
                (5, "정우성", "DORMANT", None, "SILVER", "2020-08-08"),
                (6, "박민재", "ACTIVE", None, "VIP", "2020-01-01"),
            ],
            [
                (1, "이서준", "VIP", "2022-05-01"),
                (3, "김다은", "GOLD", "2023-11-02"),
            ],
        ),
        (
            [
                (10, "가가", "DORMANT", None, "VIP", "2023-01-01"),
                (8, "다다", "DORMANT", None, "VIP", "2023-01-02"),
                (7, "나나", "DORMANT", None, "GOLD", "2023-01-01"),
            ],
            [
                (7, "나나", "GOLD", "2023-01-01"),
                (10, "가가", "VIP", "2023-01-01"),
                (8, "다다", "VIP", "2023-01-02"),
            ],
        ),
        (
            [
                (1, "공백전화", "DORMANT", "", "VIP", "2020-01-01"),
                (2, "활동회원", "ACTIVE", None, "GOLD", "2019-05-05"),
                (3, "당일가입", "DORMANT", None, "VIP", "2024-01-01"),
                (4, "전날가입", "DORMANT", None, "GOLD", "2023-12-31"),
            ],
            [
                (4, "전날가입", "GOLD", "2023-12-31"),
            ],
        ),
        (
            [
                (1, "소문자", "DORMANT", None, "vip", "2020-01-01"),
                (2, "정상", "DORMANT", None, "VIP", "2021-01-01"),
            ],
            [
                (2, "정상", "VIP", "2021-01-01"),
            ],
        ),
        (
            [
                (1, "활동", "ACTIVE", None, "VIP", "2020-01-01"),
                (2, "실버", "DORMANT", None, "SILVER", "2020-01-01"),
            ],
            [],
        ),
    ]

    for i, (rows, expected) in enumerate(tests, start=1):
        got = run(rows)
        ok = "OK" if got == expected else "FAIL"
        print(f"[{ok}] case {i}: got {got!r} (expected {expected!r})")
