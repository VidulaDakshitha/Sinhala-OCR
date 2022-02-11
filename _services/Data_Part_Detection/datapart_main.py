import cv2

from _services.Data_Part_Detection.AnswersMain import getAnswerAreaContour, clearImage
from _services.Data_Part_Detection.QuestionsMain import getQuestionContours, reorderImages


def question_datapart_main(image):


    findArea = 10

    contours_questions = getQuestionContours(image)
    question_images = []
    count = 1
    for cnt in contours_questions:
        if not cnt is None:
            x, y, w, h = cv2.boundingRect(cnt)
            img = image[y:y + h, x:x + w]
            question_images.append(img)


            count = count + 1


    new_question_images = reorderImages(question_images)
    return new_question_images

def answer_datapart_main(image):
    # =================== Answer Area Detection in Blank Form =======================
    # Getting the answer area contours from the train image and applying the boundaries for OCR image
    contours_answer = getAnswerAreaContour(image)
    count = 1
    answer_images = []
    for cnt in contours_answer:
        if not cnt is None:
            x, y, w, h = cnt[0], cnt[1], cnt[2], cnt[3]
            img=image[y:y+h,x:x+w]
            # removing the lines in answer areas and keeping only the strings
            # that takes only the string values and removes the line edges from the answer areas
            image_clean = clearImage(img)

            answer_images.append(image_clean)
            count = count + 1

    new_answer_images = reorderImages(answer_images)
    return new_answer_images