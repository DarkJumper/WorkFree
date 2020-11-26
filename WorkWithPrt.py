from os import stat


class Baustein():
    name = "leer"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    MBA = "0.0"
    MBE = "100.0"
    DIM = "%"
    M0 = ""
    M1 = ""
    GW1 = ""
    Lf1 = ""
    GW2 = ""
    Lf2 = ""
    GW3 = ""
    Lf3 = ""
    GW4 = ""
    Lf4 = ""
    custel1 = "0"
    custel2 = "0"
    custel3 = "0"
    custel4 = "0"
    prio1 = "-"
    MText1 = ""
    prio2 = "-"
    MText2 = ""
    prio3 = "-"
    MText3 = ""
    prio4 = "-"
    MText4 = ""

    def MSR(self, data):
        newfile = []
        for row in data:
            if "Standart" in row:
                newfile.append(row.replace("Standart", self.MSRName))
            elif "[PARA:PARADATA]" in row:
                if self.name == "MBIN":
                    newfile.append(self.paraMBIN(row))
                elif self.name == "IDF":
                    newfile.append(self.paraIDF(row))
                elif self.name == "MANA_900":
                    newfile.append(self.paraMANA900(row))
                elif self.name == "MANA_800":
                    newfile.append(self.paraMANA800(row))
                elif self.name == "MANA_700":
                    newfile.append(self.paraMANA700(row))
                else:
                    newfile.append(row)
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
            else:
                newfile.append(row)
        return newfile

    def paraMBIN(self, data):
        splitted_data = data.split(";")
        for i in range(len(splitted_data)):
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
        return ";".join(splitted_data)

    def paraIDF(self, data):
        return data

    def paraMANA900(self, data):
        splitted_data = data.split(";")
        for i in range(len(splitted_data)):
            if splitted_data[i] == "Mba":
                splitted_data[i + 3] = str(len(self.MBA[:7]))
                splitted_data[i + 4] = self.MBA[:7]
            if splitted_data[i] == "Mbe":
                splitted_data[i + 3] = str(len(self.MBE[:7]))
                splitted_data[i + 4] = self.MBE[:7]
            if splitted_data[i] == "Dim":
                splitted_data[i + 3] = str(len(self.DIM[:7]))
                splitted_data[i + 4] = self.DIM[:7]
            if splitted_data[i] == "Gw1":
                splitted_data[i + 3] = str(len(self.GW1[:7]))
                splitted_data[i + 4] = self.GW1[:7]
            if splitted_data[i] == "Lf1":
                splitted_data[i + 4] = self.Lf1
            if splitted_data[i] == "Gt1":
                splitted_data[i + 3] = str(len(self.custel1[:1]))
                splitted_data[i + 4] = self.custel1
            if splitted_data[i] == "Mp1":
                splitted_data[i + 4] = self.prio1
            if splitted_data[i] == "Mt1":
                splitted_data[i + 3] = str(len(self.MText1[:7]))
                splitted_data[i + 4] = self.MText1[:7]
            if splitted_data[i] == "Gw2":
                splitted_data[i + 3] = str(len(self.GW2[:7]))
                splitted_data[i + 4] = self.GW2[:7]
            if splitted_data[i] == "Lf2":
                splitted_data[i + 4] = self.Lf2
            if splitted_data[i] == "Gt2":
                splitted_data[i + 3] = str(len(self.custel2[:1]))
                splitted_data[i + 4] = self.custel2
            if splitted_data[i] == "Mp2":
                splitted_data[i + 4] = self.prio2
            if splitted_data[i] == "Mt2":
                splitted_data[i + 3] = str(len(self.MText2[:7]))
                splitted_data[i + 4] = self.MText2[:7]
        return ";".join(splitted_data)

    def paraMANA800(self, data):
        return data

    def paraMANA700(self, data):
        return data


class MBIN(Baustein):
    name = "MBIN"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    M0 = ""
    M1 = ""
    prio1 = "-"


class IDF(Baustein):
    name = "IDF"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""


class MANA900(Baustein):
    name = "MANA_900"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    MBA = "0.0"
    MBE = "100.0"
    DIM = "%"
    GW1 = ""
    Lf1 = ""
    GW2 = ""
    Lf2 = ""
    GW3 = ""
    Lf3 = ""
    GW4 = ""
    Lf4 = ""
    custel1 = "0"
    custel2 = "0"
    custel3 = "0"
    custel4 = "0"
    prio1 = "-"
    MText1 = ""
    prio2 = "-"
    MText2 = ""
    prio3 = "-"
    MText3 = ""
    prio4 = "-"
    MText4 = ""


