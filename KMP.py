# 模式搜索就是在一个主文本字符串中, 查找一个子字符串是否存在
s = 'abcaabcdba'
a = 'abcd'
def KMP(s, a):      #  时间复杂度O(n)
    i, j = 0, 0     #  维护两个指针
    for i in range(len(s)):
        if s[i] == a[j]:
            if j == len(a)-1:
                return i-len(a)+1, i
            j += 1
            continue
        else:
            j = 0
    return -1, -1
print(KMP(s,a))
