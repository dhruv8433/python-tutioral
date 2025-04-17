class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False

        myStack = []
        flag = False

        for i in range(len(s)):
            # if open bracket than push into stack
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                myStack.append(s[i])
            # else remove stack top element and compare
            else:
                if len(myStack) > 0:
                    temp = myStack.pop()

                    if (temp == "(" and s[i] == ")") or (temp == "[" and s[i] == "]") or (temp == "{" and s[i] == "}"):
                        flag = True
                    else:
                        return False
                else:
                    return False
        
        return flag and len(myStack) == 0
            

s= Solution()
print(s.isValid("[[[]"))
