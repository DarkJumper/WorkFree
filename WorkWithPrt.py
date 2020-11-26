class Baustein():
    name = "leer"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    M0 = ""
    M1 = ""
    prio1 = 5

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


class MBIN(Baustein):
    name = "MBIN"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""
    M0 = ""
    M1 = ""
    prio1 = 5


class IDF(Baustein):
    name = "IDF"
    MSRName = ""
    KurzText = ""
    LangText = ""
    VarName = ""
    VarText = ""


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
            self.Baustein_state.prio1 = args[7]
        if args[0] == "IDF":
            self.Baustein_state = IDF()
            self.Baustein_state.MSRName = args[1]
            self.Baustein_state.KurzText = args[2]
            self.Baustein_state.LangText = args[3]
            self.Baustein_state.VarName = args[1][1:]
            self.Baustein_state.VarText = args[4]

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