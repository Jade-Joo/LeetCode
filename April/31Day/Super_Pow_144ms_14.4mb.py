class Solution:
    #92ms 14.4mb
    # def superPow(self, a: int, b: List[int]) -> int:
    #     return pow(a, int(''.join(map(str, b))), 1337)
    
    #((a mod n) * (b mod n)) mod n
    def superPow(self, a, b):
        result = 1
        apower = a
        for digit in reversed(b):
            #plus
            result = result * pow(apower, digit, 1337) % 1337
            #10 multiply
            apower = pow(apower, 10, 1337)
        return result