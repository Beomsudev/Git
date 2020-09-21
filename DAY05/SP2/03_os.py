# 03_os.py

import os

# 폴더 구분자를 사용할 때 슬래시는 한번만, 역슬래시는 반드시 두 개를 적어야 한다.
myfolder = 'd:\\'
newpath = os.path.join(myfolder, 'sample')

try:
    os.mkdir(path=newpath)

    for idx in range(1,11):
        newfile = os.path.join(newpath, 'folder'+ str(idx).zfill(2))
        os.mkdir(path=newfile)

except FileExistsError as err:
    print("폴더존재")