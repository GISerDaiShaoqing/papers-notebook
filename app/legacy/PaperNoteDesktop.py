# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:24:08 2018

@author: GIS-Watcher
"""

import Tkinter as tk
from tkinter import *
from tkFileDialog import askopenfilename
import tkFileDialog
import webbrowser
import markdown
import sys
import subprocess

reload(sys)
sys.setdefaultencoding("utf-8")

# 程序名
window = tk.Tk()
window.title('GitHub Paper Notebook')
window.geometry('1080x720')
window.iconbitmap('gnb.ico')

# 支付宝支付码
alipayimg = tk.PhotoImage(file = 'alipay.gif')

# 设置功能菜单
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = '功能菜单', menu = filemenu)


# 菜单栏
def open_baidupan():
    webbrowser.open('https://pan.baidu.com/share/home?uk=2855623577&suk=QR0keGnZkZWNh9Pf3aQyaQ&view=share#category/type=0')

def open_scihubdesktop():
    webbrowser.open('https://zhuanlan.zhihu.com/p/31809890')
    
def open_luwen():
    webbrowser.open('https://lunwen.im/')

def open_labxing():
    webbrowser.open('https://www.labxing.com/paper')
    
filemenu.add_command(label = '百度网盘下载链接', command = open_baidupan)
filemenu.add_command(label = 'sci-hub desktop官网', command = open_scihubdesktop)
filemenu.add_command(label = '喵咪论文下载平台', command = open_luwen)
filemenu.add_command(label = 'Labxing Paper', command = open_labxing)

filemenu.add_separator()

def open_notebook():
    webbrowser.open('https://github.com/GISerDaiShaoqing/papers-notebook')

def open_baiduwenku():
    webbrowser.open('http://wenku.bemfa.com/')
    
def open_doiorg():
    webbrowser.open('https://doi.org/')

filemenu.add_command(label = 'doi网站', command = open_doiorg)
filemenu.add_command(label = '我的阅读笔记', command = open_notebook)
filemenu.add_command(label = '免费下载百度文库', command = open_baiduwenku)
filemenu.add_separator()

# 关闭程序
filemenu.add_command(label = '退出', command = window.quit)

frameshow = tk.LabelFrame(window, height = 340, width = 1040, text = '笔记显示').place(x = 20, y = 20)

#markdown编辑区
markdownshow = tk.Text(frameshow, height = 22, width = 130)
markdownshow.place(x = 40, y =40)

#设置滚动条
mdsv = tk.Scrollbar(frameshow, orient=tk.VERTICAL)
mdsv.place(x = 792,y = 40,width = 180, height = 285)
mdsv.config(command = markdownshow.yview)

#设置功能
#打开显示markdown源
def open_file():
    fname = tkFileDialog.askopenfilename(filetypes=[('Markdown文件', '*.md *.markdown')])
    fmd = open(fname)
    ftext = fmd.read()
    markdownshow.insert('end', ftext)

#存储markdown文件
def save_file():
    mdname = tkFileDialog.asksaveasfilename(filetypes=[('Markdown文件', '*.md *.markdown')])
    mdf = open(mdname, 'w+')
    mdcontent = markdownshow.get(0.0, tk.END)
    mdf.write(mdcontent)     
    mdf.close()
    
#清除显示的markdown文件
def clear_file():
    markdownshow.delete(0.0, tk.END)

#将显示的markdown转换为html文件
def transform():
    mdname = tkFileDialog.asksaveasfilename(filetypes=[('html文件', '*.html')])
    mdf = open(mdname, 'a')
    mdcontent = markdownshow.get(0.0, tk.END)
    mdhtml = markdown.markdown(mdcontent)
    mdf.write(mdhtml)
    mdf.close()

#打开VS code IDE    
def code_open():
    fname = tkFileDialog.askopenfilename(filetypes=[('Microsoft Visual Studio Code软件', '*.exe')])
    subprocess.call(fname)
    
openbutton = tk.Button(frameshow, text = '打开', width = 8, height = 2, command = open_file).place(x = 985, y = 40)
clearbutton = tk.Button(frameshow, text = '清除', width = 8, height = 2, command = clear_file).place(x = 985, y = 100)
savebutton = tk.Button(frameshow, text = '保存', width = 8, height = 2, command = save_file).place(x = 985, y = 160)
transbutton = tk.Button(frameshow, text = '转换', width = 8, height = 2, command = transform).place(x = 985, y = 220)
codebutton = tk.Button(frameshow, text = 'VS Code', width = 8, height = 2, command = code_open).place(x = 985, y = 280)
#openbutton = tk.Button(frameshow, text = '打开', width = 8, height = 2, command = open_file).place(x = 985, y = 40)
#clearbutton = tk.Button(frameshow, text = '清除', width = 8, height = 2, command = clear_file).place(x = 985, y = 90)
#savebutton = tk.Button(frameshow, text = '保存', width = 8, height = 2, command = save_file).place(x = 985, y = 140)
#selectbutton = tk.Button(frameshow, text = '全选', width = 8, height = 2, command = select_all).place(x = 985, y = 190)
#transbutton = tk.Button(frameshow, text = '转换', width = 8, height = 2, command = transform).place(x = 985, y = 240)
#codebutton = tk.Button(frameshow, text = 'VS Code', width = 8, height = 2, command = code_open).place(x = 985, y = 290)

#添加文章样例
framepaper = tk.LabelFrame(window, height = 330, width = 1040, text = '添加文章').place(x = 20, y = 360)

#文章输入框
paperinputbox = tk.Text(framepaper, height = 22, width = 35)
paperinputbox.place(x = 120, y =380)
inputboxlabel = tk.Label(framepaper, text = '论文题目').place(x = 40, y = 500)

#模板生成
paperoutputbox = tk.Text(framepaper, height = 22, width = 35)
paperoutputbox.place(x = 490, y =380)

#滚动条
outsv = tk.Scrollbar(framepaper, orient=tk.VERTICAL)
outsv.place(x = 578,y = 380,width = 180, height = 285)
outsv.config(command = paperoutputbox.yview)

#ghtoc目录生成
tocbox = tk.Text(framepaper, height = 22, width = 35)
tocbox.place(x = 780, y =380)

#滚动条
tocsv = tk.Scrollbar(framepaper, orient=tk.VERTICAL)
tocsv.place(x = 870,y = 380,width = 180, height = 285)
tocsv.config(command = tocbox.yview)


#添加文章按钮
def add_temple():
    paperoutputbox.delete(0.0, tk.END)
    title = paperinputbox.get(0.0, tk.END)
    text = "**Title:** " + str(title) + "\n\n**Link:** [原文链接]()\n\n**Doi:** \n\n**Notes:** \n\n**Hightlights:** \n\n**Research gap/question:** \n\n**Discussion/Conclusion** \n\n**Graph/Table interested:** \n\n**Resources:**"
    paperoutputbox.insert('end', text)

def add_picture():
    picurl = "![](https://github.com/GISerDaiShaoqing/papers-notebook/blob/master/Picture/.png)"
    paperoutputbox.insert('insert', picurl)

def select_ghmdtocexe():
    global gotocexename
    gotocexename = tkFileDialog.askopenfilename(filetypes=[('gh-md-toc.exe文件', '*.exe')])

def open_readme():
    global readmename    
    readmename = tkFileDialog.askopenfilename(filetypes=[('Markdown文件', '*.md *.markdown')])
    
def generate_toc(): 
    item = str(gotocexename) + ' ' + str(readmename.split('/')[-1])
    toc = subprocess.check_output(item)
    tocbox.insert('end', toc)
    
paperbutton = tk.Button(framepaper, text = '添加模板', width = 12, height = 2, command = add_temple).place(x = 380, y = 380)
picturebutton = tk.Button(framepaper, text = '添加图片', width = 12, height = 2, command = add_picture).place(x = 380, y = 440)
gocselectbutton = tk.Button(framepaper, text = '选择exe', width = 12, height = 2, command = select_ghmdtocexe).place(x = 380, y = 500)
MDselectbutton = tk.Button(framepaper, text = '选择文件', width = 12, height = 2, command = open_readme).place(x = 380, y = 560)
TOCbutton = tk.Button(framepaper, text = '生成目录', width = 12, height = 2, command = generate_toc).place(x = 380, y = 620)

# 作者的博客
def open_blog():
    webbrowser.open('https://giserdaishaoqing.github.io')
    
menubar.add_command(label = '作者博客', command = open_blog)

# 软件说明
def open_about():
    tl = tk.Toplevel()
    tl.title('关于软件')
    tl.geometry('340x80')
    msg = tk.Message(tl, text = 'Version 1.0\nCopyright© Dai <dsq1993qingge@163.com> 2018\n利用Github记录论文阅读笔记\nUpdate at: 2018/08/27\n', width = 1000)
    msg.pack(expand = YES)
    
menubar.add_command(label = '关于软件', command = open_about)

# 打赏
def open_donate():
    td = tk.Toplevel()
    td.title('打赏')
    td.geometry('320x320')
    alipay = tk.Label(td, image = alipayimg)
    alipay.pack()
    textdonate = tk.Label(td, text = '您的支持是对软件开发者最大的鼓励！')
    textdonate.pack()
    
menubar.add_command(label = '打赏', command = open_donate)

window.config(menu=menubar)
window.mainloop()