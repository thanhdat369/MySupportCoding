import os

#LABEL TYPE IS YOLO TXT
BASE_DIR = 'D:/FPT_Capstone/Capstone/03_Data/SignDetect2'
LABEL_DIR = f'{BASE_DIR}/Label/'
IMAGE_DIR = f'{BASE_DIR}/Data/'

all_file_label_name = os.listdir(LABEL_DIR)
all_file_name = [file_name.split('.')[0] for file_name in all_file_label_name] #without extension

all_file_image_name = os.listdir(IMAGE_DIR)
for file_image_name in all_file_image_name:
    file_name = file_image_name.split('.')[0]
    if(file_name not in all_file_name):
        os.remove(f'{IMAGE_DIR}{file_image_name}')
        print(f'Remove {file_name}')

print('DONE')