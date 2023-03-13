import numpy
import cv2 as cv
import mediapipe as mp
from datetime import datetime
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


model_path = '/home/rota2030/test_ws/src/see_how_pkg/src/scripts/train-scripts/exported_model_hagrid/gesture_recognizer.task'
base_options = BaseOptions(model_asset_path = model_path)

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))
    
options = GestureRecognizerOptions(
    base_options    = BaseOptions(model_asset_path = model_path),
    running_mode    = VisionRunningMode.LIVE_STREAM,
    result_callback = print_result)

with GestureRecognizer.create_from_options(options) as recognizer:
    cap = cv.VideoCapture(0)
  
    while(True):
        currentDateAndTime = datetime.now()
        timestamp_ms = currentDateAndTime.timestamp() * 1000
        # Capture the video frame
        # by frame
        ret, frame = cap.read()
    
        # Display the resulting frame
        #cv.imshow('frame', frame)
        frame_1 = frame
        #print(timestamp_ms)
        
        mp_image = mp.packet_creator.create_image_frame(image_format = mp.ImageFormat.SRGB, data = frame_1)
        print(mp_image)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
        #gesture_recognize = recognizer.recognize(image = mp_image)
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv.destroyAllWindows()