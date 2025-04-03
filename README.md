# TOTP Authentication Flask App

This is a simple Flask-based application that generates Time-based One-Time Passwords (TOTP) for user authentication using the `pyotp` library. The app allows you to generate secrets, retrieve TOTP codes, and get a list of usernames.

## Features

- Display a list of available usernames
- Generate a random secret key for each username
- Generate TOTP codes for each username
- Display time remaining before the TOTP code expires
- Simple and user-friendly frontend interface

## Technologies Used

- Flask
- pyotp
- Python 3.x
- HTML, CSS, and JavaScript (for frontend)

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

## Frontend: `index.html`

The user interface is built with HTML, CSS, and JavaScript, and it provides a simple, responsive layout for the TOTP generator.

### Key Components:

1. **Username Selection**:
   - The user can select a username from a dropdown list populated dynamically by the app using the `/usernames` API endpoint.
   
2. **TOTP Display**:
   - After selecting a username, the user clicks the **"Start TOTP Generator"** button to begin generating TOTP codes.
   - The TOTP code is displayed in a large font in the center of the screen.
   - The remaining time until the code expires is shown in seconds, and a progress bar visualizes the countdown.
   - A **"Use Different Username"** button allows the user to go back to the username selection screen.

3. **TOTP Timer**:
   - The timer is initialized when the user selects a username and clicks **Start TOTP Generator**.
   - The TOTP code is updated every 30 seconds as a new code is generated for the user.
   - The progress bar fills according to the time remaining.

### Key JavaScript Functions:

- **Fetching Usernames**:
   - The `fetch('/usernames')` API call retrieves the available usernames from the backend and populates the dropdown.

- **TOTP Code Generation**:
   - When the user clicks the "Start TOTP Generator" button, the app sends a `POST` request to `/get-totp` to retrieve the TOTP code for the selected username.
   - The app updates the displayed TOTP code and the countdown timer.

- **Timer Update**:
   - The app uses `setInterval()` to update the countdown timer and TOTP code every second, refreshing the display when the time reaches zero or 30 seconds.

### Screenshots


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
```

### `GET` /generate-secret

This route generates and returns a random secret key.

Response Example:
```json
{
    "secret": "JBSWY3DPEHPK3PXP"
}
```

### `POST` /get-totp

This route takes a username and returns the TOTP code for that user, along with the time remaining before the code expires.

Request Body Example:
```json
{
    "username": "user1"
}
```
Response Example:
```json
{
    "code": "123456",
    "timeRemaining": 25
}
```
Error Handling

If an invalid username is provided, the API will return an error response:
```json
{
    "error": "Invalid username"
}
```

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License

This project is open-source and available under the MIT License.


