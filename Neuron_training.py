from PIL import Image
import numpy as np
from tkinter import *

epoch = 3

inputs_number = 6400 #входные данные
learning_rate = 0.15 #скорость обучения, можно "поиграться" с этим значением

b = 10

np.set_printoptions(threshold=np.inf)

w = np.random.rand(inputs_number)


# data = im.getdata()
# data = np.matrix(data)
# new_im = Image.fromarray(data)

# w[0] = 0.5
# w[1] = 0.5
# w[2] = 0.5

test_w=open('w/test.csv.csv','r')
test_w_list=test_w.readlines()
test_w.close()