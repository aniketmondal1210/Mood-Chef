import json
import random

# Step 1: Load the recipes from a JSON file
def load_recipes():
    try:
        with open('recipes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Recipes file not found!")
        return {}

# Step 2: Function to get a recipe based on mood
def get_recipe_by_mood(mood, recipes):
    mood_recipes = recipes.get(mood.lower())
    if mood_recipes:
        return random.choice(mood_recipes)  # Randomly pick a recipe for the mood
    else:
        return None

# Step 3: Main function to interact with the user
def main():
    print("Welcome to the Mood-Based Recipe Generator!")
    print("How are you feeling today? (Happy, Sad, Stressed, Excited)")
    
    # Load recipes from JSON file
    recipes = load_recipes()
    
    # Get user input for mood
    mood = input("Enter your mood: ").strip().lower()
    
    # Get recipe based on mood
    recipe = get_recipe_by_mood(mood, recipes)
    
    if recipe:
        print(f"\nBased on your mood, we recommend you try: {recipe['name']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Steps: {recipe['steps']}")
    else:
        print("\nSorry, we don't have recipes for that mood yet!")

# Run the main function
if __name__ == "__main__":
    main()
