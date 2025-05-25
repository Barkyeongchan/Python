
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Importing all images
imgBackground = cv2.imread(r"C:\Users\xodud\Downloads\Resources\Background.png")
imgGameOver = cv2.imread(r"C:\Users\xodud\Downloads\Resources\gameOver.png")
imgBall = cv2.imread(r"C:\Users\xodud\Downloads\Resources\Ball.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread(r"C:\Users\xodud\Downloads\Resources\bat1.png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread(r"C:\Users\xodud\Downloads\Resources\bat2.png", cv2.IMREAD_UNCHANGED)

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
ballPos = [100, 100]
speedX = 15
speedY = 15
gameOver = False
score = [0, 0]

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgRaw = img.copy()

    # Find the hand and its landmarks
    hands, img = detector.findHands(img, flipType=False)  # with draw

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

    # Check for hands
    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']
            h1, w1, _ = imgBat1.shape
            y1 = y - h1 // 2
            y1 = np.clip(y1, 20, 415)

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgBat1, (59, y1))
                if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] += 30
                    score[0] += 1

            if hand['type'] == "Right":
                img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
                if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] -= 30
                    score[1] += 1

    # Game Over
    if ballPos[0] < 40 or ballPos[0] > 1200:
        gameOver = True

    if gameOver:
        img = imgGameOver
        cv2.putText(img, str(score[1] + score[0]).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX,
                    2.5, (200, 0, 200), 5)

    # If game not over move the ball
    else:

        # Move the Ball
        if ballPos[1] >= 500 or ballPos[1] <= 10:
            speedY = -speedY

        ballPos[0] += speedX
        ballPos[1] += speedY

        # Draw the ball
        img = cvzone.overlayPNG(img, imgBall, ballPos)

        cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))

    cv2.imshow(r"C:\Users\xodud\Downloads\Resources", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        ballPos = [100, 100]
        speedX = 15
        speedY = 15
        gameOver = False
        score = [0, 0]
        imgGameOver = cv2.imread(r"C:\Users\xodud\Downloads\Resources\gameOver.png")

'''import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# 이미지 불러오기
imgBackground = cv2.imread(r"C:\Users\xodud\Downloads\Resources\Background.png")
imgGameOver = cv2.imread(r"C:\Users\xodud\Downloads\Resources\gameOver.png")
imgBall = cv2.imread(r"C:\Users\xodud\Downloads\Resources\Ball.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread(r"C:\Users\xodud\Downloads\Resources\bat1.png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread(r"C:\Users\xodud\Downloads\Resources\bat2.png", cv2.IMREAD_UNCHANGED)

# 손 인식기
detector = HandDetector(detectionCon=0.8, maxHands=2)

# 게임 변수
numBalls = 3
ballPos = [[100 + i * 50, 100 + i * 50] for i in range(numBalls)]
ballSpeeds = [[15, 15] for _ in range(numBalls)]
gameOver = False
score = [0, 0]

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgRaw = img.copy()

    # 손 인식
    hands, img = detector.findHands(img, flipType=False)

    # 배경 덮기
    img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

    # 패들 위치 설정
    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']
            h1, w1, _ = imgBat1.shape
            y1 = np.clip(y - h1 // 2, 20, 415)

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgBat1, (59, y1))
            elif hand['type'] == "Right":
                img = cvzone.overlayPNG(img, imgBat2, (1195, y1))

    # 게임 오버 여부 확인
    for i in range(numBalls):
        if ballPos[i][0] < 40 or ballPos[i][0] > 1200:
            gameOver = True
            break

    if gameOver:
        img = imgGameOver
        cv2.putText(img, str(score[1] + score[0]).zfill(2), (585, 360),
                    cv2.FONT_HERSHEY_COMPLEX, 2.5, (200, 0, 200), 5)

    else:
        for i in range(numBalls):
            bx, by = ballPos[i]
            sx, sy = ballSpeeds[i]

            # 위아래 벽 충돌
            if by >= 500 or by <= 10:
                sy *= -1

            # 패들과 충돌
            if hands:
                for hand in hands:
                    x, y, w, h = hand['bbox']
                    h1, w1, _ = imgBat1.shape
                    y1 = np.clip(y - h1 // 2, 20, 415)

                    if hand['type'] == "Left":
                        if 59 < bx < 59 + w1 and y1 < by < y1 + h1:
                            sx *= -1
                            bx += 30
                            score[0] += 1

                    elif hand['type'] == "Right":
                        if 1195 - 50 < bx < 1195 and y1 < by < y1 + h1:
                            sx *= -1
                            bx -= 30
                            score[1] += 1

            # 위치 업데이트
            bx += sx
            by += sy

            ballPos[i] = [bx, by]
            ballSpeeds[i] = [sx, sy]

            # 공 그리기
            img = cvzone.overlayPNG(img, imgBall, [bx, by])

        # 점수 표시
        cv2.putText(img, str(score[0]), (300, 650),
                    cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(score[1]), (900, 650),
                    cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    # 미니 화면
    img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))

    cv2.imshow(r"C:\Users\xodud\Downloads\Resources", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        ballPos = [[100 + i * 50, 100 + i * 50] for i in range(numBalls)]
        ballSpeeds = [[15, 15] for _ in range(numBalls)]
        gameOver = False
        score = [0, 0]
        imgGameOver = cv2.imread(r"C:\Users\xodud\Downloads\Resources\gameOver.png")'''
