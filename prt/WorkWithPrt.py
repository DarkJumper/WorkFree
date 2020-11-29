import csv
import shutil
from osfi.osdir import *


def prtRoutine():
    listpath = osDir()
    std_prt = PrtFile()
    with open(listpath.getNormalDir() + "Liste.csv", newline='') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
        for row in reader:
            new_file = listpath.getOutputDir() + row[1] + ".prt"
            std_file = std_prt.getDir(row[0])
            shutil.copyfile(std_file, new_file)
            data = PrtFile.read(new_file)
            new_data = Baustein(row).MSR(data)
            std_prt.write(new_file, new_data)


class Baustein():

    def __init__(self, args):
        if args[0] == "MBIN":
            self.name = "MBIN"
            self.VarName = args[1]
        elif args[0] == "IDF":
            self.name = "IDF"
            self.VarName = args[1][1:]
        elif "MANA" in args[0]:
            if "900" in args[0]:
                self.name = "MANA"
            elif "800" in args[0]:
                self.name = "MANA"
            elif "700" in args[0]:
                self.name = "MANA"
            self.VarName = args[1]
        self.MSRName = args[1]
        self.KurzText = args[2]
        self.LangText = args[3]
        self.VarText = args[4]
        self.M0 = args[5]
        self.M1 = args[6]
        self.MBA = args[7]
        self.MBE = args[8]
        self.DIM = args[9]
        self.prio1 = args[10]
        self.GW1 = args[11]
        self.Lf1 = args[12]
        self.custel1 = args[13]
        self.MText1 = args[14]
        self.prio2 = args[15]
        self.GW2 = args[16]
        self.Lf2 = args[17]
        self.custel2 = args[18]
        self.MText2 = args[19]
        self.prio3 = args[20]
        self.GW3 = args[21]
        self.Lf3 = args[22]
        self.custel3 = args[23]
        self.MText3 = args[24]
        self.prio4 = args[25]
        self.GW4 = args[26]
        self.Lf4 = args[27]
        self.custel4 = args[28]
        self.MText4 = args[29]

    def MSR(self, data):
        newfile = []
        for row in data:
            if "Standart" in row:
                newfile.append(row.replace("Standart", self.MSRName))
            elif "[PARA:PARADATA]" in row:
                newfile.append(self.paraData(row))
            elif "M54321" in row:
                if "Kurztext" in row:
                    row = row.replace("Kurztext", self.KurzText[:12])
                if "Langtext" in row:
                    row = row.replace("Langtext", self.LangText[:30])
                newfile.append(row.replace("M54321", self.MSRName[:16]))
            elif "54321" in row:
                if "Variabel" in row:
                    row = row.replace("Variabel", self.VarText[:24])
                newfile.append(row.replace("54321", self.VarName[:9]))
            elif "[LAD:PARA_REF]" in row and "MANA" in self.name:
                newfile.append(row.replace("0.0", self.MBA[:7]))
            else:
                newfile.append(row)
        return newfile

    def paraData(self, data):
        splitted_data = data.split(";")
        for i in range(len(splitted_data)):
            if splitted_data[i] == "KVal" and splitted_data[i + 4] == "100.0":
                splitted_data[i + 3] = str(len(self.MBE[:7]))
                splitted_data[i + 4] = self.MBE[:7]
            elif splitted_data[i] == "KVal" and splitted_data[i + 4] == "0.0":
                splitted_data[i + 3] = str(len(self.MBA[:7]))
            elif splitted_data[i] == "MBE_Ausgang":
                splitted_data[i + 3] = str(len(self.MBE[:7]))
                splitted_data[i + 4] = self.MBE[:7]
            elif splitted_data[i] == "MBA_Ausgang":
                splitted_data[i + 3] = str(len(self.MBA[:7]))
                splitted_data[i + 4] = self.MBA[:7]
            if splitted_data[i] == "Bt0":
                splitted_data[i + 3] = str(len(self.M0[:7]))
                splitted_data[i + 4] = self.M0[:7]
            elif splitted_data[i] == "Bt1":
                splitted_data[i + 3] = str(len(self.M1[:7]))
                splitted_data[i + 4] = self.M1[:7]
            elif splitted_data[i] == "Mp":
                splitted_data[i + 4] = self.prio1
            elif splitted_data[i] == "Mt":
                splitted_data[i + 3] = str(len(self.M1[:7]))
                splitted_data[i + 4] = self.M1[:7]
            elif splitted_data[i] == "Mba":
                splitted_data[i + 3] = str(len(self.MBA[:7]))
                splitted_data[i + 4] = self.MBA[:7]
            elif splitted_data[i] == "Mbe":
                splitted_data[i + 3] = str(len(self.MBE[:7]))
                splitted_data[i + 4] = self.MBE[:7]
            elif splitted_data[i] == "Dim":
                splitted_data[i + 3] = str(len(self.DIM[:7]))
                splitted_data[i + 4] = self.DIM[:7]
            elif splitted_data[i] == "Gw1":
                splitted_data[i + 3] = str(len(self.GW1[:7]))
                splitted_data[i + 4] = self.GW1[:7]
            elif splitted_data[i] == "Lf1":
                splitted_data[i + 4] = self.Lf1
            elif splitted_data[i] == "Gt1":
                splitted_data[i + 3] = str(len(self.custel1[:1]))
                splitted_data[i + 4] = self.custel1
            elif splitted_data[i] == "Mp1":
                splitted_data[i + 4] = self.prio1
            elif splitted_data[i] == "Mt1":
                splitted_data[i + 3] = str(len(self.MText1[:7]))
                splitted_data[i + 4] = self.MText1[:7]
            elif splitted_data[i] == "Gw2":
                splitted_data[i + 3] = str(len(self.GW2[:7]))
                splitted_data[i + 4] = self.GW2[:7]
            elif splitted_data[i] == "Lf2":
                splitted_data[i + 4] = self.Lf2
            elif splitted_data[i] == "Gt2":
                splitted_data[i + 3] = str(len(self.custel2[:1]))
                splitted_data[i + 4] = self.custel2
            elif splitted_data[i] == "Mp2":
                splitted_data[i + 4] = self.prio2
            elif splitted_data[i] == "Mt2":
                splitted_data[i + 3] = str(len(self.MText2[:7]))
                splitted_data[i + 4] = self.MText2[:7]
            elif splitted_data[i] == "Gw3":
                splitted_data[i + 3] = str(len(self.GW3[:7]))
                splitted_data[i + 4] = self.GW3[:7]
            elif splitted_data[i] == "Lf3":
                splitted_data[i + 4] = self.Lf3
            elif splitted_data[i] == "Gt3":
                splitted_data[i + 3] = str(len(self.custel3[:1]))
                splitted_data[i + 4] = self.custel3
            elif splitted_data[i] == "Mp3":
                splitted_data[i + 4] = self.prio3
            elif splitted_data[i] == "Mt3":
                splitted_data[i + 3] = str(len(self.MText3[:7]))
                splitted_data[i + 4] = self.MText3[:7]
            elif splitted_data[i] == "Gw4":
                splitted_data[i + 3] = str(len(self.GW4[:7]))
                splitted_data[i + 4] = self.GW4[:7]
            elif splitted_data[i] == "Lf4":
                splitted_data[i + 4] = self.Lf4
            elif splitted_data[i] == "Gt4":
                splitted_data[i + 3] = str(len(self.custel4[:1]))
                splitted_data[i + 4] = self.custel4
            elif splitted_data[i] == "Mp4":
                splitted_data[i + 4] = self.prio3
            elif splitted_data[i] == "Mt4":
                splitted_data[i + 3] = str(len(self.MText4[:7]))
                splitted_data[i + 4] = self.MText4[:7]
        return ";".join(splitted_data)


class PrtFile():

    @staticmethod
    def write(filepath, data):
        with open(filepath, "w", encoding="utf-16-le") as new:
            new.write("\ufeff")
            for i in data:
                new.write(i)

    @staticmethod
    def read(filepath):
        data = []
        with open(filepath, encoding="utf-16") as file:
            for row in file:
                data.append(row)
        return data

    @staticmethod
    def getDir(key):
        standart = ""
        stdpath = osDir().getStdDir()
        if key == "MBIN":
            standart = stdpath + "MBIN_Standart.prt"
        elif key == "IDF":
            standart = stdpath + "IDF_Standart.prt"
        elif key == "MANA_900":
            standart = stdpath + "MANA_900_Standart.prt"
        elif key == "MANA_800":
            standart = stdpath + "MANA_800_Standart.prt"
        elif key == "MANA_700":
            standart = stdpath + "MANA_700_Standart.prt"
        return standart
