import os
import json
from PIL import Image

def get_filename(sprite_filename):
  return f"./sprites/{sprite_filename}"

json_file = open('../national-pokedex-ts/src/data/pokedex.json', 'r')
data = json.load(json_file)
json_file.close()
total_keys = len(data)
num_cols = 30
pic_height = 40
pic_width = 40
num_rows = total_keys // num_cols
size = (num_cols * pic_width, ((num_rows + 1) * pic_height))

canvas = Image.new(mode="RGBA", size=size)
row_counter = 0
for index, species_id in enumerate(data):
  try:
    image = Image.open(get_filename(f"{species_id}.png"))
    image_copy = image.copy().resize((40, 40))
    image.close()
    top_left_row = (index // num_cols) * pic_height
    top_left_col = (index % num_cols) * pic_width
    canvas.paste(image_copy, (top_left_col, top_left_row))
    image_copy.close()
  except Exception:
    print(species_id)
    continue
canvas.show()
canvas.save('combined.png')

# import os
# import json
# from PIL import Image

# def get_filename(sprite_filename):
#   return f"./mini-sprites/{sprite_filename}"

# for sprite_filename in os.listdir('./sprites'):
#   image = Image.open(f"./sprites/{sprite_filename}")
#   resized = image.resize((40, 40))
#   resized.save(get_filename(sprite_filename))

