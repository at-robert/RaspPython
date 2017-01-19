import pyaudio

def getaudiodevices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print "Device Index = %d , Name = %s" %(i, p.get_device_info_by_index(i).get('name'))


#----------------------------------------------------------------------
if __name__ == "__main__":

    getaudiodevices()