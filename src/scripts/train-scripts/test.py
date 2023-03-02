import os
import tensorflow as tf
import matplotlib.pyplot as plt
from mediapipe_model_maker import gesture_recognizer

dataset_path    = "hagrid-sample-30k-384p/hagrid_30k"
labels          = []
NUM_EXAMPLES    = 5

# Understanding the dataset
print(dataset_path)

for i in os.listdir(dataset_path):
    if os.path.isdir(os.path.join(dataset_path, i)):
        labels.append(i)

print(labels)


for label in labels:
    label_dir = os.path.join(dataset_path, label)
    examples_filenames  = os.listdir(label_dir)[:NUM_EXAMPLES]
    fig, axs = plt.subplots(1, NUM_EXAMPLES, figsize = (10, 2))
    
    for i in range(NUM_EXAMPLES):
        axs[i].imshow(plt.imread(os.path.join(label_dir, examples_filenames[i])))
        axs[i].get_xaxis().set_visible(False)
        axs[i].get_yaxis().set_visible(False)
        
    fig.suptitle(f'Showing {NUM_EXAMPLES} examples for {label}')

#plt.show()

# Load the dataset
data        = gesture_recognizer.Dataset.from_folder(
    dirname = dataset_path, 
    hparams = gesture_recognizer.HandDataPreprocessingParams()
)


train_data, rest_data       = data.split(0.8)
validation_data, test_data  = rest_data.split(0.5)

# Train the model
hparams             = gesture_recognizer.HParams(batch_size = 32, epochs = 15, learning_rate = 0.001, export_dir = 'exported_model_hagrid')
model_options       = gesture_recognizer.ModelOptions(dropout_rate = 0.2)
options             = gesture_recognizer.GestureRecognizerOptions(model_options = model_options, hparams = hparams)

model               = gesture_recognizer.GestureRecognizer.create(
    train_data      = train_data,
    validation_data = validation_data,
    options         = options
)

loss, acc = model.evaluate(test_data)
print(f'Test loss:{loss}, Test accuracy: {acc}')

# Export the model
model.export_model()