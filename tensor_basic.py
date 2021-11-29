# 경고 문구 제거해주는 코드
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

# 기본 텐서 -> 숫자,리스트 담는 곳(행렬 형태)
a = tf.constant([3,4,5],dtype=tf.float32)
b = tf.constant([[6,7,8]],dtype=tf.float32)
c = tf.constant([[1],[2],[3]],dtype=tf.float32)

# 기본 메소드
tf.print(tf.add(a,b))
tf.print(tf.matmul(b,c))

# 0행렬 만들기
zero = tf.zeros([2,2])
tf.print(zero)

# weight 저장하기(변수)
w = tf.Variable(2.0)
# weight 변경하기
w.assign(3)
tf.print(w)

