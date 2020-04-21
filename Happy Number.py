'''
Happy Number
A number is called happy if it leads to 1 after a sequence of steps wherein each step number is replaced by the sum of squares of its digit
that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1
'''
'''
def happyNumber(n):
        dic = dict()
        while n:
                if 1 in dic:
                        return True
                if n in dic:
                        return False
                dic[n] = 0 
                sum_of_sq = 0;
                while n:
                        sum_of_sq += (n%10)**2
                        n //= 10
                n = sum_of_sq
'''
def isHappy( n):
        dic = {}
        while n:
            #print(dic, end=' ');print(n)   
            if 1 in dic:
                return print(True)
            if n in dic:
                return print(False)
            dic[n] = 0
            sum_of_sq = 0
            while n:
                sum_of_sq += (n%10)**2
                n //= 10
            n = sum_of_sq 

n=17
isHappy(n)
