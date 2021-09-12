def play_quit():
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit...!")
    if play_game.capitalize() == "Q":
        print("Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
        exit()
    else:
        print("Enjoy the programme...!\n")
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    data.pop(i)
    data.insert(i,n)
if __name__ == '__main__':
    while True:
        try:
            chance = int(input("Enter the length of list:\n"))
            data = []
            for i in range(chance):
                list_item = int(input("Enter the items of list:"))
                data.append(list_item)
        except Exception as e:
            print("Invalid input/...! Please try again...!")
            continue
        for i in range(chance):
            if data[i] > 10:
                next_palindrome(data[i])
        print(data)
        play_quit()
