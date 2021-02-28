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
        self.ui.lbl_version.setText("Version : 0.02 AATTK")

    def getPhoneApps(self):
        dd = 0
        try:
            self.appList = []
            self.appListName = []
            data = subprocess.check_output(
                'platform-tools\\adb.exe shell "pm list packages -f"', shell=True)
            self.connectionState = True
            datasize = len(data.decode().split('\r\n'))
            for i in data.decode().split('\r\n'):
                self.appList.append(i.split("=")[-1].strip("\n"))
                if len(i) >= 0:
                    try:
                        xx = subprocess.check_output('platform-tools\\adb.exe shell "/data/local/tmp/aapt-arm-pie dump badging ' + i.split(
                            ".apk")[0].split("package:/")[1] + '.apk | grep application-label"', shell=True).decode().split("\n")[0].split("'")[1]
                        self.appListName.append(xx)
                    except Exception as e:
                        self.appListName.append("Error Read")
                dd = dd + 1
                self.ui.pb_datarate.setValue(round((dd/datasize)*100))
        except Exception as e:
            self.messagebox('Cannot connect with the device.',
                            QMessageBox.Warning)
            self.connectionState = False

    def addListView(self):
        self.ui.appList.clear()
        self.getPhoneApps()
        self.ui.lbl_info.setText(
            "Number of Applications : " + str(len(self.appList)))
        self.ui.appList.addItems(self.appListName)

    def deleteApp(self):
        index = self.ui.appList.currentRow()
        item = self.ui.appList.item(index)
        if item is None:
            self.messagebox('No application has been selected.',
                            QMessageBox.Warning)
            return
        print(item.text())
        for i in range(0, len(self.appListName)):
            if(item.text() == self.appListName[i]):
                aa = subprocess.check_output(
                    'platform-tools\\adb.exe shell "pm uninstall -k --user 0 '+self.appList[i]+'"', shell=True).decode()
                break
        self.messagebox(aa, QMessageBox.NoIcon)

    def defaultVariable(self):
        self.appListName = []
        self.appList = []
        self.connectionState = False
        self.appNum = 0

    def messagebox(self, text, typ):
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
        for ia in self.appListName:
            if (ia.capitalize().find(sname.capitalize()) != -1):
                self.ui.appList.addItem(ia)


def window():
    # app = QtWidgets.QApplication
    app = QApplication(sys.argv)
    win = App()  # Ana sayfa oluşturur.
    win.show()  # Pencereyi gösterir.
    sys.exit(app.exec_())  # ÇArpıya basınca çıkmasını sağlar.


window()


# ! Ekle
# ! adb push aapt-arm-pie /data/local/tmp
# ! adb shell chmod 0755 /data/local/tmp/aapt-arm-pie
