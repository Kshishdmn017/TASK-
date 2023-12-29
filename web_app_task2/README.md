# Car Selling Project

## Overview

The Car Selling Project is a web application built using Django, designed to facilitate the buying and selling of cars online. Users can browse listings, post their vehicles for sale, and contact sellers.

## Features

- User Registration and Authentication
- Posting Vehicles for Sale
- Viewing Vehicle Listings
- Contacting Sellers
- Admin Dashboard for Managing Listings

## Installation

To run the Car Selling Project locally on your machine, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Kshishdmn017/TASK-

    Navigate to the project directory:
    cd TASK-/web_app_task2 
   ```



Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

    On Windows:

```bash

venv\Scripts\activate
```

On macOS and Linux:

```bash

    source venv/bin/activate
```
Install project dependencies:


```bash

pip install -r requirements.txt

```
Create the database and apply migrations:

```bash

python manage.py migrate
```
Create a superuser account to access the admin dashboard:

```bash

python manage.py createsuperuser
```

Start the development server:

```bash
    python manage.py runserver
```
