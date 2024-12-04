import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')
dirPath = r'C:\Users\MARIUS-PC\Desktop'
targetFolder = os.path.join(dirPath, 'Filetxt')


os.makedirs(targetFolder, exist_ok=True)

folder = [
    file for file in os.listdir(dirPath)
    if os.path.isfile(os.path.join(dirPath, file)) and file.endswith('.txt')
]

for file in folder:
    shutil.move(os.path.join(dirPath, file), os.path.join(targetFolder, file))

if folder:
    print("Fișierele .txt au fost mutate în folderul Filetxt:", folder)
else:
    print("Nu s-au găsit fișiere .txt pentru a fi mutate.")

print("Procesul s-a încheiat.")
