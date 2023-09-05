''' Exercise #4. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################

def most_popular_character(my_string):
    d = {}
    for i in my_string:
        frequency = d.get(i , 0)
        frequency += 1
        d[i] = frequency
    sd = sorted(d, key = d.get, reverse = True) 	
    lst = []
    for key in sd:
        if d[key] == d[sd[0]]:
            lst.append(key)
    lst.sort()
    result = lst[0]
    return result

#########################################
# Question 2 - do not delete this comment
#########################################

def diff_sparse_matrices(lst):
    d = {}
    for key in lst[0]:
        d[key] = lst[0].get(key,0) 
            
    j = 1
    while j < len(lst):
        for key in lst[j]:
            if not key in d:
                d[key] = -lst[j].get(key,0)
            else:
                d[key] = d[key]-lst[j].get(key,0)
        j += 1
    result = {}   
    result = d.copy()
    for key in result.keys():
        if d[key] == 0:
            d.pop (key, 0)
            
    return d

#########################################
# Question 3 - do not delete this comment
#########################################

def find_substring_locations(s, k):
    d = {}
    for i in range(len(s)-k+1):
        new_string = s[i:i+k]
        if not new_string in d:
            d[new_string] = [i]
        else:
            d[new_string].append(i)

    return d
result = find_substring_locations('k',1)
print(result)
#########################################
# Question 4 - do not delete this comment
#########################################

def courses_per_student(tuples_lst):
             
    d = {}
    for i in range(len(tuples_lst)):
        if not tuples_lst[i][0].lower() in d:
            d[tuples_lst[i][0].lower()] = [tuples_lst[i][1].lower()]
        else:
            d[tuples_lst[i][0].lower()].append(tuples_lst[i][1].lower())
    return d

def num_courses_per_student(stud_dict):
    for key in stud_dict.keys():
        stud_dict[key] = len(stud_dict[key])
    return stud_dict

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__': #Do not delete this line!
	# Q1
	print(most_popular_character('aabbAA') == 'A')

	# Q2
	print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})
		
	# Q3
	print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})

	# Q4
	stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])
		
	print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
		
	num_courses_per_student(stud_dict)
	print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================

