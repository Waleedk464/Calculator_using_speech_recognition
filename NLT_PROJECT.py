
# saari Libraries
import operator
from typing import Text
import speech_recognition as s_r
from gtts import gTTS
from pydub import AudioSegment
import winsound
import time
import os #Unused Library

# Check karne keh liye keh code chala or 
# Speech Recogniton ki libaray neh masla toh nai kiya
print("Your speech_recognition version is: "+s_r.__version__)

#object banaya hai Recognizer Ka
r = s_r.Recognizer()

while True:
    #Mircophone ko inititalize karne keh liye
    my_mic_device = s_r.Microphone(device_index=1)
    with my_mic_device as source:
        print("Say what you want to calculate, example: 3 plus 3")

    # Distortion ko kum karne keh liye 
        r.adjust_for_ambient_noise(source)

    # Bata Rahay hen keh Audio kaha seh lani hai
        audio = r.listen(source)

    # yahan recognition hori hai 
    my_string=r.recognize_google(audio)

    # yahan show karayeGa keh uski samajh meh kiya aya
    print(my_string)

    # yahan Calculator ka code shuru hai
    def get_operator_fn(op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            'x' : operator.mul,
            'divided' :operator.__truediv__,
            'Mod' : operator.mod,
            'mod' : operator.mod,
            '^' : operator.xor,
            }[op]

    # yahan Calculation hori hai
    def eval_binary_expr(op1, oper, op2):
        op1,op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    # Calculate hui we value print hori hai
    print(eval_binary_expr(*(my_string.split())))

    # yaha int wali value ko string meh store karke 
    # FS keh variable meh dala hai
    FS = str(eval_binary_expr(*(my_string.split())))

    # By default Equals to nai bol raha tha toh usko string meh daldiya
    EQ = " Equals to "

    # Yahan jo kuch bulwana hai usko ek string meh dal rahay hen
    Final_String = my_string + EQ + FS

    # yahan bata rahay hen keh language konsi hai
    language = 'en'

    #Yahan Object bana rahay hen gTTS ka
    myobj = gTTS(text=Final_String, lang=language, slow=False)

    # yahan audio file save hori hai
    myobj.save("Audio.mp3")

    # convert wav to mp3
    # jab Mp3 play karay thay toh media player launch hora tha                                              
    sound = AudioSegment.from_mp3("Audio.mp3")
    sound.export("Wav_audio.wav", format="wav")
    winsound.PlaySound('Wav_audio.wav', winsound.SND_ASYNC)

    # Audio complete play honay seh pehle Script end hori thee isliye sleep lagaDiya 
    time.sleep(5)
    my_mic_device = s_r.Microphone(device_index=1)
    # Yaha puchayGA or kuch calcualte karna hai ?
    with my_mic_device as source:
        print("Any More Calculations ?")


    # Distortion ko kum karne keh liye 
        r.adjust_for_ambient_noise(source)

    # Bata Rahay hen keh Audio kaha seh lani hai
        audio = r.listen(source)

    # yahan recognition hori hai 
    my_string=r.recognize_google(audio)

    # Agr User No boleGa toh exit kardeGa warna repeat hojaye Program
    print(my_string)
    if my_string == "no":
        break

    # Comented code (Ignore)
    # os.system("start Audio.mp3")
