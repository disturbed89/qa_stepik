def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    try:
        assert substring in full_string
    except:
        print(f"expected '{substring}' to be substring of '{full_string}'")

print("Sample 1: ")
test_substring("fulltext", "some_value")
print("Sample 2: ")
test_substring("1", "1")
print("Sample 3: ")
test_substring("some_text", "some")