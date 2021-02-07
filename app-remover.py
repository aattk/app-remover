import os


class appRemover():
    def __init__(self):
        self.defaultVariable()
        self.deviceAppSync()
        self.deviceAppSync()
        self.appListEdit()
        self.topBar()

    def topBar(self):
        os.system("cls")
        print("#".center(100, "#"))
        print("APP ROMEVER v0.01 [No Root]".center(100, " "))
        print("#".center(100, "#"))
        self.appNum = len(self.appList)
        info = "Connection :",str(self.connectionState),"App Number : ",str(self.appNum)
        print(self.side_by_side(info,20,1))

    def appRemove(self):
        pass

    def appView(self):
        print(self.appList)

    def appInstall(self):
        pass

    def deviceAppSync(self):
        try:
            os.system('platform-tools\\adb.exe shell "pm list packages -f" > app-list')
            self.connectionState = True
        except Exception as e:
            self.connectionState = False
    def appListEdit(self):
        with open("app-list", "r", encoding="utf-8") as file:
            self.app_List = file.readlines()
        for i in self.app_List:
            self.appList.append(i.split("=")[-1].strip("\n"))

    def defaultVariable(self):
        self.app_List = []
        self.appList = []
        self.connectionState = False
        self.appNum = 0

    def side_by_side(self, strings, size=30, space=4):
        strings = list(strings)
        result = []
        while any(strings):
            line = []
            for i, s in enumerate(strings):
                line.append(s[:size].ljust(size))
                strings[i] = s[size:]
            result.append((" " * space).join(line))
        return "\n".join(result)


aR = appRemover()
