from context import set_untrainable
import pytest
import tensorflow as tf
import tensorflow.keras.backend as K
import numpy as np


def get_trainable_layers(model):
    trainable_count = int(
        np.sum([K.count_params(p) for p in set(model.trainable_weights)]))

    return trainable_count


def create_dense_model(input_size, d1, d2):

    inputs = tf.keras.layers.Input(shape=input_size)
    x = tf.keras.layers.Dense(d1)(inputs)
    x = tf.keras.layers.Dense(d2)(x)
    model = tf.keras.models.Model(inputs=inputs, outputs = x)
    return model


def create_cnn_model(input_shape, f1,f2):
    inputs = tf.keras.layers.Input(shape=input_shape)
    x = tf.keras.layers.Conv2D(f1, (3,3))(inputs)
    x = tf.keras.layers.Conv2D(f2, (3,3))(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(1)(x)
    return tf.keras.models.Model(inputs = inputs, outputs = x)


def test_get_trainable_layers():
    model = create_dense_model((10,), 10, 10)
    print(model.summary())
    assert get_trainable_layers(model) == 220


def test_set_untrainable_on_dense1():
    model = create_dense_model((10,), 10,10)
    set_untrainable(model, 1)
    assert get_trainable_layers(model) == 110


def test_set_untrainable_on_dense2():
    model = create_dense_model((10,), 10,10)
    set_untrainable(model, 0)
    assert get_trainable_layers(model) == 0


def test_get_trainable_layers2():
    model = create_dense_model((33,), 27,41)
    assert get_trainable_layers(model) == 2066


def test_set_untrainable_on_dense3():
    model = create_dense_model((33,), 27,41)
    set_untrainable(model, 1)
    assert get_trainable_layers(model) == 1148


def test_set_untrainable_on_dense4():
    model = create_dense_model((33,), 27,41)
    set_untrainable(model, 0)
    assert get_trainable_layers(model) == 0


def test_get_trainable_layers3():
    model = create_cnn_model((28,28,1), 10,10)
    assert get_trainable_layers(model) == 100+910+5761


def test_set_untrainable_on_cnn1():
    model = create_cnn_model((28,28,1), 10, 10)
    set_untrainable(model,1)
    assert get_trainable_layers(model) == 5761


def test_set_untrainable_on_cnn2():
    model = create_cnn_model((28,28,1), 10, 10)
    set_untrainable(model,3)
    assert get_trainable_layers(model) == 5761 + 910


def test_set_untrainable_on_cnn3():
    model = create_cnn_model((28,28,1), 10, 10)
    set_untrainable(model,4)
    assert get_trainable_layers(model) == 5761 + 910 + 100


def test_set_untrainable_on_cnn4():
    model = create_cnn_model((28,28,1), 10, 10)
    set_untrainable(model,0)
    assert get_trainable_layers(model) == 0
