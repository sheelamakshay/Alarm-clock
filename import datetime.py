import datetime
import time
import threading

class AlarmClock:
    def __init__(self):
        self.alarms = []

    def set_alarm(self, hour, minute):
        alarm_time = datetime.time(hour, minute)
        self.alarms.append(alarm_time)

    def run_alarms(self):
        while True:
            current_time = datetime.datetime.now().time()

            for alarm in self.alarms:
                if current_time.hour == alarm.hour and current_time.minute == alarm.minute and current_time.second == 0:
                    print(f"Alarm at {alarm.hour:02d}:{alarm.minute:02d} - Wake up!")
                    self.alarms.remove(alarm)  # Remove the alarm after it has been triggered

            time.sleep(1)  # Check every second

if __name__ == "__main__":
    alarm_clock = AlarmClock()

    # Example: Set alarms
    alarm_clock.set_alarm(7, 0)
    alarm_clock.set_alarm(8, 30)

    # Start a thread to run the alarms in the background
    alarm_thread = threading.Thread(target=alarm_clock.run_alarms)
    alarm_thread.start()

    # Keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting the alarm clock application.")
