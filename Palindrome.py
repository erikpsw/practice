print("isPalindromr('')")
def isPalindromr(s):

    def toChars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in'abcdefghijklmnopqrstuvwxyz':
                ans=ans+c
        return ans

    def is_palindrome(s):
        if len(s) <= 1:  #边界条件
            return True
        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_palindrome(toChars(s))
