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

        if kms_driven > 500000:
            st.error("❌ Input Mismatch! Please enter a valid Kilometers Driven value.")
        else:
            prediction = model.predict(input_df)
            price = round(float(prediction[0][0]))

            if price <= 0:
                st.error("❌ Invalid Prediction! Please check the entered values.")
            else:
                st.markdown(
                    f"""
                    <div style="
                        background:#d1fae5;
                        padding:30px;
                        border-radius:15px;
                        text-align:center;
                    ">
                        <h2 style="color:#065f46;">💰 Estimated Price</h2>
                        <h1 style="font-size:70px;color:#00C853;">
                            ₹ {price}
                        </h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )