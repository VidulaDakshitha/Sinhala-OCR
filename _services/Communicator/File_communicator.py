from _config.bas64_image.convertor_image import RGBtoGray, GraytoRGB
from _services.Communicator.string_builder import String_builder
from _services.Handwritten.handwritten_identification import word_builder, gethandwritten_prediction
from _services.Printed_OCR.pocr_main import PrintedOCR
from _services.Segmentation.overall_segmentation import mainFunc
import cv2
import environ

from _services.punctuation_recognition.character_validation import check_punct

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
from _services.Spell_checker.spellchecker_main import spellchecker_main
from _services.punctuation_recognition.punctuation_main import punctuation_main
from _services.Handwritten.handwritten_identification import gethandwritten_prediction
from _services.Handwritten.handwritten_identification import word_builder
import uuid
import matplotlib.pyplot as plt


def communication(array,data):
    result_question=[]
    for item in array:
        segmented_array=mainFunc(RGBtoGray(item),120)

        result_question.append(segmented_array)
        # cv2.imshow("output", item)
        # cv2.waitKey()
        # cv2.destroyAllWindows()

    question_string=""
    question_string2=""
    for i, ans_index in enumerate(result_question):
        print("Question Array", i)
        for index, item2 in enumerate(ans_index):
            identify_string = PrintedOCR(item2)
            question_string=identify_string
            print("question",identify_string)


            if index<len(result_question)-1:

                question_string2=question_string2+question_string+","
            elif index==len(result_question)-1:

                question_string2 = question_string2 + question_string


    # for i, ans_index in enumerate(result_question):
    #     print("Answer Area",i)
    #     for j, item2 in enumerate(ans_index):
    #
    #         for k,word in enumerate(item2):
    #
    #             for l,char in enumerate(word):
    #                 cv2.imwrite(env('PROJECT_SRC')+'_services/Segmentation/questions/'+str(i) + "," + str(j) + "," + str(k)+"," + str(l)+'.png', char)
    print(question_string2)
    return question_string2





def communication_answer(array, questions):
    print(questions)
    result_array = []
    for item in array:
        segmented_array = mainFunc(item, 380)

        result_array.append(segmented_array)

    prediction = ""
    result_word = []
    Final_output = []
    result_line=[]
    for i, ans_index in enumerate(result_array):
        print("Answer Area", i)

        for j, item2 in enumerate(ans_index):
            result_line = []
            result_word = []
            for k, word in enumerate(item2):

                result_pretict_word = []

                for l, char in enumerate(word):
                    ht, wd = char.shape

                    if (ht < 28 and wd < 28) or check_punct(char):
                        value = punctuation_main(GraytoRGB(char))
                        print(ht,wd)
                        result_pretict_word.append(value)

                    else:
                        # unique_filename = str(uuid.uuid4())

                        # cv2.imwrite("C:/Users/sathira/OneDrive/Desktop/sig/" +str(i) + str(j) + str(k) + str(j) +
                        # ".jpg",GraytoRGB(char))
                        # cv2.imwrite("D:/SLIIT/LectureSLIIT/Year4 SEM1/Research project/RESEARCH DOCUMENT/PP2/test_segemet/input/" +unique_filename+ ".jpg",GraytoRGB(char))

                        # cv2.imshow("image",GraytoRGB(char))
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()

                        prediction = gethandwritten_prediction(GraytoRGB(char))

                    # print("Character prediction :", prediction)
                        result_pretict_word.append(prediction)


                join_string = ''.join(result_pretict_word)
                print('############################################## ', k)

                # print('created word :', join_string)

                string_word = word_builder(join_string)

                # print('modified word :', string_word)

                result_word.append(string_word)
            # print("vidula",result_word)
            result_line.append(result_word)
        # list_value5 = ['මම', 'ඔහුව', 'පුදු', 'කළේය', 'පුදු']
            print('All WORD :',result_line)
            list_value5 =result_word

            data = spellchecker_main(list_value5),
            print("data error",data)
            result = {
                "question": questions[i],
                "answer": data,
            }
            print("result",result)
            Final_output.append(result)

    return Final_output
