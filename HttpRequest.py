class HttpRequest:
    def __init__(self, name, url, method, headers, body):
        # Initialize private variables in __init__ with default values
        self.__name = None
        self.__url = None
        self.__method = None
        self.__headers = None
        self.__body = None

        # Use setters to apply validation and set actual values
        self.set_name(name)
        self.set_url(url)
        self.set_method(method)
        self.set_headers(headers)
        self.set_body(body)

    def set_name(self, name):
        if name is None or len(name) == 0:
            raise ValueError("The 'name' cannot be None.")
        self.__name = name

    def set_url(self, url):
        if url is None or len(url) == 0:
            raise ValueError("The 'url' cannot be None.")
        self.__url = url

    def set_method(self, method):
        self.__method = method if method else "GET"

    def set_headers(self, headers):
        self.__headers = headers if headers else {}

    def set_body(self, body):
        self.__body = body if body else ""

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def get_method(self):
        return self.__method

    def get_headers(self):
        return self.__headers

    def get_body(self):
        return self.__body
