from tkinter import *
import PIL
from PIL import Image, ImageDraw
from Recog import Recognize


class Window:

    rec = Recognize()

    def __init__(self, width, height, title="MyWindow", icon=r"resources/images.ico"):
        self.weight = None
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.white = (255, 255, 255)
        self.Cwidth = 80
        self.Cheight = 80
        self.left_frame = Frame(self.root)
        self.cv = Canvas(width=self.Cwidth, height=self.Cheight, bg='white')
        self.image = PIL.Image.new("RGB", (self.Cwidth, self.Cheight), self.white)
        self.draw = ImageDraw.Draw(self.image)
        self.penSize_slider = 4
        self.buttonRecognize = Button(self.left_frame, text="Распознать", command=self.recognize_event, width=20)
        self.buttonX = Button(self.left_frame, text="Крестик", command=self.button_X_event, width=20)
        self.buttonO = Button(self.left_frame, text="Нолик", command=self.button_O_event, width=20)
        self.buttonTeach = Button(self.left_frame, text="Обучение")
        self.buttonSave = Button(self.left_frame, text="Сохранить веса", command=self.save_weights_event, width=20)
        self.buttonLoadWeight = Button(self.left_frame, text="Загрузить веса", command=self.weight_file_event, width=20)
        self.buttonClear = Button(self.left_frame, text="Очистить", command=self.clear, width=20)
        self.lbl0 = Label(self.left_frame, text="Размер пера", font="Arial 10", width=15)
        self.lbl1 = Label(self.left_frame, text=" ", font="Arial 10", fg="black")
        self.lbl2 = Label(self.left_frame, text=" ", font="Arial 9", width=20)
        self.lbl3 = Label(self.left_frame, text=" ", font="Arial 10", width=20)
        self.lbl4 = Label(self.left_frame, text=" ", font="Arial 10", width=20)
        if icon:
            self.root.iconbitmap(icon)

    def recognize_event(self):
        self.rec.recognize(self.image, self.lbl1, self.lbl2)

    def button_X_event(self):
        self.rec.btn_X()

    def button_O_event(self):
        self.rec.btn_O()

    def save_weights_event(self):
        self.rec.save_w(self.lbl3)

    def weight_file_event(self):
        self.rec.weight_file(self.lbl4)

    def draw_widgets(self):
        self.cv.bind("<B1-Motion>", self.paint)
        self.cv.pack(anchor=N, side=RIGHT, pady=40, padx=50)
        self.left_frame.pack(anchor=W, ipadx=20, pady=20, side=LEFT)
        self.buttonRecognize.pack(side=TOP)
        self.buttonX.pack(side=TOP)
        self.buttonO.pack(side=TOP)
        self.buttonSave.pack(side=TOP)
        self.buttonLoadWeight.pack(side=TOP)
        self.buttonClear.pack(side=TOP)
        self.lbl1.pack(side=TOP)
        self.lbl2.pack(side=TOP)
        self.lbl3.pack(side=TOP)
        self.lbl4.pack(side=TOP)

    def run(self):
        self.rec.weight_init()
        self.draw_widgets()
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cv.create_oval(x1, y1, x2, y2, fill="black", width=self.penSize_slider)
        self.draw.line([x1, y1, x2, y2], fill="black", width=self.penSize_slider)

    def clear(self):
        self.cv.delete("all")
        self.draw.rectangle((0, 0, self.Cwidth, self.Cheight), fill=(255, 255, 255, 255))
