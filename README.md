# FoodMenuProject

This project consists of two applications. One of the applications was created for the preparation of the content of the project and the other for user actions (such as registering, login, logout).
A base template was used in the project and other html pages were extended from base.html. Database table was created with the help of Django model. The products created with the help of the form are listed in index.html.
In index.html, the product's picture, name, product description, product price and the person who added the product are given. In index.html, it was possible to reach the detail page of the products with the help of a button.
On the detail page, users can view the product information and also have the opportunity to delete the product whenever they wish.
In the Users application, register, login and logout features were added with the help of Django forms. In addition, with the help of Django signals, a user-specific profile page was created as soon as the user was registered.
