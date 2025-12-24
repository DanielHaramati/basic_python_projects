import pygame
import time
from datetime import datetime, timedelta

pygame.mixer.init() 
pygame.mixer.music.load(r"C:\Users\Daniel\Music\calculator_project_music\elevator music.mp3")

def alarm_clock(alarm_time_str):
    alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time() 
    
    now = datetime.now()
    alarm_datetime = datetime.combine(now.date(), alarm_time)

    if alarm_datetime <= now:
        alarm_datetime += timedelta(days=1)
    
    print(f"Alarm set for: {alarm_datetime}")
    while True:
        current_time = datetime.now()

        if current_time >= alarm_datetime:
            print("WAKE UP!")
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break 
        
        time.sleep(1)

#alarm_clock("7:30")
