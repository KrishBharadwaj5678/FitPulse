from ultralytics import YOLO
import cv2
import time
from datetime import datetime
from utils import calculate_angle
from audio import playSound
from excel import saveWorkout
from graph import showGraph

# Load the model
model = YOLO("yolo26n-pose.pt")

# Start Tracking
results = model.track("samples/demo.mp4",persist=True,stream=True)
counter = 0
stage = None

# Rep Speed Tracking
rep_speed = 0
rep_start_time = None

# Workout tracking for calculating avg, total
start_time = time.time()
total_speed = 0
rep_count_for_avg = 0

# Graph Variables
rep_numbers = []
rep_speeds = []

last_warning_time = 0

for r in results:
    frame = r.plot(labels=False,conf=False) # Hide labels and conf text
    frame = cv2.resize(frame,(500,500))

    # Ensures a person is detected
    if r.keypoints is not None:
        # Gets first person’s keypoints
        kpts = r.keypoints.xy[0]

        shoulder = kpts[5]
        elbow = kpts[7]
        wrist = kpts[9]
        hip = kpts[11]
        ankle = kpts[15]

        # Calculate angle
        angle = calculate_angle(shoulder,elbow,wrist)

        # Calculate body alignment
        body_angle = calculate_angle(shoulder,hip,ankle)

        if body_angle < 150:
            cv2.putText(frame,"Keep body straight!",(20,125),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

            if time.time() - last_warning_time > 2:
                last_warning_time = time.time()

        # Push-up logic
        down_threshold = 95
        up_threshold = 155

        if stage is None:
            stage = "down" if angle < 120 else "up"

        # Start timing when going down
        if angle < down_threshold:
            if stage != "down":
                rep_start_time = time.time()
            stage = "down"
        elif angle > up_threshold and stage == "down":
            stage = "up"
            counter += 1
            # Play the sound
            playSound()

            if rep_start_time is not None:
                rep_speed = time.time() - rep_start_time
                # Accumulate speed for average
                total_speed += rep_speed
                rep_count_for_avg += 1
                # Append data for graph visuals
                rep_numbers.append(counter)
                rep_speeds.append(rep_speed)


    cv2.putText(frame,f"Push Ups: {counter}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

    cv2.putText(frame,f"Pace: {rep_speed:.2f}s",(20,85),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255, 255, 0   ),2)

    cv2.imshow("FitPulse - Smart Fitness Tracker",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

# Save workout data after loop ends
end_time = time.time()
duration = end_time - start_time

avg_speed = total_speed / rep_count_for_avg if rep_count_for_avg > 0 else 0

saveWorkout(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    counter,
    round(avg_speed, 2),
    round(duration, 2)
)

showGraph(rep_numbers,rep_speeds)