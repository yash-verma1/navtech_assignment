# Assignment 

To run the code, setup a virtualenv and install the depenendenices from requirements.txt

## Apis 
APIs can be accessed at 

    http://127.0.0.1:8000/apis/view_products/

    http://127.0.0.1:8000/apis/upload_products/

    http://127.0.0.1:8000/apis/create_order/

    http://127.0.0.1:8000/apis/view_orders/


## What's working

* View products gets all the products available in the DB 
* View orders gets all the orders available in the DB 
* Create orders accepts item in the following JSON object to add a single new order in the DB.

    {
    "user": "Yash",
    "name": "item A",
    "quantity": "1"
    }
* Upload orders accepts the following JSON object to add a single new item to the DB. Price and quantity are over written if the item already exists
    
    {
    "name": "item A",
    "price": "101",
    "quantity": "1"
    }

    