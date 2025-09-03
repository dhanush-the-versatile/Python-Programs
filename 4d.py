# Input as string
S = "LENDI"
for i in range(1, len(S)):
    f_p = S[:i+1]
    s_p = ""
    for j in range(i-1, -1, -1):
        s_p += S[j]
    pattern = f_p + s_p
    print(pattern)
