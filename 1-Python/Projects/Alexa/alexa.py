import webbrowser
import time
from time import strftime, ctime
import os
import playsound
from gtts import gTTS
import speech_recognition as sr

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def record_audio(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio
    
    def recognize_speech(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language="ar-EG") 
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")
        return ""
    
    def respond(self, response):
        tts = gTTS(text=response, lang='ar')
        filename = "response.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    
    def handle_command(self, command):
        if "صباح الخير" in command:
            self.respond("صباح الخير يا محمد! كيف يمكنني مساعدتك؟")
        elif "الوقت" in command:
            current_time = strftime("%H:%M")  # Format time to HH:MM
            self.respond(f"الساعة الآن {current_time}")
        elif "اليوم" in command:
            day_of_week = strftime("%A")
            days_in_arabic = {
                "Monday": "الاثنين",
                "Tuesday": "الثلاثاء",
                "Wednesday": "الأربعاء",
                "Thursday": "الخميس",
                "Friday": "الجمعة",
                "Saturday": "السبت",
                "Sunday": "الأحد"
            }
            current_day = days_in_arabic.get(day_of_week, "غير معروف")
            
            date_today = strftime("%d")
            month_of_year = strftime("%B")
            months_in_arabic = {
                "January": "يناير",
                "February": "فبراير",
                "March": "مارس",
                "April": "أبريل",
                "May": "مايو",
                "June": "يونيو",
                "July": "يوليو",
                "August": "أغسطس",
                "September": "سبتمبر",
                "October": "أكتوبر",
                "November": "نوفمبر",
                "December": "ديسمبر"
            }
            current_month = months_in_arabic.get(month_of_year, "غير معروف")
            
            current_year = strftime("%Y")
            
            self.respond(f"اليوم هو {current_day}, {date_today} {current_month} {current_year}")
        elif "افتح جوجل" in command:
            self.open_website(command)
        elif "سلام" in command:  # New command to stop the assistant
            self.respond("سلام يا محمد")
            self.stop_assistant()
        else:
            self.respond("أنا آسفة أنا لا أفهم هذا الأمر")
    
    def open_website(self, command):
        url = "https://www.google.com"
        webbrowser.open(url)
        self.respond("تم فتح موقع جوجل")
    
    def stop_assistant(self):
        self.respond("إلى اللقاء!")
        exit()
    
    def run(self):
        while True:
            audio = self.record_audio()
            if audio:
                command = self.recognize_speech(audio)
                if command:
                    self.handle_command(command)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
