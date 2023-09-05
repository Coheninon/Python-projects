''' Exercise #9. Python for Engineers.'''

import numpy as np
import matplotlib.pyplot as plt
import imageio

#########################################
# Question 1 - do not delete this comment
#########################################

class Roman():
    
    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val
    
    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0
        
        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num
    
    def __init__(self, input_value):
        if type(input_value) == int:
            if input_value < 0:
                self.is_neg = True
            else:
                self.is_neg = False   
            self.int_value = input_value
            self.roman_value = self.get_roman_from_int()
            
        if type(input_value) == str:
            if input_value[0] == '-':
                self.is_neg = True
            else:
                self.is_neg = False
            self.roman_value = input_value
            self.int_value = self.get_int_from_roman()
            
                
    def __str__(self):    
        return 'The integer value is ' + str(self.get_int_from_roman()) + ' and the Roman Numeral is denoted by ' + str(self.get_roman_from_int()) 

    def __repr__(self):
        return self.roman_value

    def __neg__(self):    
        return Roman(-self.int_value)
    
    def __add__(self, other):
        if type(other) == int:
            sum = self.int_value + other
        else:
            sum = self.int_value + other.int_value
        if sum == 0:
            raise ValueError ("There Is No Roman Representation For 0")
        return Roman(sum)
    
    def __lt__(self, other):
        if type(other) == int:
            if self.int_value < other:
                return True
            return False
        else:
            if self.int_value < other.int_value:
                return True
            return False
        
    def __gt__(self, other):
        if type(other) == int:
            if self.int_value > other:
                return True
            return False
        else:
            if self.int_value > other.int_value:
                return True
            return False

    def __floordiv__(self, other):
        if type(other) == int:
            div = self.int_value // other
        else:
            div = self.int_value // other.int_value
        if div == 0:
            raise ValueError ("There Is No Roman Representation For 0")
        return Roman(div)

#########################################
# Question 2 - do not delete this comment
#########################################

def load_training_data(filename):
    d = {}
    f = open(filename)
    a = []
    for line in f:        
        a.append(line.split(','))
    for i in range(len(a)):
        a[i][-1] = a[i][-1][0:-1]
    m = np.array(a)
    m[1:,1:] = m[1:,1:]
    d["column_names"] = m[0,1:]
    d["row_names"] = m[1:,0]
    d["data"] = m[1:,1:].astype(np.float)
    return d

def get_highest_weight_loss_trainee(data_dict):
    val = np.argmax(data_dict["data"][:,0] - data_dict["data"][:,-1])
    return (data_dict["row_names"][val])
    
def get_diff_data(data_dict):
    if (len(data_dict["column_names"])) %2 == 0:
        d_even = data_dict["data"][:,0::2]
        d_odd = data_dict["data"][:,1::2]
        d_1 = d_odd - d_even
        d_2 = d_even[:,1:] - d_odd[:,:-1]
        d_final = np.zeros((len(data_dict["row_names"]),len(data_dict["column_names"])-1))
        d_final[:,0::2] = d_1
        d_final[:,1:-1:2] = d_2
        return d_final
    else:
        d_even = data_dict["data"][:,0::2]
        d_odd = data_dict["data"][:,1::2]
        d_1 = d_odd - d_even[:,:-1]
        d_2 = d_even[:,1:] - d_odd[:,:]
        d_final = np.zeros((len(data_dict["row_names"]),len(data_dict["column_names"])-1))
        d_final[:,0:-1:2] = d_1
        d_final[:,1::2] = d_2
        return d_final

def get_highest_loss_month(data_dict):
    d = get_diff_data(data_dict)
    val = np.argmin(d[0,:] + d[1,:] + d[2,:] + d[3,:])
    return data_dict["column_names"][val + 1]

def get_relative_diff_table(data_dict):
    return get_diff_data(data_dict)/data_dict["data"][:,:-1]

#########################################
# Question 3 - do not delete this comment
#########################################

def histogram (img):
    im = imageio.imread(img)
    hist = np.bincount(im.flatten())
    return hist

def size (img):
    im = imageio.imread(img)
    num = im.shape[0]*im.shape[1]
    return num
    
def compute_entropy(img):
    num = 0
    num = np.sum(-histogram(img)[histogram(img) != 0]/size(img)*np.log2(histogram(img)[histogram(img) != 0]/size(img)))
    return num

def nearest_enlarge(img, a):
    im = imageio.imread(img)
    m = np.zeros((im.shape[0]*a,im.shape[1]*a))
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            m[i,j] = im[(i*(im.shape[0])//m.shape[0]),(j*(im.shape[1])//m.shape[1])]
    return m

if __name__ == '__main__':
    print(Roman(2))
    print(repr(Roman('XL')))
    print(-(-Roman(2)))
    r = Roman('V') + (5)
    print(r)
    d = Roman(6) // Roman(-5)
    print(d)

    data_dict = load_training_data("weight_input.csv")
    print(data_dict["data"])
    print(data_dict["column_names"])
    print(data_dict["row_names"])
    print(get_highest_weight_loss_trainee(data_dict))
    print(get_diff_data(data_dict))
    print(get_highest_loss_month(data_dict))
    print(get_relative_diff_table(data_dict))

    print(compute_entropy('cameraman.tif'))
    print(nearest_enlarge('cameraman.tif',2))
    I=nearest_enlarge('cameraman.tif',2)
    plt.figure()
    plt.imshow(I,cmap = plt.cm.gray)
    plt.show()
