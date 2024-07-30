# Plant Care Web Application

A web application built using Flask and SQLAlchemy for managing plants and their categories. This application allows users to add, edit, and delete plants and categories, and view them on a web interface.

## Features

- **Manage Plants**: Add, edit, and delete plant entries.
- **Manage Categories**: Add, edit, and delete categories for plants.
- **View Listings**: Display all plants and categories in a list format.

## Technology Stack

- **Flask**: Web framework for Python.
- **SQLAlchemy**: ORM for database interactions.
- **Materialize CSS**: Frontend framework for responsive design and styling.
- **PostgreSQL**: Database management system.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- PostgreSQL
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/TailorBird93/plantCare
    cd plantCare
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**

    Create a PostgreSQL database and update your `config.py` with the database URI.

    ```python
    # config.py
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/plantcare'
    ```

    Initialize the database:

    ```bash
    python
    >>> from plantcare import db
    >>> db.create_all()
    ```

5. **Run the Application**

    ```bash
    flask run
    ```

    Visit `http://127.0.0.1:5000` in your browser.


### Wireframes
1. Main Page
   ![wireframeA](https://github.com/user-attachments/assets/4e6d82a5-4ecc-4f79-a003-913373a2dad0)


### Testing 
1. Lighthouse
![1722303231369-8fb2d8d9-9366-46e6-b267-c60e384beea4_4](https://github.com/user-attachments/assets/788e0ce7-60be-422d-85e9-2d54acaf71b3)
![1722303231369-8fb2d8d9-9366-46e6-b267-c60e384beea4_3](https://github.com/user-attachments/assets/c9d1b00c-2802-4167-8d80-76b84eef70ce)
![1722303231369-8fb2d8d9-9366-46e6-b267-c60e384beea4_2](https://github.com/user-attachments/assets/a253b6d4-da85-4144-9ea0-5a75f80c288b)
![1722303231369-8fb2d8d9-9366-46e6-b267-c60e384beea4_1](https://github.com/user-attachments/assets/d78ecf2e-a965-4d64-8f64-7b34c3ca2036)

   



