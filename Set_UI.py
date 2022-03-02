from tkinter import *
from PIL import Image, ImageDraw
import PIL
from Recog import Recog

Cwidth = 80
Cheight = 80


class Window:

    rec = Recog()

    def __init__(self, width, height, title="MyWindow", icon=r"resources/images.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.left_frame = Frame(self.root)
        self.right_frame = Frame(self.root, width=Cwidth, height=Cheight)
        self.cv = Canvas(self.right_frame, width=Cwidth, height=Cheight, bg='white')
        self.image = PIL.Image.new("RGB", (width, height))
        self.draw = ImageDraw.Draw(self.image)
        self.penSize_slider = 3
        self.buttonRecognize = Button(self.left_frame, text="Распознать", command=self.rec.recognize, width=20)
        self.buttonTeach = Button(self.left_frame, text="Обучить", width=20)
        self.buttonSave = Button(self.left_frame, text="Сохранить веса", command=self.rec.save_w, width=20)
        self.buttonError = Button(self.left_frame, text="Ошибка", width=20)
        self.buttonClear = Button(self.left_frame, text="Очистить", command=self.clear, width=20)
        self.lbl0 = Label(self.left_frame, text="Размер пера", font="Arial 10", width=15)
        self.lbl1 = Label(self.left_frame, text=" ", font="Arial 10", fg="black")
        self.lbl2 = Label(self.left_frame, text=" ", font="Arial 9", width=15)
        if icon:
            self.root.iconbitmap(icon)

    def draw_widgets(self):
        self.cv.bind("<B1-Motion>", self.paint)
        self.cv.pack(pady=60)
        self.left_frame.pack(anchor=W, ipadx=20, pady=30, side=LEFT)
        self.right_frame.pack(anchor=E, ipadx=30, pady=30, fill=Y, side=LEFT)
        self.buttonRecognize.pack(side=TOP)
        self.buttonTeach.pack(side=TOP)
        self.buttonError.pack(side=TOP)
        self.buttonClear.pack(side=TOP)
        self.lbl1.pack(side=TOP)
        self.lbl2.pack(side=TOP)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cv.create_oval(x1, y1, x2, y2, fill="black", width=self.penSize_slider)
        self.draw.line([x1, y1, x2, y2], fill="black", width=self.penSize_slider)

    def clear(self):
        self.cv.delete("all")
        self.draw.rectangle((0, 0, Cwidth, Cheight), fill=(255, 255, 255, 255))

#
# if __name__ == "__main__":
#     window = Window(350, 250, "Лабораторная работа №0")
#     window.run()