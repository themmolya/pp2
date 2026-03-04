import re

# 1. 'a' followed by zero or more 'b'
def task1(s):
    pattern = r"ab*"
    return re.findall(pattern, s)


# 2. 'a' followed by 2-3 'b'
def task2(s):
    pattern = r"ab{2,3}"
    return re.findall(pattern, s)


# 3. lowercase letters joined with underscore
def task3(s):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, s)


# 4. One uppercase followed by lowercase letters
def task4(s):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, s)


# 5. 'a' followed by anything ending in 'b'
def task5(s):
    pattern = r"a.*b"
    return re.findall(pattern, s)


# 6. Replace space, comma, dot with colon
def task6(s):
    pattern = r"[ ,.]"
    return re.sub(pattern, ":", s)


# 7. snake_case → camelCase
def snake_to_camel(s):
    parts = s.split("_")
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


# 8. split string at uppercase letters
def split_uppercase(s):
    pattern = r"[A-Z][^A-Z]*"
    return re.findall(pattern, s)


# 9. insert spaces before capital letters
def insert_spaces(s):
    pattern = r"([A-Z])"
    return re.sub(pattern, r" \1", s).strip()


# 10. camelCase → snake_case
def camel_to_snake(s):
    pattern = r"([A-Z])"
    return re.sub(pattern, r"_\1", s).lower()


# Example test
if __name__ == "__main__":
    print(task1("ab abb abbb a"))
    print(task2("ab abb abbb abbbb"))
    print(task3("hello_world test_case"))
    print(task4("Hello World Test"))
    print(task5("a123b axxb"))
    print(task6("Hello, world. Test string"))
    print(snake_to_camel("hello_world_example"))
    print(split_uppercase("HelloWorldTest"))
    print(insert_spaces("HelloWorldTest"))
    print(camel_to_snake("helloWorldTest"))