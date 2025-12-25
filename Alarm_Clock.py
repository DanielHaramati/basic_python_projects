import pygame
import time
from datetime import datetime, timedelta

songs = {}

with open(r"songs_paths.txt", "r") as f:
    for line in f:
        if "=" not in line:
            continue

        parts = line.split("=", 1)
        name = parts[0].strip().lower()
        path = parts[1].strip()

        songs[name] = path

try:
    godzilla_path = songs["godzilla"]
    elevator_path = songs["elevator"]
    mockingbird_path = songs["mockingbird"]
except KeyError:
    print("Missing song paths in songs_paths.txt")
    exit()


def music_choice(song_choice):
    song_choice = song_choice.lower()

    if song_choice == "godzilla":
        return godzilla_path
    elif song_choice == "elevator":
        return elevator_path
    elif song_choice == "mockingbird":
        return mockingbird_path
    else:
        print("Invalid choice, defaulting to elevator music.")
        return elevator_path


def is_alarm_time_valid(wanted_time_for_alarm):
    if len(wanted_time_for_alarm) != 5:
        return False

    if wanted_time_for_alarm[2] != ":":
        return False

    if not wanted_time_for_alarm[0].isdigit():
        return False
    if not wanted_time_for_alarm[1].isdigit():
        return False
    if not wanted_time_for_alarm[3].isdigit():
        return False
    if not wanted_time_for_alarm[4].isdigit():
        return False

    hour = int(wanted_time_for_alarm[:2])
    minute = int(wanted_time_for_alarm[3:])

    if hour < 0 or hour > 23:
        return False
    if minute < 0 or minute > 59:
        return False

    return True

def alarm_clock(alarm_time_str):
    alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time()

    now = datetime.now()
    alarm_datetime = datetime.combine(now.date(), alarm_time)

    if alarm_datetime <= now: # if the hour has already passed today , tommorow. else today;
        alarm_datetime = alarm_datetime + timedelta(days=1)

    print("Alarm set for:", alarm_datetime)

    while True:
        if datetime.now() >= alarm_datetime:
            print("WAKE UP!")
            pygame.mixer.music.play(-1)

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

        time.sleep(1)


def final_action():
    print("Welcome to the Alarm Clock!")

    song_choice = input("Choose your alarm sound (Godzilla, Elevator, Mockingbird): ")
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(music_choice(song_choice))
    except pygame.error as error:
        print("Failed to load song:", error)
        return

    wanted_time_for_alarm = input("Please enter the alarm time (HH:MM): ")

    if is_alarm_time_valid(wanted_time_for_alarm):
        alarm_clock(wanted_time_for_alarm)
    else:
        print("The time format you entered isn't valid.")


final_action()
