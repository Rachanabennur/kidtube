import tensorflow as tf
import cv2
import math
from Video_Classification.model import OpenNsfwModel, InputType
from Video_Classification.image_utils import create_tensorflow_image_loader
from Video_Classification.image_utils import create_yahoo_image_loader
import numpy as np


IMAGE_LOADER_TENSORFLOW = "tensorflow"
IMAGE_LOADER_YAHOO = "yahoo"


def classify_video(videoFile):
   
    model = OpenNsfwModel()
    frameTotal=0
    frameNsfw=0
    image_loader = IMAGE_LOADER_YAHOO
    input_type = InputType.TENSOR
    model_weights ='Video_Classification/data/open_nsfw-weights.npy'
   
    with tf.compat.v1.Session() as sess:
               
        model.build(weights_path=model_weights, input_type=input_type)

     
        fn_load_image = None

        if input_type == InputType.TENSOR:
            if image_loader == IMAGE_LOADER_TENSORFLOW:
                fn_load_image = create_tensorflow_image_loader(tf.Session(graph=tf.Graph()))
            else:
                fn_load_image = create_yahoo_image_loader()
        elif input_type == InputType.BASE64_JPEG:
            import base64
            fn_load_image = lambda filename: np.array([base64.urlsafe_b64encode(open(filename, "rb").read())])

        sess.run(tf.compat.v1.global_variables_initializer())


        print(videoFile)
        cap = cv2.VideoCapture(videoFile)
        # print(cap)
        # print("before")
        # cap.open(videoFile)
        frameRate = cap.get(5) #frame rate
        # print(frameRate)


        # print(cap.isOpened())
        while (cap.isOpened()):
            print("after")
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            print(ret)
            print(frame)
            if (ret != True):
                break
            if (frameId % math.floor(frameRate/4) == 0):
                cv2.imwrite('D:/Projects/fyp/kidtube/project/Video_Classification/images/temp.jpg', frame)
                image = fn_load_image('D:/Projects/fyp/kidtube/project/Video_Classification/images/temp.jpg')
                frameTotal= frameTotal+1

                predictions = \
                    sess.run(model.predictions,
                        feed_dict={model.input: image})
                if(predictions[0][1]>=0.50):
                    frameNsfw= frameNsfw+1
                    cv2.imwrite('Video_Classification/NSFW Frames/frame'+str(frameNsfw)+'.jpg', frame)



        cap.release()
        print("NSFW Frames : "+str(frameNsfw))
        print("Total Frames checked :"+str(frameTotal))
        if(frameNsfw==0):
            return False
        else:
            return True

    print("NSFW Frames : "+str(frameNsfw))
    print("Total Frames checked :"+str(frameTotal))
    # print(str((frameNsfw/frameTotal)*100))

