import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

start_os = 0
print("Loading ...")
for start_os in range(101):
  print("Loading...",start_os,"%")  
if start_os == 100:
 time.sleep(4)
 clear_screen()
 print("\033[32mcomplete!\033[0m")
 del start_os
 
 
def animation_1():
    print("\n #\n")
    time.sleep(0.3)
    print(" #\n# #\n #\n")
    time.sleep(1)
    print(" #\n###\n #\n")
    time.sleep(1)
    print(" #\n# #\n #\n")
    time.sleep(0.3)
    print("\n #\n")
    time.sleep(0.7)
    clear_screen()
    
def comm_1():
    try:
        num_1 = int(input("Enter 1 value: "))
        num_2 = int(input("Enter 2 value: "))
        print("Addition:", num_1 + num_2)
        print("Subtraction:", num_1 - num_2)
        print("Multiplication:", num_1 * num_2)
        if num_2 != 0:
            print("Division:", num_1 / num_2)
        else:
            print("\033[31mError: \033[0mделение на 0")
    except ValueError:
        print("\033[31mError: \033[0m You must enter integers!")


def comm_2():
    print('\033[32mtest: Displays the text "Test"\nhelp: Displays a list of commands\ncalculator: Opens the calculator\033[0m')
    print("\033[32mclear: Clears the screen\nanimation_1: Starts animation #1\033[0m")
    

def main():
    while True:
        comm_in = input(">>> ").strip()
        
        if comm_in == "test":
            print("test")
        elif comm_in == "calculator":
            comm_1()
        elif comm_in == "help":
            comm_2()
        elif comm_in == "clear":
            clear_screen()
        elif comm_in == "animation_1":
            animation_1()
        elif comm_in == "exit":
            print("Exiting the program...")
        elif comm_in == "text":
            comm_3()
            break
        else:
            print(f"{comm_in}",":""\033[31m Not command\033[0m")


if __name__ == "__main__":
    main()