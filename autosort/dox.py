import os
import shutil
import sys


sys.stdout.reconfigure(encoding='utf-8')
dirPath = r'C:\Users\MARIUS-PC\Desktop'

while True:
    choseTheName = input("Name of the file ?(.docx, .pdf, .ppt, .txt, .xls ...etc) or press 'q' to quit: ").strip()

    if choseTheName.lower() == 'q':
        break

    print(f"Selected file extension: {choseTheName}")

    name, ext = os.path.splitext(choseTheName)

    targetFolder = os.path.join(dirPath,name)
    os.makedirs(targetFolder, exist_ok=True)

    folder = [
        i for i in os.listdir(dirPath)
        if os.path.isfile(os.path.join(dirPath, i)) and i.endswith(choseTheName)
    ]

    for i in folder:
        shutil.move(os.path.join(dirPath, i), os.path.join(targetFolder, i))

    if folder:
        print(f"Fișierele {choseTheName} au fost mutate în folderul {choseTheName}: ", folder)
    else:
        print(f"Nu s-au găsit fișiere {choseTheName} pentru a fi mutate.")

print("Programul s-a încheiat.")
