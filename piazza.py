import pyautogui
import time

url = 'https://piazza.com/class/k8661d6g2h6ho?cid='
cids = [100,99,87,82,73,72,56,47,42,37,33,19,13,11,10,9,115,114,113,112,111,110,109,106,104,102,101,98,97,96,95,94,93,92,91,90,89,88,86,84,83,81,80,79,78,77,75,74,69,67,66,65,64,63,62,61,59,58,57,55,54,53,52,50,49,45,44,43,41,40,39,38,36,35,34,32,30,28,26,25,24,23,22,21,20,18,17,16,15,14,12,8,1]
post = 1
for cid in reversed(cids):
    pyautogui.moveTo(466, 51)
    pyautogui.click()
    
    pyautogui.write(url + str(cid))
    pyautogui.press('enter')
    
    time.sleep(2)
    
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    
    pyautogui.write('post{}'.format(post))
    pyautogui.press('enter')
    
    post = post + 1
    