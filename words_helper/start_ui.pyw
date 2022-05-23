import Ui_UI
import db
import sys
from time import sleep
from os import getcwd,path
from requests import get
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QItemDelegate,QMessageBox,QAbstractItemView
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer
from PyQt5.QtCore import Qt,QUrl
from time import localtime,strftime
import datetime
from random import randrange,shuffle


class EmptyDelegate(QItemDelegate):
    def __init__(self,parent):
        super(EmptyDelegate, self).__init__(parent)
    
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None

class mainwindow(Ui_UI.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.mydb=db.db()
        self.player = QMediaPlayer() 
        self.datetime=strftime("%Y-%m-%d",localtime())
        self.setupUi(self)
        self.remake_ui()
        self.condef()
        self.autostart()
        self.lens=1
        self.group=""
        self.forgeted=0
        
    def  clear_add_chinese_table(self):
        for i in range(1,self.lens+1):
            self.add_chinese_input_table_widget.removeRow(0)
            self.lens=1

    def autostart(self):
        self.Stacked.setCurrentIndex(0)
        self.Add_Stack.setCurrentIndex(0)

    def remake_ui(self):
        #居中
        self.hello_text.setAlignment(Qt.AlignCenter)
        self.forget_label.setAlignment(Qt.AlignCenter)
        self.add_english_lable.setAlignment(Qt.AlignCenter)
        self.add_part_of_speech_label.setAlignment(Qt.AlignCenter)
        self.add_chinese_lable.setAlignment(Qt.AlignCenter)
        self.part_of_speech_dic={}#添加的单词
        #更改字符
        time_str=strftime("今天是：%Y年%m月%d日",localtime())
        #num=0 #这里获取录入了多少个单词
        self.all_words_num=self.mydb.select("SELECT Count(*) FROM words")[0][0]
        self.hello_text.setText(time_str+f"\n\n已录入{self.all_words_num}个的单词")
        self.add_english_lable.setText("填入你的英文")
        self.add_part_of_speech_label.setText("选择词性")
        self.add_chinese_lable.setText("填入对应的中文")
        self.add_chinese_input_table_widget.horizontalHeader().setVisible(False)
        self.add_chinese_input_table_widget.verticalHeader().setVisible(False)
        self.add_chinese_input_table_widget.setColumnCount(2)
        self.add_chinese_input_table_widget.setColumnWidth(0,75)
        self.add_chinese_input_table_widget.setColumnWidth(1,610)
        self.update_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.update_table.horizontalHeader().setVisible(False)
        self.update_table.verticalHeader().setVisible(False)
        self.update_table.setColumnCount(5)
        self.update_table.setRowCount(self.update_table.rowCount()+1)

    def condef(self):
        self.left_first_button.clicked.connect(self.changepage_main)
        self.left_second_button.clicked.connect(self.changepage_add)
        self.left_third_button.clicked.connect(self.changepage_update)
        self.left_forth_button.clicked.connect(self.changepage_exam)
        self.add_english_input_next.clicked.connect(self.change_add_frame_to_part_of_speech)
        self.add_english_input_edit.returnPressed.connect(self.change_add_frame_to_part_of_speech)
        self.add_part_of_speech_input_next.clicked.connect(self.change_add_frame_to_chinese)
        self.add_part_of_speech_input_last.clicked.connect(self.back_add_english_widget)
        self.add_chinese_input_last.clicked.connect(self.back_add_frame_to_part_of_speech)
        self.search.clicked.connect(self.update_page_search)
        self.add_chinese_input_next.clicked.connect(self.complete_one)
        self.exam_calendarWidget.clicked.connect(self.start_choose_exam)
        self.update.clicked.connect(self.update_all_words)
        self.forget_pushButton.clicked.connect(self.display_forget)
        self.search_forget_words.clicked.connect(self.select_forget_words)
        self.delete_choose.clicked.connect(self.delete_words)
        self.exam_choose.clicked.connect(self.exam_choose_words)
        self.exam_english_lable.returnPressed.connect(self.exam_submit)
        self.change_calendar.clicked.connect(self.changepage_exam_calendar)
        self.back_exam_main.clicked.connect(self.changepage_exam_main)
        self.exam_today_button.clicked.connect(self.today_exam)
        self.review_words_button.clicked.connect(self.review_words)
        self.radom_exam_button.clicked.connect(self.random_exam)
        self.review_Forgotten_button.clicked.connect(self.forgoten_exam)
        self.remove_forget_pushButton.clicked.connect(self.reset_wrong_times)

    def insert_to_add_chinese_table(self):
        self.part_of_speech_dic={}
        self.clear_add_chinese_table()
        if self.check_n.isChecked():
            self.add_chinese_textedit("n")
            
        if self.check_u.isChecked():
            self.add_chinese_textedit("u")

        if self.check_c.isChecked():
            self.add_chinese_textedit("c")

        if self.check_v.isChecked():
            self.add_chinese_textedit("v")
            
        if self.check_vi.isChecked():
            self.add_chinese_textedit("vi")
            
        if self.check_vt.isChecked():
            self.add_chinese_textedit("vt")
            
        if self.check_auxv.isChecked():
            self.add_chinese_textedit("aux_v")
            
        if self.check_model_verb.isChecked():
            self.add_chinese_textedit("model_verb")
            
        if self.check_conj.isChecked():
            self.add_chinese_textedit("conj")
            
        if self.check_adj.isChecked():
            self.add_chinese_textedit("adj")
            
        if self.check_adv.isChecked():
            self.add_chinese_textedit("adv")

        if self.check_art.isChecked():
            self.add_chinese_textedit("art")
            
        if self.check_prep.isChecked():
            self.add_chinese_textedit("prep")
            
        if self.check_pron.isChecked():
            self.add_chinese_textedit("pron")
            
        if self.check_num.isChecked():
            self.add_chinese_textedit("num")
            
        if self.check_int.isChecked():
            self.add_chinese_textedit("int")

    def add_chinese_textedit(self,part_of_speech):
        if part_of_speech=="n":
            self.part_of_speech_dic["n"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("n")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1

        elif part_of_speech=="u":
            self.part_of_speech_dic["u"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("u")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1

        elif part_of_speech=="c":
            self.part_of_speech_dic["c"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("c")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1

        elif part_of_speech=="v":
            self.part_of_speech_dic["v"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("v")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="vi":
            self.part_of_speech_dic["vi"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("vi")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="vt":
            self.part_of_speech_dic["vt"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("vt")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="aux_v":
            self.part_of_speech_dic["aux_v"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("aux_v")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="model_verb":
            self.part_of_speech_dic["model_verb"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("model_verb")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="conj":
            self.part_of_speech_dic["conj"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("conj")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="adj":
            self.part_of_speech_dic["adj"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("adj")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="adv":
            self.part_of_speech_dic["adv"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("adv")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="art":
            self.part_of_speech_dic["art"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("art")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="prep":
            self.part_of_speech_dic["prep"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("prep")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="pron":
            self.part_of_speech_dic["pron"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("pron")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="num":
            self.part_of_speech_dic["num"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("num")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1
            

        elif part_of_speech=="int":
            self.part_of_speech_dic["int"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("int")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))
            self.lens+=1

        self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))#禁止编辑第一列
            
    def update_all_words(self):
        for i in range(0,self.update_table.rowCount()):
            english=self.update_table.item(i, 0).text()
            chinese=self.update_table.item(i, 1).text()
            posd=self.update_table.item(i, 2).text()
            insert_date=self.update_table.item(i,3).text()
            group=self.update_table.item(i,4).text()
            rowid=self.update_words[i][0]
            self.mydb.update(f"update words set english='{english}',chinese='{chinese}',insert_date='{insert_date}',list='{group}',posd='{posd}' where rowid={rowid}")
        msg_box = QMessageBox(QMessageBox.Warning, '提示','更改成功')
        msg_box.exec_()

    def delete_words(self):
        tablelen=len(self.update_table.selectedIndexes())
        rows=len(self.update_table.selectedIndexes())//4
        if tablelen == 0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有选中单词')
            msg_box.exec_()
            return 0
        #self.update_table.selectedIndexes() #会一格一格遍历，每一格就是一个列表项
        for index in range(0,tablelen)[::5]:#设置步长为4
            row_index=self.update_table.selectedIndexes()[index+1].row() #获取行号
            row_id=self.update_words[row_index][0]
            #english=self.update_table.selectedIndexes()[index].data() #获取第一列的数据
            #chinese=self.update_table.selectedIndexes()[index+1].data() #获取第二列的数据
            sql=f"delete from words where rowid={row_id}"
            self.mydb.delete(sql)
        self.changepage_update()#刷新一波
        msg_box = QMessageBox(QMessageBox.Warning, '警告', f'成功删除{rows}个单词')
        msg_box.exec_()
            
    def exam_choose_words(self):
        if len(self.update_words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到单词')
            msg_box.exec_()
        else:
            self.changepage_exam()
            self.words=self.update_words
            self.exam_stacked.setCurrentIndex(2)
            self.words_index=0
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
            self.exam_english_lable.setText("")
            self.forget_label.setText("")

    def select_forget_words(self):
        for i in range(0,self.update_table.rowCount()+1):
            self.update_table.removeRow(0)
            self.lens=1
        eng=self.search_english.text()
        ch=self.search_chinese.text()
        date=self.search_date_time.text()
        group=self.search_list.text()
        search_filter=[]
        if eng != "":
            search_filter.append(f" english like '%{eng}%' ")
        if ch != "":
            search_filter.append(f" chinese like '%{ch}%' ")
        if date != "":
            search_filter.append(f" insert_date like '%{date}%' ")
        if group != "":
            search_filter.append(f" list like '%{group}%' ")

        search="select rowid,* from words where"
        if (len(search_filter) != 0):
            search+=search_filter[0]
            for i in range(1,len(search_filter)):
                search+=" and "
                search+=search_filter[i]
        else:
            search+=" 1=1"
        search += " and wrong_times != 0"
        self.update_words=self.mydb.select(search)

        for items in self.update_words:
            setline=self.update_table.rowCount()+1
            self.update_table.setRowCount(self.update_table.rowCount()+1)
            newItem = QTableWidgetItem(items[1])
            self.update_table.setItem(self.update_table.rowCount()-1,0,newItem)
            newItem = QTableWidgetItem(items[2])
            self.update_table.setItem(self.update_table.rowCount()-1,1,newItem)
            newItem = QTableWidgetItem(items[3])            
            self.update_table.setItem(self.update_table.rowCount()-1,2,newItem)
            newItem = QTableWidgetItem(items[4])
            self.update_table.setItem(self.update_table.rowCount()-1,3,newItem)
            newItem = QTableWidgetItem(items[6])
            self.update_table.setItem(self.update_table.rowCount()-1,4,newItem)

    def update_page_search(self):
        for i in range(0,self.update_table.rowCount()+1):
            self.update_table.removeRow(0)
            self.lens=1
        eng=self.search_english.text()
        ch=self.search_chinese.text()
        date=self.search_date_time.text()
        group=self.search_list.text()
        search_filter=[]
        if eng != "":
            search_filter.append(f" english like '%{eng}%' ")
        if ch != "":
            search_filter.append(f" chinese like '%{ch}%' ")
        if date != "":
            search_filter.append(f" insert_date like '%{date}%' ")
        if group != "":
            search_filter.append(f" list like '%{group}%' ")

        search="select rowid,* from words where"
        if (len(search_filter) != 0):
            search+=search_filter[0]
            for i in range(1,len(search_filter)):
                search+=" and "
                search+=search_filter[i]
            self.update_words=self.mydb.select(search)
        else:
            search+=" 1=1"
            self.update_words=self.mydb.select(search)

        self.update_table.setRowCount(len(self.update_words))
        for items in range(0,len(self.update_words)):
            newItem = QTableWidgetItem(self.update_words[items][1])
            self.update_table.setItem(items,0,newItem)
            newItem = QTableWidgetItem(self.update_words[items][2])
            self.update_table.setItem(items,1,newItem)
            newItem = QTableWidgetItem(self.update_words[items][3])
            self.update_table.setItem(items,2,newItem)
            newItem = QTableWidgetItem(self.update_words[items][4])
            self.update_table.setItem(items,3,newItem)
            newItem = QTableWidgetItem(self.update_words[items][6])
            self.update_table.setItem(items,4,newItem) 

    def play(self,word):
        try:
            if path.exists(f"mp3/voice_{word}.mp3") == True:
                # mp3_path=getcwd().replace("\\", "/")+f"\\mp3\\voice_{word}.mp3".replace("\\", "/")
                mp3_path=getcwd().replace("\\", "/")+f"\\mp3\\voice_{word}.mp3".replace("\\", "/")
                url = QUrl.fromLocalFile(mp3_path)
                content = QMediaContent(url)  # 加载音乐
                self.player.setMedia(content)     # 关联 QMediaPlayer控件与音乐地址
                
                self.player.play()                          # 播放
            else:
                self.getmp3(word)
        except:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '播放失败')
            msg_box.exec_()

    def getmp3(self,word):
        try:
            # respond=get(f"https://fanyi.baidu.com/gettts?lan=en&text={word}&spd=3&source=web")
            respond=get(f"https://dict.youdao.com/dictvoice?audio={word}&type=1")
            if respond.status_code == 200:
                data=respond.content
                w = open(f"mp3/voice_{word}.mp3","wb") 
                w.write(data)
                w.close()
                self.play(word)
            else:
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '下载音频文件失败，请检查你的网络环境')
                msg_box.exec_()
        except:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '下载失败')
            msg_box.exec_()

    def exam_submit(self):
        if  self.exam_english_lable.text() == self.words[self.words_index][1]:
            self.exam_english_lable.setStyleSheet('''QWidget{background-color:#66FFCC;}''')
            QApplication.processEvents()#刷新样式
            self.exam_english_lable.setText("")
            # if self.forgeted == 0:
                # english=self.words[self.words_index][1]
                # chinese=self.exam_chinese_label.text()
                # self.mydb.update(f"update words set wrong_times=0 where english='{english}' and chinese = '{chinese}'")
            english=self.words[self.words_index][1]
            self.play(english)
            sleep(1.5)
            self.exam_change()
        else:
            self.exam_english_lable.setStyleSheet('''QWidget{background-color:#FFB6C1;}''')
            self.exam_english_lable.setText("")
    
    def display_forget(self):
        self.forgeted=1
        english=self.words[self.words_index][1]
        wrong_times=self.mydb.select(f"select wrong_times from words where english='{english}'")[0][0]
        wrong_times=self.mydb.update(f"update words set wrong_times={wrong_times+1} where english='{english}'")
        self.forget_label.setText(self.words[self.words_index][1])

    def reset_wrong_times(self):
        english=self.words[self.words_index][1]
        wrong_times=self.mydb.update(f"update words set wrong_times=0 where english='{english}'")

    def exam_change(self):
        self.forgeted = 0
        self.words_index+=1
        if  len(self.words) == self.words_index:
           self.exam_stacked.setCurrentIndex(0)
           self.words_index=0
        else:
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.exam_english_lable.setText("")
            self.forget_label.setText("")
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")

    def start_choose_exam(self):
        self.remove_forget_pushButton.setHidden(True)
        self.forget_pushButton.setHidden(False)
        date=str(self.exam_calendarWidget.selectedDate().toPyDate())#获取选中日期并且转为str格式
        self.words=self.mydb.select(f"select rowid,* from words where insert_date='{date}'")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(2)
            self.words_index=0
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
            self.exam_english_lable.setText("")
            self.forget_label.setText("")
            
    def today_exam(self):
        self.remove_forget_pushButton.setHidden(True)
        self.forget_pushButton.setHidden(False)
        self.words=self.mydb.select(f"select rowid,* from words where insert_date='{self.datetime}'")
        shuffle(self.words)
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(2)
            self.words_index=0
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
            self.exam_english_lable.setText("")
            self.forget_label.setText("")

    def review_words(self):
        # 1． 第一个记忆周期：5分钟
        # 2． 第二个记忆周期：30分钟
        # 3． 第三个记忆周期：12小时
        # 4． 第四个记忆周期：1天
        # 5． 第五个记忆周期：2天
        # 6． 第六个记忆周期：4天
        # 7． 第七个记忆周期：7天
        # 8． 第八个记忆周期：15天
        self.remove_forget_pushButton.setHidden(True)
        self.forget_pushButton.setHidden(False)
        date1=str(datetime.date.today()-datetime.timedelta(days=1))
        date2=str(datetime.date.today()-datetime.timedelta(days=2))
        date3=str(datetime.date.today()-datetime.timedelta(days=4))
        date4=str(datetime.date.today()-datetime.timedelta(days=7))
        date5=str(datetime.date.today()-datetime.timedelta(days=15))
        self.words=self.mydb.select(f"select rowid,* from words where insert_date='{date1}' or insert_date='{date2}' or insert_date='{date3}'  or insert_date='{date4}'  or insert_date='{date5}'")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(2)
            self.words_index=0
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
            self.exam_english_lable.setText("")
            self.forget_label.setText("")

    def random_exam(self):
        self.remove_forget_pushButton.setHidden(True)
        self.forget_pushButton.setHidden(False)
        random_list=[]
        for i in range(1,51):
            random_list.append(randrange(1,self.all_words_num+1))
        sql="select rowid,* from words where "
        for i in random_list:
            sql+=f"rowid={i} or "
        sql=sql[:-3]
        self.words=self.mydb.select(sql)
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(2)
            self.words_index=0
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
            self.exam_english_lable.setText("")
            self.forget_label.setText("")        

    def forgoten_exam(self):
        self.remove_forget_pushButton.setHidden(False)
        self.forget_pushButton.setHidden(False)
        self.words=self.mydb.select(f"select rowid,* from words where wrong_times != 0")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(2)
            self.words_index=0
            self.part_of_speech_label.setText(self.words[self.words_index][3])
            self.exam_chinese_label.setText(self.words[self.words_index][2])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
            self.exam_english_lable.setText("")
            self.forget_label.setText("")

    def changepage_main(self):
        self.Stacked.setCurrentIndex(0)

    def changepage_add(self):
        self.Stacked.setCurrentIndex(1)

    def changepage_update(self):
        self.Stacked.setCurrentIndex(2)
        self.update_words=self.mydb.select(f"select rowid,* from words")
        self.update_table.setColumnWidth(0,150)
        self.update_table.setColumnWidth(1,420)
        self.update_table.setColumnWidth(2,30)
        self.update_table.setColumnWidth(3,80)
        self.update_table.setColumnWidth(4,20)
        self.update_table.setRowCount(len(self.update_words))
        for items in range(0,len(self.update_words)):
            newItem = QTableWidgetItem(self.update_words[items][1])
            self.update_table.setItem(items,0,newItem)
            newItem = QTableWidgetItem(self.update_words[items][2])
            self.update_table.setItem(items,1,newItem)
            newItem = QTableWidgetItem(self.update_words[items][3])
            self.update_table.setItem(items,2,newItem)
            newItem = QTableWidgetItem(self.update_words[items][4])
            self.update_table.setItem(items,3,newItem)
            newItem = QTableWidgetItem(self.update_words[items][6])
            self.update_table.setItem(items,4,newItem) 

    def changepage_exam(self):
        self.Stacked.setCurrentIndex(3)
        self.exam_stacked.setCurrentIndex(0)

    def changepage_exam_calendar(self):
        self.exam_stacked.setCurrentIndex(1)
    
    def changepage_exam_main(self):
        self.exam_stacked.setCurrentIndex(0)

    def back_add_english_widget(self):
        self.group=self.list_lineEdit_2.text()
        self.list_lineEdit_1.setText(self.group)
        self.Add_Stack.setCurrentIndex(0)
    
    def back_add_frame_to_part_of_speech(self):
        self.group=self.list_lineEdit_3.text()
        self.list_lineEdit_2.setText(self.group)
        self.Add_Stack.setCurrentIndex(1)

    def change_add_frame_to_part_of_speech(self):
        self.group=self.list_lineEdit_1.text()
        self.list_lineEdit_2.setText(self.group)
        self.Add_Stack.setCurrentIndex(1)

    def change_add_frame_to_chinese(self):
        self.group=self.list_lineEdit_2.text()
        self.list_lineEdit_3.setText(self.group)
        self.Add_Stack.setCurrentIndex(2)
        self.insert_to_add_chinese_table()
    
    def complete_one(self):
        self.group=self.list_lineEdit_3.text()
        for ch in range(0,len(self.part_of_speech_dic)):
            if (self.add_chinese_input_table_widget.item(ch, 1) == None) or (self.add_chinese_input_table_widget.item(ch, 1).text() == ""):
                    msg_box = QMessageBox(QMessageBox.Warning, '警告', '含义不能为空')
                    msg_box.exec_()
                    return 0
            else:
                chinese=self.add_chinese_input_table_widget.item(ch, 1).text()
                self.part_of_speech_dic[self.add_chinese_input_table_widget.item(ch, 0).text()]=chinese

        english=self.add_english_input_edit.text()
        if self.group == "":
            self.group=self.mydb.select("select list from words order by rowid desc;")[0][0]
        for (posd,ch) in self.part_of_speech_dic.items():
            self.mydb.insert(english,ch,posd,self.datetime,0,self.group)
        self.add_english_input_edit.setText("")
        self.clear_add_chinese_table()
        # self.part_of_speech_dic={}
        self.Add_Stack.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=mainwindow()
    window.show() 
    sys.exit(app.exec_())