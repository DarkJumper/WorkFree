from syst.prt import *
from syst.fgr import *
import sys
from osfi.osdir import *

if __name__ == "__main__":
    file_dir = os.path.dirname(__file__)
    sys.path.append(file_dir)
    print(sys.version)
    test = prt(creat)
    test.std_path = osDir().getStdDir()
    test.new_file = osDir().getOutPrtDir()
    test.excel_path = osDir().getNormalDir()
    test.execute()
    print(test.status)