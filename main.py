import shutil
import csv
from WorkWithPrt import *

if __name__ == "__main__":
    with open("C:\\Users\p.schwarz\VSCode\WorkFree\Liste.csv", newline='') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
        for row in reader:
            newdir = "C:\\Users\p.schwarz\VSCode\WorkFree\Ausgabe\{0}.prt".format(row[1])
            search_standart = PrtFile.getDir(row[0])
            shutil.copyfile(search_standart, newdir)
            data = PrtFile.read(search_standart)
            newfile = MSRdescribe(row).change(data)
            PrtFile.write(newdir, newfile)
