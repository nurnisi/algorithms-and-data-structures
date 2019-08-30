# 273. Integer to English Words
class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thous = ['Thousand', 'Million', 'Billion']
        extras = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        hund = 'Hundred'
        
        ans = []
        i = 0
        while num != 0:
            cur = num%1000
            tmp = []
            if cur%100 in extras:
                tmp.insert(0, extras[cur%100])
                cur //= 100
            else:
                if cur%10: tmp.insert(0, ones[cur%10-1])
                cur //= 10
                if cur%10: tmp.insert(0, tens[cur%10-1])
                cur //= 10
            if cur > 0:
                tmp.insert(0, hund)
                tmp.insert(0, ones[cur-1])
            if tmp and i: tmp.append(thous[i-1])
            ans = tmp + ans
            num //= 1000
            i += 1
        
        return ' '.join(ans) if ans else 'Zero'