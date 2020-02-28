import numpy as np
import tensorflow as tf
import keras as kr

model=kr.Sequential([kr.layers.Dense(units=1,input_shape=[1])])
model.compile(optimizer='sgd',loss='mean_squared_error')

xs=np.array([-1.0,0.0,1.0,2.0,3.0,4.0])
ys=np.array([-3.0,-1.0,1.0,3.0,5.0,7.0])

model.fit(xs,ys,epochs=5000)
print(model.predict([100.0]))
