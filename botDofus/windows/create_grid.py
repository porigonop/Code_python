from click import move_to
from pprint import pprint
import win32gui
import time
POS0 = (990, 160)
POSMAX = (1913, 814)
size = 66
nbx = 14
nby = 40
"""
for j in range(nby):
    for i in range(nbx):
        move_to((   POS0[0]+size*i + size*(j%2)//2,\
                    POS0[1] + j*size//4))
        time.sleep(0.01)
"""
case = "."
monte = "0"
trou = "*"

def create_map():
    map = []
    dic = {}
    #line = colomne et vice versa
    for colomn in range(nby):
        map.append([])
        for line in range(nbx):
            pixel = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()),\
                    POS0[0] + size*line + size * (colomn%2) // 2,\
                    POS0[1] + colomn * size // 4)
            pixel = (pixel & 255,(pixel >> 8) & 255, (pixel >> 16) & 255)
            dic[pixel]= dic.get(pixel, 1) + 1
            
            
            if pixel == (0, 0, 0):
                map[colomn].append(trou)
            elif pixel == (150, 142, 103) or pixel == (142, 134, 94):
                map[colomn].append(case)
            elif pixel == (88, 83, 58):
                map[colomn].append(monte)
            else:
                move_to((POS0[0] + size*line + size * (colomn%2) // 2,\
                    POS0[1] + colomn * size // 4))
                time.sleep(2)
    return dic, map
dic, map = create_map()
for key in dic:
    print(key, dic[key])
    
for elt in map:
    print("\n")
    for elt1 in elt:
        print(elt1, end = '')
        