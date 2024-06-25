# Ternet

This is a Django-based forum project where users can register, create topics, post messages, and reply to messages. The forum includes features like user authentication, message replies, and indicating whether users are online.

## Features

- User Registration and Authentication
- Create and Manage Topics
- Post and Reply to Messages
- User Profiles with Online Status Indicators
- Search Functionality
- Responsive Design

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- Virtualenv

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### User Registration and Authentication

- Users can register, log in, and log out.
- Only authenticated users can create topics and post messages.

### Forum

- Users can create topics and post messages in those topics.
- Messages can be replied to, creating a thread of replies.

### User Profiles

- Users have profiles that display their information.
- Online status is indicated with a green icon next to the user's profile picture.

## Folder Structure

