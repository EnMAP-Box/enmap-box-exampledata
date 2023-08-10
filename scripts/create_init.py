from os import listdir
from os.path import dirname, splitext

from enmapboxexampledata import berlin, potsdam

extensions = ['.bsq', '.gpkg', '.tif']

print('# berlin')
for name in listdir(dirname(berlin.__file__)):
    key, ext = splitext(name)
    if ext not in extensions:
        continue
    key = key.replace('-', '_')
    print(f"{key} = join(dirname(__file__), '{name}')")

print()
print('# potsdam')
for name in listdir(dirname(potsdam.__file__)):
    key, ext = splitext(name)
    if ext not in extensions:
        continue
    key = key.replace('-', '_')
    print(f"{key} = join(dirname(__file__), '{name}')")
