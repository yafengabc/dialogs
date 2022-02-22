import dialogs


if __name__=="__main__":
    dialogs.MsgBox()
    dialogs.MsgBox("Hello World Text","hello Caption")
    dialogs.MsgBox("你好Dialogs","你好Dialogs")
    print(dialogs.InputBox())
    print(dialogs.InputBox("Please Input something","caption!"))
    print(dialogs.InputBox("写点东西吧","输入框"))
    print(dialogs.OpenDialog())
    print(dialogs.SaveDialog())
