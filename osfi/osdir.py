import os
import json
from sys import platform as _platform


class osDir():

    def getOutputDir(self):
        with open('setting.json', 'r') as file:
            obj = json.load(file)
            if _platform == "linux" or _platform == "linux2":
                pass
            elif _platform == "darwin":
                dir = "{0}/{1}/".format(os.getcwd(), obj["outputDir"])
                return dir
            elif _platform == "win64":
                pass

    def getNormalDir(self):
        if _platform == "linux" or _platform == "linux2":
            pass
        elif _platform == "darwin":
            dir = "{0}/".format(os.getcwd())
            return dir
        elif _platform == "win64":
            pass

    def getStdDir(self):
        with open('setting.json', 'r') as file:
            obj = json.load(file)
            if _platform == "linux" or _platform == "linux2":
                pass
            elif _platform == "darwin":
                dir = "{0}/{1}/".format(os.getcwd(), obj["stdDir"])
                return dir
            elif _platform == "win64":
                pass