import tensorflow as tf


height = [170,180,175,160]
shoes = [260,270,265,255]

a = tf.Variable(0.1)
b = tf.Variable(0.2)


def loss_func():
    h = height * a + b
    return tf.square(shoes - h)

# 경사 하강법 사용하기
opt = tf.keras.optimizers.Adam(learning_rate = 0.1) # 최적화 함수 설정

for _ in range(300):
    opt.minimize(loss_func,var_list = [a,b])    # minimize(손실함수,변경할 가중치 리스트)
    tf.print(a, b)

print("예측 신발 사이즈: ",height*a+b)