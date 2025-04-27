# 🎲 Dice Simulator

A simple web-based dice roller built using Flask. This application allows users to roll a dice and view the result in real-time.

## Features
- Roll a dice with a single click.
- Displays a random number between 1 and 6.
- Simple, intuitive, and responsive UI.

---

## Project Structure
```
dice-simulator/
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies for the project
├── .env                   # Environment variables (not committed to GitHub)
├── Procfile               # For deployment on platforms like Render
└── templates/
    └── index.html         # HTML file for the Dice Simulator
```

---

## How to Run Locally

### Prerequisites
- Python 3.7 or higher installed.
- `pip` (Python package manager) installed.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Devine-swastik/dice-simulator.git
   cd dice-simulator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     FLASK_APP=app.py
     FLASK_ENV=development
     SECRET_KEY=your-secret-key
     ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## Hosting on Render

### Steps to Deploy
1. Push your code to a GitHub repository.

2. Log in to [Render](https://render.com).

3. Create a new **Web Service**:
   - Link your GitHub repository.
   - Choose the branch to deploy (e.g., `main` or `master`).

4. Set the **Start Command**:
   ```bash
   gunicorn app:app --bind 0.0.0.0:$PORT
   ```

5. Add the following **Environment Variables** in the Render Dashboard:
   - `FLASK_APP=app.py`
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key`

6. Deploy the service and wait for Render to build and start your application.

7. Once deployed, your app will be live at the URL provided by Render.

---

## Environment Variables
The following environment variables are used in this application:
- **FLASK_APP**: Entry point of the application (`app.py`).
- **FLASK_ENV**: Set to `production` for deployment and `development` for local testing.
- **SECRET_KEY**: A secure random string used by Flask for session management and security.

---

## Example
### Screenshot
![Dice Simulator Screenshot](https://via.placeholder.com/800x400.png?text=Dice+Simulator+Screenshot)

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

---

### Author
**Devine-swastik**
