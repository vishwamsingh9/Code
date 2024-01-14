import pytest
import pandas as pd
import factory
from main import compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, top_10_customers

class OrderFactory(factory.Factory):
    class Meta:
        model = dict

    order_id = factory.Sequence(lambda n: n)
    customer_id = factory.Faker('random_int', min=100, max=199)
    order_date = factory.Faker('date_between', start_date='-1y', end_date='today')
    product_id = factory.Faker('random_int', min=500, max=599)
    product_name = factory.Faker('word')
    product_price = factory.Faker('random_number', digits=2)
    quantity = factory.Faker('random_int', min=1, max=5)

@pytest.fixture
def sample_data():
    # Generate a list of 100 order dictionaries
    orders = OrderFactory.build_batch(100)
    # Convert the list of dictionaries to a DataFrame
    data = pd.DataFrame(orders)
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['total_price'] = data['product_price'] * data['quantity']
    return data

def test_compute_revenue_by_month(sample_data):
    result = compute_revenue_by_month(sample_data)
    assert not result.empty  # Ensure result is not empty

def test_compute_revenue_by_product(sample_data):
    result = compute_revenue_by_product(sample_data)
    assert not result.empty  # Ensure result is not empty

def test_compute_revenue_by_customer(sample_data):
    result = compute_revenue_by_customer(sample_data)
    assert not result.empty  # Ensure result is not empty

def test_top_10_customers(sample_data):
    result = top_10_customers(sample_data)
    assert len(result) == 10  # Ensure there are exactly 10 customers


