arr = [
        [1,1,1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]

sums = []

for i in range (4):
    for j in range (4):
        total = 0
        for k in range(3):
            for l in range(3):
                if k == 1 and l in [0,2]:
                    continue
                total += arr [i+k][j+l]
        sums.append(total)
print(max(sums))