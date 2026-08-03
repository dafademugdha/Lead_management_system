import os
import sys
import time

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
import requests

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Agro Tourism Lead Management",
    page_icon="🌾",
    layout="wide"
)

# ==========================================================
# HEADER
# ==========================================================

st.title("🌾 Agro Tourism Lead Management System")
st.caption("Capture and manage farmer leads for Agro Tourism projects.")
st.divider()

# ==========================================================
# LEAD FORM
# ==========================================================

with st.form("lead_form"):

    # ======================================================
    # PERSONAL INFORMATION
    # ======================================================

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Full Name",
            placeholder="Enter full name"
        )

    with col2:
        mobile = st.text_input(
            "Mobile Number",
            placeholder="Enter 10-digit mobile number"
        )

    same_as_mobile = st.checkbox(
    "WhatsApp number is same as Mobile Number"
    )

    if same_as_mobile:
        whatsapp = mobile
        st.text_input(
        "WhatsApp Number",
        value=mobile,
        disabled=True
        )
    else:
        whatsapp = st.text_input(
        "WhatsApp Number",
        placeholder="Enter WhatsApp number"
        )

    st.divider()

    # ======================================================
    # LOCATION INFORMATION
    # ======================================================

    st.subheader("📍 Location Information")

    location = st.text_input(
        "Village / Location",
        placeholder="Enter village or location"
    )

    city = st.selectbox(
        "Nearest City",
        [
            "Select City",
            "Pune",
            "Mumbai",
            "Nashik",
            "Nagpur",
            "Satara",
            "Kolhapur",
            "Aurangabad",
            "Other"
        ]
    )

    st.divider()

    # ======================================================
    # FARM INFORMATION
    # ======================================================

    st.subheader("🌱 Farm Information")

    land_size = st.number_input(
        "Land Size (Acres)",
        min_value=0.0,
        step=0.5,
        format="%.1f"
    )

    current_farm_status = st.selectbox(
        "Current Farm Status",
        [
            "Select Status",
            "Agriculture",
            "Unused Land",
            "Agro Tourism",
            "Farm House",
            "Mixed Farming",
            "Other"
        ]
    )

    st.divider()

    # ======================================================
    # FINANCIAL INFORMATION
    # ======================================================

    st.subheader("💰 Financial Information")

    existing_income = st.number_input(
        "Existing Annual Income (₹)",
        min_value=0.0,
        step=10000.0
    )

    monthly_maintenance_cost = st.number_input(
        "Monthly Maintenance Cost (₹)",
        min_value=0.0,
        step=1000.0
    )

    budget = st.number_input(
        "Budget (₹)",
        min_value=0.0,
        step=10000.0
    )

    st.divider()

    # ======================================================
    # OTHER INFORMATION
    # ======================================================

    st.subheader("📱 Other Information")

    tech_comfort = st.selectbox(
        "Tech Comfort",
        ["Select",
        "Does not use smartphone",
        "Basic smartphone user",
        "Uses WhatsApp",
        "Comfortable with apps",
        "Very tech savvy"]
    )

    nature_interest = st.selectbox(
        "Nature / Farming Interest",
        ["Select",
        "Very Interested",
        "Interested",
        "Somewhat Interested",
        "Not Sure"]
    )

    st.divider()

    submitted = st.form_submit_button(
        "💾 Save Lead",
        use_container_width=True
    )

# ==========================================================
# VALIDATION
# ==========================================================

