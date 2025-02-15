import streamlit as st
import cv2
import numpy as np
import speech_recognition as sr
import os
import pygame

# Set page config
st.set_page_config(page_title="Voice-Activated Photo Capture", layout="wide")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "static", "captured_photo.jpg")
DEFAULT_IMAGE_URL = "https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-600nw-1037719192.jpg"  # Replace with your actual default image URL
CLICK_SOUND_PATH = "temp_fixed.wav"  # Ensure it's a 16-bit PCM WAV file

# Function to play capture sound
def play_click_sound():
    if os.path.exists(CLICK_SOUND_PATH):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(CLICK_SOUND_PATH)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        except pygame.error as e:
            st.error(f"Error playing sound: {e}")

# Function to listen for "capture" command
def listen_for_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.write("🎤 Listening for 'capture'...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
        
        command = r.recognize_google(audio).lower()
        st.write(f"✅ Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        st.warning("🤷 Could not understand audio")
        return None
    except sr.RequestError as e:
        st.error(f"❌ Could not request results; {e}")
        return None
    except Exception as e:
        st.error(f"⚠️ Error during audio capture: {e}")
        return None

# Function to capture image
def capture_image():
    try:
        command = listen_for_command()
        if command and "capture" in command:
            cam = cv2.VideoCapture(0)
            if not cam.isOpened():
                st.error("❌ Error: Could not open the camera.")
                return

            # Allow camera to adjust
            for _ in range(10):
                ret, frame = cam.read()
            
            ret, frame = cam.read()
            if ret:
                play_click_sound()
                cv2.imwrite(IMAGE_PATH, frame)
                cam.release()
                st.session_state.image_captured = True  # Update session state
                st.rerun()  # ✅ Updated from experimental_rerun()
                st.success("📸 Photo Captured Successfully!")
            else:
                st.error("❌ Error: Could not capture image.")

            cam.release()
            cv2.destroyAllWindows()
        else:
            st.warning("🛑 No valid command recognized.")
    except Exception as e:
        st.error(f"⚠️ Error during image capture: {e}")

# Custom CSS to remove top space & center elements
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 10px !important;  /* Reduce top space */
        }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        div.stButton > button {
            width: 220px;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            display: block;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>🎤 Voice-Activated Photo Capture 📸</h1>", unsafe_allow_html=True)

# Check if an image was captured
if "image_captured" not in st.session_state:
    st.session_state.image_captured = False

# Centering using columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state.image_captured and os.path.exists(IMAGE_PATH):
        st.image(IMAGE_PATH, caption="📷 Captured Image", use_container_width=True)
    else:
        st.image(DEFAULT_IMAGE_URL, caption="📷 Waiting for Capture...", use_container_width=True)

# Center the "Start Listening" button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎙️ Start Listening", use_container_width=True):
        capture_image()
