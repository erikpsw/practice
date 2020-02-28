import tensorflow as tf
from tensorflow import keras

fashion_mnist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()

import matplotlib.pyplot as plt
plt.imshow(train_images[3])
print(train_labels[3])
print(train_images[3])
plt.show()

train_images=train_images.reshape(60000,28,28,1)
train_images=train_images/255.0
test_images=test_images.reshape(10000,28,28,1)
test_images=test_images/255.0

model=tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64,(3,3),activation='relu',
                                                input_shape=(28,28,1)),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy')
model.summary()
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.4):
            print("\nLoss is now so cancelling training")
            self.model.stop_training=True

callbacks=myCallback()
model.fit(train_images,train_labels,epochs=5,callbacks=[callbacks])

model.evaluate(test_images,test_labels)
test_los=model.evaluate(test_images,test_labels)

