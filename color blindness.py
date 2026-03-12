import cv2
import os
import numpy as np

# Function to load all images from a given directory
def load_images(directory):
    """Load all images from the specified directory and return a list of images."""
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(directory, filename))
            if img is not None:
                images.append((img, filename))
    return images


# Function to display an image
def display_image(image):
    """Display the given image in a window for the user to see."""
    cv2.imshow('Color Blindness Test', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Function to get user input
def get_user_input():
    """Prompt the user to input the number they perceive in the displayed image."""
    return input("What number do you see? ")


# Function to check user's answer
def check_answer(user_input, correct_answer):
    """Compare the user's input with the correct answer and return whether it is correct."""
    return user_input.strip() == correct_answer


# Function to calculate score
def calculate_score(correct_answers, total_images):
    """Calculate the user's score as a percentage based on correct answers and total images."""
    return (correct_answers / total_images) * 100


# Function to display final results
def display_results(correct_answers, total_images):
    """Display the total correct answers and accuracy percentage to the user."""
    score = calculate_score(correct_answers, total_images)
    print(f"\nYou got {correct_answers} out of {total_images} correct.")
    print(f"Your accuracy is {score:.2f}%.")


# Main function
def main():
    """The main function that orchestrates the flow of the program."""
    image_directory = 'path_to_your_images'  # <-- change this to your image folder path

    images = load_images(image_directory)

    correct_answers = {
        'image1.jpg': '3',
        'image2.jpg': '5',
        'image3.jpg': '2'
    }

    total_images = len(images)
    user_correct_count = 0

    if total_images == 0:
        print("No images found in the directory. Please check the path.")
        return

    for image, filename in images:
        display_image(image)
        user_input = get_user_input()

        if filename in correct_answers and check_answer(user_input, correct_answers[filename]):
            print("✅ Correct!\n")
            user_correct_count += 1
        else:
            print("❌ Incorrect!\n")

    display_results(user_correct_count, total_images)


# Entry point of the program
if __name__ == "__main__":
    main()
