import pandas
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Embedding, SpatialDropout1D, Dense
import numpy as np
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt
from keras.layers.convolutional import Conv1D, MaxPooling1D
import itertools
import csv

csv_data = pandas.read_csv('api_calls.csv')
benign = csv_data[csv_data['malware'] == 0].reset_index(drop=True)
malware = csv_data[csv_data['malware'] == 1].reset_index(drop=True)
malware = malware.drop(malware.index[len(benign):len(malware)])
X = (pandas.concat([malware,benign])).sample(frac=1).reset_index(drop=True)
Y = (X['malware'].values).tolist()
X = X.drop(['hash', 'malware'], axis=1)
X = (X.values).tolist()

max_input_length = max([len(i) for i in X])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

api_calls = []
for sublist in X:
    api_calls.extend(sublist)
distinct_api_calls = max(set(api_calls)) + 1
batchSize = 100
normalise_x = max(max(max(X_train)),max(max(X_test)))
X_train_normalised = np.array([[float(j)/normalise_x for j in i] for i in X_train])
X_test_normalised = np.array([[float(j)/normalise_x for j in i] for i in X_test])

embedding_vector_length = 32
model = Sequential()
model.add(Embedding(distinct_api_calls, 300, input_length=100))
model.add(Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(Dropout(0.1))
model.add(Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(Dropout(0.1))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.1))
model.add(LSTM(32,activation="tanh",return_sequences=True))
model.add(Dropout(0.1))
model.add(LSTM(32,activation="tanh",return_sequences=True))
model.add(Dropout(0.1))
model.add(LSTM(32,activation="tanh"))
model.add(Dropout(0.1))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, Y_train, epochs=20, batch_size=32)
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Accuracy: %.2f%%" %(scores[1]*100))

plot_confusion_matrix(conf_mat=(confusion_matrix(Y_test, model.predict_classes(X_test))), show_absolute=True, show_normed=True, colorbar=True)
