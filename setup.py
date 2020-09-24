#sudo apt-get install python3-pyqt5  
import  os
import platform
linux=["sudo apt-get install python3-pyqt5 -y",
"sudo apt-get install pyqt5-dev-tools -y",
"sudo apt-get install qttools5-dev-tools -y",
"sudo apt-get install bison build-essential gperf flex ruby python libasound2-dev libbz2-dev libcap-dev \
libcups2-dev libdrm-dev libegl1-mesa-dev libgcrypt11-dev libnss3-dev libpci-dev libpulse-dev libudev-dev \
libxtst-dev gyp ninja-build -y"]
if platform.system() =="Linux":
    for i in linux:
        os.system(i)
elif platform.system() =="Darwin":
    os.system("brew install pyqt")




