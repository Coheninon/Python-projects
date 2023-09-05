''' Exercise #10. Python for Engineers.'''

import numpy as np
import pandas as pd
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 helper functions - do not delete
# this comment or change these functions
#########################################

#helper1----------------------------------------------------------------------
def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])


#helper2----------------------------------------------------------------------
def ascii_to_np_array(s):
    return np.frombuffer(s.encode(), dtype=np.uint8)


#########################################
# Question 1 - do not delete this comment
#########################################

#1----------------------------------------------------------------------------
def arr_dist(a1, a2):
    return abs(a1.astype(int) - a2.astype(int)).sum()

#2----------------------------------------------------------------------------
def find_best_place(im, np_msg):
    val = 1000000
    for i in range(im.shape[0]):
        for j in range(im.shape[1] - len(np_msg)):
            if arr_dist(im[i, j: j + len(np_msg)], np_msg) < val:
                tupl = (i, j)
                val = arr_dist(im[i, j: j + len(np_msg)], np_msg)
    return tupl

    

#3----------------------------------------------------------------------------
def create_image_with_msg(im, img_idx, np_msg):
    copy = np.copy(im)
    copy[img_idx[0], img_idx[1]: img_idx[1] + len(np_msg)] = np_msg 
    copy[0,0] = img_idx[0]
    copy[0,1] = img_idx[1]
    copy[0,2] = len(np_msg)
    return copy 
 

#4----------------------------------------------------------------------------
def put_message(im, msg):
    return create_image_with_msg(im, find_best_place(im, ascii_to_np_array(msg)), ascii_to_np_array(msg))


#5----------------------------------------------------------------------------
def get_message(im):
    msg_i = im[0, 0]
    msg_j = im[0, 1]
    msg_len = im[0, 2]
    msg = im[msg_i, msg_j: msg_j + msg_len]
    
    return np_array_to_ascii(msg) 


##############################################################################
##############################################################################


#########################################
# Question 2 - do not delete this comment
#########################################

#A----------------------------------------------------------------------------
def read_missions_file(file_name):
    try:
        return pd.read_csv(file_name)
    except IOError:
        raise IOError ("An IO error occurred")

#B----------------------------------------------------------------------------
def add_daily_gain_col(bounties):
    bounties['Daily gain'] = (bounties["Bounty"] - bounties["Expenses"])/bounties['Duration']
    return bounties
    

#C----------------------------------------------------------------------------
def sum_rewards(bounties):
    return (bounties["Bounty"] - bounties["Expenses"]).sum()


#D----------------------------------------------------------------------------
def find_best_kingdom(bounties):
    return bounties.loc[add_daily_gain_col(bounties)["Daily gain"].idxmax()]["Kingdom"]

#########################################
# A test for Question 1 - do not delete this comment 
#########################################

def question_A_test():
    msg1 = 'Hello, NUMPY!'
    orig_file_name = 'parrot.png'

    im1 = imageio.imread(orig_file_name)
    im2 = put_message(im1, msg1)

    plot_image = np.concatenate((im1, im2), axis=1)

    plt.figure()
    plt.imshow(plot_image, cmap=plt.cm.gray)
    plt.show()

    msg2 = get_message(im2)
    return msg2

#########################
# main code - do not delete this comment
# Add test cases below
#########################
if __name__ == "__main__":
    # ****write test cases only here****
    
    # Uncomment the following test after implementing Question 1
    assert(question_A_test() == "Hello, NUMPY!")


    

