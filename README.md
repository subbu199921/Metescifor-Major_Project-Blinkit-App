# Blinkit App Inspired by E-commerce Platform

Website Link :   https://subhashba.pythonanywhere.com/

## Overview
**Blinkit** is a Django-based e-commerce application that enables seamless online shopping. It includes user authentication, vendor registration, product catalog management, shopping cart functionality, order placement, and Razorpay payment integration.


## Table of Contents
- Project Structure
- Installation
- Configuration
- Dependencies
- Usage
- Models
- Forms
- Views
- Templates
- signals
- Razorpay Integration
- Development

## Project Structure
```bash
Blinkit/
│── shop/             # Core Django app for shopping functionality
│   ├── models.py     # Database models
│   ├── views.py      # Views for handling user interactions
│   ├── forms.py      # Forms for user input
│   ├── urls.py       # URL routing for shop app
│   ├── payment.py    # Razorpay integration
│   ├── templates/    # HTML templates
│   ├── signals.py    # Django signals
│── Blinkit/          # Main Django project folder
│   ├── settings.py   # Project settings
│   ├── urls.py       # URL configurations
│── db.sqlite3        # SQLite database file
│── static/           # Static files (CSS, JS, images)
│── media/            # User-uploaded media files

##  Installation

### 1 Clone the Repository
```bash
git clone <repository_url>
cd Blinkit


### 2 Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


### 3 Install Dependencies
```bash
pip install django razorpay


### 4 Apply Migrations
```bash
python manage.py migrate

## Configuration

### Database Setup
1 By default, SQLite is used.
2 To use PostgreSQL or MySQL, update `DATABASES` in `settings.py`.

### Secret Key
1 Generate a strong `SECRET_KEY` for production.

### Debug Mode
1 `DEBUG = True` (for development)
2 **Disable in production!**

### Allowed Hosts
Configure `ALLOWED_HOSTS` to prevent unauthorized access.

###  Razorpay API Keys
 Set `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET` in `settings.py`.

### CSRF Trusted Origins
 Ensure Razorpay’s API and `rzp.io` are in `CSRF_TRUSTED_ORIGINS`.

##  Dependencies
1 **Django** (5.1.7)
2 **Razorpay**

## Usage
### Start the Development Server
```bash
python manage.py runserver

**Access the application at:** [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)

### Admin Panel
```bash
http://127.0.0.1:8000/admin/

## Models
1 **Vendor**: Stores vendor details
2 **Category**: Product categories
3 **Product**: Product details
4 **Customer**: Customer information
5 **Cart**: Shopping cart details
6 **Order**: Order details
 
## Forms
# **VendorRegistrationForm**: Vendor registration form

## Views
1 **product_list**: List of products
2 **vendor_register**: Vendor registration
3 **category_products**: Products by category
4 **cart_view**: Displays shopping cart
5 **payment_view**: Handles Razorpay payment processing
6 **payment_success**: Displays payment confirmation

## Templates
1 **base.html**: Base layout
2 **cart.html**: Shopping cart page
3 **login.html**: User login page
4 **payment.html**: Razorpay checkout page
5 **payment_success.html**: Payment success page
6 **product_list.html**: List of products

## Signals
1 **create_customer**: Creates a customer profile when a new user is registered
2 **save_customer**: Updates customer profile on user changes

##  Razorpay Integration
1 **API Keys** stored in `settings.py`
2 **Order Creation** handled in `payment.py`
3 **Payment Processing** integrated via `payment.html`

##  Development
### Create a New Django App
```bash
python manage.py startapp <app_name>

### Apply Migrations After Changes
```bash
python manage.py makemigrations
python manage.py migrate

### Create a Superuser
```bash
python manage.py createsuperuser

### Collect Static Files (For Production)
```bash
python manage.py collectstatic


## Notes
1 **Secure your `SECRET_KEY` and Razorpay API keys in production.**  
2 **Set `ALLOWED_HOSTS` properly in a live environment.**  
3 **Disable `DEBUG` mode for production deployment.**  
4 **Update documentation as new features are added.**  



