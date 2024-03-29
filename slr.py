import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datasheet = pd.read_csv('Salary_Data.csv')
X = datasheet.iloc[:, :-1].values
Y = datasheet.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, Y_train)

print(X_train)
print(Y_train)

Y_pred = lr.predict(X_test)
print(X_test)
print(Y_pred)

plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, lr.predict(X_train), color='blue')
plt.title('Salary vs Expereince(Training Data)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, Y_test, color='red')
plt.plot(X_train, lr.predict(X_train), color='blue')
plt.title('Salary vs Expereince(Test Data)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()