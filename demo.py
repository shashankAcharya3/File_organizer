import os
import shutil
import streamlit as st
from datetime import datetime

# Function to organize by file type
def organize_by_file_type(folder_path):
    if not os.path.exists(folder_path):
        st.error("The folder does not exist!")
        return

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xls'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Others': []
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    destination_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, destination_folder)
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(folder_path, 'Others')
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, others_folder)

    st.success("Files organized by file type successfully!")

# Function to organize by creation date
def organize_by_creation_date(folder_path):
    if not os.path.exists(folder_path):
        st.error("The folder does not exist!")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_time)
            year_folder = os.path.join(folder_path, str(creation_date.year))
            month_folder = os.path.join(year_folder, f"{creation_date.month:02d}")
            os.makedirs(month_folder, exist_ok=True)
            shutil.move(file_path, month_folder)

    st.success("Files organized by creation date successfully!")

# Streamlit UI
st.title("Basic File Organizer")

# Input for folder path
folder_path = st.text_input("Enter the folder path:")

# Choose organizing method
organize_method = st.selectbox("Organize by:", ["File Type", "Creation Date"])

# Organize button
if st.button("Organize"):
    if folder_path:
        if organize_method == "File Type":
            organize_by_file_type(folder_path)
        elif organize_method == "Creation Date":
            organize_by_creation_date(folder_path)
    else:
        st.error("Please enter a folder path!")

# /Users/shashank/Desktop/nothing but a dump/liftoff/generative