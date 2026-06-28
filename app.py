import streamlit as st
import pandas as pd
import pickle

# Load Model and Dataset
model = pickle.load(open("model.pkl", "rb"))
car = pd.read_csv("clean_data.csv")

# Page Configuration
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# Title
st.title("🚗 Car Price Prediction")

# Create Columns
left_col, space, right_col = st.columns([1, 0.15, 1.2])

# ================= LEFT COLUMN =================
with left_col:

    st.header("Enter Car Details")

    company = st.selectbox(
        "Select Company",
        sorted(car["company"].unique())
    )

    name = st.selectbox(
        "Select Car Name",
        sorted(car[car["company"] == company]["name"].unique())
    )

    year = st.selectbox(
        "Year",
        sorted(car["year"].unique(), reverse=True)
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        sorted(car["fuel_type"].dropna().unique())
    )

    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        step=1000
    )

    predict = st.button(
        "Predict Price",
        use_container_width=True
    )

# ================= RIGHT COLUMN =================
with right_col:

    st.write("")
    st.write("")
    st.write("")

    if predict:

        input_df = pd.DataFrame(
            [[name, company, year, kms_driven, fuel_type]],
            columns=[
                "name",
                "company",
                "year",
                "kms_driven",
                "fuel_type"
            ]
        )

        prediction = model.predict(input_df)

        st.markdown(
            "<h2 style='text-align:center;color:#00C853;'>💰 Estimated Price</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h1 style='text-align:center;font-size:70px;color:#00E676;'>₹ {int(prediction[0])}</h1>",
            unsafe_allow_html=True
        )