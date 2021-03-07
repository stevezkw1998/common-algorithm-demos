def f2(s):
    i = 0
    maxlength = 0
    if not s:
        return 0
    if len(s) == 1:
        return 1
    for j in range(1,len(s)):
        while s[j] == s[i]:
            i += 1
        maxlength = max(maxlength, j - i + 1)
    return maxlength
def f3(s):
    res = tmp = i = 0
    for j in range(len(s)):
        i = j - 1
        while i >= 0 and s[i] != s[j]: 
            i -= 1
        if tmp < j - i:
            tmp = tmp + 1
        else:
            tmp = j - i
        res = max(res, tmp)
    return res
def f(s):
    ch, maxlength, i = {}, 0, -1
    for j in range(len(s)):
        if s[j] in ch:
            i = max(ch[s[j]], i)
        ch[s[j]] = j
        maxlength = max(maxlength, j - i)
    return maxlength

s = "abcabcbb"
print(f(s))