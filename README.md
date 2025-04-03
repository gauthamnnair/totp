# TOTP Authentication Flask App

This is a simple Flask-based application that generates Time-based One-Time Passwords (TOTP) for user authentication using the `pyotp` library. The app allows you to generate secrets, retrieve TOTP codes, and get a list of usernames.

## Features

- Display a list of available usernames
- Generate a random secret key for each username
- Generate TOTP codes for each username
- Display time remaining before the TOTP code expires

## Technologies Used

- Flask
- pyotp
- Python 3.x

## Setup

### Prerequisites

1. Python 3.6 or higher
2. `pip` (Python package manager)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/gauthamnnair/totp.git
    cd totp
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have a `username_secretkey.py` file with the `user_secrets` dictionary containing the usernames and their associated secret keys:

    ```python
    # username_secretkey.py
    user_secrets = {
        "user1": "JBSWY3DPEHPK3PXP",  # Example secret
        "user2": "KZXW6Y3DHJXG4T6F"   # Example secret
    }
    ```

5. Run the Flask app:

    ```bash
    python app.py
    ```

6. The application will start running on `http://127.0.0.1:5000/`. You can access it in your browser.

## API Endpoints

### `GET /`

This route returns the main page, which displays the list of usernames.

### `GET /usernames`

This route returns a JSON response with a list of all available usernames.

**Response Example:**

```json
{
    "usernames": ["user1", "user2"]
}

GET /generate-secret

This route generates and returns a random secret key.

Response Example:

{
    "secret": "JBSWY3DPEHPK3PXP"
}

POST /get-totp

This route takes a username and returns the TOTP code for that user, along with the time remaining before the code expires.

Request Body Example:

{
    "username": "user1"
}

Response Example:

{
    "code": "123456",
    "timeRemaining": 25
}

Error Handling

If an invalid username is provided, the API will return an error response:

{
    "error": "Invalid username"
}

Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.
License

This project is open-source and available under the MIT License.


This `README.md` includes an overview of the project, setup instructions, API endpoints, and error handling details, which should help any user get started with your project quickly.

