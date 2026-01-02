 E-Commerce Backend API

A scalable backend system for an e-commerce platform built using Django REST Framework.

 Features :-
- JWT authentication
- Product management
- Cart & checkout
- Order tracking
- Razorpay sandbox payment integration
- Dockerized deployment

Tech Stack :-
- Django, DRF
- PostgreSQL
- JWT Auth
- Razorpay
- Docker
- AWS (EC2)

 Architecture :-
- Modular app-based structure
- Token-based authentication
- RESTful APIs

 Setup :-
```bash
git clone https://github.com/yourname/ecommerce-backend
cd ecommerce-backend
docker build -t ecommerce .
docker run -p 8000:8000 ecommerce
