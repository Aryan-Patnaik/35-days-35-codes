import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Generate synthetic user activity data
def generate_synthetic_data():
    np.random.seed(42)  # Set random seed for reproducibility
    normal_data = np.random.normal(loc=50, scale=10, size=(1000, 2))  # Generate normal data
    anomalous_data = np.random.uniform(low=0, high=100, size=(50, 2))  # Generate anomalous data
    data = np.vstack((normal_data, anomalous_data))  # Combine normal and anomalous data
    return pd.DataFrame(data, columns=['activity_level', 'access_frequency'])  # Create DataFrame

# Create synthetic data
data = generate_synthetic_data()

# Initialize and train the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)  # Set contamination level and random state
model.fit(data)  # Train the model

# Predict anomalies in the data
data['anomaly'] = model.predict(data)  # Add anomaly labels to the data

# Separate anomalies from normal data
anomalies = data[data['anomaly'] == -1]  # Anomalies are labeled as -1
normal_data = data[data['anomaly'] == 1]  # Normal data is labeled as 1

# Visualize the results
plt.scatter(normal_data['activity_level'], normal_data['access_frequency'], c='blue', label='Normal')  # Plot normal data
plt.scatter(anomalies['activity_level'], anomalies['access_frequency'], c='red', label='Anomaly')  # Plot anomalies
plt.xlabel('Activity Level')  # Set x-axis label
plt.ylabel('Access Frequency')  # Set y-axis label
plt.legend()  # Add legend
plt.title('Insider Threat Detection')  # Set plot title
plt.show()  # Show the plot

# Print the number of anomalies detected
print(f"Number of anomalies detected: {len(anomalies)}")

# Print details of detected anomalies
print("Anomalies detected:")
print(anomalies)

# Save the results to a CSV file
data.to_csv('insider_threat_detection_results.csv', index=False)
