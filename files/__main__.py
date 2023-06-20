#use S2T_util.py    # for speech to text

import S2T_util
import T2S_util
import T2T_util




def main():
    print("HEY IM A LANGUAGE BOT")
    T2S_util.play_text("HEY IM A LANGUAGE BOT", "en")
    T2S_util.play_text("HEY IM A LANGUAGE BOT", "ar")
    #while loop that continues to listen to the user until the user says bye
    #chat_ids empty list with two empty elements
    chat_ids = ["","",0]
    while True:
        text = S2T_util.speechtotext()
        if text == (("bye") or ("goodbye") or ("stop") or ("exit")):
            print("Bot said: Bye")
            T2S_util.play_text("Bye")
            break
        else:
            response = T2T_util.createPromptWithHistory(text, chat_ids)
            #response = T2T_util.get_singal_response(text)
            #printing the response in formated way
            print("Bot said: {}".format(response))
            T2S_util.play_text(response)




if __name__ == "__main__":
    main()