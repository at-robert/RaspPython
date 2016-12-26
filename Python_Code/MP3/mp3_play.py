
import re
import os
import sys
import shutil
import chardet

#----------------------------------------------------------------------

#----------------------------------------------------------------------
def search_file(folder):

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".mp3"):
                #newfile = re.sub(r"\[hsaaaaaa-eyny\]","", folder + file)
                newfile = folder + file
                print "%s" %(newfile)
                cmdline = "omxplayer -o local %s" %(newfile)
                os.system(cmdline)
#----------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'no argument; Usage: python mp3_play.py IN_PATH'
        sys.exit()

    target_path = str(sys.argv[1])
    print "Target Path = %s" %(target_path)
    search_file(target_path)
