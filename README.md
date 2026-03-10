# Byte-Pass 🔐

Byte-Pass is a simple Flask web application for user registration and login.
It stores users in SQLite and secures passwords using Werkzeug hashing.

## Overview

This project is designed as a lightweight authentication starter app:

- Register new users
- Store credentials in a local SQLite database
- Hash passwords before saving them
- Validate login attempts against stored password hashes
- Render clean web pages for home, registration, and login flows

## Tech Stack

- **Backend:** Flask
- **Database:** SQLite
- **Security:** `werkzeug.security` password hashing
- **Frontend:** HTML + Bootstrap 5

## Project Structure

```text
.
├── app.py
├── database.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── login.html
│   └── register.html
└── users.db
```

## Installation

### 1) Clone the repository

```bash
git clone https://github.com/Sh4dowXZ/user-login-webapp.git
cd user-login-webapp
```

### 2) (Optional but recommended) Create a virtual environment

Create the environment:

```bash
python3 -m venv .venv
```

Activate it with the command for your shell:

**macOS/Linux (bash/zsh/sh)**

```bash
source .venv/bin/activate
```

**macOS/Linux (fish shell)**

```fish
source .venv/bin/activate.fish
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Initialize the database

```bash
python database.py
```

### 5) Run the application

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000` by default.

## Usage

- Open `http://127.0.0.1:5000`
- Create a user from the **Register** page
- Sign in from the **Login** page

## Deployment

A live version is available at:

- https://bytepass.onrender.com/register

## Author

Created by **Márcio Mota** ([Sh4dowXZ](https://github.com/Sh4dowXZ)).
