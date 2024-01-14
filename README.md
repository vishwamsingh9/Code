
# Project Title: Online Store Revenue Analysis

## Overview

This project provides a comprehensive analysis of customer orders from an online store. The Python application reads order data, calculates total revenue by month, product, and customer, and identifies the top 10 customers by revenue. The repository includes Docker support for easy deployment and testing.

## Features

- **Data Analysis**: Compute total revenue by month, product, and customer.
- **Customer Insights**: Identify top 10 customers by revenue.
- **Docker Integration**: Dockerize the application for consistency across environments.
- **Automated Testing**: Includes tests for validating functionality.

## Getting Started

### Prerequisites

- Python 3.x
- Docker 
- Pandas library

### Installation

1. **Clone the Repository**

   ```sh
   git clone [https://github.com/vishwamsingh9/Code.git]
   cd [code]
   ```

2. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

- **Directly with Python**

   ```sh
   python src/main.py
   ```

- **Using Docker**

   Build and run the Docker container:

   ```sh
   docker-compose up app
   ```

### Running the Tests

- **Directly with Pytest**

   ```sh
   pytest tests/test_main.py
   ```

- **Using Docker**

   Build and run the test container:

   ```sh
   docker-compose up test
   ```

## Project Structure

```
myapp/
│
├── src/
│   └── main.py              # Main application code
│
├── tests/
│   └── test_main.py         # Tests for your application
│
├── docker/
│   ├── Dockerfile           # Dockerfile for the application
│   └── Dockerfile.test      # Dockerfile for running tests
│
├── data/
│   └── orders.csv           # Dataset file
│
├── .gitignore               # To exclude files/folders from git
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── docker-compose.yml       # Docker Compose configuration file
```

## Documentation

Each module and function in the application is well-documented. For detailed information, refer to the comments and docstrings within the codebase.

