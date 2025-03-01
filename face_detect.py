import cv2  # Import OpenCV library for computer vision tasks

# Load the pre-trained Haar Cascade classifier for frontal face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize webcam capture (0 is the default camera)
video_capture = cv2.VideoCapture(0)

# Define a function to detect faces and draw bounding boxes
def detect_bounding_box(vid):
    """
    Detect faces in a video frame and draw green rectangles around them.
    
    Args:
        vid: The video frame (in BGR color format) to process.
    Returns:
        faces: List of detected face coordinates (x, y, w, h).
    """
    # Convert the frame to grayscale (Haar Cascade works better with grayscale images)
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    
    # Detect faces using the classifier (scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    
    # Draw a green rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)  # Green color, thickness 4
    
    return faces  # Return the list of face coordinates

# Main loop to process video frames in real-time
while True:
    # Capture a single frame from the webcam
    result, video_frame = video_capture.read()  # result is True if frame is read successfully
    
    # Flip the frame horizontally (mirror effect) for a natural view
    mirror_frame = cv2.flip(video_frame, 1)
    
    # Exit the loop if the frame couldn’t be read (e.g., camera disconnected)
    if result is False:
        break
    
    # Detect faces and draw bounding boxes on the mirrored frame
    faces = detect_bounding_box(mirror_frame)
    
    # Display the processed frame in a window titled "Capture"
    cv2.imshow("Capture", mirror_frame)
    
    # Wait for 1ms and check if 'q' is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam resource to free it up
video_capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()