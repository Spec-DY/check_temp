import os
import time

HIGH_TEMP = 80
WAIT_SECONDS = 1
DEFAULT_CHECK = 3
WARNING_COLOR = "\033[38;2;255;165;0m"
RESET = "\033[0m"


def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))


def print_temp():

    temp = get_cpu_temperature()
    print("CPU Temperature:", temp, "C")
    if (temp >= HIGH_TEMP):
        print(f"{WARNING_COLOR}HIGH WARNING TEMP!{RESET}")


def get_int(user_input = DEFAULT_CHECK):
    print("=======================================\n")
    while True:
        try:
            user_input = input("How many times do you want to measure?\n")
            if (user_input == ""):
                print(f"Nothing entered\nDefault checking {DEFAULT_CHECK} times\n")
                return user_input
            else:
                user_input = int(user_input)
                return user_input
        except ValueError:
            print("Please enter an integer.\n")


def main():
    print("-----------------------")
    print("|WELCOME TO TEMP CHECK|")
    print("-----------------------\n")
    user_input = get_int()
    for i in range(0,user_input):
        print_temp()
        time.sleep(WAIT_SECONDS)


if __name__ == "__main__":
    main()
