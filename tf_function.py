import tensorflow as tf 

@tf.function
def compute_values():
  a = tf.add(tf.constant(4),tf.constant(2))
  return a

result = compute_values()

print(result)