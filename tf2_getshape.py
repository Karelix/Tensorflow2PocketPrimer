import tensorflow as tf 

a = tf.constant(3.0)
print('a.shape:',a.get_shape())

b = tf.fill([2,3],5)
print(b.numpy())
print(b.get_shape())

c = tf.constant([[1.,2.,3.],[4.,5.,6.]])
print('c.shape:',c.get_shape())

d = tf.Variable([1,2,3])
print(d.value())