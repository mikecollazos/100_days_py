import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
  def wrapper_func():
    start_time = time.time()
    func()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"{func.__name__} run time {total_time}")
  return wrapper_func


@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()