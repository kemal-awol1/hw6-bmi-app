import streamlit as st

st.title("Body Mass Index (BMI) Calculator")


weight_unit = st.selectbox(
    "Select weight unit",
    ["Kilograms", "Pounds"]
)

height_unit = st.selectbox(
    "Select height unit",
    ["Meters", "Feet"]
)


if weight_unit == "Kilograms":
    weight = st.number_input(
        "Enter weight in kilograms",
        min_value=1.0,
        format="%.2f"
    )
else:
    weight = st.number_input(
        "Enter weight in pounds",
        min_value=1.0,
        format="%.2f"
    )


if height_unit == "Meters":
    height = st.number_input(
        "Enter height in meters",
        min_value=0.1,
        format="%.2f"
    )
else:
    height = st.number_input(
        "Enter height in feet",
        min_value=0.1,
        format="%.2f"
    )


if weight_unit == "Pounds":
    weight = weight * 0.453592

if height_unit == "Feet":
    height = height * 0.3048


if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    st.success(f"Your BMI is: {bmi:.2f}")

    # BMI category
    if bmi < 18.5:
        st.info("Category: Underweight")

    elif bmi < 25:
        st.success("Category: Normal weight")

    elif bmi < 30:
        st.warning("Category: Overweight")

    elif bmi < 35:
        st.error("Category: Obesity Class I")

    elif bmi < 40:
        st.error("Category: Obesity Class II")

    else:
        st.error("Category: Obesity Class III") 

st.markdown("""
---
**Developed by:**  
Kemal Lemnuro Awol, MD, MPH Candidate  
Johns Hopkins Bloomberg School of Public Health
""")