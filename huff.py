from collections import deque

# 파일 리딩
with open('./new.lyx', 'r', encoding="UTF8") as f:
    data = f.read()

# 빈도 수로 정렬
used = {}
for char in data:
    b_char = char.encode()
    if b_char not in used:
        used[b_char] = 0
    used[b_char] += 1
result = deque(map(
    lambda x: x[0],
    sorted(
        map(lambda x: [x, used[x]], used),
        key=lambda x: (x[1], x[0]), reverse=True
    )
))
print(result)
# 트리 만들기
while True:
    if len(result) <= 2:
        break
    tr_left, tr_right = result.pop(), result.pop()
    result.appendleft(deque([tr_left, tr_right]))

def unlist(l: deque):
    if len(l) <= 1:
        return l
    left = l.popleft()
    right = l.pop()
    
    left  = unlist(left)  if isinstance(left, deque)  else deque(left)
    right = unlist(right) if isinstance(right, deque) else deque(right)
    
    return left + right

print(len(result), result)
if len(result) <= 1:
    huff_tree = result
else:
    huff_tree = unlist(result)
print(huff_tree)
