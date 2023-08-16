from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_Roundoff = round(time_delay, 2)
    speed = len(userinput) / time_Roundoff
    return round(speed)

def display_leaderboard(leaderboard):
    print("\nLeaderboard:")
    for name, score in leaderboard.items():
        print(f"{name}: {score} w/sec")

if __name__ == '__main__':
    leaderboard = {}
    
    while True:
        name = input("Enter your name: ")
        play = input("Would you like to play a typing test? (yes/no): ")
        if play.lower() == 'no':
            print("Thank you for considering! Goodbye!")
            break
        elif play.lower() != 'yes':
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue


        print("        ****  Typing Test  ******")
        print("Difficulty Levels:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Quit")

        choice = input("Select a difficulty level (1/2/3/4): ")
        
        if choice == '1':
            test = [
                "The sun is shining.",
                "I like pizza.",
                "She runs fast.",
                "The cat is black.",
                "He reads a book.",
                "Water is essential.",
                "The sky is blue.",
                "The dog barks loudly.",
                "She sings beautifully.",
                "My car is red."
            ]
        elif choice == '2':
            test = [
                "Effervescent water quenches your thirst much better than sugary drinks.",
                "The melodious symphony echoed throughout the grand concert hall.",
                "The enigmatic painting left observers pondering its hidden meanings.",
                "Persistent effort and focused dedication lead to remarkable achievements.",
                "The radiant sun cast a warm glow over the tranquil sea at dawn.",
                "Vivid imagination fuels creativity and drives innovation.",
                "The intricate pattern of the tapestry displayed masterful craftsmanship.",
                "Adversity builds character and resilience in individuals.",
                "The exquisite beauty of nature's landscapes captivates the soul.",
                "Eloquent speech conveys thoughts with eloquence and precision."
            ]
        elif choice == '3':
            test = [
                "Eloquence is the art of using language in a fluent and expressive way.",
                "Perseverance and determination are key traits of successful individuals.",
                "The labyrinthine maze posed a daunting challenge for the adventurous explorer.",
                "A cacophony of sounds filled the air as the bustling city came to life.",
                "The voracious reader devoured the captivating novel in a single sitting.",
                "Meticulous planning and strategic thinking are essential for complex projects.",
                "Ineffable emotions stirred within as the breathtaking sunset painted the sky.",
                "The audacious explorer ventured into the uncharted wilderness with courage.",
                "Diligent practice hones skills to perfection and fosters continuous improvement.",
                "The resplendent architecture of the ancient cathedral left visitors awestruck."
            ]
        elif choice == '4':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue
        
        test1 = r.choice(test)
        print("\nType the following sentence:")
        print(test1)
        print()

        

        time_1 = time()
        testinput = input("Type here: ")
        time_2 = time()

        print('Speed:', speed_time(time_1, time_2, testinput), "w/sec")
        print('Error:', mistake(test1, testinput))

        if name in leaderboard:
            if speed_time > leaderboard[name]:
                leaderboard[name] = speed_time
                print(f"Well done, {name}! New speed record unlocked!")
            else:
                print(f"{name}, you can do better! Keep practicing!")
        else:
            leaderboard[name] = speed_time
            print(f"Welcome, {name}! Your score has been added to the leaderboard!")

        display_leaderboard(leaderboard[name])
