# import tensorflow as tf
# from tensorflow.keras import layers, Model

# class GanModel(Model):
#     def __init__(self):
#         super(GanModel, self).__init__()
#         self.generator = self.build_generator()
#         self.discriminator = self.build_discriminator()

#     def build_generator(self):
#         model = tf.keras.Sequential()
#         model.add(layers.Dense(128, input_dim=100, activation='relu'))
#         model.add(layers.Dense(256, activation='relu'))
#         model.add(layers.Dense(512, activation='relu'))
#         model.add(layers.Dense(1024, activation='relu'))
#         model.add(layers.Dense(1, activation='sigmoid'))
#         return model

#     def build_discriminator(self):
#         model = tf.keras.Sequential()
#         model.add(layers.Dense(1024, input_dim=1, activation='relu'))
#         model.add(layers.Dense(512, activation='relu'))
#         model.add(layers.Dense(256, activation='relu'))
#         model.add(layers.Dense(1, activation='sigmoid'))
#         return model

#     def call(self, inputs):
#         return self.generator(inputs)


# import tensorflow as tf
# from tensorflow.keras import layers, Model

# class GanModel(Model):
#     def __init__(self):
#         super(GanModel, self).__init__()
#         self.generator = self.build_generator()
#         self.discriminator = self.build_discriminator()

#     def build_generator(self):
#         model = tf.keras.Sequential()
#         model.add(layers.Dense(128, input_dim=100, activation='relu'))
#         model.add(layers.Dense(256, activation='relu'))
#         model.add(layers.Dense(512, activation='relu'))
#         model.add(layers.Dense(1024, activation='relu'))
#         model.add(layers.Dense(1, activation='sigmoid'))
#         return model

#     def build_discriminator(self):
#         model = tf.keras.Sequential()
#         model.add(layers.Dense(1024, input_dim=1, activation='relu'))
#         model.add(layers.Dense(512, activation='relu'))
#         model.add(layers.Dense(256, activation='relu'))
#         model.add(layers.Dense(1, activation='sigmoid'))
#         return model

#     def call(self, inputs):
#         generated_data = self.generator(inputs)
#         discrimination = self.discriminator(generated_data)
#         return discrimination

import tensorflow as tf
from tensorflow.keras import layers, Model

class GanAgent(Model):
    def __init__(self):
        super(GanAgent, self).__init__()
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()

    def build_generator(self):
        model = tf.keras.Sequential([
            layers.Dense(128, input_dim=100, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(512, activation='relu'),
            layers.Dense(1024, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])
        return model

    def build_discriminator(self):
        model = tf.keras.Sequential([
            layers.Dense(1024, input_dim=1, activation='relu'),
            layers.Dense(512, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])
        return model

    def call(self, inputs):
        generated_data = self.generator(inputs)
        discrimination = self.discriminator(generated_data)
        return discrimination
