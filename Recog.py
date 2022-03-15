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
        self.matrix = None
        self.sum_w = None
        self.error = None

    def weight_file(self, lbl4: Label):
        self.weight = np.genfromtxt('w.csv', delimiter=",")
        lbl4['text'] = "Веса загружены"
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

        np.set_printoptions(threshold=np.inf)

        self.matrix = np.dot(self.img01, self.weight)
        self.sum_w = np.sum(self.matrix)
        print(self.sum_w)
        if self.sum_w >= 0:
            lbl1['text'] = 'Это крестик'
        else:
            lbl1['text'] = 'Это нолик'

        lbl2['text'] = self.sum_w

    def train(self):
        for i in range(len(self.img01)):
            if self.img01[i] == 1:
                self.weight = self.weight + (self.a * self.error * self.img01)
        print(self.weight)

    def btn_X(self):
        self.error = 1
        self.train()

    def btn_O(self):
        self.error = -1
        self.train()

    def save_w(self, lbl3: Label):
        np.savetxt("w.csv", self.weight, delimiter=",")
        lbl3['text'] = "Веса сохранены."