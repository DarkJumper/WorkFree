from syst.prt import *
from osfi.osdir import *
import shutil
import sys
import os


class renameFgr():

    def __init__(self, in_dir, pro_name, *args):
        self.in_dir = in_dir
        self.pro_name = pro_name
        self.new_name = args
        self.status = 0

    def copyFgr(self):
        dir = osDir()
        dest_dir = "{0}{1}{2}".format(dir.getOutFgrDir(), dir.getSlash(), self.pro_name)
        try:
            os.mkdir(dest_dir)
        except FileExistsError:
            self.status = 1
        for file in os.listdir(self.in_dir):
            src_file = "{0}{1}{2}".format(self.in_dir, dir.getSlash(), file)
            shutil.copy(src_file, dest_dir)

    def rename(self):
        pass

    def execute(self):
        self.copyFgr()
        return self.status


if __name__ == "__main__":
    test_dir = "C:\\Users\\p.schwarz\\Desktop\\FGR_test"
    name = "Elyse"
    test = renameFgr(test_dir, name, "TEST1", "TEST2", "TEST3")
    if test.execute() == 1:
        print("Du hast vergessen den Ordner zu loeschen du IDIOT")
