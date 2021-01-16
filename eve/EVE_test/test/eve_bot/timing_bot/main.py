import pyautogui
from time import sleep

DELAY_BETWEEN_COMMANDS = 1.00
# Задержка между командами (float)

infinity = '1'

def main():

     initializePyAutoGUI()
     countdownTimer()
     
     #exitDocStation()
     #entranceDocStation()
     
     screen_location()
     
     #reportMousePosition()
     print('Done')

def initializePyAutoGUI():
    # Инициализация PyAutoGUI
    pyautogui.FAILSAFE = True

def countdownTimer():
    # Время обратного отчёта
    print('Starting', end = '')
    for i in range(0, 10):
        print('.', end = '')
        sleep(1)
    print('Go')
    
def reportMousePosition(seconds = 10):
    # Координаты/позиция мыши
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)

def screen_location():
     # Проверка местонахождения
     pyautogui.moveTo(764, 1315, duration = 0.5)
     sleep(2)
     location = pyautogui.locateOnScreen('initialization.png', grayscale=True)
     if location == None:
          exitDocStation()
     else:
          entranceDocStation()
     #print(location)
  
def exitDocStation():
    # Выход из "Док-станции"
    pyautogui.moveTo(1190, 216, duration = 0.5)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()

    # Ожидание выхода из дока
    sleep(20.0)

    # Возвращение к кораблю по направлению
    pyautogui.click(238, 662)
    pyautogui.dragTo(538, 662, 5, pyautogui.easeInOutQuad)
    pyautogui.scroll(100)
    
def entranceDocStation():
    # Выбор ближайшей "Док-станции"
    pyautogui.moveTo(931, 314, duration = 0.5)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()

    # Подтверждение действия на вход в "Док-станцию"
    pyautogui.press('D')
    
    # Ожидание входа в "Док-станцию"
    sleep(30.0)

    # Остаёмся в "Док-станции"
    print("Complete! You've arrived at the Dock Station!")
    #exit(0)

while True:
     if infinity == '1':
          main()
          
if __name__ == '__main__':
    main()
