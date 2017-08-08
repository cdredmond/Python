def anagram_check(s1, s2):
    s1t = list(s1.lower())
    s2t = list(s2.lower())
    s1t.sort()
    s2t.sort()
    s1 = ''
    s2 = ''
    for c in s1t:
        if c != ' ':
            s1 += c
    for c in s2t:
        if c != ' ':
            s2 += c

    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

s1 = "hi man"
s2 = "Hi     Man"

print(anagram_check(s1, s2))
