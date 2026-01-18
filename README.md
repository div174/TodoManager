# 📝 TodoManager – Django Todo Application

**TodoManager** is a Django-based Todo List web application that allows users to manage daily tasks efficiently with authentication, task ownership, and a clean Bootstrap-powered UI.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/div174/TodoManager.git
cd TodoManager
```

2️⃣ Create & activate virtual environment
```Bash
# Create
python -m venv myenv
# Windows
myenv\Scripts\activate
# Linux / macOS
source myenv/bin/activate
```

3️⃣ Install dependencies
```Bash
pip install -r requirements.txt
```

4️⃣ Configure Environment Variables (Crucial!)
Create a file named .env in the root directory (the same folder as manage.py). Add the following content:

```Plaintext
SECRET_KEY=your-random-secret-key-here
DEBUG=True
```
(Note: Replace your-random-secret-key-here with a secure key.)

5️⃣ Apply migrations
```Bash
python manage.py makemigrations
python manage.py migrate
```

6️⃣ Run the development server
```Bash
python manage.py runserver
Visit your app at: http://127.0.0.1:8000/
```

🔐 Environment Variables
This project uses python-dotenv to keep sensitive information safe.

SECRET_KEY: Never share this or upload it to GitHub.

DEBUG: Set to True for development and False for production.

📁 Project Structure
```Plaintext
TodoManager/
│
├── TodoManager/          # Project settings & configuration
│   ├── settings.py       # Updated to use os.getenv()
│   └── ...
├── todolistapp/          # Core Todo logic
├── users/                # User authentication & profiles
├── templates/            # Global HTML templates
├── static/               # CSS, JS, and Images
├── .env                  # Environment secrets (Local only)
├── .gitignore            # Tells Git what to ignore
├── requirements.txt      # List of dependencies
└── manage.py
```
❗ Common Issues & Fixes
🔴 "ModuleNotFoundError: No module named 'dotenv'": Ensure your virtual environment is active and run pip install python-dotenv.

🔴 "The SECRET_KEY setting must not be empty": Your .env file is missing or the SECRET_KEY variable is not defined correctly.

🔴 Logout not working: Django 5.0+ requires Logout to be a POST request. Ensure your logout button is inside a form with a {% csrf_token %}.

👤 Author
Divyansh Python & Django Developer Learning full-stack web development 🚀
