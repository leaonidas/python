class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        xStr = str(x)
        xList = [None]*int(len(xStr))

        if xStr[0] == '-':
            isNegative = True
            xStr = xStr[1:]
            xList = [None]*int(len(xStr))

        for i in range(0, int(len(xStr)/2)):
            xList[len(xStr)-1-i] = xStr[i]
            xList[i] = xStr[len(xStr)-1-i]

        if len(xStr) % 2 != 0:
            xList[int(len(xStr)/2)] = xStr[int(len(xStr)/2)]

        xStr = "".join(xList)
        if isNegative:
            xStr = '-' + xStr

        if int(xStr) > (2 ** 31) - 1 or int(xStr) < -(2 ** 31):
            print("Returned 0!\n")
            return 0
        else:
            print("Returned " + xStr + " !\n")
            return int(xStr)


if __name__ == '__main__':
    sol = Solution()
    sol.reverse(123)
