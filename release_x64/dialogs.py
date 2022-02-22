import ctypes

dll=ctypes.WinDLL(".\dialogs.dll")

def MsgBox(Message="你好世界",Caption="提示"):
    dll.MsgBox(Message.encode("GBK"),Caption.encode("GBK"))

def InputBox(Message="请输入内容:",Caption="提示"):
    dll.InputBox.restype=ctypes.c_char_p
    ccc=dll.InputBox(Message.encode("GBK"),Caption.encode("GBK"))
    return ccc.decode("GBK")

def OpenDialog():
    dll.OpenDialog.restype=ctypes.c_char_p
    ccc=dll.OpenDialog()
    return ccc.decode("GBK")

def SaveDialog():
    dll.SaveDialog.restype=ctypes.c_char_p
    ccc=dll.SaveDialog()
    return ccc.decode("GBK")


if __name__=="__main__":
    MsgBox()
    MsgBox("Hello World Text","hello Caption")
    MsgBox("你好Dialogs","你好Dialogs")
    print(InputBox())
    print(InputBox("Please Input something","caption!"))
    print(InputBox("写点东西吧","输入框"))
    print(OpenDialog())
    print(SaveDialog())
