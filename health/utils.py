# health/utils.py

# health/utils.py
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

def predict_health_trend(user_health_data):
    """
    Predict health trends (e.g., heart rate, blood pressure) using linear regression.
    """
    # Extract heart rate and blood pressure data
    heart_rate = [d['heart_rate'] for d in user_health_data]
    blood_pressure = [d['blood_pressure'] for d in user_health_data]
    
    # Create time indices for trend prediction
    time_indices = np.array(range(len(user_health_data))).reshape(-1, 1)

    # Linear Regression model for heart rate prediction
    heart_rate_model = LinearRegression()
    heart_rate_model.fit(time_indices, heart_rate)
    heart_rate_pred = heart_rate_model.predict(time_indices)

    # Linear Regression model for blood pressure prediction
    blood_pressure_model = LinearRegression()
    blood_pressure_model.fit(time_indices, blood_pressure)
    blood_pressure_pred = blood_pressure_model.predict(time_indices)

    return {
        'heart_rate_trend': heart_rate_pred.tolist(),
        'blood_pressure_trend': blood_pressure_pred.tolist()
    }

def detect_anomalies(user_health_data):
    """
    Detect anomalies in heart rate and blood pressure using Isolation Forest.
    """
    # Extract heart rate and blood pressure data
    health_metrics = np.array([[d['heart_rate'], d['blood_pressure']] for d in user_health_data])

    # Train an Isolation Forest model for anomaly detection
    iso_forest = IsolationForest(contamination=0.1)  # 10% anomalies expected
    anomalies = iso_forest.fit_predict(health_metrics)

    # Mark anomalies with -1 and normal data with 1
    anomaly_indices = [i for i, label in enumerate(anomalies) if label == -1]

    return {
        'anomalies': anomaly_indices,
        'anomalous_data': [user_health_data[i] for i in anomaly_indices]
    }

def get_personalized_recommendations(user_health_data):
    """
    Generate personalized recommendations based on health trends.
    """
    # Calculate average heart rate and blood pressure
    avg_heart_rate = np.mean([d['heart_rate'] for d in user_health_data])
    avg_blood_pressure = np.mean([d['blood_pressure'] for d in user_health_data])

    recommendations = []

    # Heart rate recommendation
    if avg_heart_rate > 100:
        recommendations.append("Consider reducing physical activity or consulting a doctor for heart rate concerns.")
    elif avg_heart_rate < 60:
        recommendations.append("Consider increasing physical activity, but ensure it's safe for your health condition.")

    # Blood pressure recommendation
    if avg_blood_pressure > 140:
        recommendations.append("Your blood pressure is high. Consider consulting a healthcare provider.")
    elif avg_blood_pressure < 90:
        recommendations.append("Your blood pressure is low. Ensure you're hydrated and maintain a balanced diet.")

    return recommendations


def generate_health_plot(user_health_data):
    import matplotlib.pyplot as plt
    import io
    import base64

    plt.figure(figsize=(6, 4))
    plt.plot([d['heart_rate'] for d in user_health_data], label="Heart Rate")
    plt.plot([d['blood_pressure'] for d in user_health_data], label="Blood Pressure")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.title("Health Trends")

    # Save plot as image
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return base64.b64encode(image_png).decode("utf-8")
