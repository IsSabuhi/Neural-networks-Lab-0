import random
from PIL import Image, ImageDraw, ImageOps
import PIL
import numpy as np
from tkinter import *


width = 80
height = 80
b = 1 #Пороговая функция
white = (255, 255, 255)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Recog:

    def __init__(self):
        self.inverted_img = None
        self.grayscaled_img = None
        self.resized_img = None
        self.img = None
        self.img01 = None
        self.w = None
        self.data = None
        self.w1 = None
        self.sum_w1 = None

    def recognize(self):
        self.inverted_img = ImageOps.invert(image)
        self.grayscaled_img = self.inverted_img.convert('L')
        self.resized_img = self.grayscaled_img.resize((80, 80), PIL.Image.ANTIALIAS)
        self.img = np.asarray(self.resized_img, dtype='uint8')
        self.img01 = self.img / 255
        np.set_printoptions(threshold=np.inf)
        self.w = np.matrix([[round(random.uniform(-0.3, 0.3), 2) for y in range(width)] for x in range(height)])
        self.data = np.genfromtxt('test.csv', delimiter=",")

        self.w1 = np.dot(self.img01, self.w)
        self.sum_w1 = np.sum(self.w1)
        # print(self.sum_w1)

        if self.sum_w1 >= b:
            print("Это крестик")
        else:
            print("Это нолик")


        lbl1['text'] = np.argmax(self.w1)
        lbl2['text'] = 'Probability:', round(self.sum_w1, 2), '%'


rec = Recog()


def save_w():
    np.savetxt("test.csv", rec.w, delimiter=",")
    print("Успешно сохранены веса из первого слоя.")


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black", width=penSize_slider.get())
    draw.line([x1, y1, x2, y2], fill="black", width=penSize_slider.get())


def clear():
    cv.delete("all")
    draw.rectangle((0, 0, width, height), fill=(255, 255, 255, 255))


root = Tk()
root.title("Лабораторная работа №0")


cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()


image = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image)

cv.pack(side=RIGHT)
cv.bind("<B1-Motion>", paint)

left_frame = Frame(root)
right_frame = Frame(root)

left_frame.pack(anchor=W, padx=30)
right_frame.pack(anchor=E)


buttonRecognize = Button(left_frame, text="Распознать", command=rec.recognize, width=20)
buttonTeach = Button(left_frame, text="Обучить", width=20)
buttonSave = Button(left_frame, text="Сохранить веса", command=save_w, width=20)
buttonError = Button(left_frame,text="Ошибка", width=20)
buttonClear = Button(left_frame, text="Очистить", command=clear, width=20)
lbl0 = Label(left_frame, text="Размер пера", font="Arial 10", width=15)
lbl1 = Label(left_frame, text=" ", font="Arial 10", fg="black")
lbl2 = Label(left_frame, text=" ", font="Arial 9", width=20)


lbl0.pack(side=TOP)

penSize_slider = Scale(left_frame, from_=1, to=10, orient=HORIZONTAL)
penSize_slider.pack(side=TOP)

buttonRecognize.pack(side=TOP)
buttonTeach.pack(side=TOP)
buttonSave.pack(side=TOP)
buttonError.pack(side=TOP)
buttonClear.pack(side=TOP)

lbl1.pack(side=TOP)
lbl2.pack(anchor=W, side=TOP)

root.minsize(350, 250)
root.maxsize(350, 250)

if __name__ == "__main__":
    mainloop()