if submitted:

    errors = []

    # ------------------------------------------------------
    # Name
    # ------------------------------------------------------

    if name.strip() == "":
        errors.append("Name is required.")

    elif not name.replace(" ", "").isalpha():
        errors.append("Name should contain only alphabets.")

    elif len(name.strip()) < 3:
        errors.append("Name should contain at least 3 characters.")

    # ------------------------------------------------------
    # Mobile Number
    # ------------------------------------------------------

    if mobile.strip() == "":
        errors.append("Mobile number is required.")

    elif not mobile.isdigit():
        errors.append("Mobile number should contain only digits.")

    elif len(mobile) != 10:
        errors.append("Mobile number should be exactly 10 digits.")

    elif mobile[0] not in "6789":
        errors.append("Enter a valid Indian mobile number.")

    # ------------------------------------------------------
    # WhatsApp Number
    # ------------------------------------------------------

    if whatsapp.strip() == "":
        errors.append("WhatsApp number is required.")

    elif not whatsapp.isdigit():
        errors.append("WhatsApp number should contain only digits.")

    elif len(whatsapp) != 10:
        errors.append("WhatsApp number should be exactly 10 digits.")

    elif whatsapp[0] not in "6789":
        errors.append("Enter a valid WhatsApp number.")

    # ------------------------------------------------------
    # Location
    # ------------------------------------------------------

    if location.strip() == "":
        errors.append("Location is required.")

    # ------------------------------------------------------
    # City
    # ------------------------------------------------------

    if city == "Select City":
        errors.append("Please select the nearest city.")

    # ------------------------------------------------------
    # Land Size
    # ------------------------------------------------------

    if land_size <= 0:
        errors.append("Land size must be greater than 0 acres.")

    # ------------------------------------------------------
    # Current Farm Status
    # ------------------------------------------------------

    if current_farm_status == "Select Status":
        errors.append("Please select the current farm status.")

    # ------------------------------------------------------
    # Existing Income
    # ------------------------------------------------------

    if existing_income < 0:
        errors.append("Existing income cannot be negative.")

    # ------------------------------------------------------
    # Monthly Maintenance Cost
    # ------------------------------------------------------

    if monthly_maintenance_cost < 0:
        errors.append("Monthly maintenance cost cannot be negative.")

    # ------------------------------------------------------
    # Budget
    # ------------------------------------------------------

    if budget <= 0:
        errors.append("Budget should be greater than 0.")

    # ------------------------------------------------------
    # Tech Comfort
    # ------------------------------------------------------

    if tech_comfort == "Select":
        errors.append("Please select tech comfort.")

    # ------------------------------------------------------
    # Nature Interest
    # ------------------------------------------------------

    if nature_interest == "Select":
        errors.append("Please select nature/farming interest.")

    # ======================================================
    # DISPLAY ERRORS
    # ======================================================

    if errors:
        for error in errors:
            st.error(error)

    # ======================================================
    # SUCCESS
    # ======================================================

    else:
        try:
            payload = {
                "name": name,
                "location": location,
                "nearest_city": city,
                "mobile_number": mobile,
                "whatsapp_number": whatsapp,
                "land_size": land_size,
                "current_farm_status": current_farm_status,
                "existing_income": existing_income,
                "monthly_maintenance_cost": monthly_maintenance_cost,
                "budget": budget,
                "tech_comfort": tech_comfort,
                "nature_interest": nature_interest
            }

            api_response = requests.post(
                "http://127.0.0.1:8000/leads",
                json=payload
            )

            response = api_response.json()

            if response["status"] == "success":

                st.success(response["message"])

                st.markdown("## 📋 Lead Summary")

                with st.container(border=True):

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("👤 Personal Details")
                        st.write(f"**Name:** {name}")
                        st.write(f"**Mobile:** {mobile}")
                        st.write(f"**WhatsApp:** {whatsapp}")

                        st.markdown("### 📍 Location")
                        st.write(f"**Location:** {location}")
                        st.write(f"**Nearest City:** {city}")

                        st.markdown("### 🌱 Farm")
                        st.write(f"**Land Size:** {land_size} Acres")
                        st.write(f"**Farm Status:** {current_farm_status}")

                    with col2:
                        st.markdown("### 💰 Financial")
                        st.write(f"**Existing Income:** ₹ {existing_income:,.0f}")
                        st.write(f"**Maintenance Cost:** ₹ {monthly_maintenance_cost:,.0f}")
                        st.write(f"**Budget:** ₹ {budget:,.0f}")

                        st.markdown("### 📱 Other")
                        st.write(f"**Tech Comfort:** {tech_comfort}")
                        st.write(f"**Nature Interest:** {nature_interest}")
                # Wait for 3 seconds so the user can read the summary
                time.sleep(3)

                # Refresh the page to clear the form
                st.rerun()
            else:
                st.error(response["message"])

        except Exception as e:
            st.error(str(e)) 

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.caption("Agro Tourism Lead Management System | Frontend Version 1.0")