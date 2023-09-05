
''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################

def reverse_string(s):
    if len(s) == 0:
        return s

    return s[-1] + reverse_string(s[0:-1])

#########################################
# Question 2 - do not delete this comment
#########################################

def find_maximum(lst):
    
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return lst[0]
    if lst[-1] < lst[-2]:
        new_list = lst[0:-1]
        return find_maximum(new_list)
    else:
        new_list = lst[0:-2]
        new_list.append(lst[-1])
        return find_maximum(new_list)

#########################################
# Question 3 - do not delete this comment
#########################################

def is_palindrome(s):
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

#########################################
# Question 4 - do not delete this comment
#########################################

def climb_combinations(n):
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return climb_combinations(n - 1) + climb_combinations(n - 2)

print(climb_combinations(900))


#########################################
# Question 5 - do not delete this comment
#########################################

def is_valid_paren(s, cnt=0):

    s = s.strip()
    s2 = s.strip()
    if len(s2) == 0:
       return True
    
    if s2[0] != '(' and s2[0] != ')':
        return is_valid_paren(s2[1:], cnt = cnt)
    if s2[-1] != '(' and s2[-1] != ')':
        return is_valid_paren(s2[:-1], cnt = cnt)
    if len(s2) == 1:
        if s2[0] == '(':
            return False
        if cnt == 1:
            return True
        return False
    
    if s2[0] == '(':
        return is_valid_paren(s2[1:], cnt = cnt + 1)
    if cnt == 0:
        return False
    return is_valid_paren(s2[1:], cnt = cnt - 1)

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == "__main__":
    #you can add tests for your code here.
    
    assert(reverse_string("abc") == 'cba')
    assert(reverse_string("Hello!") == '!olleH')

    assert(find_maximum([9,3,0,10]) == 10)
    assert(find_maximum([9,3,0]) == 9)
    assert(find_maximum([]) == -1)

    assert(is_palindrome("aa") == True)
    assert(is_palindrome("aa ") == False)
    assert(is_palindrome("caca") == False)
    assert(is_palindrome("abcbbcba") == True)

    assert(climb_combinations(3) == 3)
    assert(climb_combinations(10) == 89)

    assert(is_valid_paren("(.(a)") == False)
    assert(is_valid_paren("p(()r((0)))") == True)
    assert(is_valid_paren("") == True)

# ============================== END OF FILE =================================
