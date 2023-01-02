class ConnectionEntity:
    def __init__(self, connection, toml_config_element):
        self.connection = connection
        self.toml_config_element = toml_config_element
        self.result = None

    def get_result(self):
        return self.result

    def get_name(self):
        return self.toml_config_element.get("name")

    def __str__(self):
        return self.toml_config_element

    def __repr__(self):
        return "ConnectionEntity:"+str(self.toml_config_element)

    def get_command(self):
        return self.toml_config_element.get("command")