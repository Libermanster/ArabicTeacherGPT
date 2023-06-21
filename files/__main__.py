#this is a robot that can talk to the user in english and arabic
#the robot can talk about any subject that the user wants to talk about
#its get prompet from the user in english and respond in english and arabic


import S2T_util
import T2S_util
import T2T_util

def main():
    #robot started message and explain how to use the robot
    #create a history for the chat
    #get the subject that the user wants to talk about
    #start a loop that continues to listen to the user until the user says bye
    #get the user input
    #if the user input is bye then break the loop
    #else get the response from the bot
        #send the user input and the history to the bot through content handler
    #print the response
    #play the response in english and the arabic





""" def main():
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
            T2S_util.play_text(response) """




if __name__ == "__main__":
    main()