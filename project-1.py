''' Exercise #1 '''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 220.0 # Replace ??? with a positive float of your choice.
AB = 20.0 # Replace ??? with a positive float of your choice.
BC = 10.0 # Replace ??? with a positive float of your choice.
AD = 15.0 # Replace ??? with a positive float of your choice.
DC = 30.0 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.
Perimeter=AB+BC+DC+AD
print('Perimeter is:',Perimeter)
Midsegment=(AB+DC)/2
print('Midsegment is:',Midsegment)
Height=S/Midsegment
print('Height is:',Height)

#########################################
# Question 2 - do not delete this comment
#########################################
my_name = 'abednadir' # Replace ??? with a string of your choice.
# Write the rest of the code for question 2 below here.
my_name_upper=my_name[0].upper()+my_name[1:]
print('Hello'+' '+my_name_upper+'!')

#########################################
# Question 3 - do not delete this comment
#########################################
number  = 109 # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.
if number%9==0:
    print('I am',number,'and I am divisible by 9')
else:
    print('I am',number,'and I am not divisible by 9')

#########################################
# Question 4 - do not delete this comment
#########################################
text ='kaboom' # Replace ??? with a string of your choice.
copies = 3  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
sub1=text[1::2]
sub2=text[0::2]
new_str=(sub1+sub2)
print(copies*new_str)

#########################################
# Question 5 - do not delete this comment
#########################################
name ='droLtromedloV' # Replace ??? with a string of your choice.
q = 4 # Replace ??? with a int of your choice.
# Write the rest of the code for question 5 below here.
if q<0 or q>len(name) or len(name)==0:
    print('Error: illegal input!')
else:
    sub1=name[0:q:]
    sub2=name[q::]
    sub1=sub1[::-1]
    sub2=sub2[::-1]
    print(sub1+" "+sub2)
