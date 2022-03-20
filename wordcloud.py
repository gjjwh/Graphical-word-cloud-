import tkinter as tk
from wordcloud import WordCloud
import numpy as np
from PIL import Image
# 实例化一个窗口对象



def pt():
    global window


window = tk.Tk()
window.geometry('500x100')
window.title('普通')

baoc = tk.Label(window, text='请输入您要创建的内容')
baoc.pack()
# 实例化一个输入框
e = tk.Entry(window, width=50, show=None)  # show='*'密文
e.pack()

baoc = tk.Label(
    window, text='如要更改字体，请将字体文件改名为：simhei.ttf；放进根目录的wordcloud文件夹里').pack()


# 实例化一个文本框


def insert_point():
    var = e.get()  # 输入框中得到var

    with open("word.txt", "w") as f:
        f.write(var)
    with open('word.txt') as fp:
        text = fp.read()
        mk = np.array(Image.open("地图map.jpg"))
        wordcloud = WordCloud(mask=mk, max_font_size=100,background_color="white",font_path = "simhei.ttf").generate(text)
        image_produce = wordcloud.to_image()
        image_produce.show()



b1 = tk.Button(window, text='确定', width=15, height=2,
               command=insert_point)
b1.pack()


window.mainloop()  # 循环显示
