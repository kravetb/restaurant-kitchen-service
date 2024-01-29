# restaurant-kitchen-service

## Overview
This project is a kitchen management system where you can add, update, and delete various dish types, cooks, and dishes.

## Contents
1. [Pages](#pages)
    - [Home Page](#home-page)
    - [Dish Type List](#dish-type-list)
    - [Create Dish Type](#create-dish-type)
    - [Update Dish Type](#update-dish-type)
    - [Delete Dish Type](#delete-dish-type)
    - [Cook List](#cook-list)
    - [Cook Details](#cook-details)
    - [Create Cook](#create-cook)
    - [Update Cook](#update-cook)
    - [Delete Cook](#delete-cook)
    - [Dish List](#dish-list)
    - [Dish Details](#dish-details)
    - [Create Dish](#create-dish)
    - [Update Dish](#update-dish)
    - [Delete Dish](#delete-dish)

2. [Instructions for Local Setup](#instructions-for-local-setup)
3. [Environment Configuration](#environment-configuration)
4. [License](#license)

## Pages

### Home Page
- URL: `/`
- Description: The main page of the project.

### Dish Type List
- URL: `/dish-types/`
- Description: Page displaying a list of all dish types.

### Create Dish Type
- URL: `/dish-types/create/`
- Description: Page for creating a new dish type.

### Update Dish Type
- URL: `/dish-types/<int:pk>/update/`
- Description: Page for updating an existing dish type.

### Delete Dish Type
- URL: `/dish-types/<int:pk>/delete/`
- Description: Page for deleting an existing dish type.

### Cook List
...

## Instructions for Local Setup
1. Clone the repository: `git clone https://github.com/yourusername/kitchen-project.git`
2. Install necessary dependencies: `pip install -r requirements.txt`
3. Start the server: `python manage.py runserver`

## Environment Configuration
- Create a `.env` file based on `env.sample` and enter your secret keys and other settings.

## License
This project is distributed under the [MIT License](LICENSE).

## Setting up Environment

1. **Copy the Environment Configuration File:**
   - Duplicate the `env.sample` file and rename the copy to `.env`.

2. **Fill in the Values:**
   - Open the `.env` file and fill in the appropriate values for each variable.

3. **Key Variables:**
   - `SECRET_KEY`: Your Django secret key.
   - `DEBUG`: Set to `True` for development, `False` for production.
   - `DATABASE_URL`: URL for your database connection.
   - `API_KEY`: Your API key (if applicable).

4. **Save and Use:**
   - Save the `.env` file.
   - This file contains sensitive information, so make sure not to share it publicly or include it in your version control system.

5. **Run the Project:**
   - Now you can run your project with the configured environment settings.

Note: Do not forget to add `.env` to your `.gitignore` file to avoid accidentally committing it to version control.
