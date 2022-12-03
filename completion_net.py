import tensorflow as tf

class CompletionNetwork(tf.keras.layers.Layer):
    def __init__(self, shape=(32,32,3), **kwargs):
        self.conv1 = tf.keras.layers.Conv2D(8, 5, strides=1, input_shape=shape, padding='SAME')
        self.bnorm1 = tf.keras.layers.BatchNormalization()
        self.relu1 = tf.keras.layers.ReLU()

        self.conv2 = tf.keras.layers.Conv2D(16, 3, strides=2, padding='SAME')
        self.bnorm2 = tf.keras.layers.BatchNormalization()
        self.relu2 = tf.keras.layers.ReLU()

        self.conv3 = tf.keras.layers.Conv2D(16, 3, strides=1, padding='SAME')
        self.bnorm3 = tf.keras.layers.BatchNormalization()
        self.relu3 = tf.keras.layers.ReLU()

        self.conv4 = tf.keras.layers.Conv2D(32, 3, strides=2, padding='SAME')
        self.bnorm4 = tf.keras.layers.BatchNormalization()
        self.relu4 = tf.keras.layers.ReLU()

        self.conv5 = tf.keras.layers.Conv2D(32, 3, strides=1, padding='SAME')
        self.bnorm5 = tf.keras.layers.BatchNormalization()
        self.relu5 = tf.keras.layers.ReLU()

        # dilated convs
        self.dil1 = tf.keras.layers.Conv2D(32, 3, dilation_rate=2, padding='SAME')
        self.bnorm6 = tf.keras.layers.BatchNormalization()
        self.relu6 = tf.keras.layers.ReLU()

        self.dil2 = tf.keras.layers.Conv2D(32, 3, dilation_rate=4, padding='SAME')
        self.bnorm7 = tf.keras.layers.BatchNormalization()
        self.relu7 = tf.keras.layers.ReLU()

        self.dil3 = tf.keras.layers.Conv2D(32, 3, dilation_rate=6, padding='SAME')
        self.bnorm8 = tf.keras.layers.BatchNormalization()
        self.relu8 = tf.keras.layers.ReLU()

        # decoding
        self.conv6 = tf.keras.layers.Conv2D(32, 3, strides=1, padding='SAME')
        self.bnorm9 = tf.keras.layers.BatchNormalization()
        self.relu9 = tf.keras.layers.ReLU()

        self.conv_trans1 = tf.keras.layers.Conv2DTranspose(16, 4, strides=2)
        self.bnorm10 = tf.keras.layers.BatchNormalization()
        self.relu10 = tf.keras.layers.ReLU()

        self.conv7 = tf.keras.layers.Conv2D(16, 3, strides=1, padding='SAME')
        self.bnorm11 = tf.keras.layers.BatchNormalization()
        self.relu11 = tf.keras.layers.ReLU()

        self.conv_trans2 = tf.keras.layers.Conv2DTranspose(8, 4, strides=2)
        self.bnorm12 = tf.keras.layers.BatchNormalization()
        self.relu12 = tf.keras.layers.ReLU()

        self.conv8 = tf.keras.layers.Conv2D(4, 3, strides=1, padding='SAME')
        self.bnorm13 = tf.keras.layers.BatchNormalization()
        self.relu13 = tf.keras.layers.ReLU()

        self.conv9 = tf.keras.layers.Conv2D(3, 3, strides=1, padding='SAME', activation='sigmoid')

    def call(self, incomplete_images):
        x = self.relu1(self.bnorm1(self.conv1(incomplete_images)))
        x = self.relu2(self.bnorm2(self.conv2(x)))
        x = self.relu3(self.bnorm3(self.conv3(x)))
        x = self.relu4(self.bnorm4(self.conv4(x)))
        x = self.relu5(self.bnorm5(self.conv5(x)))

        x = self.relu6(self.bnorm6(self.dil1(x)))
        x = self.relu7(self.bnorm7(self.dil2(x)))
        x = self.relu8(self.bnorm8(self.dil3(x)))

        x = self.relu9(self.bnorm9(self.conv6(x)))
        x = self.relu10(self.bnorm10(self.conv_trans1(x)))
        x = self.relu11(self.bnorm11(self.conv7(x)))
        x = self.relu12(self.bnorm12(self.conv_trans2(x)))
        x = self.relu13(self.bnorm13(self.conv8(x)))

        return self.conv9(x)