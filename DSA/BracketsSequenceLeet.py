class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myList = []
        flag = False
        if(len(s) % 2 == 0):
            if s[0] == ")" or s[0] == "]" or s[0] == "}":
                flag = False
            for i in range(len(s)):
                if s[i] == "(" or s[i] == "[" or s[i] == "{":
                    myList.append(s[i])
                else:
                    if len(myList) > 0:
                        temp = myList.pop()
                        print("comparing ", temp, " and ", s[i])
                        if temp == "(" and s[i] == ")":
                            print("matched ()")
                            flag = True
                        elif temp == "{" and s[i] == "}":
                            print("matched {}")
                            flag = True
                        elif temp == "[" and s[i] == "]":
                            print("matched []")
                            flag = True
                        else:
                            return False
                    else:
                        flag = False
            return flag and len(myList) == 0
                
s= Solution()
print(s.isValid("[[[]"))
