# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:46:32 2021
@author: Ania
"""
"""
a=poczatek przedziału
b=koniec przedziału
"""
def srednia(a,b):
    if a>0 and b>a:
        ilosc_niepodzielnych=0
        suma=0;
        for i in range(a,b+1):
            if i%2:
                ilosc_niepodzielnych+=1
                suma=suma+i
        print("Wynik: ",suma/ilosc_niepodzielnych)
    else:
        print("Podano nieprwidłowy przedział!")
            
    
   

srednia(3,10)

