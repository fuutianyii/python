import Ui_UI
import inserter
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QItemDelegate
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
        
        self.setupUi(self)
        self.remake_ui()
        self.condef()
        self.autostart()
    
    def insert_to_add_chinese_table(self):
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
            self.add_chinese_textedit("auxv")
            

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

    def autostart(self):
        self.Stacked.setCurrentIndex(0)
        self.Add_Stack.setCurrentIndex(0)

    def remake_ui(self):
        #居中
        self.hello_text.setAlignment(Qt.AlignCenter)
        self.add_english_lable.setAlignment(Qt.AlignCenter)
        self.add_part_of_speech_lable.setAlignment(Qt.AlignCenter)
        self.part_of_speech_dic={}#添加的单词
        #更改字符
        timestr=strftime("今天是：%Y年%m月%d日",localtime())
        #num=0 #这里获取录入了多少个单词
        self.hello_text.setText(timestr+"\n\n已录入"+str(0)+"个的单词")
        self.add_english_lable.setText("填入你的英文")
        self.add_part_of_speech_lable.setText("选择词性")
        self.add_part_of_speech_lable.setText("填入对应的中文")
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


        elif part_of_speech=="u":
            self.part_of_speech_dic["u"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("u")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

        elif part_of_speech=="c":
            self.part_of_speech_dic["c"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("c")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))


        elif part_of_speech=="v":
            self.part_of_speech_dic["v"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("v")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="vi":
            self.part_of_speech_dic["vi"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("vi")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="vt":
            self.part_of_speech_dic["vt"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("vt")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="aux_v":
            self.part_of_speech_dic["aux_v"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("aux_v")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="model_verb":
            self.part_of_speech_dic["model_verb"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("model_verb")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="conj":
            self.part_of_speech_dic["conj"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("conj")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="adj":
            self.part_of_speech_dic["adj"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("adj")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="adv":
            self.part_of_speech_dic["adv"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("adv")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="art":
            self.part_of_speech_dic["art"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("art")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="prep":
            self.part_of_speech_dic["prep"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("prep")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="pron":
            self.part_of_speech_dic["pron"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("pron")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="num":
            self.part_of_speech_dic["num"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("num")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

            

        elif part_of_speech=="int":
            self.part_of_speech_dic["int"]=""
            self.add_chinese_input_table_widget.setRowCount(self.add_chinese_input_table_widget.rowCount()+1)
            newItem = QTableWidgetItem("int")
            self.add_chinese_input_table_widget.setItem(self.add_chinese_input_table_widget.rowCount()-1,0,newItem)
            self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))

        self.add_chinese_input_table_widget.setItemDelegateForColumn(0,EmptyDelegate(self))#禁止编辑第一列
            
    def condef(self):
        self.left_first_button.clicked.connect(self.changepage_main)
        self.left_second_button.clicked.connect(self.changepage_add)
        self.add_english_input_next.clicked.connect(self.change_add_frame_to_part_of_speech)
        self.add_part_of_speech_input_next.clicked.connect(self.change_add_frame_to_chinese)
        self.add_chinese_input_next.clicked.connect(self.complete_one)

    def changepage_main(self):
        self.Stacked.setCurrentIndex(0)

    def changepage_add(self):
        self.Stacked.setCurrentIndex(1)

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
        for (posd,ch) in self.part_of_speech_dic.items():
            print("english:"+self.add_english_input_edit.text())
            print("posd:"+posd)
            print("chinese:"+ch)
            filename="test.db"
            inster=inserter.consql(filename)
            inster.ifexists()
            inster.con()
            inster.inser(self.add_english_input_edit.text(),ch,posd)

        self.add_english_input_edit.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=mainwindow()
    window.show() 
    sys.exit(app.exec_())