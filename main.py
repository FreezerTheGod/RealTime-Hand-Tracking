# We import OpenCV, MediaPipe, and time for handling video capture, hand landmark detection, and timing respectively.
import cv2
import mediapipe as mp
import time

# BaseOptions is used to specify the model asset path for the hand landmarker.
BaseOptions = mp.tasks.BaseOptions
# Handlandmarker is an AI model that detects hand landmarks in images or video frames taken from the vision tasks module of MediaPipe.
HandLandmarker = mp.tasks.vision.HandLandmarker
# HandLandmarkerOptions allows us to modify the behavior of the hand landmarker, such as setting the number of hands to detect and confidence thresholds.
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
# RunningMode specifies the mode in which the hand landmarker operates, such as processing images or video frames.
VisionRunningMode = mp.tasks.vision.RunningMode

# mp_draw provides utilities for drawing the detected hand landmarks and connections on the image.
mp_draw = mp.tasks.vision.drawing_utils
# mp_connections contains predefined connections between hand landmarks, which can be used to visualize the hand structure.
mp_connections = mp.tasks.vision.HandLandmarksConnections

# We initialize the video capture from the default camera (index 0) and set the resolution to 1280x720.
cap = cv2.VideoCapture(0) 
cap.set(3, 1280)
cap.set(4, 720)

def main():
    # We create an instance of HandLandmarkerOptions to configure the hand landmarker. We specify the model asset path, set the running mode to process images, and configure it to detect up to 2 hands with a minimum confidence threshold of 0.7 for both detection and presence.
    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
        running_mode=VisionRunningMode.IMAGE, # Standard image processing mode
        num_hands=2,
        min_hand_detection_confidence=0.7,
        min_hand_presence_confidence=0.7
    )
    # We create a hand landmarker instance using the specified options.
    with HandLandmarker.create_from_options(options) as hands:
        while True:
            # This initializes a local counter variable of 0  
            attempt = 0
            # We attempt to read a frame from the video capture
            success, img = cap.read()
            # If the frame capture is unsuccessful, we enter a loop that will retry capturing the frame up to 5 times, with a short delay of 0.2 seconds between attempts. If all attempts fail, we print an error message and break out of the loop.
            while not success and attempt < 5:
                time.sleep(0.2)
                success, img = cap.read()
                attempt += 1
            if not success:
                print("Failed to capture video after multiple attempts.")
                break
            # We flip the captured image horizontally to create a mirror effect, which is common in applications like hand tracking to provide a more intuitive user experience. We also retrieve the height and width of the image for later use in scaling the hand landmark coordinates.
            img = cv2.flip(img, 1)
            h, w, _ = img.shape
            # We convert the image from BGR color space (used by OpenCV) to RGB color space (used by MediaPipe) and create a MediaPipe Image object with the converted image data. This is necessary because the hand landmarker expects input images in RGB format. 
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            
            # We use the hand landmarker to detect hand landmarks in the processed image. The results contain the detected hand landmarks, which we can then use to draw the landmarks and connections on the original image. 
            results = hands.detect(mp_image)
            # If hand landmarks are detected, we iterate through each detected hand and draw the landmarks and connections on the original image using the drawing utilities provided by MediaPipe. We also create a dictionary to store the coordinates of the fingertips (thumb, index, middle, ring, pinky) and annotate the image with the names of the fingertips and circles at their locations for better visualization.
            if results.hand_landmarks:
                for hand_landmarks in results.hand_landmarks:
                    mp_draw.draw_landmarks(
                        img, hand_landmarks, mp_connections.HAND_CONNECTIONS)
                    
                    finger_tips = {
                        "Thumb": hand_landmarks[4],
                        "Index": hand_landmarks[8],
                        "Middle": hand_landmarks[12],
                        "Ring": hand_landmarks[16],
                        "Pinky": hand_landmarks[20]
                    }
                    # We iterate through the dictionary of fingertip landmarks, calculate their pixel coordinates by scaling the normalized landmark coordinates with the image dimensions, and annotate the image with the fingertip names and circles at their locations for better visualization.
                    for name, landmark in finger_tips.items():
                        x, y = int(landmark.x * w), int(landmark.y * h)
                        cv2.putText(img, name, (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)  
                        cv2.circle(img, (x, y), 5, (0, 255, 0), cv2.FILLED)
            # Finally, we display the annotated image in a window titled "Image". We also check for a key press event, and if the 'q' key is pressed, we break out of the loop to end the program. After the loop, we release the video capture and close all OpenCV windows to clean up resources.  
            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # After the loop, we release the video capture and close all OpenCV windows to clean up resources.
    cap.release()
    cv2.destroyAllWindows()    

if __name__ == "__main__":
    main()