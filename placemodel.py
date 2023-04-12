import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('placementdata.csv')

df = df.drop(columns=['RegNo.','Networking','CloudComp','WebServices','DataAnalytics','QualityAssurance','AI'])

x = df.drop(columns=['Placed'])
y = df['Placed']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=43)

knn = KNeighborsClassifier()
knn = knn.fit(x_train,y_train)

pickle.dump(knn, open('model_place.pkl','wb'))
model = pickle.load(open('model_place.pkl','rb'))

'''
y_pred = knn.predict(x_test)
y_pred
from sklearn import metrics
acc = metrics.accuracy_score(y_test,y_pred)
acc
'''
