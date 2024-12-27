import pygame
import pyttsx3
import re
import sys

# Initialize Pygame and pyttsx3
pygame.init()
engine = pyttsx3.init()

# Set up screen parameters
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Talking Robot")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# # Load or draw a simple robot face
robot_face = pygame.Surface((200, 200))
robot_face.fill(GRAY)

# # Robot head
pygame.draw.rect(robot_face, GRAY, (0, 0, 200, 200))  # Head
pygame.draw.rect(robot_face, BLACK, (20, 30, 30, 30))  # Left Eye
pygame.draw.rect(robot_face, BLACK, (150, 30, 30, 30))  # Right Eye
pygame.draw.rect(robot_face, BLACK, (70, 100, 60, 20))  # Mouth

# # Antennas
pygame.draw.line(robot_face, BLACK, (100, 0), (100, 20), 5)  # Antenna
pygame.draw.circle(robot_face, BLACK, (100, 20), 5)  # Antenna bulb

# # Load the robot icon image
# robot_icon = pygame.image.load("path_to_your_robot_icon.png")  # Replace with your image file path
# robot_icon = pygame.transform.scale(robot_icon, (200, 200))  # Scale the image to fit

# Text font
font = pygame.font.Font(None, 36)

# Initial questions for the robot to ask
questions = [
    "What's your name?",
    "How are you feeling today?",
    "What's your favorite color?",
    "Do you like robots?"
]
current_question = 0
question_spoken = False  # Track if the question has been spoken

# Function for the robot to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Generate response based on question and user input
def generate_response(question, user_input):
    if "name" in question.lower():
        match = re.search(r"my name (\w+)", user_input, re.IGNORECASE)
        return f"Nice to meet you, {user_input}!"

    elif "how are you" in question.lower():
        if "good" in user_input.lower() or "fine" in user_input.lower():
            return "I'm glad to hear you're doing well!"
        elif "not" in user_input.lower() or "bad" in user_input.lower():
            return "I'm sorry to hear that. I hope things get better!"
        else:
            return "Thanks for sharing!"

    elif "favorite color" in question.lower():
        colors = ["red", "blue", "green", "yellow", "purple", "pink", "orange"]
        for color in colors:
            if color in user_input.lower():
                return f"{color.capitalize()} is a beautiful color!"
        return "That's a nice choice!"

    elif "like robots" in question.lower():
        if "yes" in user_input.lower() or "sure" in user_input.lower():
            return "I'm glad you like robots!"
        elif "no" in user_input.lower():
            return "That's okay. Not everyone has to like robots!"
        else:
            return "I appreciate your honesty!"

    return "Interesting!"

# Start by greeting the user
speak("Hello! I am your friendly robot.")
print("Robot: Hello! I am your friendly robot.")

# Main program loop
running = True
user_text = ""

while running:
    screen.fill(WHITE)
    screen.blit(robot_face, (screen_width // 2 - 100, screen_height // 2 - 100))

    # Check if there are more questions
    if current_question < len(questions):
        # Speak the current question only once
        if not question_spoken:
            speak(questions[current_question])
            question_spoken = True  # Mark the question as spoken
        
        # Display the question text
        question_text = font.render(questions[current_question], True, BLACK)
        screen.blit(question_text, (20, 20))
    else:
        speak("No more questions. You can type 'quit' to exit.")
        break

    # Display user's answer
    answer_text = font.render(user_text, True, BLACK)
    screen.blit(answer_text, (20, 60))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            speak("Goodbye!")
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_text.lower() == 'quit':
                    speak("Goodbye!")
                    running = False
                else:
                    # Generate a response based on user input
                    response = generate_response(questions[current_question], user_text)
                    speak(response)
                    print(f"Robot: {response}")
                    
                    # Move to the next question
                    current_question += 1
                    question_spoken = False  # Reset the flag for the next question
                user_text = ""
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

# Exit message
speak("Thank you for chatting with me. Goodbye!")
print("Robot: Thank you for chatting with me. Goodbye!")

# Cleanup
pygame.quit()
sys.exit()
