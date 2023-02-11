
# import speech_recognition as sr
# import wikipedia as wk

# while True:
#     mic = sr.Recognizer()

#     with sr.Microphone() as source:
#         print('Speac')
#         audio = mic.listen(source)
#         mic.adjust_for_ambient_noise(source)
#         print(audio)
#         try:
#             text = mic.recognize_google()
#             summary = wk.summary(audio)
#             print(text)
#             print(summary)
#             break
#         except:
#             print("Did'n Get that")


import speech_recognition
import pyttsx3
import wikipedia
wikipedia.set_lang('UZ')

recognize = speech_recognition.Recognizer()

while True:
    try:

        with speech_recognition.Microphone() as mic:
            recognize.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognize.listen(mic)
            text = recognize.recognize_google(audio)
            print(text)

            text = text.lower()
            print(text)
            print(audio)
            print(wikipedia.summary(text))
            pyttsx3.speak(wikipedia.summary(text))


    except speech_recognition.UnknownValueError():
        recognize = speech_recognition.Recognizer()
        continue


# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters

# buttons = ReplyKeyboardMarkup([['Start'], ['Raqmni izlash'],['Dasturni ochish']], resize_keyboard=True)


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=buttons)
#     return 1 

# async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=buttons)

# async def world(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=buttons)




# conv_hendler = ConversationHandler(
#     entry_points=[CommandHandler('start', hello)],
#     states={
#         1:[
#             MessageHandler(filters.Regex('^(Statistka)$'), stats),
#             MessageHandler(filters.Regex('^(Dunyo)$'), world),
#         ]
#     },
#     fallbacks=[filters.Text ,hello]
# )


# app = ApplicationBuilder().token("5554560464:AAEYnOckVOYEXLn85nIJ2vhbLDVRFTY9URo").build()


# app.add_handler(conv_hendler)

# app.run_polling()