T = int(input().strip())
words = []

for _ in range (0,T):
    word = input()
    words.append(word)

for word in words:
    s1 = ""
    s2 = ""
    N = len(word)

    for i in range(0, N):
        if i % 2 == 0:
            s1 += word[i]
        else:
            s2 += word[i]
    print ("{} {}". format(s1, s2))
