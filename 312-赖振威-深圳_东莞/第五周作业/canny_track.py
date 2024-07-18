#!/usr/bin/env python
# encoding=gbk
# ����������ָ�� Python �������Լ������ļ�����

'''
Canny��Ե��⣺�Ż��ĳ���
'''

import cv2
import numpy as np 

# ���� CannyThreshold ����������ִ�� Canny ��Ե���
def CannyThreshold(lowThreshold):
    # �ԻҶ�ͼ����и�˹ģ������
    detected_edges = cv2.GaussianBlur(gray,(3,3),0) # ��˹�˲�
    print(detected_edges)
    # ��ʾ���
    cv2.imshow('detect_edges', detected_edges)
    '''
    [[162 162 162 ... 167 152 142]
     [162 162 162 ... 167 152 142]
     [162 162 162 ... 167 152 142]
     ...
     [ 44  46  49 ... 102 101 100]
     [ 44  46  50 ... 103 104 105]
     [ 44  47  51 ... 103 106 107]]
    '''

    # ���� cv2.Canny() ����ִ�� Canny ��Ե���
    detected_edges = cv2.Canny(detected_edges,
            lowThreshold,
            lowThreshold*ratio,
            apertureSize = kernel_size)  #��Ե���
    print(detected_edges)  # ��Ե������
    # ��ʾ���
    cv2.imshow('detected_edges', detected_edges)
    '''
    [[  0   0   0 ...   0 255   0]
     [  0   0   0 ...   0 255   0]
     [  0   0   0 ...   0 255   0]
     ...
     [  0 255   0 ...   0   0 255]
     [  0   0 255 ...   0   0   0]
     [  0 255   0 ...   0 255   0]]
    ��δ������ڵ��� OpenCV �� Canny ��Ե��⺯�� cv2.Canny()���������н��ͣ�
    detected_edges = cv2.Canny(detected_edges,����һ�д�������� cv2.Canny() ���������ĵ�һ�������� detected_edges������һ��������˹ģ��������ͼ��ͨ���ǻҶ�ͼ�����ڽ��б�Ե��⡣
    lowThreshold,������ Canny ��Ե���ĵ���ֵ����������һ�����������ڿ��Ʊ�Ե���������ȡ������ݶȵ��ڵ���ֵ�ı�Ե��ᱻ������
    lowThreshold * ratio,������� ratio ��һ��ϵ����ͨ������Ϊ 3�����ڼ��� Canny ��Ե���ĸ���ֵ������ֵ�ǵ���ֵ�ı���������ȷ��ǿ��Ե����ֵ�����ϵ����ѡ���Ǹ��ݾ���;���Ӧ�ó����������ġ�
    apertureSize=kernel_size)��apertureSize ����ָ�� Sobel ���ӵĿ׾���С�������ڼ���ͼ����ݶȡ�kernel_size ��һ��������ͨ������Ϊ 3����ʾʹ�� 3x3 �� Sobel ���ӽ����ݶȼ��㡣
    �ۺ���������һ�д���������ǵ��� Canny ��Ե����㷨���������˵���ֵ������ֵ���� Sobel ���ӵĿ׾���С�Ȳ����������ھ�����˹ģ��������ͼ����ִ�б�Ե��⡣
    '''
 
    # just add some colours to edges from original image.
    # ����⵽�ı�Ե������ԭʼͼ����
    dst = cv2.bitwise_and(img,img, mask=detected_edges)  # ��ԭʼ��ɫ��ӵ����ı�Ե��
    print(dst)
    # ��ʾ���
    cv2.imshow('canny demo',dst)
    '''
    ��δ���ʹ���� OpenCV �� cv2.bitwise_and() ���������ҽ���һ�£�
    dst = cv2.bitwise_and(img,img,mask = detected_edges)�����д���������ǽ���⵽�ı�Ե������ԭʼͼ���ϣ�����һ���µ�ͼ�� dst��
    img������ԭʼ�Ĳ�ɫͼ�񣬼�����ͼ��
    mask = detected_edges������� detected_edges �Ǿ��� Canny ��Ե����õ��ı�Եͼ������һ����ֵͼ�����б�Ե����ֵΪ���㣬�Ǳ�Ե����ֵΪ�㡣
    �� cv2.bitwise_and() �����У�mask ����ָ����һ�����룬������������Щλ�ý���λ�����㡣
    ������˵���������Ὣԭʼͼ���е�����ֵ�� detected_edges �е�����ֵ���������ص�λ�����㡣ֻ�е���������ֵΪ����ʱ���Żᱣ��ԭʼͼ���ж�Ӧλ�õ�����ֵ���������㡣������ʵ���˽���Ե������ԭʼͼ���ϵ�Ч����
    �ۺ����������д���������ǽ����� Canny ��Ե����õ��ı�Եͼ�������ԭʼ��ɫͼ���ϣ�����һ���µ�ͼ�� dst������ֻ�����˱�Ե���֡�
    '''

# ��ʼ������
lowThreshold = 0
max_lowThreshold = 100  
ratio = 3  
kernel_size = 3

# ��ȡͼ��ת��Ϊ�Ҷ�ͼ��
img = cv2.imread('lenna.png')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # ת����ɫͼ��Ϊ�Ҷ�ͼ

# ��������������ʾ���
cv2.namedWindow('canny demo')  
  
#���õ��ڸ�,
'''
�����ǵڶ���������cv2.createTrackbar()
����5����������ʵ������������������ʹ����֪����ʲô��˼��
��һ�������������trackbar���������
�ڶ��������������trackbar����������������
�����������������trackbar��Ĭ��ֵ,Ҳ�ǵ��ڵĶ���
���ĸ������������trackbar�ϵ��ڵķ�Χ(0~count)
������������ǵ���trackbarʱ���õĻص�������
'''
# �������������ڵ��ڵ���ֵ����
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)

# ��ʼ����Ե���
CannyThreshold(0)  # initialization

# �ȴ����� ESC ���˳�����
if cv2.waitKey(0) == 27:  #wait for ESC key to exit cv2
    cv2.destroyAllWindows()  
