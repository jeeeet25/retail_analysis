import configparser
from pyspark import SparkConf

def get_app_config(env):
    config = configparser.ConfigParser()
    config.read("config/app.conf")
    app_conf = {}
    for (key, val) in config.items(env):
        app_conf[key] = val
    return app_conf

def get_pyspark_config(env):
    config = configparser.ConfigParser()
    config.read("config/pyspark.conf")
    pyspark_conf = SparkConf()
    for (key, val) in config.items(env):
        pyspark_conf.set(key, val)
    return pyspark_conf

