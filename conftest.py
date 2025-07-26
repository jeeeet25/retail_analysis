import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop()


#this ficture will grab the agg_results from a file to test it with the agg results from our fuction
@pytest.fixture 
def expected_results(spark):
    test_schema = "state string,count int"
    return spark.read \
        .format("csv") \
        .schema(test_schema) \
        .load("data/test_agg_data.csv")


