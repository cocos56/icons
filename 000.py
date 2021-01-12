# -*- coding: utf-8 -*-
"""
@Python：Python 3.7.4
@author = Coco56
@date = 2019-09-25
@个人博客 : 请百度搜索“Coco56”
"""

import os
from PIL import Image

class Picture:
    def __init__(self):
        self.ext = ['jpg','jpeg','png']
        self.files = os.listdir('.')

    def handle_picture(self, file):
        img = Image.open(file).convert('RGBA')
        if img.size != (128, 128):  # 判断图片大小，统一改为 128*128
            # 修改图片尺寸
            img.thumbnail((128, 128))
        img.save(file.split('.')[0]+".ico")

    def run(self):
        cnt=1
        for file in self.files:
            if file.split('.')[-1] in self.ext and not os.path.exists(file.split('.')[0]+".ico"):
                print(cnt, file)
                self.handle_picture(file)
                cnt+=1

if __name__ == "__main__":
    ins = Picture()
    ins.run()