import shutil
import csv


def writePRT(filepath, data):
    with open(filepath, "w", encoding="utf-16-le") as new:
        new.write("\ufeff")
        for i in data:
            new.write(i)


def readPRT(filepath):
    data = []
    with open(filepath, encoding="utf-16") as file:
        for row in file:
            data.append(row)
    return data


def paraMBIN(data, M1, M0):
    splitted_data = data.split(";")
    for i in range(len(splitted_data)):
        if splitted_data[i] == "MELD0":
            splitted_data[i] = M0
            splitted_data[i - 1] = str(len(M0))
        elif splitted_data[i] == "MELD1":
            splitted_data[i] = M1
            splitted_data[i - 1] = str(len(M1))
        elif splitted_data[i] == "MELDT":
            splitted_data[i] = M1
            splitted_data[i - 1] = str(len(M1))
    return ";".join(splitted_data)


def paraIDF(data):
    print(data)
    return 0


def reform(data):
    print(data)
    Baustein = data[0]
    MSRName = data[1]
    KurzText = data[2]
    LangText = data[3]
    VarText = data[4]
    M0 = data[5]
    M1 = data[6]
    newfile = []
    newdir = "C:\\Users\p.schwarz\VSCode\WorkFree\Ausgabe\{0}.prt".format(MSRName)
    standart = ""
    if Baustein == "MBIN":
        standart = "C:\\Users\p.schwarz\VSCode\WorkFree\{0}.prt".format("MBIN_Standart")
    elif Baustein == "IDF":
        standart = "C:\\Users\p.schwarz\VSCode\WorkFree\{0}.prt".format("IDF_Standart")
    shutil.copyfile(standart, newdir)
    data = readPRT(standart)
    for row in data:
        if "Standart" in row:
            newfile.append(row.replace("Standart", MSRName))
        elif "[PARA:PARADATA]" in row:
            if Baustein == "MBIN":
                newfile.append(paraMBIN(row, M1, M0))
            elif Baustein == "IDF":
                newfile.append(row)
            else:
                newfile.append(row)
        elif "M54321" in row:
            if "Kurztext" in row:
                row = row.replace("Kurztext", KurzText)
            if "Langtext" in row:
                row = row.replace("Langtext", LangText)
            newfile.append(row.replace("M54321", MSRName))
        elif "54321" in row and Baustein == "MBIN":
            if "Variabel" in row:
                row = row.replace("Variabel", VarText)
            newfile.append(row.replace("54321", MSRName))
        elif "54321" in row and Baustein == "IDF":
            if "Variabel" in row:
                row = row.replace("Variabel", MSRName)
            newfile.append(row.replace("54321", MSRName[1:]))
        else:
            newfile.append(row)

    writePRT(newdir, newfile)


if __name__ == "__main__":
    with open("C:\\Users\p.schwarz\VSCode\WorkFree\Liste.csv", newline='') as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
        for row in reader:
            reform(row)
