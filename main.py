from PIL import Image as Img
#import winsound
from time import sleep
import musicalbeeps
from tkinter import filedialog
from tkinter import *
import os

# winsound.PlaySound("*", winsound.SND_ALIAS)
# winsound.Beep(262, 5000)

player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

color_range = [(range(1, 2396746), "C"),          # DO (261.63)
               (range(2396746, 4793492), "D"),    # RE (293.66)
               (range(4793492, 7190238), "E"),    # MI (329.63)
               (range(7190238, 9586984), "F"),    # FA (349.23)
               (range(9586984, 11983730), "G"),   # SOL(392.00)
               (range(11983730, 14380476), "A"),  # LA (440.00)
               (range(14380476, 16777217), "B")]  # SI (493.88)

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("jpeg files","*.jpg"), ("png files","*.png"), ("all files","*.*")))
print(root.filename)
im = Img.open(root.filename)

colors_list = list(im.getdata())

# for note in color_range:
 #   winsound.Beep(note[1], 1000)
notes = []

im.show()
for pixel in colors_list:
    color_value = pixel[0] * pixel[1] * pixel[2]
    for i in range(0, 7):
        if color_value in color_range[i][0]:
          player.play_note(color_range[i][1], 0.2)
          #notes.append(color_range[i][1])

            # print(color_range[i][1])
            # sleep(1)
            #winsound.Beep(color_range[i][1], 100)

# print(notes)

# k = 0
# start = 1
# for i in range(4, len(notes)):
#   if k >= 15:
#     deleted_note = notes[i-1]
#     del notes[start:i]
#     notes.insert(i-1, deleted_note)
#     start = i
#     k = 0
#   else:
#     if notes[i-2:i-1] == notes[i]:
#       k += 1
#     else:
#       start = i
#       k = 0

# list1 = ["-", "-", "-"]

# print(list1)
# print(list1)
# print(list1)
# print(list1)
# print(list1)
# print(list1)
# print(list1)
# print(list1)
# print(list1)

# sleep(5)

# print(notes)



