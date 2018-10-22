# coding:utf-8
# 引入opencv库
import cv2
"""
1 加载分类器 cv2.CascadeClassifier
CascadeClassifier是Opencv中做人脸检测时候的一个级联分类器，
该类中封装的是目标检测机制即滑动窗口机制+级联分类器的方式。
数据结构包括Data和FeatureEvaluator两个主要部分。
Data中存储的是从训练获得的xml文件中载入的分类器数据；
而FeatureEvaluator中是关于特征的载入、存储和计算。
这里采用的训练文件是OpenCV中默认提供的haarcascade_frontalface_default.xml。
至于Haar，LBP的具体原理，可以参考opencv的相关文档，简单地，可以理解为人脸的特征数据。
"""
face_patterns = cv2.CascadeClassifier('/home/username/Face_Detection/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
"""
2 加载目标图片
人脸识别系统一般分为：人脸图像采集、人脸图像预处理、人脸图像特征提取以及匹配与识别。 
以下读入的是一张nvidia与linkface签署战略合作时的集体照
"""
sample_image = cv2.imread('faceExp.jpg')
"""
3 多尺度检测 detectMultiScale
调用 CascadeClassifier 中的调detectMultiScale函数进行多尺度检测，多尺度检测中会调用单尺度的方法detectSingleScale。 
参数说明：
	scaleFactor 是图像的缩放因子
	minNeighbors 为每一个级联矩形应该保留的邻近个数，可以理解为一个人周边有几个人脸
	minSize 是检测窗口的大小，当图片人脸较多较小时可适当缩小人脸框尺寸
这些参数都是可以针对图片进行调整的，处理结果返回一个人脸的矩形对象列表。
"""
faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(80, 80))
""" 
4 为每个人脸画一个框
循环读取人脸的矩形对象列表，获得人脸矩形的坐标和宽高， 
然后在原图片中画出该矩形框，调用的是OpenCV的rectangle方法，其中矩形框的颜色等是可调整的。
"""
for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
# 保存检测后的结果图片
cv2.imwrite('faceExp_detected.png', sample_image);
