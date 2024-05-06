import cv2
import click
from utils import calculate_points


@click.command()
@click.option(
    "--video_path",
    type=click.Path(exists=True),
    default="video.mp4",
    help="Path to the video file",
)
def main(video_path):
    frame_interval = 400  # process every 400th frame
    frame_counter = 0
    remaining_points = ""
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 640))

        if frame_counter % frame_interval == 0:
            remaining_points = calculate_points(frame)

        frame_counter += 1
        cv2.putText(
            frame,
            f"Remaining points: {remaining_points}",
            (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
