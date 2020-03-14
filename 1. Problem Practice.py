
#Make the list non-decreasing by changing only one digit of the elements

'''
Given an array arr[] of N integers where every element is from the range[1000, 9999]. The task is to make the array non-decreasing by changing
only one digit from the array elements and the elements of the resultant list will have to be from the given range of elements.
If it is possible to make the array non-decreasing with the given operation then print the updated list otherwise print "Not Possible".
'''
#Constant initialization
DIGITS = 4; MIN = 1000; MAX = 9999


#Function which return best smallest value by cahnging one digit
def getBest(prev , curr):

    # To start with the value  
    # we have achieved in the last step  
    maximum = max(MIN, prev);
    
    for i in range(maximum, MAX + 1):
        
        count = 0
        # Store the value with which the  
        # current will be compared 
        a = i
        
        # Current value
        b = curr

        for k in range(DIGITS):
            
            # If the current digit differs  
            # in both the numbers
            if a%10 != b%10 :
                count += 1

            # Eliminate last digits in  
            # both the numbers  
            a //= 10;  
            b //= 10; 

        # If the number of different  
        # digits is at most 1 
        if count <= 1:
            return i
            
    # If we can't find any number for which  
    # the number of change is less than or  
    # equal to 1 then return -1        
    return -1


#function to get non decreasing list by changing one digit
def getList(array, n):

    #new List to store changed values
    newList = []

    # Let's assume that it is possible to 
    # make the list non-decreasing 
    possible = True;
    
    newList.append(0)
    for i in range(n):
        
        # Element of the original array 
        curr = array[i]

        newList.append(getBest(newList[-1], curr))

        # Can't make the list non-decreasing  
        if (newList[-1] == -1) :  
            possible = False 
            break

        '''
        value = getBest(newList[-1], curr)
        if (value != -1):
            newList.append(getBest(newList[-1], curr))
            
        else:
            possible = False;  
            break;
        '''

    if possible == True:
        for i in range(1, len(newList)):
            print(newList[i], end = " ")
    else:
        print("Not possible")
    
    


#driver function
if __name__ == '__main__':

    array = [ 1095, 1094, 1095 ]
    n = len(array)

    getList(array, n)
