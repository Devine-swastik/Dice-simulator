from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')  # Load SECRET_KEY from environment variables

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
