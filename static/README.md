#Guess the Number Game

##Overview
Guess the Number is a simple web-based game where the user has to guess a randomly generated number between 1 and 100. The game provides feedback to the user in the form of color changes, indicating how close their guess is to the actual number.

##Directory Arrangement
The game is organized into the following directories and files:

app.py: The main application file that contains the Flask app and routes.
templates/: A directory containing the HTML templates for the game.
	index.html: The main game page.
	result.html: The page that displays the result of the user's guess.
	win.html: The page that displays the winning message.
static/: A directory containing any static assets, such as CSS files.
	README.md: This file, which contains information about the game and how to set it up.
 
##Setup and Installation
To set up and run the game, follow these steps:

Install Flask: If you haven't already, install Flask using pip: pip install flask.
Clone the repository: Clone this repository to your local machine using Git: git clone https://github.com/your-username/guess-the-number.git.
Navigate to the directory: Navigate to the directory where you cloned the repository: cd guess-the-number.
Run the app: Run the app using Flask: python app.py.
Open the game: Open a web browser and navigate to http://localhost:5000 to play the game.

##Gameplay
Here's how to play the game:

Guess a number: Enter a number between 1 and 100 in the input field.
Submit your guess: Click the "Guess" button to submit your guess.
Get feedback: The game will provide feedback in the form of a color change, indicating how close your guess is to the actual number.
Red: Your guess is too high or too low (difference > 25).
Orange: Your guess is high or low (difference between 10 and 25).
Yellow: Your guess is slightly high or low (difference between 5 and 10).
Green: Congratulations! You guessed the correct number!
Keep guessing: Keep guessing until you get the correct number.
Play again: Click the "Play Again" button to start a new game.

##Technical Details
The game uses the following technologies:

Flask: A micro web framework for Python.
HTML: HyperText Markup Language for structuring and presenting content.
CSS: Cascading Style Sheets for styling and layout.
JavaScript: Not used in this game, but could be used for additional features.
The game uses a simple random number generator to generate the number to be guessed. The game also uses session variables to store the number to be guessed and the number of tries.

##License
This game is licensed under the MIT License. See the LICENSE file for details.

##Contributing
Contributions are welcome! If you'd like to contribute to the game, please fork the repository and submit a pull request.
