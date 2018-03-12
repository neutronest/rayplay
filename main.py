import unittest
import ray
#import ray.test.test_functions as test_functions
#import ray.test.test_utils
import time

@ray.remote
def f():
    time.sleep(1)
    return 1

if __name__ == "__main__":
    ray.init()
    results = ray.get([f.remote() for i in range(4)])
    print("results: ", results)
