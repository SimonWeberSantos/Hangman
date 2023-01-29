import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the window
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Hangman")

# Load the images for the hangman
def draw_hangman(screen, incorrect_guesses):
    # Draw the scaffold
    pygame.draw.line(screen, (0, 0, 0), (100, 480), (100, 50), 5)
    pygame.draw.line(screen, (0, 0, 0), (100, 50), (300, 50), 5)
    pygame.draw.line(screen, (0, 0, 0), (300, 50), (300, 100), 5)

    # Draw the parts of the hangman
    if incorrect_guesses > 0:
        pygame.draw.circle(screen, (0, 0, 0), (300, 130), 30, 5)
    if incorrect_guesses > 1:
        pygame.draw.line(screen, (0, 0, 0), (300, 160), (300, 280), 5)
    if incorrect_guesses > 2:
        pygame.draw.line(screen, (0, 0, 0), (300, 190), (270, 230), 5)
    if incorrect_guesses > 3:
        pygame.draw.line(screen, (0, 0, 0), (300, 190), (330, 230), 5)
    if incorrect_guesses > 4:
        pygame.draw.line(screen, (0, 0, 0), (300, 280), (270, 350), 5)
    if incorrect_guesses > 5:
        pygame.draw.line(screen, (0, 0, 0), (300, 280), (330, 350), 5)

def draw_word(surface, word, correct_letters):
    # Create a string to store the visible word
    visible_word = ""

    # Add a space between each letter
    for letter in word:
        if letter in correct_letters:
            visible_word += letter + " "
        else:
            visible_word += "_ "

    # Render the text
    text = font.render(visible_word, True, (0, 0, 0))

    # Get the size of the text
    text_rect = text.get_rect()

    # Position the text in the center of the screen
    text_rect.center = (350, 250)

    # Draw the text on the surface
    surface.blit(text, text_rect)

def draw_incorrect_letters(surface, incorrect_letters):
    # Create a string to store the incorrect letters
    incorrect_letters_string = " ".join(incorrect_letters)

    # Render the text
    text = font.render(incorrect_letters_string, True, (0, 0, 0))

    # Get the size of the text
    text_rect = text.get_rect()

    # Position the text at the top of the screen
    text_rect.center = (350, 50)

    # Draw the text on the surface
    surface.blit(text, text_rect)

def draw_message(surface, message):
    # Render the text
    text = font.render(message, True, (0, 0, 0))

    # Get the size of the text
    text_rect = text.get_rect()

    # Position the text in the center of the screen
    text_rect.center = (350, 400)

    # Draw the text on the surface
    surface.blit(text, text_rect)


# Set the font and size for the text
font = pygame.font.SysFont("arial", 30)

# Set the list of words for the game
words = ["python", "javascript", "programming", "computer", "science"]

# Choose a random word for the game
word = random.choice(words)

# Create a list to store the correctly guessed letters
correct_letters = []

# Create a list to store the incorrectly guessed letters
incorrect_letters = []

# Set the number of lives
lives = 5

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            # Get the letter that was pressed
            letter = event.unicode

            # Check if the letter is in the word
            if letter in word:
                # Add the letter to the correct_letters list
                correct_letters.append(letter)
            else:
                # Add the letter to the incorrect_letters list
                incorrect_letters.append(letter)
                # Remove a life
                lives -= 1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the word on the screen
    draw_word(screen, word, correct_letters)

    # Draw the incorrectly guessed letters on the screen
    draw_incorrect_letters(screen, incorrect_letters)

    # Draw the hangman on the screen
    draw_hangman(screen, lives)

    # Check if the player has won or lost
    if set(correct_letters) == set(word):
        draw_message(screen, "You won!", (350, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False
    elif lives == 0:
        draw_message(screen, "You lost!", (350, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
