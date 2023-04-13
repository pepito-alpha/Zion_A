# -*- coding: utf-8 *-*
#!/usr/bin/env python

# Un esqueleto de calculadora sin sizer

import wx

class MiFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        # Sizers
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.inputsz = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
        self.buttonsz = wx.BoxSizer(wx.HORIZONTAL)

        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "A")
        self.labelB = wx.StaticText(self, wx.ID_ANY, "B")
        self.labelR = wx.StaticText(self, wx.ID_ANY, "Resultado")
        
        # Inputs
        self.A = wx.TextCtrl(self, wx.ID_ANY)
        self.B = wx.TextCtrl(self, wx.ID_ANY)
        self.R = wx.TextCtrl(self, wx.ID_ANY)

        # Botones
        self.suma = wx.Button(self, wx.ID_ANY, "+")
        self.resta = wx.Button(self, wx.ID_ANY, "-")
        self.multiplicacion = wx.Button(self, wx.ID_ANY, "*")
        self.division = wx.Button(self, wx.ID_ANY, "/")

        # Agregando a sizers
        for obj in [self.labelA, self.A, self.labelB, self.B, self.labelR, self.R]:
            self.inputsz.Add(obj, 1, wx.EXPAND|wx.ALL, 2)
        self.inputsz.AddGrowableCol(1)

        for obj in [self.suma, self.resta, self.multiplicacion, self.division]:
            self.buttonsz.Add(obj, 1, wx.EXPAND|wx.ALL, 2)
            obj.SetInitialSize((20,-1))

        # Configurando sizers
        self.mainsz.Add(self.inputsz, 2, wx.EXPAND|wx.ALL, 5)
        self.mainsz.Add(self.buttonsz, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(self.mainsz)

        self.Centre(True)
        self.Show()
            
if __name__=='__main__':
    app = wx.App() 
    fr = MiFrame(None, -1, "wxPython App", size=(300,200))
    app.MainLoop()