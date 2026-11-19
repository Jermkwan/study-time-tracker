import streamlit as st

from data_store import load_records, save_record
from logic import create_study_record


st.title("Study Time Tracker")

with st.form("study_form"):
    subject = st.text_input("Subject")
    minutes = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=1,
        step=1,
    )
    submitted = st.form_submit_button("Save")

if submitted:
    try:
        record = create_study_record(subject, minutes)
        save_record(record)
    except ValueError as error:
        st.error(str(error))
    except OSError as error:
        st.error(f"Could not save study record: {error}")
    else:
        st.success("Study record saved.")

st.subheader("Study history")
try:
    records = load_records()
except (OSError, ValueError) as error:
    st.error(f"Could not load study history: {error}")
else:
    if records:
        st.dataframe(records, use_container_width=True, hide_index=True)
    else:
        st.info("No study records yet.")