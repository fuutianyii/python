import Ui_UI
import db
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QItemDelegate,QMessageBox
from PyQt5.QtCore import Qt
from time import localtime,strftime

class EmptyDelegate(QItemDelegate):
    def __init__(self,parent):
        super(EmptyDelegate, self).__init__(parent)
    
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None

class mainwindow(Ui_UI.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.mydb=db.db()
        self.datetime=strftime("%Y-%m-%d",localtime())
        self.setupUi(self)
        self.remake_ui()
        self.condef()
        self.autostart()
        self.lens=1
        
    def  clear_add_chinese_table(self):
        for i in range(1,self.lens+1):
            self.add_chinese_input_table_widget.removeRow(0)
            self.lens=1

    def insert_to_add_chinese_table(self):
        self.clear_add_chinese_table()
        # self.add_chinese_textedit.setRowCount(0)
        # self.add_chinese_textedit.clearContents()
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
        # print(self.add_chinese_input_table_widget.rowCount())

    def autostart(self):
        self.Stacked.setCurrentIndex(0)
        self.Add_Stack.setCurrentIndex(0)

    def remake_ui(self):
        #居中
        self.hello_text.setAlignment(Qt.AlignCenter)
        self.add_english_lable.setAlignment(Qt.AlignCenter)
        self.add_part_of_speech_lable.setAlignment(Qt.AlignCenter)
        self.add_chinese_lable.setAlignment(Qt.AlignCenter)
        self.part_of_speech_dic={}#添加的单词
        #更改字符
        
        time_str=strftime("今天是：%Y年%m月%d日",localtime())
        #num=0 #这里获取录入了多少个单词
        all_words_num=self.mydb.select("SELECT Count(*) FROM words")[0][0]
        self.hello_text.setText(time_str+f"\n\n已录入{all_words_num}个的单词")
        self.add_english_lable.setText("填入你的英文")
        self.add_part_of_speech_lable.setText("选择词性")
        self.add_chinese_lable.setText("填入对应的中文")
        self.add_chinese_input_table_widget.horizontalHeader().setVisible(False)
        self.add_chinese_input_table_widget.verticalHeader().setVisible(False)
        self.add_chinese_input_table_widget.setColumnCount(2)
        self.add_chinese_input_table_widget.setColumnWidth(0,75)
        self.add_chinese_input_table_widget.setColumnWidth(1,545)

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
            
    def condef(self):
        self.left_first_button.clicked.connect(self.changepage_main)
        self.left_second_button.clicked.connect(self.changepage_add)
        self.left_third_button.clicked.connect(self.chagnepage_update)
        self.left_forth_button.clicked.connect(self.changepage_exam)
        self.add_english_input_next.clicked.connect(self.change_add_frame_to_part_of_speech)
        self.add_part_of_speech_input_next.clicked.connect(self.change_add_frame_to_chinese)
        self.add_part_of_speech_input_last.clicked.connect(self.change_add_english_widget)
        self.add_chinese_input_last.clicked.connect(self.change_add_frame_to_part_of_speech)
        self.add_chinese_input_next.clicked.connect(self.complete_one)
        self.choose_exam.clicked.connect(self.start_choose_exam)
        self.year_exam.clicked.connect(self.choose_year_exam)
        self.month_exam.clicked.connect(self.choose_month_exam)
        self.day_exam.clicked.connect(self.choose_today_exam)
        self.exam_english_lable.returnPressed.connect(self.exam_submit)


    def start_choose_exam(self):
        date=str(self.exam_calendarWidget.selectedDate().toPyDate())#获取选中日期并且转为str格式
        self.words=self.mydb.select(f"select * from words where insert_date='{date}'")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(1)
            self.words_index=0
            print(self.words[self.words_index][1])
            self.exam_chinese_lable.setText(self.words[self.words_index][1])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")

    def exam_submit(self):
        if  self.exam_english_lable.text() == self.words[self.words_index][0]:
            print(self.words[self.words_index])
            self.exam_change()
        else:
            self.exam_english_lable.setStyleSheet('''QWidget{background-color:#EE0000;}''')
            self.exam_english_lable.setText("")
    
    def exam_change(self):
        self.words_index+=1
        if  len(self.words) == self.words_index:
           self.exam_stacked.setCurrentIndex(0)
           self.words_index=0
        else:
            self.exam_english_lable.setStyleSheet('''QWidget{background-color:#66FFCC;}''')
            self.exam_chinese_lable.setText(self.words[self.words_index][1])
            self.exam_english_lable.setText("")
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")

    def choose_month_exam(self):
        date=str(self.exam_calendarWidget.selectedDate().toPyDate())#获取选中日期并且转为str格式
        date=date[:7]
        self.words=self.mydb.select(f"select * from words where insert_date like '{date}%'")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(1)
            self.words_index=0
            print(self.words[self.words_index][1])
            self.exam_chinese_lable.setText(self.words[self.words_index][1])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")

    def choose_year_exam(self):
        date=str(self.exam_calendarWidget.selectedDate().toPyDate())#获取选中日期并且转为str格式
        date=date[:4]
        self.words=self.mydb.select(f"select * from words where insert_date like '{date}%'")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(1)
            self.words_index=0
            print(self.words[self.words_index][1])
            self.exam_chinese_lable.setText(self.words[self.words_index][1])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")


    def choose_today_exam(self):
        self.words=self.mydb.select(f"select * from words where insert_date='{self.datetime}'")
        if len(self.words)==0:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有获取到words')
            msg_box.exec_()
        else:
            self.exam_stacked.setCurrentIndex(1)
            self.words_index=0
            print(self.words[self.words_index][1])
            self.exam_chinese_lable.setText(self.words[self.words_index][1])
            self.word_num=len(self.words)
            self.progress_label.setText(f"{self.words_index}/{self.word_num}")
    
    def changepage_main(self):
        self.Stacked.setCurrentIndex(0)

    def changepage_add(self):
        self.Stacked.setCurrentIndex(1)

    def chagnepage_update(self):
        self.Stacked.setCurrentIndex(2)

    def changepage_exam(self):
        self.Stacked.setCurrentIndex(3)
        self.exam_stacked.setCurrentIndex(0)

    def change_add_english_widget(self):
        self.Add_Stack.setCurrentIndex(0)

    def change_add_frame_to_part_of_speech(self):
        self.Add_Stack.setCurrentIndex(1)

    def change_add_frame_to_chinese(self):
        self.Add_Stack.setCurrentIndex(2)
        self.insert_to_add_chinese_table()
    
    def complete_one(self):
        self.Add_Stack.setCurrentIndex(0)
        for ch in range(0,len(self.part_of_speech_dic)):
            chinese=self.add_chinese_input_table_widget.item(ch, 1).text()
            self.part_of_speech_dic[self.add_chinese_input_table_widget.item(ch, 0).text()]=chinese
        english=self.add_english_input_edit.text()
        for (posd,ch) in self.part_of_speech_dic.items():
            # print("english:"+english)
            # print("posd:"+posd)
            # print("chinese:"+ch)
            
            self.mydb.insert(english,ch,posd,self.datetime,0)
            # inster.inser(self.add_english_input_edit.text(),ch,posd)

        self.add_english_input_edit.setText("")
        self.clear_add_chinese_table()
        self.part_of_speech_dic={}

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=mainwindow()
    window.show() 
    sys.exit(app.exec_())