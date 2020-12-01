import os
import json
from sys import platform as _platform


class osDir():

    def getNormalDir(self):
        if _platform == "linux" or _platform == "linux2":
            pass
        elif _platform == "darwin":
            return "{0}/".format(os.getcwd())
        elif _platform == "win64":
            return "{0}\\".format(os.getcwd())
        elif _platform == "win32":
            return "{0}\\".format(os.getcwd())

    def getStdDir(self):
        with open('setting.json', 'r') as file:
            obj = json.load(file)
            if _platform == "linux" or _platform == "linux2":
                pass
            elif _platform == "darwin":
                return "{0}/{1}/".format(os.getcwd(), obj["stdDir"])
            elif _platform == "win64":
                return "{0}\\{1}\\".format(os.getcwd(), obj["stdDir"])
            elif _platform == "win32":
                return "{0}\\{1}\\".format(os.getcwd(), obj["stdDir"])

    def getOutPrtDir(self):
        with open('setting.json', 'r') as file:
            obj = json.load(file)
            if _platform == "linux" or _platform == "linux2":
                pass
            elif _platform == "darwin":
                return "{0}/{1}/{2}/".format(os.getcwd(), obj["outputDir"], obj["prtDir"])
            elif _platform == "win64":
                return "{0}\\{1}\\{2}\\".format(os.getcwd(), obj["outputDir"], obj["prtDir"])
            elif _platform == "win32":
                return "{0}\\{1}\\{2}\\".format(os.getcwd(), obj["outputDir"], obj["prtDir"])

    def getOutFgrDir(self):
        with open('setting.json', 'r') as file:
            obj = json.load(file)
            if _platform == "linux" or _platform == "linux2":
                pass
            elif _platform == "darwin":
                return "{0}/{1}/{2}/".format(os.getcwd(), obj["outputDir"], obj["fgrDir"])
            elif _platform == "win64":
                return "{0}\\{1}\\{2}\\".format(os.getcwd(), obj["outputDir"], obj["fgrDir"])
            elif _platform == "win32":
                return "{0}\\{1}\\{2}\\".format(os.getcwd(), obj["outputDir"], obj["fgrDir"])
