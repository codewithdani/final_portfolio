# Chuck Norris Jokes Web Application

This web application allows users to generate and view Chuck Norris jokes. Users can generate random Chuck Norris jokes and view their own list of jokes.

## Features

- **Generate Joke**: Click the "Generate Joke" button to generate a random Chuck Norris joke.
- **View Your List of Jokes**: Click the "Show Your List of Jokes" button to view your list of generated jokes.
- **Last Generated Joke**: The last generated joke is displayed at the top of the page.
- **User Authentication**: Users can sign up, sign in, and log out. Each user has their own list of jokes.
- **Database Storage**: Jokes are stored in a SQLite database.
- **Responsive Design**: The web application is responsive and works well on different devices.

## Installation

1. Clone the repository:
git clone https://github.com/codewithdani/chuck-norris-jokes.git

2. Install dependencies:
pip install -r requirements.txt

3. Set up the database:
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)

4. Run the application:
python app.py

5. Open your web browser and navigate to `http://localhost:8000`.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- sqlite3
- HTML/CSS
- JavaScript
- Jinja2 templating engine

## Third-Party Services Used

- Chuck Norris API (https://api.chucknorris.io) for generating jokes.

## Project Structure

- `app.py`: Main Flask application file.
- `templates/`: HTML templates for rendering pages.
- `static/`: Contains static files (e.g., CSS, JavaScript).

## Contributors

- Daniel Giday (daneximpex@gmail.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
This README.md file provides information about the Chuck Norris Jokes web application, including features, installation instructions, technologies used, project structure, contributors, and license details. Adjust the content as needed for your specific project.