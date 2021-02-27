from csv import reader
import random 
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dropout, LSTM, Dense, Bidirectional
from keras.layers.convolutional import Conv1D, MaxPooling1D
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
from tensorflow import keras
from tensorflow import reshape

with open('out.csv', 'r') as f:
    csv_reader = reader(f)
    data_frag = list(csv_reader)

random.shuffle(data_frag)
Y_frag = [int(sublist[len(sublist)-1]) for sublist in data_frag]
X_frag = [sublist[0:len(sublist)-1] for sublist in data_frag]

max_input_length = max([len(i) for i in X_frag])

api_calls = []
for sublist in X_frag:
    api_calls.extend(sublist)
api_calls_list = list(set(api_calls))
int_api_calls = [int(i) for i in api_calls_list]
distinct_api_calls = max(int_api_calls) + 1


X_train, X_test, Y_train, Y_test = train_test_split(X_frag, Y_frag, test_size=0.33, random_state=42)
batchSize = 100
X_train_normalised = np.array([[float(j)/distinct_api_calls for j in i] for i in X_train])
X_test_normalised = np.array([[float(j)/distinct_api_calls for j in i] for i in X_test])
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)
input_len = len(X_train_normalised[1])
X_train = np.array([[int(j) for j in i] for i in X_train])
X_test = np.array([[int(j) for j in i] for i in X_test])

embedding_vector_length = 32
keras.initializers.GlorotNormal(seed=None)
initializer = keras.initializers.GlorotNormal()

model = Sequential()
model.add(Embedding(distinct_api_calls, 300, input_length=10, embeddings_initializer=initializer))
model.add(Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(Dropout(0.5))
model.add(Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(Dropout(0.5))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.5))
model.add(Bidirectional(LSTM(32,activation="tanh",return_sequences=True)))
model.add(Dropout(0.5))
model.add(Bidirectional(LSTM(32,activation="tanh",return_sequences=True)))
model.add(Dropout(0.5))
model.add(Bidirectional(LSTM(32,activation="tanh")))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, Y_train, epochs=20, batch_size=32)
model.save('lstm_model.h5')
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Accuracy: %.2f%%" %(scores[1]*100))

plot_confusion_matrix(conf_mat=(confusion_matrix(Y_test, model.predict_classes(X_test))), show_absolute=True, show_normed=True, colorbar=True)