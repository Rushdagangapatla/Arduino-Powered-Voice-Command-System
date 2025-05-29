import pyttsx3
import PyPDF2
def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate',250)
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()

def read_pdf(file_path):
    try:
        with open(file_path,'rb')as pdf_file:
            pdf_reader =PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page=pdf_reader.pages[page_num]
                text=page.extract_text()
                print(f"Reading page {page_num+1}...")
                speak(text)
    except Exception as e:
        print(f"An error occurred :{e}")
        speak("sorry ,I couldn't read the PDF file.")
if __name__ =="__main__":
    pdf_file_path=[r"D:\ai\Robotics.pdf",
                   r"D:\ai\Robotics.pdf",
                   r"D:\ai\Robotics.pdf"]
                   
    i=1
    for filepath in pdf_file_path:
        print("PDF number : " + str(i))
        i+=1
        read_pdf(filepath)