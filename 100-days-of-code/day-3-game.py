# 📜 Treasure Island 📜
# Bruin Games UK
# ASCII Art https://ascii.co.uk/art/treasure
# print(r"""  is 'print raw' and it allows you to print a multi-line string without using \n.
print(r"""                             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")

print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure....")

direction = input("\nYou're at a junction. Where do you want to go? Type 'left' or 'right': ").lower()

if direction == "left":
    action = input("\nYou've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()

    if action == "wait":
        door = input("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue.\nWhich colour door do you choose? ").lower()

        if door == "red":
            print("You were burned alive by fire.\nGame Over....")
        elif door == "blue":
            print("You've been eaten by a hungry troll.\nGame Over....")
        elif door == "yellow":
            print("You found the treasure!\nYou win! 🎉")
        else:
            print("You chose a door that doesn't exist.\nGame Over....")

    else:
        print("You were attacked by an alligator.\nGame Over....")

else:
  print("You fell into a very deep hole.\nGame Over....")
