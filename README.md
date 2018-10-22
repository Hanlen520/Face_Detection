# Face_Detection
利用python实现人脸检测

# 开发环境：Ubuntu 18.04x64
# 开发步骤：
# 1、安装opencv环境
$sudo apt install aptitude
$sudo aptitude -f install
$sudo apt-get update
$sudo apt-get install build-essential
$sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
$sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
$git clone https://github.com/Itseez/opencv.git
# 2、编译安装
$cd opencv
$mkdir build
$cd build
$cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
$sudo apt install python-opencv
$python -c "import cv2; print dir(cv2)"
如果输出了很多cv2 的属性和函数名的字典，就表示成功
# 3、运行脚本
# cd ../..
# python main.py
4、查看检测后生成的图片faceExp_detected.png
我们会发现里面所有的人脸都被框起来了，说明检测成功
