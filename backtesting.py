import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

ticker = "AAPL" 
stock_data = yf.Ticker(ticker)
historical_data = stock_data.history(period="1y")

#Moving Averages 
historical_data['MA10'] = historical_data['Close'].rolling(10).mean()
historical_data['MA50'] = historical_data['Close'].rolling(50).mean()

#STDEV
historical_data['STD10'] = historical_data['Close'].rolling(10).std()

risk_free_rate = 0.0001

# Calculate daily returns
historical_data['daily_return'] = historical_data['Close'].pct_change()

# Calculate rolling Sharpe Ratio (considering last 10 days)
historical_data['Sharpe'] = (historical_data['daily_return'] - risk_free_rate) / historical_data['STD10']

# Remove NaN values (which were a result of moving averages and Sharpe Ratio calculations)
historical_data.dropna(inplace=True)

# Step 3: Label Data
# Classify each day as "1" if the stock went up the next day, and "0" otherwise
historical_data['Label'] = np.where(historical_data['Close'].shift(-1) > historical_data['Close'], 1, 0)

# Step 4: Split Data
features = ['MA10', 'MA50', 'STD10', 'Sharpe']
X = historical_data[features]
y = historical_data['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 6: Test Model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Display the last 5 rows of the processed data, accuracy, and confusion matrix
print(historical_data.tail())
print("Accuracy:", accuracy)
print("Confusion Matrix:", conf_matrix)
