class Solution:
    def romanToInt(self, s: str) -> int:
        map_dict = {'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        }

        total = 0
        pre_num = 0

        for str in s[::-1]:
            num = map_dict[str]
            if num < pre_num:
                total -= num
            else :
                total += num
            
            pre_num = num


        return total

        