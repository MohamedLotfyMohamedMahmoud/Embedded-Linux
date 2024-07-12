""" 
Using PyAutoGUI 
- To open vscode 
- install clangd from extension
- install c++ testmate from extension
- install c++ helper from extension
- install cmake from extension
- install cmake tools from extension
"""

import pyautogui
from time import sleep


pyautogui.hotkey('win','d')
pyautogui.click(150,50)
sleep(5)
location=None
try:
    while location is None:
        location=pyautogui.locateOnScreen('visual.png',confidence=0.9)
        pyautogui.moveTo(location.left+30,location.top+location.height-70,duration=1)
        pyautogui.doubleClick(location.left+30,location.top+location.height-70)
        sleep(3)
        pyautogui.hotkey('ctrl','shift','x')
        sleep(3)
        pyautogui.typewrite('clangd')
        sleep(2)
except pyautogui.ImageNotFoundException:
    print("image1 is not found")


location2=None
try:
    while location2 is None:
        location2=pyautogui.locateOnScreen('clangd.png',confidence=0.9)
        sleep(3)
        pyautogui.moveTo(location2.left+397,location2.top+61,duration=1)
        pyautogui.doubleClick(location2.left+397,location2.top+61)
        sleep(5)
except pyautogui.ImageNotFoundException:
    print("image2 is mot found")        
sleep(3)
pyautogui.click(location2.left+300,location2.top-30)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('delete')
pyautogui.typewrite('c++ testmate')
sleep(3)
location3=None
try:
    while location3 is None:
        location3=pyautogui.locateOnScreen('c++ testmate.png',confidence=0.9)
        sleep(3)
        #print("image3 is  found")
        pyautogui.moveTo(location3.left+390,location3.top+70,duration=1)    
        pyautogui.doubleClick(location3.left+390,location3.top+70)    
        
except pyautogui.ImageNotFoundException:
    print("image3 is not found")
sleep(3)
pyautogui.click(location2.left+300,location2.top-30)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('delete')
pyautogui.typewrite('c++ helper')
sleep(3)
location4=None
try:
    while location4 is None:
        location4=pyautogui.locateOnScreen('c++ helper.png',confidence=0.9)
        sleep(3)
        pyautogui.moveTo(location4.left+390,location4.top+70,duration=1)    
        pyautogui.doubleClick(location4.left+390,location4.top+70)    
        
except pyautogui.ImageNotFoundException:
    print("image4 is not found")    

sleep(3)
pyautogui.click(location2.left+300,location2.top-30)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('delete')
pyautogui.typewrite('cmake')
sleep(3)
location4=None
try:
    while location4 is None:
        location4=pyautogui.locateOnScreen('cmake.png',confidence=0.9)
        sleep(3)
        pyautogui.moveTo(location4.left+390,location4.top+70,duration=1)    
        pyautogui.doubleClick(location4.left+390,location4.top+70)    
        
except pyautogui.ImageNotFoundException:
    print("image4 is not found")    

sleep(3)
pyautogui.click(location2.left+300,location2.top-30)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('delete')
pyautogui.typewrite('cmake tools')
sleep(3)
location4=None
try:
    while location4 is None:
        location4=pyautogui.locateOnScreen('cmake tools.png',confidence=0.9)
        sleep(3)
        pyautogui.moveTo(location4.left+390,location4.top+73,duration=1)    
        pyautogui.doubleClick(location4.left+390,location4.top+70)    
        
except pyautogui.ImageNotFoundException:
    print("image4 is not found")    

