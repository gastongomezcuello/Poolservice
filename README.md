# Project Overview

This project is an online administration and sales platform for a pool supply business. It includes functionalities for managing products, clients, users, and orders. 

## Installation

To set up the project, ensure you have the following installed:

- **Python** (preferably version 3.11, as this is the version used)
- **Pandas**
- **SQLAlchemy**
- **Django**
- **Openpyxl** (primarily for `add_data.py` which adds data from an Excel file)
- **Pillow** (required for working with `ImageField`—note that it doesn’t appear in the profile completion form, but it should be included)

## Features

- **Product Management**: Add, modify, and view products including unique codes, descriptions, prices, exchange rates, and stock availability. 
- **Client Management**: Create and manage client profiles.
- **User Management**: Create and manage user accounts.
- **Order Management**: Create and modify orders, including linking products and clients.

## Functionality

- **Data Import**: Use `add_data.py` to import product data from a provider’s Excel file. This functionality is operational.
- **Homepage**: Currently displays text only. Future updates will include images, links, and additional minor functions.
- **Forms**: All forms are `forms.ModelForm`. Forms are validated before data is added to the database.
- **Client Profiles**: Clients can create and update their profiles upon registration or by clicking on their user profile when logged in. This profile is created as a `one-to-one` relationship with the user.
- **Access Control**: 
  - Products can be viewed without registration but cannot be updated or created.
  - Registered clients should not have the ability to modify or create objects. This restriction will be enforced in future updates.
- **Contact Us**: Queries submitted through the contact form are saved in the database and sent to the company’s email. Additionally, an automatic email is sent to the person who submitted the query.
- **Client, Product, and Order Creation**: Links for creating new clients and orders will appear in the navigation menu for logged-in users. 

## Important Details

- **Client Type**, **Exchange Rates** in products, and **Payment Methods** in orders are crucial for calculating final prices. Discounts apply to resellers, exchange rates vary by product, and payment methods may affect pricing. This functionality is planned but not yet implemented.
- **Link Restrictions**: The "New Client" link should not be used.
- **Profile Completion**: The client profile is completed upon registration or by accessing the user profile when logged in. This applies whether the user is created via the console or the registration page.

## Future Updates

- Styling and page creation are ongoing.
- Only the product page with a list of products, prices, business information, contact details, and frequently asked questions will be publicly accessible. Registered users will have access to create clients, products, and orders.
