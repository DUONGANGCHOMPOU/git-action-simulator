print("--- Starting Application ---")
print("Hello, World! Python CI/CD is working perfectly.")
print("--- Application Finished ---")


def print_hi(name):
    print(f'Hi, {name}')


def test_print_hi(capsys):
    print_hi('PyCharm')
    captured = capsys.readouterr()
    assert captured.out == "Hi, PyCharm\n"


def test_hello_world():
    message = "Hello, World! Python CI/CD is working perfectly."
    assert "CI/CD" in message
    assert len(message) > 0


if __name__ == '__main__':
    print_hi('PyCharm')