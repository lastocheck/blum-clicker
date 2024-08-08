import pyautogui, sys
from time import sleep
from random import uniform, randint

def main():
  # for i in range(3):
  #   for i in range(20):
  #     pyautogui.click(randint(250, 350), randint(450, 550))
  #     sleep(uniform(0.005, 0.02))
  #   # close the tab
  #   pyautogui.click(210, 100)
  #   sleep(5)
  #   # open the tab
  #   pyautogui.click(390, 95)
  #   sleep(8)
    
  #   pyautogui.click(280, 870)
  #   sleep(8)
  #   pyautogui.click(280, 870)
  #   sleep(5)

#(1150, 286, 370, 1072)
  try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
  except KeyboardInterrupt:
      print('\n')
    

if __name__ == "__main__":
    main()