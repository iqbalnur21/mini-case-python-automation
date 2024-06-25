# Selenium Automation Project

This project automates interactions with a web application using Selenium. It includes functionalities for logging in, performing CRUD operations on user data, and handling various web elements dynamically.

## Prerequisites

- Chrome
- Python 3.x installed on your system
- pip (Python package installer)

## Project Structure

Selenium_Automation_Project/
│
├── main.py
├── actions.py
├── config.py
├── APICache.pkl
├── requirements.txt
├── README.md

- `main.py`: The main script that runs the automation.
- `actions.py`: Contains reusable functions for interacting with web elements.
- `config.py`: Stores configuration variables like URLs and API tokens.
- `APICache.pkl`: Cache for login the API.
- `requirements.txt`: Lists required Python packages.

## Setup

### Step 1: Clone the repository

Clone this repository to your local machine using:

```sh
git clone https://github.com/iqbalnur21/mini-case-python-automation
cd mini-case-python-automation
```

### Step 2: Install Dependencies

The script automatically checks for required packages (`selenium`, `webdriver_manager`) and installs them if they are not already installed.

### Step 3: Update Configuration

Update the `config.py` file with your actual token.

```python-repl
# config.py

token = "your_token"
userAPI = "https://gorest.co.in/public/v2/users"
url = "https://gorest.co.in/rest-console""
```

## Running the Script

Execute the main script using Python:

`python main.py`

Or if you use windows operating system just double click `main.py` file in your computer

## Customization

* To modify actions or add new ones, edit the `actions.py` file.
* To change configuration variables like URLs or token, edit the `config.py` file.
