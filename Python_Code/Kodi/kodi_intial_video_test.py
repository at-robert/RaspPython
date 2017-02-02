# coding=UTF-8
import re
import os
import sys
import shutil
import time


#----------------------------------------------------------------------
if __name__ == "__main__":

        view_time = 30
        print "KODI initial Video Test scheme"
        os.system('kodi-send --action="PlayerControl(Stop)"')
        time.sleep(3)
        os.system('kodi-send --action="PlayMedia(/media/sda5-usb-ST912081_7AS_ST9/Video/鷸Piper_DD51_DTS/Piper.2016.720p.BluRay.DD5.1.x264-decibeL[EtHD].mkv)"')
        os.system('kodi-send --action="Action(Select)"')
        time.sleep(view_time)
        os.system('kodi-send --action="PlayerControl(Stop)"')
        time.sleep(3)
        os.system('kodi-send --action="PlayMedia(/media/sda5-usb-ST912081_7AS_ST9/Video/鷸Piper_DD51_DTS/Piper.2016.PROPER.BluRay.REMUX.AVC.DTS.HD-MA.7.1-EPSiLON.mkv)"')
        os.system('kodi-send --action="Action(Select)"')
        time.sleep(view_time)
        os.system('kodi-send --action="PlayerControl(Stop)"')
        time.sleep(3)
        os.system('kodi-send --action="PlayMedia(/media/sda5-usb-ST912081_7AS_ST9/Video/馬^ϯ^ٽ_DTS/Macbeth 2015 1080p BluRay x264 DTS-JYK.mkv)"')
        os.system('kodi-send --action="Action(Select)"')
        time.sleep(view_time)
        os.system('kodi-send --action="PlayerControl(Stop)"')
        time.sleep(3)
        os.system('kodi-send --action="PlayMedia(/media/sda5-usb-ST912081_7AS_ST9/Video/251 AC3 2.0 & AC35.1 - Daily Show with commercials.m2ts)"')
        os.system('kodi-send --action="Action(Select)"')
        time.sleep(view_time*2)
        os.system('kodi-send --action="PlayerControl(Stop)"')
        time.sleep(3)
        os.system('kodi-send --action="PlayMedia(/media/sda5-usb-ST912081_7AS_ST9/Video/Dolby_Digital_Plus/dolby_digital_plus_channel_check_lossless-DWEU.mkv)"')
        os.system('kodi-send --action="Action(Select)"')
        time.sleep(view_time)
        os.system('kodi-send --action="PlayerControl(Stop)"')
        os.system('kodi-send --action="Action(PreviousMenu)"')