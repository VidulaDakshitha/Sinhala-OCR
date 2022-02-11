
import tensorflow as tf

from _config.bas64_image.convertor_image import GraytoRGB
from _config.validators.sha256_validator import valid
from _services.Printed_OCR.preprocessing_pocr import predictLetter
from _services.Printed_OCR.preprocessing_pocr import array
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
dict = {}
dict['9274'] = 'කෙ'
dict['14274'] = 'කේ'
dict['19274'] = 'ගෙ'
dict['24274'] = 'ගේ'
dict['43274'] = 'ටෙ'
dict['50274'] = 'ටේ'
dict['74274'] = 'දෙ'
dict['79274'] = 'දේ'
dict['83274'] = 'නෙ'
dict['84274'] = 'නේ'
dict['91274'] = 'පෙ'
dict['92274'] = 'පේ'
dict['100274'] = 'බෙ'
dict['101274'] = 'බේ'
dict['108274'] = 'මෙ'
dict['109274'] = 'මේ'
dict['114274'] = 'යෙ'
dict['115274'] = 'යේ'
dict['120274'] = 'රෙ'
dict['121274'] = 'රේ'
dict['126274'] = 'ලෙ'
dict['127274'] = 'ලේ'
dict['132274'] = 'වෙ'
dict['133274'] = 'වේ'
dict['157274'] = 'සෙ'
dict['158274'] = 'සේ'
dict['165274'] = 'හෙ'
dict['166274'] = 'හේ'
dict['114275'] = 'යා'
dict['198275'] = 'භා'
dict['36275'] = 'ජා'
dict['219275'] = 'ථා'
dict['148275'] = 'ශා'
dict['132275'] = 'වා'
dict['1275'] = 'ආ'
dict['74275'] = 'දා'
dict['83275'] = 'නා'
dict['132275'] = 'වා'
dict['126275'] = 'ලා'
dict['108275'] = 'මා'
dict['120275'] = 'රා'
dict['9275'] = 'කා'
dict['139275'] = 'ෂා'
dict['165275'] = 'හා'
dict['91275'] = 'පා'
dict['100275'] = 'බා'
dict['157275'] = 'සා'
dict['1280'] = 'අං'
dict['75280'] = 'දිං'
dict['120276'] = 'රු'
dict['74276'] = 'දැ'
dict['114276'] = 'යැ'
dict['91276'] = 'පැ'
dict['132276'] = 'වැ'
dict['1276'] = 'ඇ'
dict['100276'] = 'බැ'
dict['65276'] = 'තැ'
dict['165276'] = 'හැ'

new_model = tf.keras.models.load_model(env('PROJECT_SRC')+'_models/printedOCR/model_new_2.h5')

# def loadModel():
#     new_model = tf.keras.models.load_model(env('PROJECT_SRC')+'_models/printedOCR/model_new_2.h5')
#     return new_model

def PrintedOCR(arrayGet):
    # new_model = loadModel()
    previous_letter = 0
    next_letter = 0
    letter = ""
    word = ""
    completeSen = ""
    length = len(arrayGet)
    if length < 1:
        return "Error Occured in Printed OCR"
    else:
        for i in arrayGet:
            # to track the comb
            comb_detected = False
            # completeSen = valid(data2,idta)
            # to track the sub letter part
            sub_next = False
            
            # index of the element of the current word array
            index = 0
            for j in i:
                # Converting numpy to image
                c_pred, pred_letter, pred_con = predictLetter(j,new_model)
                print(pred_letter)
                next_letter = -1
                if c_pred == 274:
                    comb_detected = True
                else:
                    if comb_detected is True:
                        # use the dict var for letter creation
                        letter = str(c_pred) + "274" 
                        try:
                            if dict[letter] != "":
                                word = word + dict[letter]
                                letter = ""
                            else:
                                print('Empty')
                        except:
                            print('Cannot find the predicted letter')
                            print("Null")
                        comb_detected = False
                    else:
                        if index+1 is not len(i):
                            c_pred_next, pred_letter, pred_con = predictLetter(i[index+1],new_model)
                            next_letter = c_pred_next
                        
                        if next_letter == 275 or next_letter == 280 or next_letter == 276:
                            sub_next = True
                            previous_letter = str(c_pred) + str(next_letter)
                            
                        else:   
                            if sub_next is True:
                                # use the dict var for letter creation
                                try:
                                    if dict[previous_letter] != "":
                                        word = word + dict[previous_letter]
                                        previous_letter = ""
                                    else:
                                        print('Empty')
                                except:
                                    print('Cannot find the predicted letter')
                                    print("Null")
                                    word="null"
                                sub_next = False
                            else:
                                letter = array[c_pred]   
                                word = word + letter
                index = index + 1


            completeSen = completeSen + word + " "
            letter = ""
            word = ""
        return completeSen