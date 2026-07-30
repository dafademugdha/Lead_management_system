import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
from backend.main import save_lead

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

    # -------------------------
    # PERSONAL INFORMATION
    # -------------------------
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

    st.divider()

    # -------------------------
    # LOCATION
    # -------------------------
    st.subheader("📍 Location")

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

    # -------------------------
    # FARM INFORMATION
    # -------------------------
    st.subheader("🌱 Farm Information")

    land_size = st.number_input(
        "Land Size (Acres)",
        min_value=0.0,
        step=0.5,
        format="%.1f"
    )

    st.divider()

    # -------------------------
    # FINANCIAL INFORMATION
    # -------------------------
    st.subheader("💰 Financial Information")

    budget = st.number_input(
        "Budget (₹)",
        min_value=0,
        step=10000
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

    # ---------- Name ----------
    if name.strip() == "":
        errors.append("Name is required.")

    elif not name.replace(" ", "").isalpha():
        errors.append("Name should contain only alphabets.")

    elif len(name.strip()) < 3:
        errors.append("Name should contain at least 3 characters.")

    # ---------- Mobile ----------
    if mobile.strip() == "":
        errors.append("Mobile number is required.")

    elif not mobile.isdigit():
        errors.append("Mobile number should contain only digits.")

    elif len(mobile) != 10:
        errors.append("Mobile number should be exactly 10 digits.")

    elif mobile[0] not in "6789":
        errors.append("Enter a valid Indian mobile number.")

    # ---------- City ----------
    if city == "Select City":
        errors.append("Please select a city.")

    # ---------- Land Size ----------
    if land_size <= 0:
        errors.append("Land size should be greater than 0.")

    # ---------- Budget ----------
    if budget <= 0:
        errors.append("Budget should be greater than 0.")

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
            response = save_lead(
            name=name,
            mobile=mobile,
            city=city,
            land_size=land_size,
            budget=budget
            )

            if response["status"] == "success":

                st.success(response["message"])

                st.markdown("## 📋 Lead Summary")

                with st.container(border=True):

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("👤 Personal Details")
                        st.write(f"**Name:** {name}")
                        st.write(f"**Mobile:** {mobile}")

                    with col2:
                        st.subheader("🌾 Farm Details")
                        st.write(f"**Nearest City:** {city}")
                        st.write(f"**Land Size:** {land_size} Acres")
                        st.write(f"**Budget:** ₹ {budget:,}")

            else:
                st.error(response["message"])

        except Exception as e:
            st.error(str(e)) 

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.caption("Agro Tourism Lead Management System | Frontend Version 1.0")