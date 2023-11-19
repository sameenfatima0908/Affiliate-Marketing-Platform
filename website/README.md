
# Affiliate Marketing Platform Application

The Project Name is a Affiliate Marketing Platform web application designed to serve as an affiliate marketing hub. It provides users with the ability to explore and purchase a variety of products through affiliate links. The platform emphasizes user authentication and product discovery.

## Key Features

- **User Authentication:** Allows users to sign up, log in, and log out securely.
- **Product Listings**: Explore a diverse range of products with affiliate links.
- **Responsive Design:** The application is designed with responsiveness in mind, ensuring a seamless experience across various devices.**


## Installation

To install and run the project locally, follow the steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/sameenfatima0908/Affiliate-Marketing-Platform.git
    ```
    
2. Navigate to the project directory:

    ```bash
    cd online_affiliate_platform
    ```

3. Create a virtual environment:

    ```bash
    # For Windows
    python -m venv env
    
    # For macOS and Linux
    python3 -m venv env
    ```
   
4. Activate the virtual environment:

    ```bash
    # For Windows
    env\Scripts\activate
    
    # For macOS and Linux
    source env/bin/activate
    ```
    
5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```    

6. Apply database migrations:

    ```bash
    cd website
    ```

    ```bash
    python manage.py makemigrations
    ```  

    ```bash
    python manage.py migrate
    ```    

## Usage

1. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

2. Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and recipes.

3. Visit `http://127.0.0.1:8000/signup/` to register yourself as a user on the project.

4. Visit `http://127.0.0.1:8000/login/` to log in and access the application functionality.

5. Visit `http://127.0.0.1:8000/` to redirect to Home Page.

## Credits

- [Django Framework](https://www.djangoproject.com/)
- [Bootstrap Framework](http://bootstrap.com)