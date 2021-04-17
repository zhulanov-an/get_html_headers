import random

LOCALHOST = "127.0.0.1"
BEGIN_PORT = 20000
END_PORT = 30000


def get_host_random_port():
    host_port = (LOCALHOST, random.randint(20000, 30000))
    return host_port
