import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('/home/rota2030/test_ws/src/see_how_pkg/src/scripts/train-scripts/')
tflite_model = converter.convert()

with open('model.tflite', 'wb') as f:
    f.write(tflite_model)