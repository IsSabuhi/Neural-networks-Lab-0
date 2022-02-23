import random
from PIL import Image, ImageDraw, ImageOps
import PIL
import numpy as np
from tkinter import *

width = 40
height = 40
n = 2
white = (255, 255, 255)


def recognize():

    inverted_img = ImageOps.invert(image)
    grayscaled_img = inverted_img.convert('L')
    resized_img = grayscaled_img.resize((40, 40), PIL.Image.ANTIALIAS)

    img = np.asarray(resized_img, dtype='uint8')
    img01 = img / 255

    np.set_printoptions(threshold=np.inf)

    w = [[round(random.uniform(-0.3, 0.3), 2) for y in range(width)] for x in range(height)]

    w1 = np.dot(img01, w)


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


buttonRecognize = Button(text="Распознать", command=recognize, width=20)
buttonError = Button(text="Ошибка", width=20)
buttonClear = Button(text="Очистить", command=clear, width=20)
lbl0 = Label(text="Размер пера", font="Arial 10", width=15)
lbl1 = Label(text=" ", font="Arial 30", fg="red")
lbl2 = Label(text=" ", font="Arial 12", width=15)

lbl0.pack()

penSize_slider = Scale(from_=1, to=10, orient=HORIZONTAL)
penSize_slider.pack()

buttonRecognize.pack()
buttonError.pack()
buttonClear.pack()

lbl1.pack()
lbl2.pack()


root.minsize(350, 200)
root.maxsize(350, 200)

root.mainloop()