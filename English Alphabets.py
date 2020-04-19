def main():
    """
    Count the no. of vowels and consonants for a given string in a respective testcase and multiply them

    In English, there are two types of characters, vowels and consonants. Romi is a student in school and is new to computers. He knows about vowels and consonants but does not know how to write code to get the correct output. He needs your help to learn to code and print the number of vowels, consonants and the product of them. Help Romi understand the code.

    Input Format
    The first line of input consist of number of test cases, T.

    Next T lines consist of strings.



    Constraints
    1<= T <=10

    1<= |S| <=1000



    Output Format
    For each string print the number of vowels, number of consonants and the product of them space separately.

    Input:-
    2
    abcdefgh
    zxcvbnm

    Output:-
    2 6 12
    0 7 0

    """
   
    t = int(input())
    for i in range(t):
        a = input()
        print("length of a is ",len(a))
        print("a is" ,a[0])
        count_vowel = 0;
        count_consonants = 0;
        for j in range(len(a)):
            
            if(a[j] == 'a' or a[j]=='e' or a[j]=='i' or a[j]=='o' or a[j]=='u'):
                count_vowel  += 1;
            else:
                count_consonants  += 1;
            
            
        print(count_vowel, end=" ")
        print(count_consonants, end = " ")
        print(count_vowel * count_consonants)

main()

