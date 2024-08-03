
# E-Voting System

This project is an electronic voting system designed to facilitate secure and efficient voting processes. It includes features for user authentication, voting interface, real-time results, and an admin panel for managing elections and candidates.

## Features

- **Secure Authentication:** Users can register and log in securely.
- **Voting Interface:** Provides a user-friendly interface for casting votes.
- **Real-time Results:** Displays election results in real-time.
- **Admin Panel:** Admins can manage elections, candidates, and monitor results.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.x
- Django
- SQLite (or any other preferred database)

### Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/MahmoudBayoumi58/E-Voting-System.git
    cd E-Voting-System
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and navigate to \`http://localhost:8000\`.
2. Register a new user or log in with an existing account.
3. Admins can log in to the admin panel at \`http://localhost:8000/admin\` to manage elections and candidates.
4. Users can cast their votes and view real-time results.

## Project Structure

- **backend/**: Contains the Django project settings and configuration files.
- **templates/**: HTML templates for rendering frontend views.
- **static/**: Static files (CSS, JavaScript, images).
- **voting/**: Contains the core application files, including models, views, and forms.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature/your-feature-name\`).
3. Make your changes.
4. Commit your changes (\`git commit -m 'Add some feature'\`).
5. Push to the branch (\`git push origin feature/your-feature-name\`).
6. Create a pull request.


## Acknowledgements

- Django
- Bootstrap
