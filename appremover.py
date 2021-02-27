from appremover_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMessageBox


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("App Remover [NoRoot]")
        self.defaultVariable()
        self.ui.btn_getApp.clicked.connect(self.addListView)
        self.ui.btn_deleteapp.clicked.connect(self.deleteApp)
        self.ui.btn_search.clicked.connect(self.searchApp)
        self.ui.lbl_version.setText("Version : 0.01 AATTK")
        

    def getPhoneApps(self):
        dd = 0
        try:
            self.appList = []
            data = subprocess.check_output('platform-tools\\adb.exe shell "pm list packages -f"', shell=True)
            self.connectionState = True
            datasize = len(data.decode().split('\r\n'))
            for i in data.decode().split('\r\n'): 
                self.appList.append(i.split("=")[-1].strip("\n"))
                dd = dd + 1
                self.ui.pb_datarate.setValue((dd/datasize)*100)
                print(dd)
        except Exception as e:
            self.messagebox('Cannot connect with the device.',QMessageBox.Warning)
            self.connectionState = False
        
        
    def addListView(self):
        self.ui.appList.clear()
        self.getPhoneApps()
        self.ui.lbl_info.setText("Number of Applications : " +str(len(self.appList)))
        self.ui.appList.addItems(self.appList)

    def deleteApp(self):
        index = self.ui.appList.currentRow()
        item = self.ui.appList.item(index)
        if item is None:
            self.messagebox('No application has been selected.',QMessageBox.Warning)
            return
        print(item.text())
        data = subprocess.check_output('platform-tools\\adb.exe shell "pm uninstall -k --user 0 '+item.text()+'"', shell=True).decode()
        self.messagebox(data,QMessageBox.NoIcon) 

    def defaultVariable(self):
        self.appListName = []
        self.appList = []
        self.connectionState = False
        self.appNum = 0

    def messagebox(self,text,typ):
        msg = QMessageBox()
        msg.setWindowTitle('AppRemover [NoRoot]')
        msg.setText(text)
        msg.setIcon(typ)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def searchApp(self):
        if len(self.appList) == 0:
            self.getPhoneApps()
        self.ui.appList.clear()
        sname = self.ui.searchName.text()
        for ia in self.appList:
            if (ia.find(sname) > 0 ):
                self.ui.appList.addItem(ia)
    
def window():
    # app = QtWidgets.QApplication
    app = QApplication(sys.argv)
    win = App()  # Ana sayfa oluşturur.
    win.show()  # Pencereyi gösterir.
    sys.exit(app.exec_())  # ÇArpıya basınca çıkmasını sağlar.


window()