# READ FILE
with open("QUIZ.txt", "r") as f:
    data = f.read()

# CUT SENTENCES
a = data.split("\n")

result = []

word = "memorize"
for y in range(len(a)):
    for x in range(len(a[0])):
        # FIND "A" LOCATION
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

            #----------------------------------------------------
                    

            # LEFT
            check = True
            if x - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            #----------------------------------------------------
                    

            # DOWM
            check = True
            if y + len(word) - 1 < len(a):
                for b in range(len(word)):
                    if a[y + b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            #----------------------------------------------------
                    

            # UP
            check = True
            if y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y - b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            #----------------------------------------------------
                    

            # UP RIGHT
            check = True
            if x + len(word) - 1 < len(a[0]) and y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y - b][x + b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            #----------------------------------------------------


            # UP LEFT
            check = True
            if x - len(word) + 1 >= 0 and y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y - b][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            #----------------------------------------------------


            # DOWN RIGHT
            check = True
            if x - len(word) + 1 >= 0 and y + len(word) - 1 < len(a):
                for b in range(len(word)):
                    if a[y + b][x + b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            #----------------------------------------------------


            # DOWN LEFT
            check = True
            if x - len(word) + 1 >= 0 and y + len(word) - 1 < len(a):
                for b in range(len(word)):
                    if a[y + b][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])
                    
            #----------------------------------------------------

                    
print(result)
