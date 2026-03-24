import speech_recognition as sr

r = sr.Recognizer()

# Prompt user for the audio file path
file_path = input("Enter the path to the audio file (e.g., file.wav): ")
file_path = file_path.strip('"')

try:
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        print("Recognized text:", text)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except sr.UnknownValueError:
    print("Error: Could not understand the audio.")
except sr.RequestError as e:
    print(f"Error: Could not request results from Google Speech Recognition service; {e}")