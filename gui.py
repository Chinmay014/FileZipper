import PySimpleGUI
from zip_creator import make_archive

label1 = PySimpleGUI.Text("Select Files to compress")
input1 = PySimpleGUI.Input()
choose_button1 = PySimpleGUI.FilesBrowse("Browse..",key="files")

label2 = PySimpleGUI.Text("Select zipped file destination")
input2 = PySimpleGUI.Input()
choose_button2 = PySimpleGUI.FolderBrowse("Choose",key="folder")

compress_button = PySimpleGUI.Button("Compress")

status_label = PySimpleGUI.Text(key="status") # any empty tect box

window = PySimpleGUI.Window("File Compressor",layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[compress_button,status_label]])
while True:
    event,values = window.read()
    print(event,values)
    filepaths = values["files"].split(';')
    folderpath = values["folder"]
    if event == PySimpleGUI.WIN_CLOSED:
        break
    make_archive(filepaths,folderpath)
    window["status"].Update(value = "compression completed")
window.close()