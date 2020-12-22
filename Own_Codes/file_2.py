from tensorflow import keras as tfk


model = tfk.models.Sequential()
model.add( tfk.layers.Dense( 16,
                         activation = 'relu',
                       )
         )
         
print(model)

print("Hello World")


