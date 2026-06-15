<img width="400" height="307" alt="myfirst" src="https://github.com/user-attachments/assets/3ed34020-6f0b-4030-b6c4-5eb0f7bc8f71" />


# 🤖 Real-Time Hand Tracking & Finger Labeling AI

Welcome to the first stop in my journey of exploring computer vision models, one step at a time! This project uses a live webcam feed to map out human hands and dynamically label each finger tip in real-time.

---

## 🚀 The Backstory: Breaking Out of the "Tutorial Trap"

I built this while following a step-by-step YouTube tutorial by **Manoj Singh Negi**: [Create a Hand Tracker in Python](https://www.youtube.com/watch?v=1lN4L74BwW0). 

But during development, I hit a massive wall: **outdated code**. The tutorial used MediaPipe's old setup (`mp.solutions.hands`), which Google has since deprecated. Instead of giving up when the code crashed, I dug through the documentation and figured out how to migrate the entire project over to the modern framework.

### 🧠 What I Actually Learned & Fixed:
* **Switched to Tasks Vision:** I replaced the old `mp.solutions.hands` pipeline entirely and set it up using the new, modern `mp.tasks.vision.HandLandmarker`. 
* **Loading the AI's Brain:** I learned that the new Tasks API requires you to manually download and point to an external model asset file (`hand_landmarker.task`) to actually load the neural network weights into the script.
* **The List Indexing Bug Fix (My Big Win):** The tutorial called coordinates using `hand_landmarks.landmark[x]`, which caused my code to throw an error and crash. I figured out that in the new Tasks API, the landmarks are already returned as a direct Python list, so I had to completely strip out the `.landmark` attribute to fix the crash.
* **Doing the Math for Pixels:** The AI doesn't give you coordinates in screen pixels; it gives you decimals/percentages (0.0 to 1.0). I learned how to multiply those percentages against the webcam's actual width and height to get the exact pixel coordinates for drawing circles and text.

---

## 🛠️ Tools Used
* **Python** (Core language)
* **OpenCV / `cv2`** (For handling the webcam feed and drawing things on screen)
* **MediaPipe Tasks API** (The machine learning framework running the tracking engine)
* **Python's `time` module** (Used as a quick safety net to give the webcam a moment to wake up so the script doesn't instantly freeze on boot)

---

## 📊 How the Hand is Mapped

The MediaPipe engine tracks exactly **21 points** on your hand in real-time:



To make the finger-labeling feature work, I mapped the dictionary directly to the exact index points of the fingertips:
* **Thumb:** Point 4
* **Index:** Point 8
* **Middle:** Point 12
* **Ring:** Point 16
* **Pinky:** Point 20

---

## 📈 What's Next?
Now that the baseline tracking is working using the modern API, I want to take this further:
* Use vector math to calculate the distance between fingertips (like detecting a "pinch" or "click" gesture).
* Connect those gestures to actual keyboard or mouse commands on my PC (like controlling volume with my hand!).

*Drop a star ⭐️ if this repo helped you fix your MediaPipe version errors!*
