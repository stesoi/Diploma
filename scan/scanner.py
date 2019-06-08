import cv2 as cv
import numpy as np


# параметры цветового фильтра
lower_level = np.array([30, 150, 50])
upper_level = np.array([255, 255, 180])
# размеры экрана
WIDTH, HEIGHT = 600, 600
# толщина линии контура
THICKNESS = 3


def scanner(filename = ""):
    continue_cycle = True
    from_video = (filename == "")
    cap = cv.VideoCapture(0) if from_video else None # захват видеопотока, аргумент - номер камеры или название видеофайла

    while (continue_cycle):
        _, frame = cap.read() if from_video else (None, cv.imread(filename)) # получение кадра

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # изменение цветовой схемы

        mask = cv.inRange(hsv, lower_level, upper_level) # накладывае на кадр цветовой фильтр в заданном диапазоне

        res = cv.bitwise_and(frame, frame, mask=mask) # вычисляет битовое соединение двух массивов или массива и скаляра
                                                      # для каждого элемента

        result = cv.Canny(frame, 100, 200)  # детектор границ Кенни

        # ищем контуры и складируем их в переменную contours
        contours, hierarchy = cv.findContours(result, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)

        # отображаем контуры поверх изображения
        cv.drawContours(result, contours, -1, (255, 255, 255), THICKNESS, cv.LINE_AA, hierarchy, 1)

        # # рисуем расположение долевой нити
        # cv.arrowedLine(result, (20, 300), (20, 200), (250, 0, 0), 1)

        # отображение полученных результатов
        cv.namedWindow('Original', cv.WINDOW_NORMAL)
        cv.imshow('Original', frame)
        cv.resizeWindow('Original', WIDTH, HEIGHT)
        cv.namedWindow('Result', cv.WINDOW_NORMAL)
        cv.imshow('Result', result)
        cv.resizeWindow('Result', WIDTH, HEIGHT)


        k = (cv.waitKey(5) & 0xFF) if from_video else cv.waitKey(0) # выход по ESC
        if k == 27:
            continue_cycle = False

    cv.destroyAllWindows()
    if(from_video):
        cap.release()