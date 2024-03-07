import colorgram
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

extract_color_qty = 30

colors = colorgram.extract('hirst_painting.jpg', extract_color_qty)

color_list = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    tup = (r, g, b) 
    color_list.append(tup)

print(color_list)

