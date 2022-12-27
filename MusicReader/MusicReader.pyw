import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem,QHeaderView,QAbstractItemView
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QPoint
from PyQt5.Qt import QUrl
from PyQt5.QtGui import QMovie,QIcon,QPixmap,QMouseEvent
from threading import Thread
from time import sleep,time
from pyjavaget import Weber
from requests import get
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from win10toast import ToastNotifier


class mainwindow(Ui_MainWindow.Ui_MainWindow,QMainWindow):
    def __init__(self):
        self.index=None
        self.maxindex=None
        self.gosonglong=[0,0]
        self.maxsonglong=[0,0]
        self.engine="netease"
        self.enginelist=["netease","qq","kugou","kuwo"]
        super().__init__()
        self.setupUi(self)
        self._initUI()
        self.setstyle()
        

    def _initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.changepaper(0)

    def setstyle(self):
        self.setWindowTitle("musicreader") 
        self.setWindowIcon(QIcon('musicreader/icons.ico'))

        ####################################设置背景
        self.setStyleSheet("#MainWindow{background-color:#171718}")
        ####################################

        ####################################
        # 初始化模式图片
        pixmap = QPixmap("musicreader/netease.png") 
        self.logo.setPixmap(pixmap)  # 在label上显示图片
        self.logo.setScaledContents (True)  # 让图片自适应label大小
        ####################################

        ####################################模式切换按钮设置
        self.firstbuttom.setStyleSheet('''QPushButton{background:#1e1e1f;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')        
        self.firstbuttom.clicked.connect(self.changenetease)
        self.secondbutton.setStyleSheet('''QPushButton{background:#1e1e1f;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')
        self.secondbutton.clicked.connect(self.changeqq)
        self.secondbutton.setEnabled(False) ## 禁用
        self.thirdbuttom.setStyleSheet('''QPushButton{background:#1e1e1f;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')
        self.thirdbuttom.clicked.connect(self.changekugou)
        self.forthbuttom.setStyleSheet('''QPushButton{background:#1e1e1f;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')
        self.forthbuttom.clicked.connect(self.changekuwo)
        self.frithbuttom.setStyleSheet('''QPushButton{background:#1e1e1f;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')
        self.frithbuttom.setEnabled(False) ## 禁用
        ####################################

         ####################################
        #waitpage
        self.gif = QMovie('localfile/waiting.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        ####################################
        
        ####################################
        #mainpage
        pixmap = QPixmap("musicreader/logo.png")  # 按指定路径找到图片
        self.mainlogo.setPixmap(pixmap)  # 在label上显示图片
        self.mainlogo.setScaledContents (True)  # 让图片自适应label大小
        self.mainsearch.returnPressed.connect(self.mainsearchdo)##绑定回车
        ####################################

        #音乐列表样式
        ####################################
        self.tableWidget.setStyleSheet("QTableWidget::item:selected{ background-color:#1e1e1f;color:#1eb085}QTableWidget{font-family:'微软雅黑';font-size:20px;color:rgb(255,255,255,255);background:#171718;border:0px}")
        self.tableWidget.setColumnCount(2)#设置列成员
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)#设置表格的选取方式是行选取
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)#设置单行选取
        self.tableWidget.clicked.connect(self.changemaininfo)
        self.getmusic.setStyleSheet('''QPushButton{background:#1fd2a9;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')
        self.getmusic.clicked.connect(self.downmainmusic)
        self.return1.setStyleSheet('''QPushButton{background:#1fd2a9;border-radius:5px;}QPushButton:hover{background:#1ece9c;}QPushButton{font-family:'微软雅黑';font-size:25px;color:rgb(255,255,255,255);}''')
        self.return1.clicked.connect(self.returnmain)
        ####################################
        #音乐控制控件
        # 将各个子页面添加到对应控件form
        # 在stackedWidget添加子控件form 
        self.Playersongname.setStyleSheet('''font-family:'微软雅黑';font-size:20px;color:rgb(255,255,255,255);background:#171718;''')
        self.maxtime.setStyleSheet('''font-family:'微软雅黑';font-size:20px;color:rgb(255,255,255,255);background:#171718;''')
        self.runnedtime.setStyleSheet('''font-family:'微软雅黑';font-size:20px;color:rgb(255,255,255,255);background:#171718;''')
        self.OnandOff.setStyleSheet('''background:#1eb085;border-style:none;border:1px solid #3f3f3f; padding:5px;min-height:20px;border-radius:15px;border:0px''')
        self.OnandOff.setIcon(QIcon('musicreader/play.png'))
        self.OnandOff.clicked.connect(self.changeonandoff)
        self.lastmusic.setStyleSheet('''background:#1eb085;border-style:none;border:1px solid #3f3f3f; padding:5px;min-height:20px;border-radius:15px;border:0px''')
        self.lastmusic.setIcon(QIcon('musicreader/previous.png'))
        self.lastmusic.clicked.connect(self.lastsong)
        self.nextmusic.setStyleSheet('''background:#1eb085;border-style:none;border:1px solid #3f3f3f; padding:5px;min-height:20px;border-radius:15px;border:0px''')
        self.nextmusic.setIcon(QIcon('musicreader/next.png'))
        self.nextmusic.clicked.connect(self.nextsong)
        self.musicplayers()
        # self.setMusic()
        ####################################
        self.shutdownwindows1.setStyleSheet("background:#171718;border-radius:0px;")
        self.shutdownwindows2.setStyleSheet("background:#171718;border-radius:0px;")
        self.shutdownwindows1.clicked.connect(self.shutdown)
        self.shutdownwindows2.clicked.connect(self.shutdown)

    ##########################################################################
    #案件绑定
    def nextsong(self):#下一曲绑定事件
        if (self.index==None):
            pass
        elif (self.index+1 < self.maxindex):
            self.index+=1
            self.tableWidget.selectRow(self.index)
            self.mainsonginfo=self.pc.clickli(self.index)
            self.setmusicinfo(self.mainsonginfo)
        else:
            pass
    
    def lastsong(self):#上一曲绑定事件
        if (self.index==None):
            pass
        elif (self.index-1 >= 0):
            self.index-=1
            self.tableWidget.selectRow(self.index)
            self.mainsonginfo=self.pc.clickli(self.index)
            self.setmusicinfo(self.mainsonginfo)
        else:
            pass        

    def returnmain(self):#返回按钮绑定
        self.changepaper(0)

    def shutdown(self):#关闭窗口
        self.showMinimized()
        sys.exit(0)

    def changekuwo(self):#酷我音乐搜索模式的函数
        self.engine=self.enginelist[3]
        pixmap = QPixmap("musicreader/"+self.engine+".png")  # 按指定路径找到图片
        self.logo.setPixmap(pixmap)  # 在label上显示图片
        print(self.engine)
    def changekugou(self):#酷狗音乐搜索模式的函数
        self.engine=self.enginelist[2]
        pixmap = QPixmap("musicreader/"+self.engine+".png")  # 按指定路径找到图片
        self.logo.setPixmap(pixmap)  # 在label上显示图片
        print(self.engine)
    def changeqq(self):#qq音乐搜索模式的函数
        self.engine=self.enginelist[1]
        pixmap = QPixmap("musicreader/"+self.engine+".png")  # 按指定路径找到图片
        self.logo.setPixmap(pixmap)  # 在label上显示图片
        print(self.engine)
    def changenetease(self):#网易云音乐搜索模式的函数
        self.engine=self.enginelist[0]
        pixmap = QPixmap("musicreader/"+self.engine+".png")  # 按指定路径找到图片
        self.logo.setPixmap(pixmap)  # 在label上显示图片
        print(self.engine)

    def mainsearchdo(self):#初始页面的搜索函数
        t=Thread(target=self.pychrome)
        t.start()

    def pychrome(self  ):#搜索绑定函数
        self.changepaper(1)
        self.pc=Weber()
        self.pc.toget(r'https://music.haom.ren/?name={name}&type={model}'.format(name=self.mainsearch.text().replace("\n",""),model=self.engine))
        songinfo=self.pc.getmain()
        # songinfo[0]
        data=get(songinfo[0])
        with open("localfile/mainsongpic.jpg","wb") as w:
            w.write(data.content)
        pixmap = QPixmap('localfile/mainsongpic.jpg')  # 按指定路径找到图片
        self.mainimage.setPixmap(pixmap)
        songlist=self.pc.togetall()
        self.mainsonginfo=self.pc.getmain()
        self.setMusic(self.mainsonginfo[2])
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏列名
        self.tableWidget.verticalHeader().setVisible(False)#隐藏行名
        self.tableWidget.setRowCount(len(songlist)/2)#添加行
        self.maxindex=int(len(songlist)/2)
        for value in range(0,len(songlist)):
            item_id = QTableWidgetItem(songlist[value])
            item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)# 设置物件的状态为只可被选择（默认可编辑）
            self.tableWidget.setItem(value//2,value%2, item_id)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.selectRow(0)
        self.changepaper(2)
        self.changemaininfo()

    def changemaininfo(self):#设置当前播放歌曲的信息
        self.index=self.tableWidget.currentRow()
        self.mainsonginfo=self.pc.clickli(self.index)
        self.setmusicinfo(self.mainsonginfo)
        
    def setmusicinfo(self,mainsonglist): #设置音乐地址并且播放
        self.setMusic(mainsonglist[2])
        self.Playersongname.setText(mainsonglist[1])
        data=get(mainsonglist[0])
        with open("localfile/mainsongpic.jpg","wb") as w:
            w.write(data.content)
        pixmap = QPixmap('localfile/mainsongpic.jpg')  # 按指定路径找到图片
        self.mainimage.setPixmap(pixmap)
        
    def downmainmusic(self):#下载绑定事件
        messagetime=time()
        try:
            data=get(self.mainsonginfo[2])
            with open("localfile/"+self.mainsonginfo[1]+self.mainsonginfo[2][-4:],"wb") as w:
                w.write(data.content)
            messagetime=Thread(target=self.showmessage,args=("下载成功😀\n曲名:"+self.mainsonginfo[1],))
            messagetime.start()
        except:
            messagetime=Thread(target=self.showmessage,args=("下载失败/(ㄒoㄒ)/~~\n曲名"+self.mainsonginfo[1],))
            messagetime.start()


    ##########################################################################
    #设置无边框移动事件
    def mouseMoveEvent(self, e: QMouseEvent):  #设置无边框移动事件
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            print("Hi sb! This is a bug. Can you solve it?")#拖动元素报此错

    def mousePressEvent(self, e: QMouseEvent): #设置无边框移动事件
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())
    def mouseReleaseEvent(self, e: QMouseEvent): #设置无边框移动事件
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
    ##########################################################################

    def changepaper(self,pageid):
        self.Rightframe.setCurrentIndex(pageid)

    ##########################################################################
    #音乐控制
    def changeonandoff(self):#控制播放状态
        if self.player.state() == 1:
            self.player.pause()
            self.OnandOff.setIcon(QIcon('musicreader/play.png'))
        else:
            self.player.play()
            self.OnandOff.setIcon(QIcon('musicreader/pause.png'))

    def musicplayers(self):#音乐播放初始化以及设置控制函数
        self.player = QMediaPlayer(self)            # 1
        self.player.durationChanged.connect(self.get_duration_func)
        self.player.positionChanged.connect(self.get_position_func)
        self.player.setVolume(100)                   #音量
        self.progress_slider.sliderMoved.connect(self.update_position_func)
        self.musicvoice.valueChanged.connect(self.set_volume_func)

    def set_volume_func(self):#读取音量控制调并且设置为播放音量
        self.player.setVolume(self.musicvoice.value()/10)

    def setMusic(self,mp3url):#设置播放音乐地址并且自动播放
        try:
            self.media_content = QMediaContent(QUrl(mp3url))
            self.player.setMedia(self.media_content)    # 3
            self.player.play()
            self.OnandOff.setIcon(QIcon('musicreader/pause.png'))
        except:
            pass

    def get_time_func(self, d):#设置音乐播放时间的显示的函数（有点乱）
        seconds = int(d / 1000)
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        if minutes == 0 and seconds == 0:#到了最后
            if (len(str(self.gosonglong[0]))==1):
                minu='0'+str(self.gosonglong[0])
            else:
                minu=str(self.gosonglong[0])
            if (len(str(self.gosonglong[1]))==1):
                sec='0'+str(self.gosonglong[1])
            else:
                sec=str(self.gosonglong[1])
            self.runnedtime.setText(minu+":"+sec)
            pass
        else:
            if seconds-self.maxsonglong[1] < 0:
                seconds=str(seconds-self.maxsonglong[1]+60)
            else:
                seconds=str(seconds-27)
            if str(60-int(seconds)) =="60":
                seconds="1"
            elif str(60-int(seconds)) =="59":
                self.gosonglong[0]=int(str(minutes-4).replace("-", ""))
                seconds=str(60-int(seconds)+1)
            else:
                seconds=str(60-int(seconds)+1)
                if (len(str(self.gosonglong[0]))==1):
                    minu='0'+str(self.gosonglong[0])
                else:
                    minu=str(self.gosonglong[0])
                if (len(str(self.gosonglong[1]))==1):
                    sec='0'+str(self.gosonglong[1])
                else:
                    sec=str(self.gosonglong[1])
                self.runnedtime.setText(minu+":"+sec)
    
    def get_position_func(self, p):#进度条控制函数？
        self.progress_slider.setValue(p)
        p=str(p)[:-3]
        if p!="":
            p=int(p)
            self.gosonglong[1]=p%60
            self.gosonglong[0]=p//60
            if (len(str(self.gosonglong[0]))==1):
                minu='0'+str(self.gosonglong[0])
            else:
                minu=str(self.gosonglong[0])
            if (len(str(self.gosonglong[1]))==1):
                sec='0'+str(self.gosonglong[1])
            else:
                sec=str(self.gosonglong[1])
            self.runnedtime.setText(minu+":"+sec)

    def update_position_func(self, v):#自动跟新控制条
        self.player.setPosition(v)
        d = self.progress_slider.maximum() - v
        self.get_time_func(d)
        v=str(v)[:-2]
        # print(v)

    def get_duration_func(self, d):#获得播放时间？
        seconds = int(d / 1000)
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        self.maxsonglong=[minutes,seconds]
        self.maxtime.setText(str(self.maxsonglong[0])+":"+str(self.maxsonglong[1]))
        if (len(str(self.gosonglong[0]))==1):
            minu='0'+str(self.gosonglong[0])
        else:
            minu=str(self.gosonglong[0])
        if (len(str(self.gosonglong[1]))==1):
            sec='0'+str(self.gosonglong[1])
        else:
            sec=str(self.gosonglong[1])
        self.runnedtime.setText(minu+":"+sec)
        self.progress_slider.setRange(0, d)
        self.progress_slider.setEnabled(True)
        self.get_time_func(d)
    def showmessage(self,message):
        toaster = ToastNotifier()
        try:
            toaster.show_toast("musicreader", message,icon_path="musicreader/icons.ico",duration=3)
        except:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window=mainwindow()
    window.show() 
    sys.exit(app.exec_())
