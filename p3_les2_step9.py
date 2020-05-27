expected_result = "one"
actual_result = "two"
try:
    assert expected_result == actual_result
except:
    print(f"expected  {expected_result}, got {actual_result}")