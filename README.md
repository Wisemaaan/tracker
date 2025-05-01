# Tracker - Django Task Manager

A simple task management web application built with Django. It allows users to manage their daily tasks in an intuitive and responsive interface.

---

## Features

-  User registration and login
-  Add new tasks
-  Edit existing tasks
-  Mark tasks as completed or not completed
-  Delete tasks
-  Filter tasks (all, completed, not completed)
-  Responsive design using Bootstrap
-  Success messages after actions
-  Authentication protection for all views

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Wisemaaan/tracker.git
   cd tracker
2. Install dependencies (you can also create a virtual environment):
    ```bash
    pip install -r requirements.txt

3. Run migrations and start the development server:
    ```bash
    python manage.py migrate
    python manage.py runserver

4. Visit http://127.0.0.1:8000/ in your browser.

## Tests

1. To run unit tests:

    ```bash
    python manage.py test

    Tests include:

- Adding a task

- Editing a task

- Filtering tasks

- Protecting views from unauthenticated users

## Future Plans

- Adding a task

- Editing a task

- Filtering tasks

- Protecting views from unauthenticated users

## Author

- Wisemaaan