<img width="400" height="307" alt="myfirst" src="https://github.com/user-attachments/assets/3ed34020-6f0b-4030-b6c4-5eb0f7bc8f71" />


# 🤖 Real-Time Hand Tracking & Finger Labeling

This is my first project trying out computer vision models. It connects to a live webcam feed, tracks human hands, and labels each finger tip on the screen in real-time.

---

## 💻 The Backstory

I was following this step-by-step YouTube tutorial by Manoj Singh Negi: [Create a Hand Tracker in Python](https://www.youtube.com/watch?v=1lN4L74BwW0). 

The code in the video used MediaPipe's old setup (`mp.solutions.hands`), but it kept crashing because Google updated the library and deprecated those old functions. Instead of quitting, I checked the documentation and learned how to switch everything over to the new version.

### 🧠 What I Learned & Fixed:
* **Switched to Tasks Vision:** I replaced the old `mp.solutions.hands` stuff entirely and set it up using the modern `mp.tasks.vision.HandLandmarker`.
* **Adding the .task File:** The new version requires you to download a model asset file called `hand_landmarker.task` and point your code to it so the AI engine actually has a brain file to read.
* **Fixing the Landmark Crash:** The tutorial used `hand_landmarks.landmark[x]` to get finger coordinates, which broke my code. I figured out that in the new Tasks API, you have to strip out `.landmark` and just write `hand_landmarks[x]` directly because it returns a regular Python list now.
* **Webcam Pixels Math:** The AI outputs positioning coordinates as percentages (0.0 to 1.0) instead of raw screen pixels. I learned how to multiply those percentages by the webcam's actual width and height to get the correct `(x, y)` pixel spots to draw the circles and text.

---

## 🛠️ Tools Used
* **Python**
* **OpenCV (`cv2`)** - For opening the webcam and rendering the text/shapes on screen.
* **MediaPipe Tasks API** - The AI library handling the actual hand tracking.
* **Time module** - A quick fallback script to give the webcam a moment to boot up so the app doesn't crash on startup.

---

## 📊 How the Hand is Mapped

The tracking engine finds 21 points on your hand. To label the fingertips, I mapped my code to these specific index points:
* **Thumb:** Point 4
* **Index:** Point 8
* **Middle:** Point 12
* **Ring:** Point 16
* **Pinky:** Point 20

---

*Drop a star ⭐️ if this repo helped you fix your MediaPipe version errors!*
