import cv2


def extract_images(path_in: str, path_out: str = 'frames'):
    vidcap = cv2.VideoCapture(path_in)

    if not vidcap.isOpened():
        print('Error opening video')

    count = 0
    while vidcap.isOpened():
        status, image = vidcap.read()

        if not status:
            print('Video file finished. Total Frames:', int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
            break

        cv2.imwrite(rf'{path_out}\frame{count}.jpg', image)
        count += 1


if __name__== '__main__':
    extract_images('videos/sample.mp4')
