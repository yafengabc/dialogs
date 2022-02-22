# dialogs
A dialogs libs write by win32,very small

一个非常小的基于Dialog的库，只能运行在windows下。
使用时只需要下载release_x64.zip解压缩到你的python文件位置然后
import dialogs即可导入使用

暂时先实现了MsgBox,InputBox,OpenDialog,SaveDialog等几个函数，有空再往上加。
示例代码：

```python
import dialogs

dialogs.MsgBox()
dialogs.MsgBox("Hello World Text","hello Caption")
dialogs.MsgBox("你好Dialogs","你好Dialogs")
print(dialogs.InputBox())
print(dialogs.InputBox("Please Input something","caption!"))
print(dialogs.InputBox("写点东西吧","输入框"))
print(dialogs.OpenDialog())
print(dialogs.SaveDialog())
```

编译：
本程序的dll文件需要安装Pelles C for Windows打开工程编译即可。