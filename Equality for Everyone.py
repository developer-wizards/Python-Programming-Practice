''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
The new world believes in equality for everyone and that they must have equal rights and individual identity, regardless of what they are and from where they belong. In this problem, everyone should be present equally. The string may contain lowercase alphabets, uppercase alphabets, numbers or other characters but everyone should exist equally. If the string is such then print "Equality For Everyone" otherwise print "No Equality".

Input Format
The first line of input consists of numbers of test cases, T.

Next T lines consist of strings to check.



Constraints
1<= T <=10

1<= |string| <=1000



Output Format
Print the required output.

Input:
3
aaabbBBAAA12345)(*&^
aa11BB!!!!!!
aWsEdR1!2@3#

Output:
Equality For Everyone
No Equality
Equality For Everyone

'''

def main():
    t = int(input())
    for i in range(t):
        a = input()
        lower_case = 0
        upper_case = 0
        numbers = 0
        special_char = 0
        for i in range(len(a)):
            if(a[i].islower()):
                lower_case += 1;
            elif(a[i].isupper()):
                upper_case += 1;
            elif(a[i].isdigit()):
                numbers += 1;
            else:
                special_char += 1;
        
        if(lower_case == upper_case and upper_case == numbers and numbers==special_char):
            print("Equality For Everyone")
        else:
            print("No Equality")





main()

