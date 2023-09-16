import os
import json
from PIL import Image

def get_filename(sprite_filename):
  return f"./sprites/{sprite_filename}"

for sprite_filename in os.listdir('./sprites'):
  image = Image.open(f"./sprites/{sprite_filename}")
  image.resize((40, 40))
  image.save(get_filename(sprite_filename))

