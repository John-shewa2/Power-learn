while True:
    score = 0
    question1 = print(
        "what is the output of the following code: \nx = 5, print(type(x)) \nA. <class 'float'>  \nB. <class 'str'>  \nC. <class 'int'>  \nD.<class 'bool'>")
    your_answer1 = input(" Answer: ").lower()
    if your_answer1 == "c":
        score = 10
    question2 = print(
        "Which of the following is a valid way to create a list in Python? \nA. list = 1, 2, 3, 4 \nB. list = {1, 2, 3, 4} \nC. list = [1, 2, 3, 4] \nD. list = (1, 2, 3, 4)")
    your_answer2 = input(" Answer: ").lower()

    if your_answer2 == "c":
        score += 10

    print(f"You scored {score} / 20")

    play_again = input("\nDo you want to try again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
