import picamera
import sys



#----------------------------------------------------------------------
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf-8')

    camera = picamera.PiCamera()
    camera.start_preview()
    s = raw_input("Camera Preview - enter any key to stop")
    camera.stop_preview()
