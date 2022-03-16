
for _ in range(n):
    s = input()
    s_len = len(s)
    for i in range(s_len):
        if (i + 1 != s_len):
            if (s[i] != s[i + 1]):
                if (s[i] in s[(i + 1):]):
                    break
                else:
                    continue
        else:
            answer += 1
print(answer)