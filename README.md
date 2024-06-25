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

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or need further assistance, please contact me at [your-email@example.com].

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - For responsive design
- [Font Awesome](https://fontawesome.com/) - For icons
- [jQuery](https://jquery.com/) - For JavaScript operations
- [Django REST framework](https://www.django-rest-framework.org/) - For API creation

## Troubleshooting

### Common Issues

1. **Database Issues**
    - Ensure you've applied migrations using `python manage.py migrate`.
    - Check your database configuration in `settings.py`.

2. **Static Files Not Loading**
    - Make sure you've collected static files using `python manage.py collectstatic`.
    - Check the `STATIC_URL` and `STATIC_ROOT` settings in `settings.py`.

3. **Template Errors**
    - Ensure custom template tags and filters are correctly registered.
    - Check for syntax errors or missing context variables.

4. **User Authentication Issues**
    - Verify that you have correctly set up the authentication backends in `settings.py`.
    - Check if the user is properly authenticated using `request.user.is_authenticated`.

### Getting Help

If you encounter any issues or need further assistance, you can:

- Open an issue on the [GitHub repository](https://github.com/yourusername/your-repo-name/issues).
- Check the [Django documentation](https://docs.djangoproject.com/en/stable/) for more information.
- Contact the project maintainer at [your-email@example.com].

## Future Enhancements

- Implement notifications for user activities.
- Add more customization options for user profiles.
- Enhance the search functionality with filters and sorting.
- Integrate a rich text editor for messages.
- Add support for private messaging between users.

## Screenshots

![image](https://github.com/Misha2007/ternet/assets/55316381/76b4e4e4-3e62-456d-9a84-203b46b4cf26)
*Description of the home page.*

![image](https://github.com/Misha2007/ternet/assets/55316381/6d0f4736-a3f9-4920-b0b8-66beaee1ce14)

*Description of the user profile page.*

![image](https://github.com/Misha2007/ternet/assets/55316381/566abf7c-463b-4e14-b7a0-98c1f2a788ba)
*Description of the message reply functionality.*

## Credits

- Special thanks to all contributors who have helped improve this project.
- Thanks to the [Django](https://www.djangoproject.com/) community for their valuable resources and support.



