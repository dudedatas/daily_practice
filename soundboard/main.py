
import pygame

# initialize
pygame.init()
pygame.mixer.init()

# window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Soundboard")

# load sound
sound_a = pygame.mixer.Sound("stay_fly.wav")
sound_b = pygame.mixer.Sound("tell_me_why.wav")
sound_y = pygame.mixer.Sound("lil_jon_yeah.wav")
sound_d = pygame.mixer.Sound("lil_jon_what.wav")
sound_z = pygame.mixer.Sound("lil_jon_ok1.wav")
sound_x = pygame.mixer.Sound("lil_jon_ok2.wav")
sound_c = pygame.mixer.Sound("lil_jon_ok3.wav")

# loop
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                sound_a.play()

            elif event.key == pygame.K_b:
                sound_b.play()

            elif event.key == pygame.K_y:
                sound_y.play()

            elif event.key == pygame.K_w:
                sound_d.play()

            elif event.key == pygame.K_z:
                sound_z.play()

            elif event.key == pygame.K_x:
                sound_x.play()

            elif event.key == pygame.K_c:
                sound_c.play()

            elif event.key == pygame.K_q:
                pygame.mixer.stop()
                
        

pygame.quit() 