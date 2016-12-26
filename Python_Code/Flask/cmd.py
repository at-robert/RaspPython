 # coding=UTF-8
import os
from flask import Flask, render_template, Response
app = Flask(__name__)
 
@app.route('/')
@app.route('/<cmd>')
def index(cmd=None):
    """Video streaming home page."""
    if cmd == 'go':
        print 'go'
    elif cmd == 'stop':
        print 'stop'
    elif cmd == 'back':
        print 'back'
    elif cmd == 'right':
        print 'right'
    elif cmd == 'left':
        print 'left'
    return render_template('cmd.html',cmd=cmd)

@app.route('/LG_TV')
@app.route('/LG_TV/<cmd>')
def index_lg(cmd=None):
    """Video streaming home page."""
    if cmd == 'go':
        print 'LG_TV power'
        os.system('irsend SEND_ONCE LG_TV KEY_POWER')
    elif cmd == 'stop':
        print 'LG_TV VOL UP'
        os.system('irsend SEND_ONCE LG_TV KEY_VOLUMEUP')
    elif cmd == 'back':
        print 'LG_TV VOL DOWN'
        os.system('irsend SEND_ONCE LG_TV KEY_VOLUMEDOWN')
    elif cmd == 'right':
        print 'LG_TV right'
        os.system('irsend SEND_ONCE LG_TV KEY_RIGHT')
    elif cmd == 'left':
        print 'LG_TV left'
    elif cmd == 'rights':
        print 'LG_TV AV'
        os.system('irsend SEND_ONCE LG_TV KEY_A')
    elif cmd == 'lefts':
        print 'LG_TV lefts'
    return render_template('LG_TV.html',cmd=cmd)
    
@app.route('/DB0204')
@app.route('/DB0204/<cmd>')
def index_db0204(cmd=None):
    """Video streaming home page."""
    if cmd == 'go':
        print 'DB0204 up'
        os.system('irsend SEND_ONCE DB0204 KEY_UP')
    elif cmd == 'stop':
        print 'DB0204 enter'
        os.system('irsend SEND_ONCE DB0204 KEY_ENTER')
    elif cmd == 'back':
        print 'DB0204 down'
        os.system('irsend SEND_ONCE DB0204 KEY_DOWN')
    elif cmd == 'right':
        print 'DB0204 right'
        os.system('irsend SEND_ONCE DB0204 KEY_RIGHT')
    elif cmd == 'left':
        print 'DB0204 left'
        os.system('irsend SEND_ONCE DB0204 KEY_LEFT')
    elif cmd == 'rights':
        print 'DB0204 return'
        os.system('irsend SEND_ONCE DB0204 KEY_RETURN')
    elif cmd == 'lefts':
        print 'DB0204 power'
        os.system('irsend SEND_ONCE DB0204 KEY_POWER')
    return render_template('DB0204.html',cmd=cmd)

if __name__ == "__main__":  
    app.run('0.0.0.0') 


