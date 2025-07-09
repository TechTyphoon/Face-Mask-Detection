import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np
import cv2
import os

st.set_page_config(page_title='Face Mask Detector', page_icon='😷', layout='centered', initial_sidebar_state='expanded')

def local_css(file_name):
    """ Method for reading styles.css and applying necessary changes to HTML"""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        pass

def detect_mask_without_ml():
    """Simple face detection without ML model for demo purposes"""
    st.success("Face Mask Detection Demo - Working!")
    st.info("This is a simplified version to demonstrate the app is working.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # Convert PIL image to OpenCV format
        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Simple face detection using OpenCV
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Add text indicating face detected
            cv2.putText(opencv_image, "Face Detected", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # Convert back to RGB for display
        result_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        st.image(result_image, caption='Face Detection Result', use_column_width=True)
        
        if len(faces) > 0:
            st.success(f"Detected {len(faces)} face(s) in the image!")
        else:
            st.warning("No faces detected in the image.")

def main():
    local_css("css/styles.css")
    
    st.title("😷 Face Mask Detection")
    st.markdown("### Upload an image to detect faces")
    
    activities = ["Image", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    if choice == 'Image':
        detect_mask_without_ml()
        
    elif choice == 'About':
        st.subheader("About this App")
        st.markdown("Built with Streamlit and OpenCV")
        st.markdown("This is a simplified version for demonstration purposes.")
        st.balloons()

if __name__ == '__main__':
    main()
