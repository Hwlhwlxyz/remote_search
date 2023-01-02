from src.remote_search.models import toml_config, remote_connection
from src.remote_search.models.ConnectionEntity import ConnectionEntity


def parse_toml_file():
    config_path = toml_config.find_config_file_path()
    configuration = toml_config.read_toml(config_path)
    server = configuration.get("server")
    proxyjump = configuration.get("proxyjump")
    server_list = []
    proxyjump_list = []
    print("server:")
    for s in server:
        if s is not None:
            server_list.append(ConnectionEntity(remote_connection.get_connection(s), s))
    print("proxyjump")
    for p in proxyjump:
        if p is not None:
            proxyjump_list.append(ConnectionEntity(remote_connection.get_jump_proxy_connection(p), p))
    print(server_list)
    print(proxyjump_list)
    server_list.extend(proxyjump_list)
    return server_list


def execute_commands(connection_list, input_str):
    for connectionEntity in connection_list:
        command = connectionEntity.get_command().format(input_str)
        connectionEntity.result = remote_connection.execute_command(connectionEntity.connection, command)
    return connection_list

def run(input_str):
    connection_list = parse_toml_file()
    connection_list = execute_commands(connection_list, input_str)
    print(connection_list)
    return connection_list