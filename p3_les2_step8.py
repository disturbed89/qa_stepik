def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
    except:
        print(f"expected  {expected_result}, got {actual_result}")


test_input_text(8, 9)
