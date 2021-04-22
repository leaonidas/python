class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)

        if xStr[0] == '-':
            print("- print\n")
            return False

        for i in range(0, int(len(xStr)/2)):
            if xStr[i] != xStr[int(len(xStr))-i-1]:
                print("false print")
                return False
            else:
                i += 1
        print("True: " + xStr)
        return True


if __name__ == '__main__':
    sol = Solution()
    sol.isPalindrome(1231)
