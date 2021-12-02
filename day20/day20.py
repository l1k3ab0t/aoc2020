from PIL import Image
import numpy as np
from collections import defaultdict

tiles = [tile.splitlines() for tile  in open("input").read().split("\n\n")]






border_dict = defaultdict(list)

border_cnt = defaultdict(int)

for tile in tiles:
    tile_id  = int(tile[0].split(" ")[1][:-1])
    tile_matrix = tile[1:]

    border_dict[tile_matrix[0]].append(tile_id)
    border_cnt[tile_matrix[0]]+=1

    border_dict[tile_matrix[-1]].append(tile_id)
    border_cnt[tile_matrix[-1]]+=1

    border_dict[tile_matrix[0][::-1]].append(tile_id)
    border_cnt[tile_matrix[0][::-1]]+=1

    border_dict[tile_matrix[-1][::-1]].append(tile_id)
    border_cnt[tile_matrix[-1][::-1]]+=1

    leftb = ""
    rghtb = ""

    for l in tile_matrix:
        leftb += l[0]
        rghtb += l[-1]


    border_dict[leftb].append(tile_id)
    border_cnt[leftb]+=1

    border_dict[rghtb].append(tile_id)
    border_cnt[rghtb]+=1

    border_dict[leftb[::-1]].append(tile_id)
    border_cnt[leftb[::-1]]+=1

    border_dict[rghtb[::-1]].append(tile_id)
    border_cnt[rghtb[::-1]]+=1



print(sorted(border_cnt.items(), key=lambda item: item[1]))

fit_cnt = defaultdict(int)

for key, value in border_cnt.items():
    if value == 2:
        for tile_id in border_dict[key]:
            fit_cnt[tile_id]+=1


print(sorted(fit_cnt.items(), key=lambda item: item[1]))





# 4 Rotations, 

images = []

for tile in tiles:
    img_arry =np.reshape(list(map(lambda x: list(map(lambda y: 1 if y =="#" else 0, x)), tile[1:])),(10,10))
    img = Image.fromarray(np.uint8(img_arry*255), "L")
    img.rotate
    images.append(img)

widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)


new_im = Image.new('L', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.show()
