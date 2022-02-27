import random
from PIL import Image, ImageDraw, ImageOps
import PIL
import numpy as np
from tkinter import *


width = 80
height = 80
n = 2
white = (255, 255, 255)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def recognize():

    inverted_img = ImageOps.invert(image)
    grayscaled_img = inverted_img.convert('L')
    resized_img = grayscaled_img.resize((80, 80), PIL.Image.ANTIALIAS)

    img = np.asarray(resized_img, dtype='uint8')
    img01 = img / 255

    np.set_printoptions(threshold=np.inf)

    w = np.matrix([[round(random.uniform(-0.3, 0.3), 2) for y in range(width)] for x in range(height)])

    data = np.genfromtxt('test.csv', delimiter=",")

    w1 = np.dot(img01, w)
    sum_w1 = np.sum(w1)
    print(sum_w1)
    outputs = sigmoid(w1)
    print(outputs)

    # for i in range(2000):
    #     outputs = sigmoid(w1)
    #
    #     err = data - outputs
    #     adj = np.dot(w1.T, err * (outputs * (1 - outputs)) )
    #
    #     w += adj
    #
    # print("Веса после обучения")
    # print(w)
    #
    # print(outputs)

    # np.savetxt("test.csv", w, delimiter=",")
    # print("Успешно сохранены веса из первого слоя.")

    lbl1['text']=np.argmax(w1),
    lbl2['text']='Probability:',sum_w1,'%'


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


buttonRecognize = Button(left_frame, text="Распознать", command=recognize, width=20)
buttonTeach = Button(left_frame, text="Обучить", width=20)
buttonError = Button(left_frame,text="Ошибка", width=20)
buttonClear = Button(left_frame, text="Очистить", command=clear, width=20)
lbl0 = Label(left_frame, text="Размер пера", font="Arial 10", width=15)
lbl1 = Label(left_frame, text=" ", font="Arial 10", fg="black")
lbl2 = Label(left_frame, text=" ", font="Arial 9", width=15)


lbl0.pack(side=TOP)

penSize_slider = Scale(left_frame, from_=1, to=10, orient=HORIZONTAL)
penSize_slider.pack(side=TOP)

buttonRecognize.pack(side=TOP)
buttonTeach.pack(side=TOP)
buttonError.pack(side=TOP)
buttonClear.pack(side=TOP)

lbl1.pack(side=TOP)
lbl2.pack(side=TOP)

root.minsize(350, 250)
root.maxsize(350, 250)

if __name__ == "__main__":
    mainloop()