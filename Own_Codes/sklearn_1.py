#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Data Analysis on Wine Quality Dataset
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

#Get the Wine Dataset
X, y = load_wine(return_X_y=True)

#Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True,
                                                    random_state = 20,
                                                    test_size = 0.2)

#Scale the Dataset
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Let us use ExtraTreesClassifier to predict
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()
model.fit(X_train, y_train)
y_preds = model.predict(X_test)

#We will use cross validation score to judge the performance
print(cross_val_score(model, X_test, y_test).mean())