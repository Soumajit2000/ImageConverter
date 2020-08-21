import sys
import os
from PIL import Image

# grab the first and second argument
# check if new/ exists , if not create
# loop through Pokedex
# convert images to png
# save to the  new folder

# newpath = r'sys.argv[1]\sys.argv[2]'
# if not os.path.exists(newpath):
#     os.makedirs(newpath)

# directory = r'.\sys.argv[1]'
# c=1
# for filename in os.listdir(directory):
#     if filename.endswith(".jpg"):
#         im = Image.open(filename)
#         name='img'+str(c)+'.png'
#         rgb_im = im.convert('RGB')
#         rgb_im.save(name)
#         c+=1
#         print(os.path.join(directory, filename))
#         continue
#     else:
#         continue

image_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.mkdir(new_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')
