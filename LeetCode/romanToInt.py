def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """

    result = 0
    i=0
    li = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    while i<len(s)-1:
        if li[s[i]] < li[s[i+1]]:
            result += li[s[i+1]] - li[s[i]]
            i+=2
        else:
            result += li[s[i]]
            i+=1

    if i!=len(s):
        result += li[s[len(s)-1]]


    return result

