#loops
#while loop
bullets=10

while bullets>0:
    bullets-=1
    print(f"shoot(),{bullets} are left")

bullets=10

while bullets>0:
    if bullets>8:
        print("user dead, game over")
        break
    bullets-=1
    print(f"shoot(),{bullets} are left")
else:
    print("Game over.  you win the game")
