import wx 
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (350,300))
		
      panel = wx.Panel(self) 
      box = wx.BoxSizer(wx.HORIZONTAL) 
		
      self.text = wx.TextCtrl(panel,style = wx.TE_MULTILINE) 
      #self.text1 = wx.TextCtrl(panel,style = wx.TE_MULTILINE)    

      languages = ['C', 'C++', 'Java', 'Python', 'Perl', 'JavaScript', 'PHP', 'VB.NET','C#']   
      lst = wx.ListBox(panel, size = (100,-1), choices = languages, style = wx.LB_SINGLE)
		
      box.Add(lst,0,wx.EXPAND) 
      box.Add(self.text, 1, wx.EXPAND)
      #box.Add(self.text1, 2, wx.EXPAND) 
		
      panel.SetSizer(box) 
      panel.Fit() 
		
      self.Centre() 
      self.Bind(wx.EVT_LISTBOX, self.onListBox, lst) 
      self.Show(True)  
		
   def onListBox(self, event): 
      self.text.AppendText( "Current selection: "+event.GetEventObject().GetStringSelection()+"\n")
		
ex = wx.App() 
Mywin(None,'ListBox Demo') 
ex.MainLoop()