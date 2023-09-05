''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################

def sum_nums(file_name):
    f = open(file_name)
    for line in f:
        tokens = line.split()
    sums = 0
    for token in tokens:
        sums += int(token)
    f.close()
    return sums 

#########################################
# Question 2 - do not delete this comment
#########################################

def copy_lines_with_str(in_file_name, out_file_name, target_str):
    
    infile = 'OK_in'
    outfile = 'OK_out'
    
    try: 
        infile = open(in_file_name)
        outfile = open(out_file_name, 'w')
        for line in infile:
            if target_str in line:
                outfile.write(line)
                
    except IOError:
        pass

    finally:
        if infile != 'OK_in':
            infile.close()
        if outfile != 'OK_out':
            outfile.close()

#########################################
# Question 3 - do not delete this comment
#########################################

def is_prime(number):
    
    for i in range(2,int((number)**0.5)+1):
        if number%i==0:
            return False
    return True

def write_twin_primes(num, out_file_name):
    # use the following code to raise the errors you need:
    # raise ValueError("Illegal value num={}".format(num))
    # raise ValueError("Cannot write to {}".format(out_file_name))‎
    outfile = 'OK_out'
    if int(num) <= 0:
            raise ValueError("Illegal value num={}".format(num))
    try:
        outfile = open(out_file_name, 'w')
        if int(num) == 1:
            outfile.write('3,5')
        else:
            primes = [3,5]
            twins = [[3,5]]
            number = 7
            j = 2
            while len(twins) < num:
                if is_prime(number) == True:
                    primes.append(number)
                    number += 1
                    if primes[j] - primes[j-1] == 2:
                        twins.append([primes[j-1],primes[j]])
                    j+=1 
                    continue
                    
                else:
                    number += 1
                    continue
                    
            for i in range(len(twins)):
                for j in range(1):
                    outfile.write((str(twins[i][j])+','+str(twins[i][j+1])+'\n'))
        
    except IOError:
        raise ValueError("Cannot write to {}".format(out_file_name))

    finally:
        if outfile != 'OK_out':
            outfile.close()
                 
#########################################
# Question 4 - do not delete this comment
#########################################

def calc_avg_position_per_band(in_file_name):
    # use the following code to raise the error you need:
    # raise ValueError("At least one of the bands does not appear in the file {}".format(in_file_name))

    d = {}
    ABBA_sum = 0
    Beatles_sum = 0
    Radiohead_sum = 0
    ABBA_count = 0
    Beatles_count = 0
    Radiohead_count = 0
    f = open(in_file_name)
    
    lines = []
    for line in f:        
        lines.append(line.split(','))
    for i in range(len(lines)):
        if lines[i][1] == 'ABBA':
            ABBA_sum += int(lines[i][2])
            ABBA_count += 1
        if lines[i][1] == 'The Beatles':
            Beatles_sum += int(lines[i][2])
            Beatles_count += 1
        elif lines[i][1] == 'Radiohead':
            Radiohead_sum += int(lines[i][2])
            Radiohead_count += 1
            
    if ABBA_count == 0 or Beatles_count == 0 or Radiohead_count == 0:
        raise ValueError("At least one of the bands does not appear in the file {}".format(in_file_name))
        
    d['The Beatles'] = round(Beatles_sum/Beatles_count)
    d['Radiohead'] = round(Radiohead_sum/Radiohead_count)
    d['ABBA'] = round(ABBA_sum/ABBA_count)

    f.close()

    return d
    
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    # Q1
    q1_input_file_name = "q1_input_1.txt"
    print(sum_nums(q1_input_file_name) == 139)

    # Q2
    # compare manually your output files with the correct output files
    copy_lines_with_str("q2_input_1.txt", "q2_output_1_Rocky_res.txt", "Rocky") 
    copy_lines_with_str("q2_input_1.txt", "q2_output_1_ere_res.txt", "ere")
    copy_lines_with_str("q2_input_2.txt", "q2_output_2_Rocky_res.txt", "Rocky")
    copy_lines_with_str("q2_input_2.txt", "q2_output_2_boy_res.txt", "boy")
    copy_lines_with_str("q2_input_2.txt", "q2_output_2_Nancy_res.txt", "Nancy")

    # Q3
    write_twin_primes(4, "q3_output_1_res.txt")
    write_twin_primes(20, "q3_output_2_res.txt")
    try:
        num = 0
        write_twin_primes(num, "q3_output_2_res.txt")  # this line should raise an exception
        print("Exception must be raised for this input")
    except ValueError as ex:
        correct_error_message = "Illegal value num={}".format(num)
        if ex.args[0] == correct_error_message:
            print("True")
        else:
            print("Wrong message in raise exception. \nExpected:\t{}\ngot:\t\t{}".format(correct_error_message,
                                                                                         ex.args[0]))

    # Q4
    res_1 = calc_avg_position_per_band("q4_input_1.txt")
    print(res_1['The Beatles'] == 23 and res_1['Radiohead'] == 11 and res_1['ABBA'] == 4)
    try:
        input_file = "q4_input_2.txt"
        res_1 = calc_avg_position_per_band(input_file)
        print("Exception must be raised for this input")

        
    except ValueError as ex:
        correct_error_message = "At least one of the bands does not appear in the file {}".format(input_file)
        if ex.args[0] == correct_error_message:
            print("True")
        else:
            print("Wrong message in raise exception. \nExpected:\t{}\ngot:\t\t{}".format(correct_error_message,
                                                                                         ex.args[0]))



# add more tests here

# ============================== END OF FILE =================================
