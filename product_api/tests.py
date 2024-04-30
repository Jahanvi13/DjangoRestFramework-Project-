from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()  # Initialize an API client

    
    #Test the GET /products Endpoint:

    def test_get_all_products(self):
    # Create some sample products
        Product.objects.create(name="Product1", description="Description1", price=10.00, in_stock=True)
        Product.objects.create(name="Product2", description="Description2", price=20.00, in_stock=True)

    # Make a GET request to the /products endpoint
        response = self.client.get('/products/')

    # Check that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Ensure the response contains 2 products
        self.assertEqual(len(response.data), 2)


    #Test the POST /products Endpoint:

    def test_create_product(self):
    # Create product data
        new_product = {
            "name": "New Product",
            "description": "A new product",
            "price": 15.00,
            "in_stock": True
        }

    # Make a POST request to create a product
        response = self.client.post('/products/', new_product, format='json')

    # Check if the product was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Verify the created product's details
        self.assertEqual(response.data['name'], new_product['name'])


    #Test the GET /products/{id} Endpoint:    

    def test_get_product_by_id(self):
    # Create a sample product
        product = Product.objects.create(name="Product1", description="Description1", price=10.00, in_stock=True)

    # Make a GET request to get the product by ID
        response = self.client.get(f'/products/{product.id}/')

    # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Ensure the retrieved product has the correct name
        self.assertEqual(response.data['name'], product.name)


    
    #Test the PUT /products/{id} Endpoint:

    def test_update_product(self):
    # Create a sample product
        product = Product.objects.create(name="Product1", description="Description1", price=10.00, in_stock=True)

    # New data to update the product
        updated_data = {
            "name": "Updated Product",
            "description": "Updated Description",
            "price": 12.00,
            "in_stock": True
        }

    # Make a PUT request to update the product
        response = self.client.put(f'/products/{product.id}/', updated_data, format='json')

    # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Verify the updated product's details
        self.assertEqual(response.data['name'], updated_data['name'])


   #Test the DELETE /products/{id} Endpoint:

    def test_delete_product(self):
    # Create a sample product
        product = Product.objects.create(name="Product1", description="Description1", price=10.00, in_stock=True)

    # Make a DELETE request to delete the product
        response = self.client.delete(f'/products/{product.id}/')

    # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Ensure the product is removed from the database
        self.assertFalse(Product.objects.filter(id=product.id).exists())






