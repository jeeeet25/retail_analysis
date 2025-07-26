import pytest
from lib.DataReader import read_customers, read_orders
from lib.DataManipulation import  filter_closed_orders, count_orders_state,filter_orders_generic
#from lib.Utils import get_spark_session
from lib.ConfigReader import get_app_config

#setup code to inject resources (spark session)
# you can create fixtures in a different file and save it to, conftest.py
#@pytest.fixture
#ef spark():
#    return get_spark_session("LOCAL")

@pytest.mark.skip()   
def test_read_customers(spark):
    customers_count = read_customers(spark,"LOCAL").count()
    assert customers_count == 12435

@pytest.mark.skip()   
def test_read_orders(spark):
    orders_count = read_orders(spark,"LOCAL").count()
    assert orders_count == 68884

@pytest.mark.skip()   
def test_filter_closed_orders(spark):
    order_df = read_orders(spark,"LOCAL")
    filter_count = filter_closed_orders(order_df).count()
    assert  filter_count == 7556

@pytest.mark.skip()   
def test_app_config():
    config = get_app_config("LOCAL")
    assert config["orders.file.path"] == "data/orders.csv"
    
@pytest.mark.skip()    
def test_count_orders_state(spark, expected_results):
    customer_df = read_customers(spark,"LOCAL")
    actual_data = count_orders_state(customer_df)
    assert actual_data.collect() == expected_results.collect()


#generic function to count the status == CLOSED   --- 1 
@pytest.mark.skip()    
def test_filter_orders_generic(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_df = filter_orders_generic(orders_df,"CLOSED").count()
    assert filtered_df == 7556

#generic function to count the status == CLOSED   --- 1 
@pytest.mark.skip()    
def test_filter_orders_generic(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_df = filter_orders_generic(orders_df,"COMPLETE").count()
    assert filtered_df == 22900

#parameterized generis funciton to test diffferent status, instead of having different functions -- 1, use this generic to test diff status's
@pytest.mark.parametrize(
        "status,count",
        [("CLOSED",7556),
         ("PENDING_PAYMENT",15030),
         ("COMPLETE",22900)
         ]
)

def test_check_count(spark,status,count):
    orders_df = read_orders(spark,"LOCAL")
    filtered_df = filter_orders_generic(orders_df,status).count()
    assert filtered_df == count


