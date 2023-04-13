import wx

app = wx.App()

# Estilos de frame 

style =[wx.DEFAULT_FRAME_STYLE, wx.CAPTION, wx.MINIMIZE_BOX, wx.MAXIMIZE_BOX, wx.CLOSE_BOX, wx.SYSTEM_MENU, wx.RESIZE_BORDER, wx.STAY_ON_TOP, wx.FRAME_FLOAT_ON_PARENT] 
j=0
for i in style:
    print("El estilo es:", style[j])
    j=j+1
    window=wx.Frame(None, -1, title="Hello",  pos=(10,10), size=(300,200), style=i, name="frame")
    
    panel=wx.Panel(window)
    label=wx.StaticText(panel,label="Hello World",pos=(100,50))
    window.Show(True)
    app.MainLoop()

#window = wx.Frame(None,title="wxPython Frame",size=(300,200))
#window=wx.Frame(None, -1, title="Hello", pos=(10,10), size=(300,200), style=wx.DEFAULT_FRAME_STYLE, name="frame")
#window=wx.Frame(None, -1, title="Hello",  pos=(10,10), size=(300,200), style=wx.CAPTION, name="frame")
#window=wx.Frame(None, -1, title="Hello",  pos=(10,10), size=(300,200), style=wx.MINIMIZE_BOX, name="frame")
#window=wx.Frame(None, -1, title="Hello",  pos=(10,10), size=(300,200), style=wx.MAXIMIZE_BOX, name="frame")
#window=wx.Frame(None, -1, title="Hello",  pos=(10,10), size=(300,200), style=wx.CLOSE_BOX, name="frame")





#panel=wx.Panel(window)
#label=wx.StaticText(panel,label="Hello World",pos=(100,50))
#window.Show(True)
#app.MainLoop()