import shutil
import os
import re
import types
from osfi.osdir import *


# Erstellt von Peter Schwarz am 01.12.2020
# Klasse wird wie folgt importiert -> from syst.fgr import *
# Es muss Projekt name filepath angegeben werden aber über variablen zugriff in class übertragen werden
# Dictionarie mit Neuen Name und Alten namen werden direkt an klasse übergeben. (Alte Name sollten immer gleich sein)
# Um funktion aufzurufen muss fgr(FunktionName) aufgerufen werden und mit execute wird die Funktion erst ausgeführt.
# Über die Variable Status kann der fehler ausgegeben werden.
# 0 = Nicht ausgeführt | 1 = Erfolgreich Ausgeführt | -1 = FileNotFoundError | -2 = FileExistsError
# Daten werden im fgr / Projektname ordner abgegeben Original Datein werden behalten.
class fgr():

    def __init__(self, func=None, **kwargs):
        self.file_path = ""
        self.project_name = ""
        self.new_names_dict = kwargs
        self.status = 0
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        pass


def rename(self):
    try:
        grafic = copyRenameFgr(self.file_path, self.project_name)
        grafic.copyFgr()
        grafic.renameFgr(self.new_names_dict)
        self.status = 1
    except FileNotFoundError:
        self.status = -1
    except FileExistsError:
        self.status = -2


class copyRenameFgr():

    def __init__(self, in_dir, pro_name):
        self.dir = osDir()
        self.in_dir = in_dir
        self.pro_name = pro_name
        self.dest_dir = ""

    def copyFgr(self):
        self.dest_dir = "{0}{1}{2}".format(self.dir.getOutFgrDir(), self.dir.getSlash(), self.pro_name)
        os.mkdir(self.dest_dir)
        for file in os.listdir(self.in_dir):
            src_file = "{0}{1}{2}".format(self.in_dir, self.dir.getSlash(), file)
            shutil.copy(src_file, self.dest_dir)

    def renameFgr(self, dict_names):
        file_list = os.listdir(self.dest_dir)
        file_list.sort()
        for file in file_list:
            old_name = self.dest_dir + self.dir.getSlash() + file
            file_format = re.split('\.', file)
            for new_file in dict_names:
                if str(dict_names[new_file]) == file_format[0]:
                    new_name = self.dest_dir + self.dir.getSlash() + new_file + "." + file_format[1]
                    del dict_names[new_file]
                    os.rename(old_name, new_name)
                    break