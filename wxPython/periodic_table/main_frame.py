# -*- coding: utf-8 *-*
# -*- coding: latin1 -*-
#!/usr/bin/env python

import wx

import io

#simbol=[H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn, Fr, Ra, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Nh, Fl, Mc, Lv, Ts, Og]
simbol=["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
#name=[Hidrógeno, Helio, Litio, Berilio, Boro, Carbono, Nitrógeno, Oxígeno, Flúor, Neón, Sodio, Magnesio, Aluminio, Silicio, Fósforo, Azufre, Cloro, Argón, Potasio, Calcio, Escandio, Titanio, Vanadio, Cromo, Manganeso, Hierro, Cobalto, Níquel, Cobre, Zinc, Galio, Germanio, Arsénico, Selenio, Bromo, Kriptón, Rubidio, Estroncio, Itrio, Zirconio, Niobio, Molibdeno, Tecnecio, Rutenio, Rodio, Paladio, Plata, Cadmio, Indio, Estaño, Antimonio, Teluro, Yodo, Xenón, Cesio, Bario, Lantano, Cerio, Praseodimio, Neodimio, Prometio, Samario, Europio, Gadolinio, Terbio, Disprosio, Holmio, Erbio, Tulio, Iterbio, Lutecio, Hafnio, Tantalio, Wolframio, Renio, Osmio, Iridio, Platino, Oro, Mercurio, Talio, Plomo, Bismuto, Polonio, Astato, Radón, Francio, Radio, Actinio, Torio, Protactinio, Uranio, Neptunio, Plutonio, Americio, Curio, Berkelio, Californio, Einstenio, Fermio, Mendelevio, Nobelio, Laurencio, Rutherfordio, Dubnio, Seaborgio, Bohrio, Hassio, Meitnerio, Darmstadtio, Roentgenio, Copernicio, Nihonio, Flerovio, Moscovio, Livermorio, Teneso, Oganesón]
name=["Hidrógeno", "Helio", "Litio", "Berilio", "Boro", "Carbono", "Nitrógeno", "Oxígeno", "Flúor", "Neón", "Sodio", "Magnesio", "Aluminio", "Silicio", "Fósforo", "Azufre", "Cloro", "Argón", "Potasio", "Calcio", "Escandio", "Titanio", "Vanadio", "Cromo", "Manganeso", "Hierro", "Cobalto", "Níquel", "Cobre", "Zinc", "Galio", "Germanio", "Arsénico", "Selenio", "Bromo", "Kriptón", "Rubidio", "Estroncio", "Itrio", "Zirconio", "Niobio", "Molibdeno", "Tecnecio", "Rutenio", "Rodio", "Paladio", "Plata", "Cadmio", "Indio", "Estaño", "Antimonio", "Teluro", "Yodo", "Xenón", "Cesio", "Bario", "Lantano", "Cerio", "Praseodimio", "Neodimio", "Prometio", "Samario", "Europio", "Gadolinio", "Terbio", "Disprosio", "Holmio", "Erbio", "Tulio", "Iterbio", "Lutecio", "Hafnio", "Tantalio", "Wolframio", "Renio", "Osmio", "Iridio", "Platino", "Oro", "Mercurio", "Talio", "Plomo", "Bismuto", "Polonio", "Astato", "Radón", "Francio", "Radio", "Actinio", "Torio", "Protactinio", "Uranio", "Neptunio", "Plutonio", "Americio", "Curio", "Berkelio", "Californio", "Einstenio", "Fermio", "Mendelevio", "Nobelio", "Laurencio", "Rutherfordio", "Dubnio", "Seaborgio", "Bohrio", "Hassio", "Meitnerio", "Darmstadtio", "Roentgenio", "Copernicio", "Nihonio", "Flerovio", "Moscovio", "Livermorio", "Teneso", "Oganesón"]

k=0
for i in simbol:
    k=k+1

#print (" ", j)
x_s=70
y_s=70
class table(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)


        # Letras del encabezado tiulo
        #wx.StaticText(self, -1, "Tabla Periódica",pos=(500, 10))
        str = "Tabla Periódica"
        text = wx.StaticText(self, -1, str, (500, 10))
        font = wx.Font(25, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)

        #==================================

       ## Botones de elementos

        j=0
        a=0
        a1=0
        a2=0
        a3=0
        a4=0
        a5=0
        for i in simbol:
            if j==4 or j==10 or j==12 or j==18 or j==36 or j==54 or j==56:# or j==71:
                a=0
            if j==0: #Hidrogeno
                #n = simbol[j] + "\n" + name[j]
                self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(10,10))
            elif j==1: #helio
                self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(1200,10))
            elif j==2 or j==3: # Litio y berilio
                x_p=10+a
                self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,80))
                a+=70
            elif j>3 and j<10: # Boro-Neon
                x_p=850+a
                self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,80))
                a+=70
            elif j==10 or j==11: # sodio y magnesio
                x_p=10+a
                self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,150))
                a+=70
            elif j>11 and j<18: # aluminio - argon
                x_p=850+a
                self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,150))
                a+=70    
            elif j>17:
                #if j==18 or j==36 or j==54:# or j==71:
                #    a=0
                if j<36:
                    x_p=10+a
                    self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,220))
                    a=a+70                                   
                elif j>35 and j<54:
                    x_p=10+a
                    self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,290))
                    a=a+70
                elif j>53 and j<86:
                    if  j==54 or j==55:# or j>70:
                        x_p=10+a
                        self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,360))
                        a=a+70
                    elif j>55 and j<70:
                        x_p=150+a
                        if j!=56:
                            self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,520))
                            a=a+70
                        elif j==56:
                            self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,520))
                            self.button = wx.Button(self, -1, "56-57"  , size=(x_s,y_s), pos=(150,360))
                            a+=70
                    elif j>70:
                        x_p=220+a2
                        self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,360))
                        a2=a2+70
                    #elif j==56:
                    #    self.button = wx.Button(self, -1, "56-57"  , size=(x_s,y_s), pos=(20,350))
                    #    a+=70
                    else:
                        pass
                 #Elementos del periodo siete   
                #else:
                #    pass
                elif j>85:# and j<118:
                    if  j==86 or j==87:# or j>70:
                        x_p=10+a5
                        self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,430))
                        a5=a5+70
                    elif j>87 and j<102:
                        x_p=150+a4
                        if j!=88:
                            self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,590))
                            a4=a4+70
                        elif j==88:
                            self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,590))
                            self.button = wx.Button(self, -1, "89-103"  , size=(x_s,y_s), pos=(150,430))
                            a4+=70
                    elif j>102:
                        x_p=220+a3
                        self.button = wx.Button(self, -1, simbol[j] + "\n" + name[j]  , size=(x_s,y_s), pos=(x_p,430))
                        a3=a3+70
                    #elif j==56:
                    #    self.button = wx.Button(self, -1, "56-57"  , size=(x_s,y_s), pos=(20,350))
                    #    a+=70
                    else:
                        pass
                else:
                    pass                  
            else:
                #j+=1
                pass
            j+=1
            xp=10

        #=====================================

        # Agregando botones
        #self.button = wx.Button(self, -1, u"H \n Hidrogeno", size=(70,70), pos=(10,10))
        #self.button = wx.Button(self, -1, u"He \n Hidrogeno", size=(70,70), pos=(880,10))
        #self.button = wx.Button(self, -1, u"Li", size=(50,50), pos=(10,110))
        #self.button = wx.Button(self, -1, u"Na", size=(50,50), pos=(10,190))
        
        # Conectando el evento de un botón
        self.Bind(wx.EVT_BUTTON, self.OnClick)
        
        # Mostrando la interfaz
        self.Show()
        

      

    def OnClick(self,event):
        element = event.EventObject.GetLabel()
        print(u"Botón presionado: %s"%(event.EventObject.GetLabel()))
        #cont=0
        if element[1] == "\n":
            ele=element[0]+ ".txt"
            elemento =  open( ele, "r", encoding = "utf8")
            element =""
            for linea in elemento:
                element+=linea
                #print("%s" %linea)
            #multiText = wx.TextCtrl(self, -1, "%s" %element , size=(600, 900), pos=(1300,10), style=wx.TE_MULTILINE)
            multiText = wx.TextCtrl(self, -1, size=(600, 900), pos=(1300,10), style=wx.TE_MULTILINE)
            #multiText = wx.StaticText(self, -1, "%s" %element , size=(600, 900), pos=(1300,10), style=wx.TE_MULTILINE)
            multiText.Clean()
            multiText.WriteText("%s" %element)
        elif element[2] == "\n":
            ele = element[0] + element[1] + ".txt"
            elemento =  open( ele, "r", encoding = "utf8")
            element =""
            for linea in elemento:
                element+=linea
                #print("%s" %linea)
            multiText = wx.TextCtrl(self, -1, "%s" %element , size=(600, 900), pos=(1300,10), style=wx.TE_MULTILINE)
            #multiText.WriteText("Holas")
            elemento.close()
        print(" Este es ", ele)
        
        
        
        
        
        #if element == "H\nHidrógeno":
        #    #class info(wx.frame)           
        #    elemento =  open("H.txt", "r", encoding = "utf8")
        #    element =""
        #    for linea in elemento:
        #        element+=linea
        #        #print("%s" %linea)
        #    multiText = wx.TextCtrl(self, -1, "Hidrógeno \n ""%s" %element , size=(600, 900), pos=(1300,10), style=wx.TE_MULTILINE)

            #multiText = wx.TextCtrl(self, -1, "Here is a looooooooooooooong line " "of text set in the control.\n\n" "See that it wrapped, and that " "this line is after a blank", size=(600, 900), pos=(1300,10), style=wx.TE_MULTILINE)
        #    elemento.close()

 




#elemento =  open("hidrogeno.txt", "r")

#if if dlg.ShowModal()==wx.ID_OK:
 #   print(u"Has decidido continuar, gracias.")





if __name__=='__main__':
    app = wx.App() 
    fr = table(None, -1, "Tabla periódica", size=(1500,1000))
    fr.Centre(True)
    app.MainLoop()