class MANA800(Baustein):
    name = "MANA_800"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    MBA = "0.0"
    MBE = "100.0"
    DIM = "%"
    GW1 = ""
    Lf1 = ""
    GW2 = ""
    Lf2 = ""
    GW3 = ""
    Lf3 = ""
    GW4 = ""
    Lf4 = ""
    custel1 = "0"
    custel2 = "0"
    custel3 = "0"
    custel4 = "0"
    prio1 = "-"
    MText1 = ""
    prio2 = "-"
    MText2 = ""
    prio3 = "-"
    MText3 = ""
    prio4 = "-"
    MText4 = ""


class MANA700(Baustein):
    name = "MANA_700"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    MBA = "0.0"
    MBE = "100.0"
    DIM = "%"
    GW1 = ""
    Lf1 = ""
    GW2 = ""
    Lf2 = ""
    GW3 = ""
    Lf3 = ""
    GW4 = ""
    Lf4 = ""
    custel1 = "0"
    custel2 = "0"
    custel3 = "0"
    custel4 = "0"
    prio1 = "-"
    MText1 = ""
    prio2 = "-"
    MText2 = ""
    prio3 = "-"
    MText3 = ""
    prio4 = "-"
    MText4 = ""


class MSRdescribe():

    def __init__(self, args):
        if args[0] == "MBIN":
            self.Baustein_state = MBIN()
            self.Baustein_state.MSRName = args[1]
            self.Baustein_state.KurzText = args[2]
            self.Baustein_state.LangText = args[3]
            self.Baustein_state.VarName = args[1]
            self.Baustein_state.VarText = args[4]
            self.Baustein_state.M0 = args[5]
            self.Baustein_state.M1 = args[6]
            self.Baustein_state.prio1 = args[10]
        if args[0] == "IDF":
            self.Baustein_state = IDF()
            self.Baustein_state.MSRName = args[1]
            self.Baustein_state.KurzText = args[2]
            self.Baustein_state.LangText = args[3]
            self.Baustein_state.VarName = args[1][1:]
            self.Baustein_state.VarText = args[4]
        if "MANA" in args[0]:
            if "900" in args[0]:
                self.Baustein_state = MANA900()
            elif "800" in args[0]:
                self.Baustein_state = MANA800()
            elif "700" in args[0]:
                self.Baustein_state = MANA700()
            self.Baustein_state.MSRName = args[1]
            self.Baustein_state.KurzText = args[2]
            self.Baustein_state.LangText = args[3]
            self.Baustein_state.VarName = args[1]
            self.Baustein_state.VarText = args[4]
            self.Baustein_state.MBA = args[7]
            self.Baustein_state.MBE = args[8]
            self.Baustein_state.DIM = args[9]
            self.Baustein_state.prio1 = args[10]
            self.Baustein_state.GW1 = args[11]
            self.Baustein_state.Lf1 = args[12]
            self.Baustein_state.custel1 = args[13]
            self.Baustein_state.MText1 = args[14]
            self.Baustein_state.GW2 = args[15]
            self.Baustein_state.Lf2 = args[16]
            self.Baustein_state.custel2 = args[17]
            self.Baustein_state.MText2 = args[18]
            self.Baustein_state.GW3 = args[19]
            self.Baustein_state.Lf3 = args[20]
            self.Baustein_state.custel3 = args[21]
            self.Baustein_state.MText3 = args[22]
            self.Baustein_state.GW4 = args[23]
            self.Baustein_state.Lf4 = args[24]
            self.Baustein_state.custel4 = args[25]
            self.Baustein_state.MText4 = args[26]

    def change(self, data):
        return self.Baustein_state.MSR(data)


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
        if key == "MBIN":
            standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\MBIN_Standart.prt"
        elif key == "IDF":
            standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\IDF_Standart.prt"
        elif key == "MANA_900":
            standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\MANA_900_Standart.prt"
        elif key == "MANA_800":
            standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\MANA_800_Standart.prt"
        elif key == "MANA_700":
            standart = "C:\\Users\p.schwarz\VSCode\WorkFree\Standarts\MANA_700_Standart.prt"
        return standart
