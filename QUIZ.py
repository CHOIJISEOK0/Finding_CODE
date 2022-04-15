#READ FILE
with open("QUIZ.txt", "r") as f:
         data = f.read()

#CUT SENTENCE
a = data.split("\n")

for y in range(len(a)):
        for x in range(len(a[0])):
                if a[y][x] == "a":
                           print(x,y)
