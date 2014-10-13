# -*- coding: utf-8 -*-

'''The script scans the directory (cwd)
for the presence of specific files and moves them to dest.

'''

import sys
import pathlib
import shutil
from os.path import join

if sys.platform.startswith('linux'):
    cwd = '/home/username/Downloads'
    dest = '/home/username'

elif sys.platform.startswith('win32'):
    cwd = 'Загрузки'
    dest = 'Мои документы'

dirs = {
        'Docs': 'doc txt pdf rtf ppt pptx docx xls odt ods',
        'Images': 'jpg png jpeg bmp gif tiff',
        'Archives': 'zip tgz rar gz bz2 7z xz',
        'ISOs': 'iso nrg',
        'Videos': 'avi mov mp4 mkv 3gp flv',
        'Other Music': 'mp3',
        'Programs': 'exe deb rpm',
        'EBooks': 'fb2 epub djvu',
        'Torrents': 'torrent',
        'Scripts': 'py sh bat'
    }

if __name__ == '__main__':

    for dir in [dir for dir in dirs if not pathlib.Path(join(dest, dir)).exists()]:
        pathlib.Path(join(dest, dir)).mkdir()

    for dir, exts in dirs.items():
        for e in exts.split():
            for file in list(
                    map(
                        str,
                        pathlib.Path(cwd).glob('*.{}'.format(e))
                    )
                ):
                shutil.move(file, join(dest, dir))
