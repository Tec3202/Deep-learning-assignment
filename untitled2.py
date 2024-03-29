# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nJhet0HiplRX-ZEsCDjiNHV0SFVhaZuF

1. Data Preprocessing:
"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Load the Fashion MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data()

# Normalize the image data to range between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Reshape the data to fit the model input requirements
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# Convert the labels into one-hot vectors
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

"""2. Model Development:"""

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compile your model with an appropriate optimizer, loss function, and metrics
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

"""3. Model Training:"""

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

"""4. Evaluation and Analysis:"""

# Evaluate the model's performance on the test dataset
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')

# Plot the training and validation accuracy and loss over epochs
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Display sample images with their predicted and actual labels
predictions = model.predict(test_images)
sample_images = test_images[:5]

for i in range(5):
    plt.imshow(sample_images[i].reshape(28, 28), cmap='gray')
    plt.title(f"Actual: {tf.argmax(test_labels[i])}, Predicted: {tf.argmax(predictions[i])}")
    plt.show()