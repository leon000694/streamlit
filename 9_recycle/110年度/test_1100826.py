print()

import pyautogui,time
# set these to the correct coordinates for your computer.
nameField = (648,319)
submitButton = (651,817)
submitButtonColor = (75,141,249)
submitAnotherLink = (760,224)
 
formData = [{'name':'Alice','fear':'eavppers','source':'wand','robocop':4,'comments':'Tell us'},
            {'name':'Bog','fear':'eaves','source':'crystal','robocop':4,'comments':'Big room'},
            {'name':'Kad','fear':'apple','source':'woold','robocop':1,'comments':'Nice day'},
            {'name':'Cace','fear':'ppers','source':'ball','robocop':5,'comments':'n/a'}
           ]
pyautogui.PAUSE = 0.5
for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
        time.sleep(0.5)
    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0],nameField[1])       # 單擊第一個文字欄位輸入位置
    # Fill out the Name field.
    pyautogui.typewrite(person['name']+'\t')         # 輸入該域，並按下 tab 鍵，將焦點轉向下一個輸入框
    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear']+'\t')
    # 處理下拉框
    # Fill out the Source of Wizard Powers Field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down','\t'])
    elif person['source'] == 'crystal':
        pyautogui.typewrite(['down','down','\t'])
    elif person['source'] == 'woold':
        pyautogui.typewrite(['down','down','down','\t'])
    elif person['source'] == 'ball':
        pyautogui.typewrite(['down','down','down','down','\t'])                
    # 處理單選按鈕
    # Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.typewrite([' ','\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right','\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right','right','\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right','right','right','\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right','right','right','right','\t'])
    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments']+'\t')
    # Click Submit.
    pyautogui.press('enter')
    # Wait until form page has loaded.
    print('Clicked submit.')
    time.sleep(5)
    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])

print()