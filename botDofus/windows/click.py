import win32api, win32con
UPPER = (1414, 161)
LEFT = (975, 400)
RIGHT = (1900, 520)
LOWER = (1431, 821)

def move_to(pos):
    win32api.SetCursorPos(pos)
def click(pos):
    move_to(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1],0,0)

#haut 1414, 161
#gauche 975, 400
#droite 1900, 520
#bas 1431, 821
