def test_add_correct():
    result = 10 + 5
    assert result == 15, f"ОШИБКА: ожидали 15, но получили {result}"

def test_multiple_check():
    number = 10

    assert number > 5, f"ERROR: the count should be greater then 5, we have {number}"
    assert number < 20, f"ERROR: the count should be less then 20, we have {number}"
    assert number != 0, f"ERROR: the count shold be not != 0 "

def test_text_contains():
    message = "Hello, Nastya!"
    # Проверяем, что строка содержит слово
    assert "Nastya" in message, f"ОШИБКА: в сообщении нет имени — message='{message}'"

def test_text_not_contains():
    message = "Hello, world!"
    # Проверяем, что сообщение не содержит плохих слов
    assert "error" not in message, "ОШИБКА: текст содержит запрещённое слово 'error'"

