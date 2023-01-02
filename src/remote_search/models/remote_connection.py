from fabric import Connection




def get_connection(toml_element):
    host = toml_element['host']
    port = toml_element['port']
    password = toml_element['password']
    c = Connection(host, port=port, connect_kwargs={"password": password})
    return c

def jump_proxy_array_connect(toml_element_list):
    c = get_connection(toml_element_list[0])
    for t in toml_element_list[1:]:
        print(t)
        host = t['host']
        port = t['port']
        password = t['password']
        c = Connection(host, port=port, gateway=c, connect_kwargs={"password": password})
    return c

def get_jump_proxy_connection(toml_jump_list):
    # c = Connection('root@193.29.63.239', gateway=Connection('root@198.98.48.47', connect_kwargs={"password": "c9w6WmiryhfoTJx"} ), connect_kwargs={"password":"S6JeQ38yzSns6O50dG"} )
    c = jump_proxy_array_connect(toml_jump_list.get('server'))
    return c



def execute_command(connection, command):
    result = connection.run(command, hide=True).stdout
    return result
