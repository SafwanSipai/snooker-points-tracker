from ultralytics import YOLO


def calculate_points(image):
    classes_points = {
        "0": {"ball": "black", "points": 7},
        "1": {"ball": "blue", "points": 5},
        "2": {"ball": "brown", "points": 4},
        "3": {"ball": "green", "points": 3},
        "4": {"ball": "pink", "points": 6},
        "6": {"ball": "red", "points": 1},
        "7": {"ball": "white", "points": 0},
        "8": {"ball": "yellow", "points": 2},
    }

    model = YOLO("model.pt")
    results = model.predict(source=image)
    remaining_points = 0
    ball_count = {}

    for class_name in results[0].boxes.cls.tolist():
        class_name = str(int(class_name))
        if class_name in ball_count and class_name != "6":
            ball_count["6"] += 1
        elif class_name in ball_count and class_name == "6":
            ball_count[class_name] += 1
        else:
            ball_count[class_name] = 1
    try:
        remaining_points += ball_count["6"] * 8
    except Exception as e:
        print(e)

    for ball in ball_count:
        if ball != "6":
            remaining_points += classes_points[ball]["points"]

    return remaining_points
