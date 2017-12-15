import picamera
import sys
import time



#----------------------------------------------------------------------
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf-8')

    camera = picamera.PiCamera()
    camera.start_preview()

    if(sys.argv[1] == 'd') & (len(sys.argv) > 1) :
        time.sleep(3)
        print("delay 3 seconds")
    else:
        s = raw_input("Camera Preview - enter any key to stop")

    camera.stop_preview()
