import tkinter as tk
import pandas as pd
import numpy as np
        
dict1={
'A': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
'B': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
'C': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
'    ': pd.Series(["    ","    ","    ","    ","    ","    ","    ","    ","    ","    "],index=np.arange(1,11,1)),
'D': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
'E': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
'F': pd.Series([False,False,False,False,False,False,False,False,False,False],index=np.arange(1,11,1)),
}
back=""

df=pd.DataFrame(dict1)

def checkseat(col,row):
    if df.loc[row,col]==True:
        back="red"
        return back
    else:
        back="green"
        return back

top=tk.Tk()


a1=tk.Button(top,text="A1",command=checkseat("A",1), bg=back)





a1.pack( )
top.mainloop()
