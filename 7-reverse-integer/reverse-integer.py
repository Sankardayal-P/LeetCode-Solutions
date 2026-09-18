class Solution:
    def reverse(self, x: int) -> int:
        string=str(x)
        if string[0]== '+' or string[0]=='-':
            temp = string[0]
            temp1 = string[1:][::-1]
        else:
            temp = ''
            temp1 = string[::-1]
        result = int(temp + temp1)
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result