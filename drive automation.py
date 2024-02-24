import cv2
from pydrive.auth import GoogleAuth
import os
from pydrive.drive import GoogleDrive

# Capture image from webcam
def capture_image():
    video_capture = cv2.VideoCapture(0)
    _, frame = video_capture.read()
    video_capture.release()
    return frame

# Save image to local file
def save_image(image):
    image_path = "captured_image.jpg"
    cv2.imwrite(image_path, image)
    return image_path

# Upload image to Google Drive
def upload_to_drive(file_path):
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': 'captured_image.jpg'})
    file.SetContentFile(file_path)
    file.Upload()

# Main function
def main():
    # Capture image
    image = capture_image()

    # Save image to local file
    image_path = save_image(image)
    print("Image saved:", image_path)

    # Upload image to Google Drive
    upload_to_drive(image_path)
    print("Image uploaded to Google Drive.")

    # Clean up the local file
    os.remove(image_path)

# Run the main function
if __name__ == "__main__":
    main()
