DIFFICULTY = 2
TWITTER_ACC = 'XXXX'

import random
import arcade
import math
import time
import tweepy

consumer_key = "XXXX"
consumer_secret = "XXXX"

access_token = "XXXX" 
access_token_secret = "XXXX" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

BACKGROUND0 = "map/start.png"
BACKGROUND1 = "map/floor.png"
BACKGROUND2 = "map/dirt.png"
BACKGROUND3 = "map/snow.png"
BACKGROUND_CHOICE = ""

PLAYER_SKIN = "sprites/player.png"
ENNEMY0_SKIN = "sprites/eyeball.png"
ENNEMY1_SKIN = "sprites/turtle.png"
ENNEMY2_SKIN = "sprites/slime.png"
ENNEMY0_SKIN_CHOICE = ""

EYEBALL = "Vol'Oeil"
TURTLE = "Tortépée"
SLIME = "Slime"
ENNEMY_NAME =""

nbtweets = api.get_user(TWITTER_ACC).statuses_count

tweet = int(str(nbtweets)[:DIFFICULTY])

ENNEMY0_COUNT = 1 + tweet

SCREEN_HEIGHT = 745
SCREEN_WIDTH = 900
SCREEN_TITLE = "Cereal Carnage"

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3
WIN = 4

FIRE_RATE = 90
MOVEMENT_SPEED = 6
BULLET_SPEED = 6
BULLET1_SPEED = 5.5

SPRITE_SCALING_PLAYER = 0.75
SPRITE_SCALING_ENNEMY0 = [1,0.75,0.5,0.3]
SPRITE_SCALING_LOOP = 0.3
SPRITE_SCALING_LASERRED = 0.5

LASER_SKIN_ENNEMY0 = "laser/laserred.png"
LASER_SKIN_PLAYER = "laser/loopblue.png"
LASER_SKIN_PLAYER1 = "laser/looppurple.png"
LASER_SKIN_PLAYER2 = "laser/loopyellow.png"
LASER_SKIN_PLAYER3 = "laser/loopred.png"
LASER_SKIN_PLAYER4 = "laser/loopgreen.png"

PICK = [LASER_SKIN_PLAYER,LASER_SKIN_PLAYER1,LASER_SKIN_PLAYER2,LASER_SKIN_PLAYER3,LASER_SKIN_PLAYER4]

if int(str(nbtweets)[:1]) <= 4:
    BACKGROUND_CHOICE = BACKGROUND1
    ENNEMY0_SKIN_CHOICE = ENNEMY0_SKIN
    SPRITE_SCALING_ENNEMY0 = [1,1.5,2]
    ENNEMY_NAME = EYEBALL
if int(str(nbtweets)[:1]) >= 6:
    BACKGROUND_CHOICE = BACKGROUND2
    ENNEMY0_SKIN_CHOICE = ENNEMY1_SKIN
    ENNEMY_NAME = TURTLE
if  int(str(nbtweets)[:1]) == 5:
    BACKGROUND_CHOICE = BACKGROUND3
    ENNEMY0_SKIN_CHOICE = ENNEMY2_SKIN
    ENNEMY_NAME = SLIME

print("Compte :", TWITTER_ACC)
print ("Nombre de Tweet :", nbtweets)
print ("Difficulté :", DIFFICULTY)
print("Map :", BACKGROUND_CHOICE)  
print ("Nombres d'ennemis :", ENNEMY0_COUNT, ENNEMY_NAME)    
 
for i in range(5):
    print(str(5 - i))
    time.sleep(1)    

class Player(arcade.Sprite):

    def update(self):
        """ Permet d'empêcher le joueur de sortir de la fenêtre. """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
            
