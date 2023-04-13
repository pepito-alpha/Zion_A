#!/bin/env python

import wx

class Table(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Periodic Table')
        frame.Show()
        return True

app = Table()
app.MainLoop()