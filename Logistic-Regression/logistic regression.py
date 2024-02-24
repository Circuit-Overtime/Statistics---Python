import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

data = pd.read_csv("escape_velocity.csv")
temp = data["Velocity"].tolist()
melt = data["Escaped"].tolist()

fig = px.scatter(x = temp, y = melt)
fig.show()




temp_array = np.array(temp)
melt_array = np.array(melt)

m,c = np.polyfit(temp_array, melt_array, 1)

y = []
for i in temp_array:
  y_value = m*i+c
  y.append(y_value)

fig = px.scatter(x = temp_array, y = melt_array)
fig.update_layout(shapes  = [
                             dict(
                                 type = "line",
                                  y0 = min(y), y1 = max(y),
                                  x0 = min(temp_array), x1 = max(temp_array)

                             )
])
fig.show()





temp_array = np.array(temp)
melt_array = np.array(melt)

m,c = np.polyfit(temp_array, melt_array, 1)

y = []
for i in temp_array:
  y_value = m*i+c
  y.append(y_value)

fig = px.scatter(x = temp_array, y = melt_array)
fig.update_layout(shapes  = [
                             dict(
                                 type = "line",
                                  y0 = min(y), y1 = max(y),
                                  x0 = min(temp_array), x1 = max(temp_array)

                             )
])
fig.show()



temp_array = np.array(temp)
melt_array = np.array(melt)

m,c = np.polyfit(temp_array, melt_array, 1)

y = []
for i in temp_array:
  y_value = m*i+c
  y.append(y_value)

fig = px.scatter(x = temp_array, y = melt_array)
fig.update_layout(shapes  = [
                             dict(
                                 type = "line",
                                  y0 = min(y), y1 = max(y),
                                  x0 = min(temp_array), x1 = max(temp_array)

                             )
])
fig.show()




temp_array = np.array(temp)
melt_array = np.array(melt)

m,c = np.polyfit(temp_array, melt_array, 1)

y = []
for i in temp_array:
  y_value = m*i+c
  y.append(y_value)

fig = px.scatter(x = temp_array, y = melt_array)
fig.update_layout(shapes  = [
                             dict(
                                 type = "line",
                                  y0 = min(y), y1 = max(y),
                                  x0 = min(temp_array), x1 = max(temp_array)

                             )
])
fig.show()







x = np.reshape(temp_array, (len(temp_array), 1))
y = np.reshape(melt_array, (len(melt_array), 1))

lr = LogisticRegression()
lr.fit(x,y)
plt.figure()
plt.scatter(x.ravel(), y, color = "black", zorder = 20)

def model(x):
  return 1/ (1 + np.exp(-x))

x_test = np.linspace(0,5000,10000)
chances = model(x_test * lr.coef_ + lr.intercept_).ravel()

plt.plot(x_test, chances, color = "blue", linewidth = 3)
plt.axhline(y=0, color = "k", linestyle = "-")
plt.axhline(y=1, color = "k", linestyle = "-")
plt.axhline(y=0.5, color = "b", linestyle = "--")

n = 6843
plt.axvline(x = x_test[n], color = "b", linestyle = "--")

plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.xlim(3400, 3450)
plt.show()
print(f"The value of the test result of x-test of {n} is {x_test[n]}" )



usr_temp = float(input("Enter the Velocity: "))
chances = model(usr_temp * lr.coef_ + lr.intercept_).ravel()[0]
if chances <= 0.01:
  print("Will not Escape Earth")
elif chances < 0.5:
  print("It might not Escape Earth")
elif chances >= 1:
  print("It will Escape Earth")
else:
  print("It might get escape Earth")