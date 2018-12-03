from xmlrpc.server import SimpleXMLRPCServer


class CalcService:
    def add(self, a, b):
        return a+b


def main():
    server_address = ('localhost', 10000)
    server
