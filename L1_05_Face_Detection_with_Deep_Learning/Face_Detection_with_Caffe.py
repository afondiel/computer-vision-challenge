#!/usr/bin/python

#                          License Agreement
#                         3-clause BSD License
#
#       Copyright (C) 2018, Xperience.AI, all rights reserved.
#
# Third party copyrights are property of their respective owners.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#   * Neither the names of the copyright holders nor the names of the contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# This software is provided by the copyright holders and contributors "as is" and
# any express or implied warranties, including, but not limited to, the implied
# warranties of merchantability and fitness for a particular purpose are disclaimed.
# In no event shall copyright holders or contributors be liable for any direct,
# indirect, incidental, special, exemplary, or consequential damages
# (including, but not limited to, procurement of substitute goods or services;
# loss of use, data, or profits; or business interruption) however caused
# and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of
# the use of this software, even if advised of the possibility of such damage.

import cv2
import sys

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

#/!\ opencv deep neural net api for reading pre-trained models such as: caffe, tensorflow pytorch, darknet, onnx...

# create Caffe DNN object with pre-trained model, some defaults parameters 
## more details can be found: https://github.com/opencv/opencv/tree/4.x/samples/dnn
net = cv2.dnn.readNetFromCaffe("./models/caffe/deploy.prototxt", "./models/caffe/res10_300x300_ssd_iter_140000_fp16.caffemodel")

# Model parameters
in_width = 300
in_height = 300
mean = [104, 117, 123] 
conf_threshold = 0.7 # sensivility of the detections

while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    frame = cv2.flip(frame,1)
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]

    # Create a 4D blob from a frame.
    """
    @brief Preprocessing of the image to put in the right format
    
    - frame: image frame from video stream
    - 1.0 : rescaled the img based on the model range
    - (in_width, in_height): input size 
    - mean: mean value subtracted from all the images 
    - swapRB = False : opencv & caffe use the same convention for channel camera 
    - crop = False: resize the image
    """
    blob = cv2.dnn.blobFromImage(frame, 1.0, (in_width, in_height), mean, swapRB = False, crop = False)
    # Run a model
    net.setInput(blob)
    # model inference => replay result scoring and prediction
    detections = net.forward()
    ## Debugging
    # Detections:[i,j,k,l] => k: numbers of row, l:number of columns 
    # print(f'detections: {detections}, detections-shape: {detections.shape}')
    # print(f'detections-size: {detections.size}, detections-ndim: {detections.ndim}')
    # break
    
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            # drawing a box
            x_left_bottom = int(detections[0, 0, i, 3] * frame_width)
            y_left_bottom = int(detections[0, 0, i, 4] * frame_height)
            x_right_top = int(detections[0, 0, i, 5] * frame_width)
            y_right_top = int(detections[0, 0, i, 6] * frame_height)

            cv2.rectangle(frame, (x_left_bottom, y_left_bottom), (x_right_top, y_right_top), (0, 255, 0))
            label = "Confidence: %.4f" % confidence
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            cv2.rectangle(frame, (x_left_bottom, y_left_bottom - label_size[1]),
                                (x_left_bottom + label_size[0], y_left_bottom + base_line),
                                (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, label, (x_left_bottom, y_left_bottom),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    # time required to perform inference
    t, _ = net.getPerfProfile()
    label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
    cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)
