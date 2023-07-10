# EM-Commerce
# Table of Contents
* [Introduction](#introduction)
* [User Expereince (UX) design](#1-user-expereince-ux-design)
    * [User Goals](#11-user-goals)
    * [User Expectations](#12-user-expectations)
    * [User Stories](#13-user-stories)
    * [E-commerce Business Model](#14-e-commerce-business-model)
    * [Color Scheme](#15-color-scheme)
    * [Images and Logo](#16-images-and-logo)
    * [Site Skeleton](#17-site-skeleton)
* [Features](#2-features)
    * [Main Section](#main-section)
* [Technologies Used](#3-technologies-used)
* [Testing](#4-testing)
    * [Testing tools](#41-testing-tools)
    * [Manual Testing](#42-manual-testing)
    * [Lighthouse Reports](#43-lighthouse-reports)
* [Bugs](#5-bugs)
* [Deployment](#6-deployment)
* [Acknowledgement](#7-acknowledgement)

Welcome to [E.M-Commerce!](https://em-comm.herokuapp.com/)

# Introduction

E.M-Commerce is an online shop which can sell all kind of products from clothes to big home appliances. The app was build with HTML, CSS, JavaScript,Python and Django. The main purpose of the project is to Create, Read, Update and Delete (CRUD) entries in a database and display them, integrate payment system with Stripe and in the same time trying to give a good user experience.

![responsive image](/media/responsive1.PNG)
![responsive image](/media/responsive2.PNG)
![responsive image](/media/responsive3.PNG)

# 1. User Expereince (UX) design

* The site structure is designed considering the expectation of users to be simple and easy to use;
* The user interface is easy to navigate;
* The app is interactive, with nice alerts after each action;
* Responsive design for all screen/device sizes like mobile, tablet and desktop;

# Scope

## First Phase
* Responsive design
* Account registration
* View a list of products and each product individualy
* Ability to search and sort products
* Create, edit and delete products

## Second Phase
* Add a comment and rate products
* Add product variations for clothes (color and size)
* Create user profiles 
* Place an order and be able to do online payments


# 1.1 User Goals

* As a Site Admin, I want to manage the site content.
* As a Site User, I want to be able to interact with the content.
* As a Site User, I want the information to be easy to find and read.
* As a Site User, see products individualy, add comments and rate a product.

# 1.2 User Expectations

The content of the app changes at every action of a user. Folloiwng user's expections ware considered while designing the site:

* The site structure is designed considering the expectation of users to be simple and easy to use;
* The user interface is easy to navigate;
* Responsive design for all screen/device sizes like mobile, tablet and desktop;

# 1.3 User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

# 1.4 E-commerce Business Model 

## Executive Summary:
* This document presents a business model for EM-Commerce, an e-commerce platform. It provides an overview of the platform's mission, target market, product offering, marketing strategies and operational considerations.

## Introduction:
* EM-Commerce is an e-commerce platform where users can purchase different products from clothes to electronics. 

## Business Overview:
* EM-Commerce provides various products and deliver the products to the clients. Payments are made online and secure thanks to our online payment system. If the purchase value excedes 50 Euro the delivery will be free.

## Target Market:
* Targeted users are based in Ireland at the moment but in the future we want to increase our market to Europe.

## Product Offering:
* We offer a vast category of products at the moment from Clotes to Electronics and Furniture. Here is a list of products that you will find on our platform: Clothes, Computing, Furniture, Gaming, Home Appliances, Phones & Tablets, TV & Audio. For Clothes we have a variation of products with different sizes and colors that users can pick.


## Revenue Streams:
* Our revenue conssists in our sold products. For clients that are purchasing products for more then 50 Euro we provide free delivery across the entire country.

## Operational Considerations:
* We have implemented an effective inventory management system to track product availability, stock levels, and reorder points. Our stocks are  real-time inventory data to prevent overselling or stockouts selling. We have implemented the comments and rating section for each individual product to handle inquiries, complaints, and support requests.
* Also we have implemented a data privacy and security measures to protect customer information and maintain their trust that Comply with applicable data protection regulations, such as GDPR or CCPA.

## Conclusion:
* All these be considered EM-Commerce will progress day by day offering quality and trust for our clients. Our clients needs to take advantage of our comments section and express their opinion about our products and our delivery system because this will help us to improve our platform and provide an user experience.

# 1.5 Color Scheme

The choice of website right foreground and background colour is essential that decides the site visitors wheather to emote the site or not. I used [Color Hunt](https://colorhunt.co/) to select the background and foreground color. Colors that i used are:

* the content it`s mostly blank and white and because the app will store many images it will take the colors from them;
* and some bootstrp5 colors: warning, info, primary, alert

# 1.6 Images and Logo

This website was created for academic purposes, all photos were searched and downloaded from [Giphy website](https://giphy.com/) and [Google search](https://google.com/)

# 1.7 Site Skeleton

[Balsamiq](https://balsamiq.com/) was used to create wireframes of the website. This was very useful as it gives the template of the UI. Wireframes were designed for web browser and a mobile browser format:

## Main Page:
![Main page whireframe image](/media/main-page.PNG)



# Main Section

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* Banner is centered on the top 
* Products are listed on the main page using OwlCarousel 
* Popular categories are listed on the main page with catecogires links


## Products Page:
![Products page whireframe image](/media/products-page.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* Side menu to filter products by category, price and rating
* Products are displayed with names, price, category and rating


## Products Details:
![Products Details page whireframe image](/media/product-detail.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* Product image is shown on the left side
* Product details are on the rigth side with review stars also
* Under the product details I have added product reviwe. A user must be logged in to be able to submit a review


## Cart:
![Cart page whireframe image](/media/cart.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* A teble is displayed with the products added to cart. In the table I put product image, product variation if it`s the case, an input to increse and decrese the product quantity, a button to remove the product from cart no metter the quantity added.
* On the right side I displayed the total of the purchase with price for items, VAT and delivery and to buttons one for checout and one to go back to products search


## Checkout:
![Cart page whireframe image](/media/checkout.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* A form is displayed on the left to compleate shipping details.
* On the right side si a table with products that you are about to pay with details and price.
* Under the form is an input from Stripe to add card details with two buttons one to go back to the cart and one to proced checkout

## Checkout Informations:
![Cart page whireframe image](/media/checkout-infromation.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* A list with checkout information is displayed including order number, shipping details and Personal Informations
* Under the list I put a button to go to the perosnal profile

## My Profile:
![Cart page whireframe image](/media/profile.PNG)

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout;
* Buttons for login, register and logout are on a dropdown menu
* In the footer I put links to social media, link to Privacy Policy file, categories are listed, login and register links and newsletter
* On the profile page I put a side menu with links to personal details, order history, add a new product if user is superuser, and change password
* on the main profile page the from with personal details is displayed


# 2. Features

* Header, footer and navigation bar are consistent through all pages.
* Links and forms provide clear feedback to the site user.
* The opportunity to add comments and rate products will have all the users that are registered and logged in.
* A custom 404-error page is available for cart if the cart doesn`t exists.

# Site Presentation
![Header and menu](/media/header-and-menu.png)
* On the header I have the logo the search bar, a small welcome text with the username, the menu to login and the cart!

![Products carousel](/media/products-carousel.png)
* Also on the main page I created a small carousel to present a part of the products so the users can have an ideea of what they will find on the platform.

![Popular categories](/media/popular-categories.png)
* Under the products carousel I have displayed some of the popular categories that users can find on the website so that will make it easier to navigate and find what they are looking for.

![Footer](/media/footer.png)
* Footer is consitent to the entire site and there users can access the social media, categories, users can login or register and they can subscribe to the platform to recive new offers on their email.

![Products Page](/media/products-page-presentation.png)
* On the products page users can see all products displayed and sort them as by name, price or category.

![Products Details](/media/product-detail-image.png)
* Here users can see the details of the products, and add them to cart


![Customer Reviews](/media/customer-reviews.png)
* All users can place a review for each products and rate them, to be able to leave a review user must be logged in

![Shopping Cart](/media/shopping-cart.png)
* All pruducts are displayed in the shopping cart wehere you can increese or decreese the quantity of the products or remove them from the cart 

![Checkout Page](/media/checkout-page-image.png)
* The form with users details needs to be completed for shipping and payment details. Users will continue to see what they will purchase and they can keep track of they order.

![Profile Page](/media/checkout-page-image.png)
* All users will have a profile created when they register. If user is an admin will be able to add new products from the profile page. If user is a regular customer will be able to see the personal details, order history and manage their password.

# 3. Technologies Used

* HTML5 was used for structuring and presenting content of the website;
* CSS3 was used to provide the style to the content written in a HTML;
* JavaScript was used to add some nice alerts;
* Django was used as web framework;
* Django Template was used as a templating language for Django to display backend data to HTML;
* Django Allauth was used for user authentication, registration, and account management.
* Django Crispy Form was used to control the rendering of the forms;
* Django countries was used to list all contries dynamicly;
* Stripe was used for card payments;
* OwlCarousel was used to display products on the main page
* Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application;
* Cloudinary has been used as image management solution;
* ElephantSQL database was used in production, as a service based on PostgreSQL;
* Heroku was used to deploy the website
* Balsamiq was used to create wireframes of the website;
* Font Awsome was used to improt icons to the sites;
* Google Fonts was used to import font-family 'Raleway' into style.css file;
* Chrome was used to debug and test the source code using HTML5 as well as to test site responsiveness;
* Github was used to create the repository and to store the cproject's code after pushed from Git;
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub
* Gitpod was used as the Code Editor for the site;
* Color Hunt was used to select the background and font color in the website;
* W3C Markup and Jigsaw validation tools were used to validate the HTML code and CSS style used in the proejct;


# 4. Testing

## 4.1 Testing tools:

* Google Developer Tools for debug and test css and JavaScript code;
* W3C Validator Tools was used to check for any errors within my HTML pages:
* W3C CSS Validation was used to check for any error within my CSS stylesheet

## 4.2 Manual Testing

I have tested my site on multiple devices. These include:
* Galaxy Fold (280 x 653);
* Iphone 6/7/8 Plus (414 x 736);
* Ipad (768 x 1024);
* Nest Hub (1024 x 600);


## Main Page

| TEST | OUTCOME | PASS / FAIL |
|:---:|:---:|:---:|
| Login Button| When Login is clicked I am redirected to login page | PASS |
| Logout Button| When Logout is clicked I am redirected to index page | PASS |
| Products are displayed| I can see products displayed and when I click on a product it takes me to the rigth product details | PASS |
| Categories are displayed| I can see categories displayed and when I click on a category it takes me to the rigth filtered products list | PASS |
| Responsive | All pages and elements are responsive (mobile and desktop) using differnt breakpoints. | PASS |
| Text | Checked if all fonts and colors used are consistent or not | PASS |

## Products and Purchase Testing

| TEST | OUTCOME | PASS / FAIL |
|:---:|:---:|:---:|
| Menus |All menus links redirect me to the right url | PASS |
| Username | Username is displayed for the right user when he is loged in | PASS |
| Logout Button | When I am loged in the login button change to logout | PASS |
| Products | All products are displayed on product page correctly | PASS |
| Product Detail | When I click on a product it takes me to the rigth product | PASS |
| Product Image | When I click on the image it opens in a new window | PASS |
| Add to cart | Products are added to cart correctly | PASS |
| Product Variation | For clothes category I can select size and color | PASS |
| Product Variation on cart | When I add the same product on cart with different variation it will add it as a new product and if I add the same product with the same variation it will increse the quantity | PASS |
| Checkout | Form is rendered correctly and products that are about to be purchased are displayed correctly | PASS |
| Order | After checkout the order description is rendered including the order number | PASS |
| Profile | On the home page of the profile form with personal details is rendered correctly | PASS |
| Order History | On the order history all orders are displayed in a table | PASS |
| Add Product | Form is rendered correctly and the new product is displayed on products page | PASS |
| Update Product | The correct product is displayed and the new product descriptions are saved correctly | PASS |
| Delete a product | From the cart I can delete a product if I press delete no matter the quantity, I can decrease the quantity with + and - buttons and if I am a Site Admin if I delete a product it will be deleted from the database | PASS |
| Search and Sort | If I type the correct searh criteria the product from that category will be displayed and I can sort products by price, category, rating  | PASS |
| Product review | If I leave a comment it will be displayed on the product details with the stars and for each product the rating average is displayed correctly  | PASS |

## HTML Validation

![HTML Validation](/media/html-validation.png)
* Most of the HTML pages have errors beacuse of the use of django code passed in the HTML Tags

## CSS Validation
![CSS Validation](/media/css-validation.png)
* No errors ware found in the CSS 

## Python Validation
![Python Validation](/media/python-check.png)
* Most of the errors are because the lines are to long but because some part of the code is easyer to be read I chose to leave it like that like in exemple above!


## 4.3 Lighthouse Reports:

## Home:
![Lighthouse report](/media/home_lighthouse.PNG)

## Products:
![Lighthouse report](/media/products_lighthouse.PNG)

* Because of the search and refresh buttons from the search bar Accessibility is under 90!


# 5. Bugs

* During the development process I had multiple bugs with the page rendering and content displayed. Ussualy some missed informations in my views was the problem all fixed;
* I had errors during the deployment on heroku, for some reason static files ware not rendered on the page eaven if the static files ware successfuly uploaded on the AWS S3 bucket. I couldn`t fix this issue and after a few days of trying I had to rebuild the project.
* On lighthouse report accessibility is under 90 because of the buttons beside search bar . This wasn`t fix
* I had multiple issues with stripe webhooks Error 302 that was because the codeanywhere rediercted the page so I had to use VS Code local.

# 6. Deployment

 The site was deployed to Heroku using the following steps: 

 * Sign up to GutHub;
 * Create a new repository on GitHub;
 * Link Github project to Heroku
 * Add Procfile
 * Update settings.py
 * Add Environment Variables
 * Automatic deployment by Heroku
 * Created a new account on AWS
 * Created a new bucket, user and user group with the rigth setting and policyes
 * Linked Bucket with the project to store static files


 # 7. Acknowledgement

* This App was created for academic purposes, all photos were searched and downloaded from the[Giphy website](https://giphy.com/) and [Google website](https://google.com/)
* For README.md file, reference of https://github.com/dhakal79/Portfolio-project-MS1 was considered; 
* Most of the checkout app was from Btique Ado project form CI 


