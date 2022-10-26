from swagger_client import RemoteServerApi
from swagger_client.rest import ApiException

api_instance = RemoteServerApi()


def screenshot():
    try:
        api_response = api_instance.screenshot()
        with open("screenshot.jpg", "wb") as file:
            file.write(bytearray(map(int, api_response)))

    except ApiException as e:
        print("Exception when calling RemoteServerApi->screenshot: %s\n" % e)


def get_process_list():
    try:
        api_response = api_instance.get_process_list()
        for line in api_response:
            print(line)
    except ApiException as e:
        print(
            "Exception when calling RemoteServerApi->get_process_list: %s\n" %
            e)


def reboot():
    try:
        api_instance.system_reboot()
    except ApiException as e:
        print("Exception when calling RemoteServerApi->system_reboot: %s\n" %
              e)


command_map = {
    'screenshot': screenshot,
    '1': screenshot,
    'processes': get_process_list,
    '2': get_process_list,
    'reboot': reboot,
    '3': reboot,
    'quit': lambda: exit(0),
    '0': lambda: exit(0)
}


def menu():
    print('\n')
    print('<-------- Remote Access Tool -------->')
    print('What command would you like to issue?\n')
    print('1 | screenshot')
    print('2 | processes')
    print('3 | reboot')
    print('0 | quit\n')
    print('Your choice:', end=' ')
    command = input()
    print('\n')
    print('<--------                    -------->')
    return command


if __name__ == '__main__':
    while (True):
        command = menu()
        fun = command_map.get(command.lower(), None)
        if not fun:
            print('\nInvalid Function! Please try again\n')
        else:
            fun()
