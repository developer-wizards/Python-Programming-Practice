#function to print the matrix in spiral way
def matrix_spiral_print(row, col, X):
    '''
    [row, col] - dimension of matrix X
    row - end index of row
    col- end index of col
    let k and l be the starting index of the rows and columns respectively
    '''
    
    k=0;l=0
    
    while k < row and l < col:
        #loop for Printing in direction - left to right
        for i in range(l, col):
            print(X[k][i], end = ' ')
        
        #Since kth(initially 0 to 1 ) row is printed, increment the lowerbound by 1 
        k += 1
    
        #loop for printing in direction - Top to Bottom
        for i in range(k, row):
            print(X[i][col -1], end = ' ')
        
        #Since last column is printed we need to decrement it to second last
        col -= 1
    
        #Condition that lowerbound should not be greater than upperbound - for row, since next we'll be printing row (Right to left)
        if(k<row):
        
            #loop for printing in direction - Right to left
            for i in range(col-1, l-1, -1):
                print(X[row-1][i], end = ' ')
            
            #Since we have printed last row we have to decrement the upperbound of row by 1
            row -= 1
    
        #Condition that lowerbound should not be greater than upperbound - for col, since next we'll be printing column (Bottom to up)
        if(l<col):
        
            #loop for printing in direction - bottom to up
            for i in range(row - 1, k -1, -1):
                print(X[i][l], end = ' ')
            
            #Since we have printed 1st column, col lowerbound increment by 1
            l += 1
    

    

#Function to get the dimension of matrix
def dimen(multiDimArray):
    return([len(multiDimArray)] + dimen(multiDimArray[0]) if type(multiDimArray) == list else [])

#Driver code
grid = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20]]
shape = dimen(grid)
row = shape[0]; col = shape[1]
matrix_spiral_print(row, col, grid)

    
