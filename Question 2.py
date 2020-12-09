
#Solution for Question 2
"""
Question 2:
Counting the pairs with k different from an integer list 
eg: list = [1, 3,5] and k = 2 
expected: we will have 2 pairs: {(1,3), (3,5)} 
Note: we also consider the negative numbers.
"""

def pairswithkdiff(Lst,n,k):
    
    counter = 0
    
    Lst.sort()         # Sort the list elements
    
    i=0
    j=0
    
    while j<n:
        if Lst[j] - Lst[i] == k:
            counter+=1
            i+=1
            j+=1
            
        elif Lst[j] - Lst[i] > k:
            i+=1
        else:
            j+=1
    return counter

if __name__=='__main__':
    Lst = [1, 3, 5]
    n = len(Lst)
    k = 2
    print("Count of pairs with difference 2 is: ", pairswithkdiff(Lst, n, k))
    
#This code works for negative numbers as well
    
            