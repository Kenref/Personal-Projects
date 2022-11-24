# improved pomodoro timer
import time
import os
import sys


def main():
    #default pomodoro method
    if len(sys.argv) == 1:
        print("Default mode")
        work, rest = get_times()
        work_seconds, rest_seconds = convert_to_seconds(work), convert_to_seconds(rest)
        pomo = input("Amount of times: ")
        default_timer(work_seconds, rest_seconds, pomo)

    #continuous mode, timer does not stop
    elif len(sys.argv) == 2:
        if sys.argv[1] == "mode2" or sys.argv[1] == "continuous":
            print("Continuous mode")
            work, rest = get_times()
            work_seconds, rest_seconds = convert_to_seconds(work), convert_to_seconds(rest)
            continuous_timer(work_seconds, rest_seconds)

def get_times():
    try:
        work = int(input("Enter work minutes: "))
        rest = int(input("Enter rest minutes: "))
    except ValueError:
        sys.exit("Input number")
    else:
        return work, rest

def convert_to_seconds(minutes):
    seconds = int(minutes) * 60
    return seconds

def counter_down(times, label):
    try:
        while times:
            min, sec = divmod(times, 60)
            print(f"{label} time left: {min:02d}:{sec:02d}", end="\r")
            time.sleep(1)
            times -= 1
    except TypeError:
        sys.exit("Type Error")

def counter_up():
    timer = 0
    try:
        while True:
            min, sec = divmod(timer, 60)
            print(f"Overtime: -{min:02d}:{sec:02d}", end="\r")
            time.sleep(1)
            timer += 1
    except TypeError:
        sys.exit("Type Error")
    except KeyboardInterrupt:
        os.system("clear")
        print("Timer stopped")
        return timer

def default_timer(work_seconds, rest_seconds, pomo):
        try:
            for _ in range(int(pomo)):
                counter_down(work_seconds, "Work")
                os.system("clear")
                print("Break time!")

                counter_down(rest_seconds, "Break")
                os.system("clear")
                print("Break over")
        except ValueError:
            print("Input numbers")
        except KeyboardInterrupt:
            os.system("clear")
            print("stopped")

def continuous_timer(work_seconds, rest_seconds):
    try:
        counter_down(work_seconds, "Work")
        os.system("clear")
        print("Time is up")
        overtime_worked = counter_up()
    except TypeError:
        sys.exit("Input number")
    except KeyboardInterrupt:
        os.system("clear")
        sys.exit("Timer Stopped")
    else:
        overtime_rest = (work_seconds // rest_seconds)
        total_rest = ((overtime_worked // overtime_rest) + rest_seconds)
        counter_down(total_rest, "Break")
        os.system("clear")
        print("Break over")


if __name__ == "__main__":
    main()