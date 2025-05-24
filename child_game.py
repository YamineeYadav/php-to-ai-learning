import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Function to display text on the screen
def display_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Generate a random math problem
def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
        num1 = num1 * num2  # Ensure num1 is divisible by num2
    question = f"{num1} {operator} {num2} = ?"
    answer = eval(str(num1) + operator + str(num2))
    return question, answer

# Main game loop
running = True
question, answer = generate_problem()
user_answer = ''

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_answer == str(answer):
                    display_text('Correct!', font, black, 300, 250)
                else:
                    display_text('Wrong!', font, black, 300, 250)
                pygame.display.update()
                pygame.time.delay(2000)
                question, answer = generate_problem()
                user_answer = ''
            elif event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]
            else:
                user_answer += event.unicode

    # Display the math problem
    display_text(question, font, black, 200, 150)
    display_text(user_answer, font, black, 400, 300)

    pygame.display.update()

pygame.quit()
