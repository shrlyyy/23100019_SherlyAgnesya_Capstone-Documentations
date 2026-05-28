import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset.
data = pd.read_csv("Experience_Salary.csv")

X = data[["YearsExperience"]]
y = data["Salary"]

model = LinearRegression()
model.fit(X, y)

data["PredictedSalary"] = model.predict(X)

print("Model Coefficient (slope)", round(float(model.coef_[0]), 2))
print("Model Intercept (base salary)", round(float(model.intercept_), 2))

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, data["PredictedSalary"], color="red", label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs. Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()