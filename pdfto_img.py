import fitz
import os
import tkinter


def pyMuPDF_fitz(pdfPath, imagePath, img_type='jpg'):
    """
    :param pdfPath: pdf绝对路径
    :param imagePath: 转化为图片的目录-绝对路径
    :param img_type: 图片类型，默认jpg
    """
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=72
        zoom_x = 5  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 5
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.save(imagePath + '/' + 'images_%s.%s' % (pg, img_type))  # 将图片写入指定的文件夹内


def covert_format(pdfPath, imagePath, img_format, text3):
    try:
        pyMuPDF_fitz(pdfPath, imagePath, img_format)
        text3.delete(1.0, tkinter.END)
        text3.insert('insert', '成功')
        # text.insert(index,string)  index = x.y的形式,x表示行，y表示列
        print('成功')
    except:
        print('失败，请重新再来')
        text3.delete(1.0, tkinter.END)
        text3.insert('insert', '失败，请重新再来')

def PdfGui():
    window = tkinter.Tk()
    window.title('Pdf转图片')
    window.geometry('700x400')

    # 单选框框架
    frame_radio = tkinter.Frame(window, height=6)
    frame_radio.grid(row=5, column=0, ipadx=50, ipady=10, padx=20)
    img_type = tkinter.StringVar()
    img_type.set('jpg')
    img_types = [('jpg', 'jpg'), ('png', 'png'), ('jpeg', 'jpeg'), ('tiff', 'tiff'), ('gif', 'gif')]
    for text, value in img_types:
        radio = tkinter.Radiobutton(frame_radio, text=text, value=value, variable=img_type)
        column = img_types.index((text, value))
        radio.grid(row=0, column=column)
    # 单选框结束

    # 输入框框架
    frame_label = tkinter.Frame(window)
    frame_label.grid(row=7, column=0, ipadx=50, ipady=10, padx=20)
    label1 = tkinter.Label(frame_label, text='输入pdf路径:', font=(None, 16))  # width,height,bg
    label2 = tkinter.Label(frame_label, text='输入img路径:', font=(None, 16))
    label1.grid(row=7, column=0, sticky=tkinter.SE)
    label2.grid(row=8, column=0, sticky=tkinter.SE)
    text1 = tkinter.Entry(frame_label, show=None, width=55, borderwidth=2, relief=tkinter.GROOVE, bd=2)
    # bd边框  relief边框格式  width框长度
    text2 = tkinter.Entry(frame_label, show=None, width=55, borderwidth=2, relief=tkinter.GROOVE, bd=2)
    text1.grid(row=7, column=1, pady=2, ipadx=3, ipady=2)
    # row，column行列  padx，pady框外样式内  ipadx，ipady框内
    text2.grid(row=8, column=1, pady=2, ipadx=3, ipady=2)
    button1 = tkinter.Button(frame_label, text='确定', font=(None, 19),
                             command=lambda: covert_format(text1.get(), text2.get(), img_type.get(), text3))
    button1.grid(column=1)
    # 输入框结束

    text3 = tkinter.Text(window, height=2)
    text3.grid()
    window.mainloop()


PdfGui()


# C:\Users\admin\Desktop\标定图片\pdf\个人独资企业变更登记1\11310118342309462Y331010071700402_496_tpl_1636529634992.pdf
# C:\Users\admin\Desktop\标定图片\test_covfpdf