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

4. The `username_secretkey.py` file contains a `user_secrets` dictionary with usernames and their associated secret keys. Change the username and secret key according to your use case:

    ```python
    # username_secretkey.py
    user_secrets = {
        "user1": "JBSWY3DPEHPK3PXP",  # Example secret
        "user2": "KZXW6Y3DHJXG4T6F"   # Example secret
    }
    
    ```
    - If you need to generate new secret keys, you can use a Python tool like [pyotp](https://pypi.org/project/pyotp/) to generate them. Here's an example of how to generate a new secret key:

    ```python
    import pyotp
    print(pyotp.random_base32())  # This will print a new secret key
    ```

    After generating a new secret key, you can replace the old key in the `user_secrets` dictionary with the new one.

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
![image](https://github.com/user-attachments/assets/38da4174-eaba-4327-b04c-a70ee48e1ea6)
   
2. **TOTP Display**:
   - After selecting a username, the user clicks the **"Start TOTP Generator"** button to begin generating TOTP codes.
   - The TOTP code is displayed in a large font in the center of the screen.
   - The remaining time until the code expires is shown in seconds, and a progress bar visualizes the countdown.
   - A **"Use Different Username"** button allows the user to go back to the username selection screen.

3. **TOTP Timer**:
   - The timer is initialized when the user selects a username and clicks **Start TOTP Generator**.
   - The TOTP code is updated every 30 seconds as a new code is generated for the user.
   - The progress bar fills according to the time remaining.
![image](https://github.com/user-attachments/assets/cefc5056-d09e-40ef-8c8f-89e9fd759127)

### Key JavaScript Functions:

- **Fetching Usernames**:
   - The `fetch('/usernames')` API call retrieves the available usernames from the backend and populates the dropdown.

- **TOTP Code Generation**:
   - When the user clicks the "Start TOTP Generator" button, the app sends a `POST` request to `/get-totp` to retrieve the TOTP code for the selected username.
   - The app updates the displayed TOTP code and the countdown timer.

- **Timer Update**:
   - The app uses `setInterval()` to update the countdown timer and TOTP code every second, refreshing the display when the time reaches zero or 30 seconds.

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


