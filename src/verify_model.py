import joblib

model = joblib.load("models/random_forest.joblib")

print("Model Type:", type(model))
print("Number of Trees:", model.n_estimators)
print("Max Depth:", model.max_depth)
print("Random State:", model.random_state)