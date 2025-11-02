import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Window")
background_img = pygame.transform.scale(pygame.image.load('bg.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
donut = pygame.transform.scale(pygame.image.load('donut.png').convert_alpha(), (200, 200))
Candy = pygame.transform.scale(pygame.image.load('candy.png').convert_alpha(), (200, 200))


Candy_rect = Candy.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
donut_rect = donut.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

text_font = pygame.font.Font(None, 36).render("Sweet!", True, pygame.Color('pink'))
text_rect = text_font.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    display_surface.blit(background_img, (0, 0))
    display_surface.blit(donut, donut_rect)  
    display_surface.blit(Candy, Candy_rect)
    display_surface.blit(text_font, text_rect)

    pygame.display.flip()
    clock.tick(30)