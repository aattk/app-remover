import os
import subprocess
from tkinter import *
root = Tk()
# root.geometry("800x500")
root.title("App-Remover - NO ROOT")
def çıkış():
    # etiket['text'] = 'Elveda zalim dünya...'
    # cikis['text'] = 'Bekleyin...'
    # cikis['state'] = 'disabled'
    print("Güle Güle")
    root.after(2000, root.destroy)

# Label(root, text="Find:").grid(row=0, column=0, sticky='e')
# Entry(root, width=60).grid(row=0, column=1,padx=2, pady=2, sticky='we', columnspan=9)
# Label(root, text="Replace:").grid(row=1, column=0, sticky='e')
# Entry(root).grid(row=1, column=1, padx=2, pady=2, sticky='we',columnspan=9)
# Button(root, text="Find").grid(row=0, column=10, sticky='e' + 'w', padx=2, pady=2)
# Button(root, text="Find All").grid(row=1, column=10, sticky='e' + 'w', padx=2)
# Button(root, text="Replace").grid(row=2, column=10, sticky='e' +'w', padx=2)
# Button(root, text="Replace All").grid(row=3, column=10, sticky='e' + 'w', padx=2)
# Checkbutton(root, text='Match whole word only').grid(row=2, column=1, columnspan=4, sticky='w')
# Checkbutton(root, text='Match Case').grid(row=3, column=1, columnspan=4, sticky='w')
# Checkbutton(root, text='Wrap around').grid(row=4, column=1, columnspan=4, sticky='w')
# Label(root, text="Direction:").grid(row=2, column=6, sticky='w')
# Radiobutton(root, text='Up', value=1).grid(row=3, column=6, columnspan=6, sticky='w')
# Radiobutton(root, text='Down', value=2).grid(row=3, column=7, columnspan=2, sticky='e')
list = Listbox(root, font="serif 12 bold", bd=5,relief="raised")
list.insert("1","alpaslan")
list.grid(row=1,column=0,sticky='e',columnspan=100)
Label(root,text="App List").grid(row=0,column=0,sticky='w',columnspan=100)
Button(root,text="Çıkış").grid(row=21,column=0,sticky='w',columnspan=50)
Button(root,text="Yenile").grid(row=21,column=51,sticky='w',columnspan=50)
root.mainloop()


# stream = os.popen('platform-tools\\adb.exe shell "pm list packages -f"')
# aa = stream.read()

# os.system('platform-tools\\adb.exe shell "pm list packages -f" > app-list')

# with open("app-list","r",encoding="utf-8") as file:
#     app_list = file.readlines()

# for i in app_list:
#     print(i.split("/")[-1])