from PIL import Image
import winsound
from time import sleep

# winsound.PlaySound("*", winsound.SND_ALIAS)
# winsound.Beep(262, 5000)

color_range = [(range(1, 2396746), 262),          # DO (261.63)
               (range(2396746, 4793492), 294),    # RE (293.66)
               (range(4793492, 7190238), 330),    # MI (329.63)
               (range(7190238, 9586984), 349),    # FA (349.23)
               (range(9586984, 11983730), 392),   # SOL(392.00)
               (range(11983730, 14380476), 440),  # LA (440.00)
               (range(14380476, 16777217), 494)]  # SI (493.88)

im = Image.open("test3.jpg")
colors_list = list(im.getdata())

# for note in color_range:
 #   winsound.Beep(note[1], 1000)
im.show()
for pixel in colors_list:
    color_value = pixel[0] * pixel[1] * pixel[2]
    for i in range(0, 7):
        if color_value in color_range[i][0]:
            # print(color_range[i][1])
            # sleep(1)
            winsound.Beep(color_range[i][1], 100)



