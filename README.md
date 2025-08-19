Company Portal Readme
This project is a web-based company portal developed using the Django framework. It features user registration with a custom user model, job listings with search functionality, and an administrative interface for managing job postings and applicants.

1. Prerequisites
Before you begin, make sure you have the following installed on your system:

Python 3.8+

pip (Python's package installer)

virtualenv (optional, but recommended)

2. Getting Started
Step 1: Clone the Repository
Clone the project from its source into a local directory on your machine.

Bash

git clone <repository_url>
cd <project_directory>
Step 2: Create a Virtual Environment
It's a best practice to use a virtual environment to manage project dependencies.

Bash

python -m venv venv
Activate the virtual environment.

On Windows:

Bash

.\venv\Scripts\activate
On macOS and Linux:

Bash

source venv/bin/activate
Step 3: Install Dependencies
You will need to install Django and any other necessary packages.

Bash

pip install django
Step 4: Configure Project Files
Add .gitignore: To prevent unnecessary files from being committed, create a .gitignore file in your project's root folder and add the following lines to exclude your virtual environment and the database file.

# Virtual environment
/venv/
# Django
db.sqlite3
/media/
Download Bootstrap: For local hosting, download Bootstrap's compiled CSS and JS files. Place the bootstrap.min.css file in static/bootstrap/ and bootstrap.bundle.min.js in the same folder. Your project directory should look like this:

company_portal/
├── static/
│   └── bootstrap/
│       ├── bootstrap.min.css
│       └── bootstrap.bundle.min.js
3. Running the Project
Once all files are configured, you can run the server.

Step 1: Apply Migrations
Apply the database migrations to create the necessary tables for your accounts and jobs apps.

Bash

python manage.py makemigrations accounts jobs
python manage.py migrate
Step 2: Create a Superuser
You need an administrator account to access the Django admin panel and create new job postings.

Bash

python manage.py createsuperuser
Follow the prompts to set up your admin username, email, and password.

Step 3: Run the Server
Start the development server.

Bash

python manage.py runserver
You can now access the portal by navigating to http://127.0.0.1:8000/ in your web browser. The admin site is available at http://127.0.0.1:8000/admin/.
