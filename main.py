import shutil
import csv
from WorkWithPrt import *

if __name__ == "__main__":
    with open("C:\\Users\p.schwarz\VSCode\WorkFree\Liste.csv", newline='') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
        for row in reader:
            newdir = "C:\\Users\p.schwarz\VSCode\WorkFree\Ausgabe\{0}.prt".format(row[1])
            standart = ""
            if row[0] == "MBIN":
                standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\{0}.prt".format("MBIN_Standart")
            elif row[0] == "IDF":
                standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\{0}.prt".format("IDF_Standart")
            shutil.copyfile(standart, newdir)
            data = PrtFile.read(standart)
            newfile = MSRdescribe(row).change(data)
            PrtFile.write(newdir, newfile)
