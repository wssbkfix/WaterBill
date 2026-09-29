## 1- verfiies that JSON file has everyting setup 
## 2- verfiy the Input file for activity 
## 3- verify the Input file for Holdings 
## 4- verify the spreadsheet for Activity exists 
## 5- verify the spreadsheet for Holdings exists 

##import json
import sys 
import  os  
import readConfigFile as cfg
import GSFileUtilities as utlFGS
from verifyWaterBillSub import WaterBillVerifySub
from GenUtilities import getAsList
from GenUtilities import insert_before_key

from tkinter import * 

## 1- initialize parent window 
root = Tk()
root.title("Water Bill ")

## POsition the parent wndow using geomertry()
window_width = 500 
window_height = 400 

## get monitor dimensions 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center-right X and Y Pixel coordinates 
center_x = int(screen_width/2)
center_y = int(screen_height/4)

## Apply format 
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

## 2- Get configuration information 
## Verify JSON file 

WaterBillDict = WaterBillVerifySub('List') 

WaterBillDict =  insert_before_key(WaterBillDict,'RevLin0',
                                    ['OS Files','-------------'],'Path')
WaterBillDict =  insert_before_key(WaterBillDict,'RevLin1',
                                  ['Spreadsheet Info','-------------'],'WaterBillSS')
WaterBillDict =  insert_before_key(WaterBillDict,'RevLin2',
                                  ['Revised SS Name','-------------'],'spreadsheetName')

rowCount = 0 
for key, value in WaterBillDict.items():
    lineValues = getAsList(WaterBillDict, key )
    descValue = Label(root,text=lineValues[0])
    value     = Label(root,text=lineValues[1])
    descValue.grid(row=rowCount, padx=20, column=0,sticky=W)
    value.grid(row=rowCount, column=1,sticky=W)
    if len(lineValues) == 3:
        descValue2 = Label(root,text=lineValues[2])
        descValue2.grid(row=rowCount,column=2, sticky=W)

    rowCount += 1

root.mainloop()

