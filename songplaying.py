import pygame
import os
def play_mp3(file_path):
    pygame.mixer.init()
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    try:
        pygame.mixer.music.load(file_path)
        print(f"playing {os.path.basename(file_path)}...")
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"An error occurred while playing the file : {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
if __name__=="__main__":
    mp3_file_path =r"D:\ai\song.mp3"
    play_mp3(mp3_file_path)