class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.frame_count = 0
        
        self.current_state = INSTRUCTIONS_PAGE_0
        
        self.player_list = None
        self.ennemy_list = None
        self.bullet_list = None
        self.bullet1_list = None
        
        self.player = None
                
        self.score = 0
        self.score_text = None

        self.background = None
        self.background = arcade.load_texture(BACKGROUND_CHOICE)
        
        
        self.instructions = []
        texture = arcade.load_texture(BACKGROUND0)
        self.instructions.append(texture)
        
    def setup(self):

        """ Set up le jeu et crée les variables, crée aussi le sprite du joueur/goblins. """
       
        self.score = 0

        self.player_list = arcade.SpriteList()
        self.ennemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.bullet1_list = arcade.SpriteList()
        
        self.player_sprite = Player(PLAYER_SKIN, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 450
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)
        
        for i in range(ENNEMY0_COUNT):
            ennemy = arcade.Sprite(ENNEMY0_SKIN_CHOICE, random.choice(SPRITE_SCALING_ENNEMY0))
            ennemy.center_x = random.randrange(SCREEN_WIDTH)
            ennemy.center_y = random.randrange(120, SCREEN_HEIGHT)
            ennemy.angle = 180
            self.ennemy_list.append(ennemy)
       
        for ennemy in self.ennemy_list:
            hit_list = arcade.check_for_collision_with_list(ennemy, self.ennemy_list)
            
            if len(hit_list) > 0:
                ennemy.kill()
                
        
    def draw_instructions_page(self, page_number):
        
        """ Affiche une page de démarrage (image). """
        
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.66,
                                      page_texture.width * 1.025,
                                      page_texture.height *1.1, page_texture, 0)
    
               
    def draw_game_over(self):
        """
        Ecris "Game over" sur l'écran.
        """
        output = "Game Over"
        arcade.draw_text(output, 290, 550, arcade.color.WHITE, 54)

        output = "Cliquer n'importe ou pour recommencer. "
        arcade.draw_text(output, 190, 450, arcade.color.WHITE, 25)
         
        output = f"Votre score : {self.score}"
        arcade.draw_text(output, 280, 350, arcade.color.WHITE, 40)
        
    def draw_game(self):
        """ Dessine tous les sprites et le score. """
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
       
        self.player_list.draw()
        self.ennemy_list.draw()
        self.bullet_list.draw()
        self.bullet1_list.draw()
        
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 20)
        
    def draw_win(self):
        """ Ecris "You Win !" sur l'écran. """
        
        output = "You Win !"
        arcade.draw_text(output, 290, 450, arcade.color.WHITE, 54)
        
        output = f"Votre score: {self.score}"
        arcade.draw_text(output, 280, 350, arcade.color.WHITE, 40)       
            
    def on_draw(self):
        """ Affiche le jeu ou les instructions sur l'écran. """
        
        arcade.start_render()
       
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)


        elif self.current_state == GAME_RUNNING:
            self.draw_game()
            
        
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

            self.draw_game_over()
        
        if len(self.ennemy_list) == 0:
            self.draw_win()
            
        self.background = arcade.load_texture(BACKGROUND_CHOICE)
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ Utilisé quand la souris bouge ou est cliqué. """
        
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.setup()
            self.current_state = GAME_RUNNING
        
        if self.current_state == WIN:
            self.setup()
            self.current_state = GAME_RUNNING
        
        elif self.current_state == GAME_OVER:
            self.setup()
            self.current_state = GAME_RUNNING
       
        bullet = arcade.Sprite(random.choice(PICK), SPRITE_SCALING_LOOP)
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        dest_x = x
        dest_y = y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        bullet.angle = math.degrees(angle)
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED
        self.bullet_list.append(bullet)
    
    def update(self, delta_time):
        """ Mouvements et logique du jeu. """
        
        arcade.start_render()
        
        self.frame_count += 1
        
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)
                    
        else:
            self.draw_win()
            self.draw_game_over()
                        
        if self.current_state == GAME_RUNNING:
            
            self.player_list.update()
            self.ennemy_list.update()
            self.bullet_list.update()
            self.bullet1_list.update()
               
        for ennemy in self.ennemy_list:
                
            start_x = ennemy.center_x
            start_y = ennemy.center_y
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            ennemy.angle = math.degrees(125.71)
            
            if self.frame_count % FIRE_RATE == 0:
                bullet1 = arcade.Sprite(LASER_SKIN_ENNEMY0, SPRITE_SCALING_LASERRED)
                bullet1.center_x = start_x
                bullet1.center_y = start_y
                bullet1.angle = math.degrees(angle)
                bullet1.change_x = math.cos(angle) * BULLET1_SPEED
                bullet1.change_y = math.sin(angle) * BULLET1_SPEED
                self.bullet1_list.append(bullet1)        
        
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.ennemy_list)
            
            if len(hit_list) > 0:
                bullet.kill()
                
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.kill()
        
            for ennemy in hit_list:
               ennemy.kill()
               self.score += 1
               
        for bullet1 in self.bullet1_list:
            hit_list = arcade.check_for_collision_with_list(bullet1, self.player_list)

            if len(hit_list) > 0:
                bullet1.kill()
                self.current_state = GAME_OVER
                
            if bullet1.bottom > self.width or bullet1.top < 0 or bullet1.right < 0 or bullet1.left > self.width:
                bullet1.kill()
            
        self.bullet_list.update() 
        self.bullet1_list.update() 
   
    def on_key_press(self, key, modifiers):
        """Appelé quand une touche du clavier est pressé. """

        if key == arcade.key.Z:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.Q:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Appelé quand une touche du clavier est relaché. """

        if key == arcade.key.Z or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.Q or key == arcade.key.D:
            self.player_sprite.change_x = 0
            

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
