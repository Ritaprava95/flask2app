import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import flask
import os
import threading
import time

class GUIWindow():
    def __init__(self,title):
        self.title= title

    def start_window(self):
        host=self.host
        if host==None:
            host="http://127.0.0.1:5000"
        app = QApplication(sys.argv)
        web = QWebEngineView()
        web.setWindowTitle(self.title)

        web.load(QUrl(host))

        web.show()

        exit_code=app.exec_()
        
        sys.exit(exit_code)

    def run_server(self):
        host= self.host
        port=self.port
        if host is None and port is None:
            self.app.run()
        elif host is None and port is not None:
            app.run(port=str(port))
        else:
            app.run(host= host,port=str(port))


    def run(self,app,host=None,port=None):
        self.app=app
        self.host= host
        self.port=port
        app=threading.Thread(target=self.run_server)
        #window=threading.Thread(target=self.start_window)
        #window.start()
        #window.join()
        app.daemon = True  
        app.start()
        time.sleep(1)
        self.start_window()
        app.join()
        

    
#start_window()