# 📝 TodoManager – Django Todo Application

**TodoManager** is a professional Django-based Todo List web application. It allows users to manage daily tasks efficiently with built-in authentication, task ownership, and a modern UI powered by Bootstrap 5.

This project is now configured with **industry-standard security practices**, including environment variable management to protect sensitive data.

---

## 📌 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [Common Issues & Fixes](#-common-issues--fixes)
- [Author](#-author)

---

## 🚀 Features
- 👤 **User Authentication**: Secure Registration, Login, and Logout.
- 🗂️ **Task Management**: Full CRUD (Create, Read, Update, Delete) functionality.
- 🔐 **Task Ownership**: Users can only see and manage their own tasks.
- 🎨 **Modern UI**: Styled with **Bootstrap 5** and **Django Crispy Forms**.
- 🛡️ **Security**: Protected against common vulnerabilities using Django's middleware and environment variables.

---

## 🛠️ Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Backend** | Django 6.0 |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Database** | SQLite3 (Development) |
| **Forms** | django-crispy-forms & crispy-bootstrap5 |
| **Environment** | python-dotenv |

---

## ⚙️ Installation & Setup

Because this project uses environment variables for security, it will not run "out of the box" without a `.env` file. Follow these steps carefully:

### 1️⃣ Clone the repository
```bash
git clone [https://github.com/div174/TodoManager.git](https://github.com/div174/TodoManager.git)
cd TodoManager
### 2️⃣ Create & activate virtual environment
```Bash
# Create
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Linux / macOS)
source myenv/bin/activate
### 3️⃣ Install dependencies
```Bash
pip install -r requirements.txt
### 4️⃣ Configure Environment Variables (Crucial!)
Create a file named .env in the root directory (the same folder as manage.py). Add the following content:

```Plaintext
SECRET_KEY=your-random-secret-key-here
DEBUG=True
(Note: Replace your-random-secret-key-here with a secure key.)

### 5️⃣ Apply migrations
```Bash
python manage.py makemigrations
python manage.py migrate
### 6️⃣ Run the development server
```Bash
python manage.py runserver
Visit your app at: http://127.0.0.1:8000/

🔐 Environment Variables
This project uses python-dotenv to keep sensitive information safe.

SECRET_KEY: Never share this or upload it to GitHub.

DEBUG: Set to True for development and False for production.

Note: The .env file is included in .gitignore to prevent it from being pushed to the public repository.

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
❗ Common Issues & Fixes
🔴 "ModuleNotFoundError: No module named 'dotenv'"
Fix: Ensure your virtual environment is active and run pip install python-dotenv.

🔴 "The SECRET_KEY setting must not be empty"
Fix: This means your .env file is missing or the SECRET_KEY variable inside it is not defined correctly.

🔴 Logout not working
Fix: Django 5.0+ requires Logout to be a POST request. Ensure your logout button is inside a form with a {% csrf_token %}.

👤 Author
Divyansh Python & Django Developer Learning full-stack web development 🚀

⭐ If you like this project, please star the repository on GitHub!
