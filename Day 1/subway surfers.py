import pygame
import random
import sys

# Initialize Pygame
pygame.init()
# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.is_jumping = False
        self.jump_power = 20
        self.gravity = 0.6
        self.lane = 1  # 0 = left, 1 = middle, 2 = right
        
    def handle_input(self, keys):
        if keys[pygame.K_LEFT] and self.lane > 0:
            self.lane -= 1
        if keys[pygame.K_RIGHT] and self.lane < 2:
            self.lane += 1
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.vel_y = -self.jump_power
    
    def update(self):
        # Update x position based on lane
        target_x = 60 + self.lane * 140
        self.rect.x = target_x
        
        # Jump physics
        if self.is_jumping:
            self.vel_y += self.gravity
            self.rect.y += self.vel_y
            
            if self.rect.y >= SCREEN_HEIGHT - 100:
                self.rect.y = SCREEN_HEIGHT - 100
                self.is_jumping = False
                self.vel_y = 0
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, lane):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lane = lane
        self.speed = 7
    
    def update(self):
        self.rect.y += self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, lane):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y
        self.lane = lane
        self.speed = 7
    
    def update(self):
        self.rect.y += self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Subway Surfers Ripoff")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        
        self.player = Player(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 100)
        self.obstacles = []
        self.coins = []
        
        self.score = 0
        self.coins_collected = 0
        self.spawn_timer = 0
        self.spawn_rate = 40
        self.difficulty = 1
        
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)
    
    def spawn_obstacles(self):
        self.spawn_timer += 1
        
        # Increase difficulty over time
        if self.score > 500:
            self.spawn_rate = 35
            self.difficulty = 1.2
        if self.score > 1000:
            self.spawn_rate = 30
            self.difficulty = 1.4
        if self.score > 1500:
            self.spawn_rate = 25
            self.difficulty = 1.6
        
        if self.spawn_timer > self.spawn_rate:
            self.spawn_timer = 0
            
            # Spawn obstacles
            if random.random() < 0.7:
                lane = random.randint(0, 2)
                x = 60 + lane * 140
                obstacle = Obstacle(x, -40, lane)
                self.obstacles.append(obstacle)
            
            # Spawn coins occasionally
            if random.random() < 0.3:
                lane = random.randint(0, 2)
                x = 60 + lane * 140
                coin = Coin(x, -20, lane)
                self.coins.append(coin)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if self.game_over and event.key == pygame.K_SPACE:
                    self.__init__()  # Restart game
    
    def check_collisions(self):
        # Check collision with obstacles
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.game_over = True
        
        # Check collision with coins
        for coin in self.coins[:]:
            if self.player.rect.colliderect(coin.rect):
                self.coins_collected += 1
                self.score += 10
                self.coins.remove(coin)
    
    def update(self):
        if not self.game_over:
            keys = pygame.key.get_pressed()
            self.player.handle_input(keys)
            self.player.update()
            
            self.spawn_obstacles()
            
            # Update obstacles
            for obstacle in self.obstacles[:]:
                obstacle.update()
                if obstacle.rect.y > SCREEN_HEIGHT:
                    self.obstacles.remove(obstacle)
                    self.score += 5
            
            # Update coins
            for coin in self.coins[:]:
                coin.update()
                if coin.rect.y > SCREEN_HEIGHT:
                    self.coins.remove(coin)
            
            self.check_collisions()
    
    def draw(self):
        self.screen.fill(GRAY)
        
        # Draw game background with lanes
        pygame.draw.line(self.screen, WHITE, (90, 0), (90, SCREEN_HEIGHT), 2)
        pygame.draw.line(self.screen, WHITE, (230, 0), (230, SCREEN_HEIGHT), 2)
        
        # Draw ground
        pygame.draw.line(self.screen, BLACK, (0, SCREEN_HEIGHT - 100), 
                        (SCREEN_WIDTH, SCREEN_HEIGHT - 100), 3)
        pygame.draw.rect(self.screen, (100, 100, 100), 
                        (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
        
        # Draw game objects
        self.player.draw(self.screen)
        
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        
        for coin in self.coins:
            coin.draw(self.screen)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        coins_text = self.font.render(f"Coins: {self.coins_collected}", True, YELLOW)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(coins_text, (10, 50))
        
        # Draw game over screen
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            game_over_text = self.large_font.render("GAME OVER", True, RED)
            final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            final_coins_text = self.font.render(f"Coins Collected: {self.coins_collected}", True, YELLOW)
            restart_text = self.font.render("Press SPACE to Restart", True, WHITE)
            
            self.screen.blit(game_over_text, 
                           (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 100))
            self.screen.blit(final_score_text, 
                           (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, 200))
            self.screen.blit(final_coins_text, 
                           (SCREEN_WIDTH // 2 - final_coins_text.get_width() // 2, 250))
            self.screen.blit(restart_text, 
                           (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 400))
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
