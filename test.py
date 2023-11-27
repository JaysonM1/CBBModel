import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputClassifier

# Assuming you have a DataFrame named 'df' with the necessary columns

# Extract features (X) and target variables (y_winner, y_margin)
X = df.drop(columns=['Winner', 'Margin'])
y_winner = df['Winner']
y_margin = df['Margin']

# Split the data into training and testing sets
X_train, X_test, y_winner_train, y_winner_test, y_margin_train, y_margin_test = train_test_split(
    X, y_winner, y_margin, test_size=0.2, random_state=42
)

# Standardize features (optional but often beneficial)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a RandomForestClassifier for predicting the winner
model_winner = RandomForestClassifier(n_estimators=100, random_state=42)

# Create a RandomForestRegressor for predicting the margin
model_margin = RandomForestRegressor(n_estimators=100, random_state=42)

# Wrap classifiers/regressors in MultiOutputClassifier for multi-target prediction
multi_target_model = MultiOutputClassifier(estimator=model_winner)

# Train the model
multi_target_model.fit(X_train_scaled, {'winner': y_winner_train, 'margin': y_margin_train})

# Make predictions on the test set
predictions = multi_target_model.predict(X_test_scaled)

# Extract predictions for each target variable
y_winner_pred = predictions['winner']
y_margin_pred = predictions['margin']

# Evaluate the model for the winner prediction
accuracy_winner = accuracy_score(y_winner_test, y_winner_pred)
print(f'Accuracy for Winner prediction: {accuracy_winner:.2f}')

# Evaluate the model for the margin prediction (you may use regression metrics)
# Example: mean_absolute_error, mean_squared_error
mean_absolute_error_margin = mean_absolute_error(y_margin_test, y_margin_pred)
print(f'Mean Absolute Error for Margin prediction: {mean_absolute_error_margin:.2f}')
