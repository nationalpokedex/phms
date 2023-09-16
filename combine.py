import os
import json
from PIL import Image

def get_filename(sprite_filename):
  return f"./mini-sprites/{sprite_filename}"

json_file = open('pokedex.json', 'r')
data = json.load(json_file)
total_keys = len(data)
num_cols = 30
pic_height = 40
pic_width = 40
num_rows = total_keys // num_cols
size = (num_cols * pic_width + num_cols, ((num_rows + 1) * pic_height + num_rows))


canvas = Image.new(mode="RGBA", size=size)
row_counter = 0
for index, species_id in enumerate(data):
  image = Image.open(get_filename(f"{species_id}.png"))
  image_copy = image.copy()
  row_gap = index // num_cols
  top_left_row = index // num_cols * pic_height
  col_gap = index % num_cols
  top_left_col = index // num_cols * pic_width
  canvas.paste(image_copy, (top_left_row + row_gap, top_left_col + col_gap))
  if index == 31:
    canvas.show()
    break

