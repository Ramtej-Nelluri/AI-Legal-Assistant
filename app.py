import streamlit as st

# --- SHARED ON ALL PAGES ---
st.sidebar.caption("Made with ❤️ by Kamal, Reka, Kopika, Deepesh & Ashir")

# --- PAGE SETUP ---
pages = {
    "AI Legal Assistant": "views/chatbotLegalv2.py",
    "Judgment Predictor": "views/judgmentPred.py",
    "Legal Doc Generator": "views/docGen.py",
}

# --- PAGE NAVIGATION ---
page_selection = st.sidebar.selectbox("Choose a page", list(pages.keys()))

# --- DISPLAY SELECTED PAGE OUTPUT ---
selected_page = pages[page_selection]

try:
    # Run the selected page's script and capture the output
    with open(selected_page, "r", encoding="utf-8") as f:
        script_code = f.read()

    # Use exec() to execute the script and display output
    exec(script_code)

except UnicodeDecodeError:
    st.error(f"Error reading the file {selected_page}. The file might contain invalid characters.")
except FileNotFoundError:
    st.error(f"The file {selected_page} was not found. Please check the file path.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

# --- PAGE CONTENT ---
st.header(page_selection)
