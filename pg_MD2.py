import pyautogui as pg
pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.hotkey('winleft','up')
pg.hotkey('winleft','up')
pg.typewrite('amazon.com\n', 0.5)
pg.moveTo(472, 174, 1)
pg.click()
pg.typewrite('Winter boots\n', 0)
