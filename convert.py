import tensorflow as tf

# Load the TensorFlow model
model = tf.keras.models.load_model('C:/Users/Kannan kailash/OneDrive/Desktop/Cubethon/Facial Emotional Reg/models/saved_models/fer2013_simple_CNN-e88-a0.65.hdf5')

# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
# Set optimization options (optional)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# Convert the model
tflite_model = converter.convert()

# Save the TensorFlow Lite model to a file
with open('converted_model.tflite', 'wb') as f:
    f.write(tflite_model)
