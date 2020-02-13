from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os
import time
import threading
from threading import Timer
import shutil
import progressbar

def selectPath1():
    path_1 = askdirectory()
    path1.set(path_1)

def selectPath2():
    path_2 = askdirectory()
    path2.set(path_2)

def selectPath3():
    path_3 = askdirectory()
    path3.set(path_3)

def selectPath4():
    path_4 = askdirectory()
    path4.set(path_4)

def selectPath_goal():
    path_g = askdirectory()
    path_goal.set(path_g)

def showTime():
    while True:
        showc_time.set(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        windows.update
        time.sleep(1)

def programEnd():
    global signal_e
    global count_thread
    if signal_e == count_thread:
        signal_e = 0
        count_thread = 0
        p1.stop()
        text_show.delete(1.0,END)
        windows.update
        tkinter.messagebox.showinfo('Python Message Info Box', '迁移完成！')
        return
    else:
        time.sleep(1)
    t_programEnd=Timer(1,programEnd())
   
def startProgram():
    global signal
    if signal != 0:
        tkinter.messagebox.showinfo('Python Message Info Box', '程序正在运行中！')
        return
    if path1.get() != "":
        i=1
        thread1=threading.Thread(target=moveFile,
                                 args=(path1.get(),
                                       path_goal.get(),i,)
                                 )
        thread1.start()
    else:
        pass
    if path2.get() != "":
        i=2
        thread2=threading.Thread(target=moveFile,
                                 args=(path2.get(),
                                       path_goal.get(),i,)
                                 )
        thread2.start()
    else:
        pass
    if path3.get() != "":
        i=3
        thread3=threading.Thread(target=moveFile,
                                 args=(path3.get(),
                                       path_goal.get(),i,)
                                 )
        thread3.start()
    else:
        pass
    if path4.get() != "":
        i=4
        thread4=threading.Thread(target=moveFile,
                                 args=(path4.get(),
                                       path_goal.get(),i,)
                                 )
        thread4.start()
    else:
        pass
    p1.start(30)
    threadE=threading.Thread(target=programEnd)
    threadE.start()
    
def moveFile(path_send,path_gsend,j):
    global count_thread
    count_thread +=1
    global signal
    signal+=1
    filedir=path_send
    filedirg=path_gsend
    global text_show
    text_show.insert(1.0,"线程%d 拷贝开始\n"%j)
    windows.update
    netcondition=True
    for roots, dirs, filenames in os.walk(filedir):
        for filename in filenames:
            old_address=os.path.join(roots,filename)
            fpath,fname=os.path.split(old_address)
            abs_path=fpath[len(filedir)+1:]
            if "/" in old_address:
                cc=filedir[filedir.rfind("/")+1:]
            else:
                cc=filedir[filedir.rfind("\\")+1:]
            new_address=os.path.join(filedirg,cc,abs_path)
            if "RAW_IMAGE" in old_address or ".csv" in old_address:
                if os.path.exists(new_address):
                    while netcondition == True:
                        try:
                            shutil.copy(old_address,new_address)
                            os.remove(old_address)
                            break
                        except OSError:
                            time.sleep(1)
                            text_show.insert(1.0,"等待网络恢复 %s\n"%fname)
                            windows.update
                    text_show.insert(1.0,"拷贝 %s\n"%fname)
                    windows.update
                else:
                    while netcondition == True:
                        try:
                            os.makedirs(new_address)
                            shutil.copy(old_address,new_address)
                            os.remove(old_address)
                            break
                        except OSError:
                            time.sleep(1)
                            text_show.insert(1.0,"等待网络恢复 %s\n"%fname)
                            windows.update
                    text_show.insert(1.0,"拷贝 %s\n"%fname)
                    windows.update
            else:
                while netcondition == True:
                    try:
                        os.remove(old_address)
                        break
                    except OSError:
                        time.sleep(1)
                        text_show.insert(1.0,"等待网络恢复 %s\n"%fname)
                        windows.update
                text_show.insert(1.0,"删除 %s\n"%fname)
                windows.update
    text_show.insert(1.0,"线程%d 拷贝完成\n"%j)
    windows.update
    global signal_e
    signal_e += 1
    signal -= 1

def main():
    global path1
    path1 = StringVar()
    global path2
    path2 = StringVar()
    global path3
    path3 = StringVar()
    global path4
    path4 = StringVar()
    global path_goal
    path_goal = StringVar()
    global words
    words = StringVar()
    style1 = ttk.Style()
    style1.configure("C.TButton", 
                     relief="flat",
                     background="#33CCFF"
                     )
    style1.map("C.TButton",
        foreground=[('pressed', 'red'),('active', 'blue')],
        background=[('pressed', '!disabled', 'blue'), ('active', 'white')]
        )
    style2 = ttk.Style()
    style2.configure("D.TButton", 
                     relief="flat",
                     background="#66FF00"
                     )
    style2.map("D.TButton",
        foreground=[('pressed', '#66FF00'),('active', '#00CC00')],
        background=[('pressed', '!disabled', '#66FF00'), ('active', 'white')]
        )
    style3 = ttk.Style()
    style3.configure("E.TButton", 
                     relief="flat",
                     background="#FFFF00"
                     )
    style3.map("E.TButton",
        foreground=[('pressed', 'yellow'),('active', 'orange')],
        background=[('pressed', '!disabled', 'orange'), ('active', 'white')]
        )
    Label(windows,
          text = "文件夹路径1:",
          font=('Calibri', 12)
          ).grid(row=0, 
                 column=0, 
                 padx=10,
                 pady=5
                 )
    Entry(windows,
         textvariable = path1,
         font=('Calibri', 12)
         ).grid(row=0, 
                column=1,
                padx=0,
                pady=5
                )
    ttk.Button(windows, 
               text = "路径选择",
               command = selectPath1,
               style="C.TButton"
               ).grid(row=0,
                      column=2,
                      padx=10,
                      pady=5
                      )
    Label(windows,
          text = "文件夹路径2:",
          font=('Calibri', 12)
          ).grid(row=1, 
                 column=0, 
                 padx=10,
                 pady=5
                 )
    Entry(windows,
          textvariable = path2,
          font=('Calibri', 12)
          ).grid(row=1, 
                 column=1,
                 padx=0,
                 pady=5
                 )
    ttk.Button(windows, 
               text = "路径选择",
               command = selectPath2,
               style="C.TButton"
               ).grid(row=1,
                      column=2,
                      padx=10,
                      pady=5
                      )
    Label(windows,
          text = "文件夹路径3:",
          font=('Calibri', 12)
          ).grid(row=2, 
                 column=0,
                 padx=10,
                 pady=5
                 )
    Entry(windows, 
          textvariable = path3,
          font=('Calibri', 12)
          ).grid(row=2, 
                 column=1,
                 padx=0,
                 pady=5
                 )
    ttk.Button(windows, 
               text = "路径选择",
               command = selectPath3,
               style="C.TButton"
               ).grid(row=2,
                      column=2,
                      padx=10,
                      pady=5
                      )
    Label(windows,
          text = "文件夹路径4:",
          font=('Calibri', 12)
          ).grid(row=3, 
                 column=0,
                 padx=0,
                 pady=5
                 )
    Entry(windows, 
          textvariable = path4,
          font=('Calibri', 12)
          ).grid(row=3, 
                 column=1,
                 padx=0,
                 pady=5
                 )
    ttk.Button(windows, 
               text = "路径选择",
               command = selectPath4,
               style="C.TButton"
               ).grid(row=3,
                      column=2,
                      padx=10,
                      pady=5
                      )
    Label(windows,
          text = "目标路径:",
          font=('Calibri', 12)
          ).grid(row=4, 
                 column=0, 
                 padx=10,
                 pady=5
                 )
    Entry(windows, 
          textvariable = path_goal,
          font=('Calibri', 12)
          ).grid(row=4, 
                 column=1,
                 padx=0,
                 pady=5
                 )
    ttk.Button(windows, 
               text = "路径选择",
               command = selectPath_goal,
               style="E.TButton"
               ).grid(row=4,
                      column=2,
                      padx=10,
                      pady=5
                      )
    global p1
    p1=ttk.Progressbar(windows,
                       length=360,
                       mode="indeterminate",
                       maximum=360,
                       orient=HORIZONTAL
                       )
    p1.grid(row=3,
            column=3,
            columnspan=3,
            padx=10,
            pady=5
            )
    global showc_time
    showc_time=StringVar()
    Label(windows,
          textvariable = showc_time,
          font=('Calibri', 12)
          ).grid(row=4, 
                 column=4, 
                 columnspan=2,
                 padx=10,
                 pady=5
                 )
    ttk.Button(windows, 
               text = "开始迁移",
               command = startProgram,
               style="D.TButton"
               ).grid(row=4, 
                      column=3,
                      padx=10,
                      pady=5
                      )
    global text_show
    text_show = Text(windows,
                height=6.5,
                width=45
                )
    text_show.grid(row=0,
                   rowspan=3,
                   column=3,
                   columnspan=3,
                   padx=10,
                   pady=5)

if __name__ == '__main__':
    windows= Tk()
    windows.title('转移文件v1.0')
    windows.geometry('790x215')
    main()
    signal = 0
    signal_e=0
    count_thread=0
    thread_time=threading.Thread(target=showTime)
    thread_time.start()
    windows.mainloop()
    

