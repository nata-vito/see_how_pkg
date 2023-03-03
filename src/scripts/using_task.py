import mediapipe as mp
from mediapipe.tasks import python
from matplotlib import pyplot as plt
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

plt.rcParams.update({
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'xtick.labelbottom': False,
    'xtick.bottom': False,
    'ytick.labelleft': False,
    'ytick.left': False,
    'xtick.labeltop': False,
    'xtick.top': False,
    'ytick.labelright': False,
    'ytick.right': False
})

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

model_path      = 'gesture_recognizer.task'
base_options    = python.BaseOptions(model_asset_path = model_path)
options         = vision.GestureRecognizerOptions(base_options = base_options)
recognizer      = vision.GestureRecognizer.create_from_options(options)

