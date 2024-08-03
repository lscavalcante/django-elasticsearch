# Django and Elasticsearch

## Description

This is a web API project using Django REST Framework and Elasticsearch.

## Requirements

Here are the packages required for this project:

- asgiref==3.8.1
- certifi==2024.2.2
- Django==5.0.6
- django-elasticsearch-dsl==8.0
- elastic-transport==8.13.0
- elasticsearch==8.13.1
- elasticsearch-dsl==8.13.1
- python-dateutil==2.9.0.post0
- six==1.16.0
- sqlparse==0.5.0
- typing_extensions==4.11.0
- urllib3==2.2.1

## Getting Started with the Django Project

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**: Use the `git clone` command to clone the repository. Replace `repository_url` with the URL
   of your repository.
2. **Create a virtual environment**: `python3 -m venv venv`
3. **Activate the virtual environment**: Use the `source venv/bin/activate` command to activate the virtual environment.
   For Windows, use the following command: `.\venv\Scripts\activate`
4. **Run migrations**: Use the `manage.py migrate` command to apply migrations.
5. **Create a superuser**: Use the `manage.py createsuperuser` command to create a superuser for the Django admin
   interface.
6. **Start the services with Docker Compose**: Use the `docker-compose up` command to start your services, including
   Elasticsearch.
7. **Create Elasticsearch index**: `python manage.py search_index --rebuild`

## Endpoints

This API provides the following endpoints:

- `GET /api/v1/posts/`: Retrieve a list of posts. You can provide a query parameter `q` to search for posts. The search
  fields
  include "title", "body", "comments.text", "author.username", and "author.email". The results are sorted by post ID in
  descending order.

- `POST /api/v1/posts/`: Create a new post. You need to provide the post data in the request body. The post is created
  with the
  provided data and the author ID is set to 1. The created post is also updated in the Elasticsearch index.

## Elasticsearch

- To start the Elasticsearch service using Docker Compose, you need to have a `docker-compose.yml` file.
- docker-compose up -d --build 

