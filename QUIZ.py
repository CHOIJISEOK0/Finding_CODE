# READ FILE
with open("code.txt", "r") as f:
    data = f.read()

# CUT SENTENCES
a = data.split("\n")

result = []

word = "improve"
for y in range(len(a)):
    for x in range(len(a[0])):
        # a 가 있는 위치 찾기
        if a[y][x] == word[0]:
            # RIGHT
            check = True
            if x + len(word) - 1 < len(a[0]):
                for b in range(len(word)):
                    if a[y][x + b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # LEFT
            check = True
            if x - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # DOWM
            check = True
            if y + len(word) - 1 < len(a):
                for b in range(len(word)):
                    if a[y + b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # UP
            check = True
            if y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y - b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

print(result)
