""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 3  # Replace the assignment with a positive integer to test your code.
lst = [1,2,3,4,5]# Replace the assignment with other lists to test your code.

# Write the rest of the code for question 1 below here.
for elem in lst:
    if elem%a==0:
     print(lst.index(elem))
     break
    
else:
    print('-1')
# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['hello', 'world', 'course', 'python', 'day']
# Replace the assignment with other lists of strings (str) to test your code.

# Write the code for question 2 using a for loop below here.
sum=0
avg=0
num=0
for i in lst2:
    sum+=len(i)
    
avg=sum/len(lst2)

for i in lst2:
    if len(i)>avg:
     num+=1
     
print ('The number of strings longer than the average is:',num)

# Write the code for question 2 using a while loop below here.
sum_2=0
avg_2=0
num_2=0
j=0
k=0
while j<len(lst2):
    sum_2+=len(lst2[j])
    j=j+1
avg_2=sum/len(lst2)
    
while k<len(lst2):
    if len(lst2[k])>avg:
     num_2+=1
    k=k+1
     
print ('The number of strings longer than the average is:',num_2)
# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [0, 1, 2, 3, 4]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
sum=0
i=0
if len(lst3)==0:
    print('0')
elif len(lst3)==1:
    print(lst3[0])
else:
   while i<len(lst3)-1:
      sum+=lst3[i]*lst3[i+1]
      i=i+1
   print(sum)
 
# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, 2, 4, 7]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.

i = 2
new_list = [lst4[0],lst4[1]]
sub = 0

while i<len(lst4):
    sub = lst4[i]-lst4[i-1]
    if abs(sub) > abs(lst4[i-1]-lst4[i-2]):
        new_list.append(lst4[i])
    i += 1
    
print(new_list)

# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaaddddgdddddddddefggg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.

i=0
sum=0

if len(my_string)==0:
    print("Didn't find a substring of length",k)
elif k==1:
    print("For length",k,"found the substring",my_string[0]+'!')
else:
    for i in range(len(my_string)-k+1):
        if sum == k-1:
            break
        else:
            sum = 0
        for j in range(i,i+k,1):
            if sum == k-1:
                break
            elif my_string[j]==my_string[j+1]:
                sum += 1
                if sum == k-1:
                    print("For length",k,"found the substring",my_string[i+1]*k+'!')
                    break
                else:
                    continue
            else:
                break
            
        else:
            break
    else:
        if sum == k-1:
            pass
        else:
            print("Didn't find a substring of length",k)
    













        
       















    
  
# End of code for question 5
