# 학생 A의 점수 입력
a_math, a_english = map(int, input().split())
# 학생 B의 점수 입력
b_math, b_english = map(int, input().split())

# 우선순위 결정
if (a_math > b_math) or (a_math == b_math and a_english > b_english):
    print("A")
else:
    print("B")
