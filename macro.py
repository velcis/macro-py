import pyautogui
import pyperclip
import json


# Define the screen positions for text selection
start_x, start_y = 162, 210  # Replace with your desired starting position
end_x, end_y = 380, 210      # Replace with your desired ending position


# pyautogui.moveTo(start_x, start_y)
# pyautogui.mouseDown()
# pyautogui.moveTo(end_x, end_y, 0.1)
# pyautogui.mouseUp()
# pyautogui.hotkey('ctrl', 'c')
user = {}
users = []
# Retrieve the copied text from the clipboard


def getName():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x + 80, end_y, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getAddress():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y + 20, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x + 50, end_y + 20, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getNeighborhood():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y + 40, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x - 70, end_y + 40, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getCity():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y + 60, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x - 70, end_y + 60, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getPhone():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y + 95, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x - 100, end_y + 95, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getPhoneTwo():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y + 120, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x - 100, end_y + 120, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getBirthdate():
    pyperclip.copy("")
    pyautogui.moveTo(start_x, start_y + 150, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x - 120, end_y + 150, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getWords():
    pyperclip.copy("")
    pyautogui.moveTo(start_x + 115, start_y + 190, 0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x + 50, end_y + 300, 0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()


def getProntuario():
    pyperclip.copy("")
    pyautogui.click(start_x - 65, start_y + 275)
    pyautogui.sleep(0.5)
    pyautogui.click(start_x, start_y + 75)
    px = pyautogui.pixel(800, 538)
    print(px)
    if px[0] != 255 and px[1] != 255 and px[2] != 255:
        pyautogui.doubleClick(start_x, start_y + 75)
        pyautogui.moveTo(start_x + 53, start_y + 85, 0.1)
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x + 2000, end_y + 3000, 1)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        return pyperclip.paste()


def checkSecondProntuario():
    pyperclip.copy("")
    pyautogui.click(start_x + 170, start_y + 90)
    pyautogui.sleep(0.5)
    px = pyautogui.pixel(800, 598)
    # print(px)
    if px[0] != 255 and px[1] != 255 and px[2] != 255:
        pyautogui.doubleClick(start_x + 170, start_y + 90)
        pyautogui.sleep(0.5)
        pyautogui.moveTo(start_x + 53, start_y + 85, 0.1)
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x + 2000, end_y + 3000, 1)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('esc')
        return pyperclip.paste()


def getPatient():
    name = getName()
    address = getAddress()
    neighborhood = getNeighborhood()
    city = getCity()
    phone = getPhone()
    phone2 = getPhoneTwo()
    birthdate = getBirthdate()
    words = getWords()
    prontuario = getProntuario()
    prontuario2 = checkSecondProntuario()
    return {'name': name, 'address': address, 'neighborhood': neighborhood, 'city': city, 'mobile': phone, 'phone': phone2, 'birthdate': birthdate, 'words': words, 'prontuario': prontuario, 'prontuario2': prontuario2}


def main():
    pyautogui.doubleClick(start_x - 100, start_y - 5)
    i = 0
    while i < 500:
        patient = getPatient()
        users.append(patient)
        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press("down")
        pyautogui.press("enter")
        i += 1
        print(i)
    with open("patients.json", "w") as f:
        json.dump(users, f)
    print(users)


main()
