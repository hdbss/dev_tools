import fitz
import os
import tkinter


def pyMuPDF_fitz(pdfPath, imagePath, img_type='jpg'):
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


def PdfGui():
    window = tkinter.Tk()
    window.title('Pdf转图片')
    window.geometry('700x400')
    frame_radio = tkinter.Frame(window, height=6)
    frame_radio.grid(row=5, column=1, ipadx=50, ipady=10, padx=20)
    img_type = tkinter.IntVar()
    img_type.set('jpg')
    img_types = [('jpg', 'jpg'), ('png', 'png'), ('jpeg', 'jpeg'), ('tiff', 'tiff'), ('gif', 'gif')]
    for text, value in img_types:
        radio = tkinter.Radiobutton(frame_radio, text=text, value=value, variable=img_type)
        print(img_types.index((text, value)))
        column = img_types.index((text, value))
        radio.grid(row=0, column=column)
    label1 = tkinter.Label(window, text='输入pdf路径:')
    label2 = tkinter.Label(window, text='输入img路径:')
    label1.grid(row=7, column=0)
    label2.grid(row=8, column=0)
    text1 = tkinter.Entry(window, show=None, width=40, borderwidth=2)
    text2 = tkinter.Entry(window, show=None, width=40, borderwidth=2)
    text1.grid(row=7, column=1, pady=2)
    text2.grid(row=8, column=1)
    button1 = tkinter.Button(window, text='确定', command=lambda: pyMuPDF_fitz(text1.get(), text2.get()))
    button1.grid(column=1)
    text3 = tkinter.Text(window)
    text3.grid(row=10)
    text3.insert('insert', '123')
    window.mainloop()

PdfGui()


# if __name__ == "__main__":
#     type_all = ['jpeg', 'jpg', 'tiff', 'gif', 'png', '']
#     img_type = input('输入图片类型(jpg,png?):')
#     while img_type not in type_all:
#         print('图片格式不存在,需重新输入')
#         img_type = input('输入图片类型(jpg,png?):')
#     while True:
#         pdfpath = input('输入pdf路径:')
#         imgpath = input('输入img路径:')
#         if not os.path.exists(pdfpath):
#             print('不存在pdf路径:{}'.format(pdfpath))
#             continue
#         elif not os.path.exists(imgpath):
#             print('不存在此图片路径:{}，需手动创建'.format(imgpath))
#         else:
#             pyMuPDF_fitz(pdfpath, imgpath, img_type)
#             print('成功')

# C:\Users\admin\Desktop\标定图片\pdf\个人独资企业变更登记1\11310118342309462Y331010071700402_496_tpl_1636529634992.pdf
# C:\Users\admin\Desktop\标定图片\test_covfpdf