# -*- coding: utf-8 *-*
#!/usr/bin/env python

import wx

app = wx.App()
dlg = wx.MessageDialog(None, u"¿Deseas continuar?", u"Python Diario")
if dlg.ShowModal()==wx.ID_OK:
    print(u"Has decidido continuar, gracias.")
else:
    print(u"Has abandonado, vuelve pronto.")
app.MainLoop()