# EM-Commerce
# Table of Contents
* [Introduction](#introduction)
* [User Expereince (UX) design](#1-user-expereince-ux-design)
    * [User Goals](#11-user-goals)
    * [User Expectations](#12-user-expectations)
    * [Color Scheme](#13-color-scheme)
    * [Images and Log](#14-images-and-logo)
    * [Site Skeleton](#15-site-skeleton)
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


# 1.1 User Goals

The app is designed for shoppers that want to do their shopping online and secure;

# 1.2 User Expectations

The content of the app changes at every action of a user. Folloiwng user's expections ware considered while designing the site:

* The site structure is designed considering the expectation of users to be simple and easy to use;
* The user interface is easy to navigate;
* Responsive design for all screen/device sizes like mobile, tablet and desktop;

# 1.3 Color Scheme

The choice of website right foreground and background colour is essential that decides the site visitors wheather to emote the site or not. I used [Color Hunt](https://colorhunt.co/) to select the background and foreground color. Colors that i used are:

* the content it`s mostly blank and white and because the app will store many images it will take the colors from them;
* and some bootstrp5 colors: warning, info, primary, alert

# 1.4 Images and Logo

This website was created for academic purposes, all photos were searched and downloaded from [Giphy website](https://giphy.com/) and [Google search](https://google.com/)

# 1.5 Site Skeleton

[Balsamiq](https://balsamiq.com/) was used to create wireframes of the website. This was very useful as it gives the template of the UI. Wireframes were designed for web browser and a mobile browser format:

## Main Page:
![Main page whireframe image](/media/main-page.PNG)

# 2. Features

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

## Dashboard Section

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


