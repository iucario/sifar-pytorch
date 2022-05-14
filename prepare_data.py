import os


def prepare_annotation(annotation_path, image_path, output_path):
    anns = os.listdir('ucf101/annotations')
    for ann in anns:
        with open('ucf101/annotations/' + ann, 'r') as f:
            if 'train' in ann:
                with open('ucf101/train.txt', 'a') as t:
                    lines = f.readlines()
                    for line in lines:
                        path, label = line.split(' ')
                        t.write(path + ' 1 100 ' + label )
            elif 'test' in ann:
                with open('ucf101/test.txt', 'a') as t:
                    lines = f.readlines()
                    for line in lines:
                        t.write(line.rstrip() + ' 1 100\n')


def prepare_image(image_path, output_path):
    """video to raw frames output to folder in video's name"""
    path = 'sifar-pytorch/ucf101/videos'
    output_path = '/home/umi/repos/sifar-pytorch/ucf101/raw_frames'
    folders = os.listdir(path)
    for folder in folders:
        videos = os.listdir(path + '/' + folder)
        for video in videos:
            os.system('ffmpeg -i ' + path + '/' + folder + '/' + \
                video + ' ' + output_path + '/' + folder + '/' + video + '.jpg')


path = 'sifar-pytorch/ucf101'
# SkateBoarding/v_SkateBoarding_g20_c04 171 79  -> videos/SkateBoarding/v_SkateBoarding_g20_c04 1 171 79
annos = os.listdir(path)
for ann in annos:
    if 'ucf101' in ann and 'rawframes' in ann:
        print('ucf101/' + ann)
        with open('ucf101/' + ann) as f:
            if 'train' in ann:
                t = open('ucf101/train.txt', 'a')
            else:
                t = open('ucf101/val.txt', 'a')
            lines = f.readlines()
            for line in lines:
                path, length, label, = line.split(' ')
                t.write(f'rawframes/{path} 1 {length} {label}')
            t.close()

            