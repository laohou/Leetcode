class Solution:
    # @return a string
    def intToRoman(self, num):
            result=''
##hanle if the num is bigger than 1000
            if num < 4000 and num >= 1000:
                result=(num/1000)* 'M'
                num = num - num/1000*1000
##hanle the hundred digit          
            if num < 1000 and num >=900:
                result = result+'CM'
                num= num - 900
            elif num<900 and num >=500:
                result = result+'D'
                num = num - 500
                result = result + num/100*'C'
                num = num - num/100*100
            elif num < 500 and num >=400:
                result = result + 'CD'
                num = num - 400
            elif num < 400 and num >= 100:
                result = result + num/100*'C'
                num = num - num/100*100
##handle decimal digit
            if num < 100 and num >=90:
                result = result + 'XC'
                num = num - 90
            elif num <90 and num >=50:
                result = result + 'L'
                num = num -50
                result = result + num/10*'X'
                num = num - num/10*10
            elif num < 50 and num >=40:
                result = result + 'XL'
                num = num -40
            elif num < 40 and num >= 10:
                result = result+num/10*'X'
                num = num-num/10*10
##
            if num == 9:
                result = result +'IX'
            elif num <9 and num >=5:
                result = result + 'V'
                num = num -5
                result = result + num *'I'
            elif num == 4:
                result = result+'IV'
            else:
                result  = result + num*'I'

            return result

if __name__=="__main__":
    solution = Solution()
    print solution.intToRoman(600)
