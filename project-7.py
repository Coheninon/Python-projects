''' Exercise #7. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################

def four_bonacci_rec(n):
    if n < 4:
        return n
    return four_bonacci_rec(n-1) + four_bonacci_rec(n-2) + four_bonacci_rec(n-3) + four_bonacci_rec(n-4)

#########################################
# Question 1.b - do not delete this comment
#########################################

def four_bonacci_mem(n, memo=None):    
    if n < 4:
        return n
    if memo == None:
        memo = {}
    mem_key = (n)
    if mem_key not in memo:
        memo[mem_key] = four_bonacci_mem(n-1, memo) + four_bonacci_mem(n-2, memo) + four_bonacci_mem(n-3, memo) + four_bonacci_mem(n-4, memo)

    return  memo[mem_key]

#########################################
# Question 2 - do not delete this comment
#########################################

def climb_combinations_memo(n, memo=None):  
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if memo == None:
        memo = {}
        
    mem_key = n
    if mem_key not in memo:
        memo[mem_key] = climb_combinations_memo(n - 1, memo) + climb_combinations_memo(n - 2, memo)
        
    return memo[mem_key]

#########################################
# Question 3 - do not delete this comment
#########################################

def catalan_rec(n, memo=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if memo == None:
        memo = {}
     
    mem_key = n
    if mem_key not in memo:
        sum = 0
        for i in range(0,n):
            sum += catalan_rec(i,memo)*catalan_rec(n-i-1,memo)
        memo[mem_key] = sum
        
    return memo[mem_key]

#########################################
# Question 4.a - do not delete this comment
#########################################

def find_num_changes_rec(n, lst):
    
    if n == 0:
        return 1
    elif len(lst) == 0 and n != 0:
        return 0

    cnt = 0   
    if lst[-1] <= n:     
        cnt += find_num_changes_rec(n,lst[0:-1]) + find_num_changes_rec(n-lst[-1],lst)  
        return cnt
    else:
        return find_num_changes_rec(n,lst[0:-1])
        
#########################################
# Question 4.b - do not delete this comment
#########################################

def find_num_changes_mem(n, lst, memo=None):
    
    if n == 0:
        return 1
    elif len(lst) == 0 and n != 0:
        return 0
    
    if memo == None:
        memo = {}
    mem_key = (n,tuple(lst))
    if mem_key not in memo:
        cnt = 0
        if lst[-1] <= n:     
            cnt += find_num_changes_mem(n,lst[0:-1],memo) + find_num_changes_mem(n-lst[-1],lst,memo) 
            memo[mem_key] = cnt
        else:
            return find_num_changes_mem(n,lst[0:-1],memo)

    return memo[mem_key]

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    #Question 1.a tests - you can and should add more    
    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)

    
    #Question 1.b tests - you can and should add more
    print(four_bonacci_mem(0) == 0)
    print(four_bonacci_mem(5) == 12)
    print(four_bonacci_mem(8) == 85)

    
    #Question 2 tests - you can and should add more
    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    
    #Question 3 tests - you can and should add more
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    
    #Question 4.a tests - you can and should add more
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(105,[1,105,999,100]) ==3)

    
    #Question 4.b tests - you can and should add more
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)

# ============================== END OF FILE =================================
