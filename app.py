import streamlit as st
import pandas as pd

# Simulated API response
api_response = {
    "train_name": "Rajdhani Express",
    "train_number": "12301",
    "route": [
        {"station": "New Delhi",      "arrival": "Source",      "departure": "07:05"},
        {"station": "Kanpur Central", "arrival": "10:10",       "departure": "10:15"},
        {"station": "Allahabad Jn",   "arrival": "12:00",       "departure": "12:10"},
        {"station": "Patna Jn",       "arrival": "16:30",       "departure": "16:40"},
        {"station": "Howrah Jn",      "arrival": "21:30",       "departure": "Destination"}
    ]
}

# ✅ Task 1 — Parse Data
data = []

for stop in api_response["route"]:
    data.append({
        "Station": stop["station"],
        "Arrival": stop["arrival"],
        "Departure": stop["departure"]
    })

df = pd.DataFrame(data)

# ✅ Task 2 — Streamlit UI

# Title
st.markdown(f"## 🚆 {api_response['train_name']} ({api_response['train_number']})")

# Table
st.dataframe(df)

# Selectbox
station = st.selectbox("Select Station", df["Station"])

# Show details
selected_row = df[df["Station"] == station].iloc[0]

st.text(f"Arrival Time: {selected_row['Arrival']}")
st.text(f"Departure Time: {selected_row['Departure']}")