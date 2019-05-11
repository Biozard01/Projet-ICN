import arcade
import time
import gamefile
import tweet
import var
  
for i in range(5):
    print(str(5 - i))
    time.sleep(1)    

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()