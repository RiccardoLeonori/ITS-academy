def recursivePalindrome(s):
    s = s.strip().lower()
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return recursivePalindrome(s[1:-1])
    else:
        return False



print(recursivePalindrome("radar"))
print(recursivePalindrome("Anna"))
print(recursivePalindrome(" I topi non avevano nipoti"))
print(recursivePalindrome("casa"))
print(recursivePalindrome("marta"))
print(recursivePalindrome("roma e amore"))