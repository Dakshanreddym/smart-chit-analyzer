import numpy as np
from sklearn.linear_model import LinearRegression

# Training data (dummy dataset)
# [members, month_number]
X = np.array([
    [20,1],[20,5],[20,10],[20,15],[20,20],
    [25,1],[25,5],[25,10],[25,15],[25,20],
    [30,1],[30,5],[30,10],[30,15],[30,20]
])

# Winning bid discount %
y = np.array([
    30,27,24,22,20,
    28,25,22,20,18,
    26,23,20,18,16
])

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_bid(members, month):
    prediction = model.predict([[members, month]])
    return round(prediction[0], 2)
