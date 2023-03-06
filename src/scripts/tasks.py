import cv2 as cv
import mediapipe as mp

BaseOptions                 = mp.tasks.BaseOptions
GestureRecognizer           = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions    = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult     = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode           = mp.tasks.vision.RunningMode

model_path  = 'train-scripts/exported_model_hagrid/gesture_recognizer.task'
base_options =  BaseOptions(model_asset_path = model_path)

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('gesture recognition result: {}'.format(result))

options = GestureRecognizerOptions(
          base_options=BaseOptions(model_asset_path = model_path),
          running_mode=VisionRunningMode.LIVE_STREAM,
          result_callback=print_result
        )

cap = cv.VideoCapture(0)
fps = cap.get(cv.CAP_PROP_FPS)

while cap.isOpened():
    success, image = cap.read()
    
    while not success:
        success, image = cap.read()
    
    image.flags.writeable = False
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    
    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
    #mp_image = mp.Image(format = mp.ImageFormat.SRGB, data = image)
    with GestureRecognizer.create_from_options(options) as recognizer:
        recognizer.recognizer_async(image, fps)
    #print(fps)
    #recognizer.recognize_async(mp_image, fps)
