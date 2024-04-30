Product Management System API

This project is a REST API for a simple product management system built with Django. It allows users to perform CRUD operations on a product database. The API endpoints enable listing all products, creating new ones, retrieving, updating, and deleting specific products by ID.

Features:

List All Products: Retrieve a list of all products in the system.
Create Product: Add new products to the database.
Retrieve Product: Get details of a specific product by its ID.
Update Product: Update existing product information.
Delete Product: Remove a product from the database by its ID.
HTTP Methods

The API supports a set of RESTful HTTP methods to perform CRUD operations:

GET /products: List all products.
POST /products: Create a new product.
GET /products/{id}: Retrieve a product by its ID.
PUT /products/{id}: Update a product by its ID.
DELETE /products/{id}: Delete a product by its ID.
