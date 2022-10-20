from csv import writer
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('fods_1.csv')
rows=data.values.tolist()


X_train, X_test = train_test_split(rows,test_size=0.2)
#print("\nX_train:\n")
#print(len(X_train))

#print("\nX_test:\n")
#print(len(X_test))

with open('Train.csv', 'a') as f_object:
    writer_object = writer(f_object)
    for x in X_train:
        writer_object.writerow(x)
    f_object.close()

with open('Test.csv', 'a') as f_object:
    writer_object = writer(f_object)
    for x in X_test:
        writer_object.writerow(x)
    f_object.close()

#print(X_train)