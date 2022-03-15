import random
from tkinter import Label
import PIL
from PIL import ImageOps, Image
import numpy as np


class Recognize:

    def __init__(self):
        self.weight = None
        self.Cwidth = 80
        self.Cheight = 80
        self.inverted_img = None
        self.grayscaled_img = None
        self.resized_img = None
        self.img = None
        self.img01 = None
        self.a = 0.3
        self.w = None
        self.data = None
        self.sum_elem_matrix = None
        self.sum_w = None
        self.error = None

    def weight_file(self):
        self.weight = np.genfromtxt('w.csv', delimiter=",")
        return self.weight

    def weight_init(self):
        self.weight = np.array([[(random.uniform(-0.3, 0.3)) for y in range(self.Cwidth)] for x in range(self.Cheight)]).flatten()
        return self.weight

    def recognize(self, image, lbl1, lbl2: Label):
        self.inverted_img = ImageOps.invert(image)
        self.grayscaled_img = self.inverted_img.convert('L')
        self.resized_img = self.grayscaled_img.resize((80, 80), PIL.Image.ANTIALIAS)
        self.img = np.asarray(self.resized_img, dtype='uint8').flatten()

        self.img01 = self.img / 255
        # self.img01 = np.array(self.img01).flatten()
        np.set_printoptions(threshold=np.inf)

        self.sum_elem_matrix = np.dot(self.img01, self.weight)
        self.sum_w = np.sum(self.sum_elem_matrix)
        # print(self.sum_w)
        if self.sum_w >= 0:
            lbl1['text'] = 'Это крест'
        else:
            lbl1['text'] = 'Это нолик'

        lbl2['text'] = self.sum_elem_matrix
        print(self.weight)

    def train(self):
        for i in range(len(self.img01)):
            if self.img01[i] == 1:
                self.weight = self.weight + (self.a * self.error)
        print(self.weight)

    def btn_X(self):
        self.error = 1
        self.train()

    def btn_O(self):
        self.error = -1
        self.train()

    def save_w(self):
        np.savetxt("w.csv", self.weight, delimiter=",")
        print("Веса успешно сохранены веса.")