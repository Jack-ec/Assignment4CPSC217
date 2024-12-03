def get_file_names():
    with open("file_names.txt", "r") as file:
        content = file.read()
        print(str(content))
    return content


def read_config(config_file_name):
    with open(config_file_name + ".txt", "r") as file:
        content = file.read()

        order_map = {value: index for index, value in enumerate(READ_CONFIG_VALUE_ORDER)}

