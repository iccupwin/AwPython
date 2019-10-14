import numpy as np;from PIL import Image, ImageDraw, ImageFont, ImageMath;from pyray.axes import *
from pyray.rotation import *;from pyray.axes import draw_2d_arrow, Path, ZigZagPath, draw_grid, draw_grey_grid
from pyray.misc import dist

im = draw_grid()
draw = ImageDraw.Draw(im,'RGBA')
pts = np.array([[0,0],[1,1],[5,-3]])
pth = Path(pts)
pth.zg.draw_lines(draw,i/10.0)
im.save("im" + str(i) + ".png")