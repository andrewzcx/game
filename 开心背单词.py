import tkinter as tk
import tkinter.messagebox
import random

files = ['小学英语/三年级上.txt',
         '小学英语/三年级下.txt',
         '小学英语/四年级上.txt',
         '小学英语/四年级下.txt',
         '小学英语/五年级上.txt',
         '小学英语/五年级下.txt',
         '小学英语/六年级上.txt',
         '小学英语/六年级下.txt']
words_list = []


class MainFace:
    def __init__(self):
        self.create_widget()

    def create_widget(self):
        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame, text='开心背单词', font=(None, 32)).pack(pady=10)
        frame1 = tk.Frame(self.frame)
        frame1.pack(padx=20, pady=20, side=tk.LEFT)
        self.v = tk.IntVar()
        for i in range(len(files)):
            tk.Radiobutton(frame1, text=files[i][0:-4], variable=self.v, value=i, font=(None, 18)).pack()
        frame2 = tk.Frame(self.frame)
        frame2.pack(padx=20, pady=20, side=tk.RIGHT)
        tk.Button(frame2, text='开始背诵', command=self.goto_study_face, font=(None, 18)).pack(pady=30)
        tk.Button(frame2, text='开始测试', command=self.goto_test_face, font=(None, 18)).pack(pady=30)

    def goto_study_face(self):
        self.readfile()
        self.frame.destroy()
        StudyFace()

    def goto_test_face(self):
        self.readfile()
        self.frame.destroy()
        TestFace()

    def readfile(self):
        words_list.clear()
        filename = files[self.v.get()]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    word = line.strip().split()  # 假设每行单词格式为 单词 音标 中文
                    if len(word) == 3:
                        words_list.append(word)
        except FileNotFoundError:
            tkinter.messagebox.showerror('错误', f'文件 {filename} 未找到')


class StudyFace:
    def __init__(self):
        self.word_eg = tk.StringVar()
        self.word_ch = tk.StringVar()
        self.word_pronounce = tk.StringVar()
        self.create_widget()
        self.new_word()

    def create_widget(self):
        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame, text="背单词", font=(None, 32)).pack(pady=20)
        frame1 = tk.Frame(self.frame)
        frame1.pack()
        tk.Label(frame1, textvariable=self.word_eg, font=(None, 40)).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(frame1, textvariable=self.word_pronounce, font=(None, 12)).grid(row=1, column=0)
        tk.Label(frame1, textvariable=self.word_ch, font=(None, 24)).grid(row=2, column=0, padx=10, pady=10)
        frame2 = tk.Frame(self.frame)
        frame2.pack()
        tk.Button(frame2, text="知道", command=self.know, font=(None, 18), width=6).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(frame2, text="不知道", command=self.dont_know, font=(None, 18), width=6).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="返回", command=self.back, font=(None, 18)).pack()

    def new_word(self):
        if words_list:
            self.word = random.choice(words_list)  # 从字典中选出一个单词
            self.word_eg.set(self.word[0])
            self.word_pronounce.set(self.word[1])
            self.word_ch.set("")
        else:
            tkinter.messagebox.showinfo('提示', '已完成')

    def know(self):
        self.word_ch.set(self.word[2])
        words_list.remove(self.word)
        self.frame.after(2000, self.new_word)

    def dont_know(self):
        self.word_ch.set(self.word[2])
        self.frame.after(2000, self.new_word)

    def back(self):
        self.frame.destroy()
        MainFace()


class TestFace:
    def __init__(self):
        self.word_eg = tk.StringVar()
        self.word_sound = tk.StringVar()
        self.word_ch_0 = tk.StringVar()
        self.word_ch_1 = tk.StringVar()
        self.word_ch_2 = tk.StringVar()
        self.word_ch_3 = tk.StringVar()
        self.count = 0  # 背单词计数
        random.shuffle(words_list)
        self.create_widget()
        self.new_word()

    def create_widget(self):
        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame, text="单词测试", font=(None, 32)).pack()
        frame1 = tk.Frame(self.frame)
        frame1.pack()
        tk.Label(frame1, textvariable=self.word_eg, font=(None, 40)).grid(row=0, column=0)
        tk.Label(frame1, textvariable=self.word_sound, font=(None, 12)).grid(row=1, column=0)
        frame2 = tk.Frame(self.frame)
        frame2.pack()
        self.v = tk.IntVar()
        tk.Radiobutton(frame2, variable=self.v, value=0, textvariable=self.word_ch_0, font=(None, 18)).grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
        tk.Radiobutton(frame2, variable=self.v, value=1, textvariable=self.word_ch_1, font=(None, 18)).grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
        tk.Radiobutton(frame2, variable=self.v, value=2, textvariable=self.word_ch_2, font=(None, 18)).grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)
        tk.Radiobutton(frame2, variable=self.v, value=3, textvariable=self.word_ch_3, font=(None, 18)).grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)
        frame3 = tk.Frame(self.frame)
        frame3.pack()
        tk.Button(frame3, text="返回", command=self.back, font=(None, 22)).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(frame3, text="确定", command=self.check, font=(None, 22)).grid(row=0, column=0, padx=10, pady=10)

    def new_word(self):
        if self.count >= len(words_list):
            tkinter.messagebox.showinfo('提示', '测试已结束')
            self.back()
        else:
            self.v.set(-1)
            word = words_list.pop(0)
            words = random.sample(words_list, 3)
            self.index = random.randint(0, 3)
            words.insert(self.index, word)
            self.word_eg.set(word[0])
            self.word_sound.set(word[1])
            self.word_ch_0.set(words[0][2])
            self.word_ch_1.set(words[1][2])
            self.word_ch_2.set(words[2][2])
            self.word_ch_3.set(words[3][2])
            words_list.append(word)
            self.count += 1

    def check(self):
        if 0 <= self.v.get() <= 3:
            if self.index == self.v.get():
                tkinter.messagebox.showinfo('结果', '正确')
            else:
                tkinter.messagebox.showinfo('结果', '错误')
            self.new_word()

    def back(self):
        self.frame.destroy()
        MainFace()


root = tk.Tk()
root.title('开心背单词')
root.geometry('600x400')
MainFace()
root.mainloop()
