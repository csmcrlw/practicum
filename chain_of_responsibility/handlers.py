""" Обработчики для разных заявок """


class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class ManagerHandler(Handler):
    def handle_request(self, request):
        if request.days <= 5:
            print(f"Manager approved leave for {request.employee}")
        elif self.successor:
            self.successor.handle_request(request)


class HRHandler(Handler):
    def handle_request(self, request):
        if 5 < request.days <= 10:
            print(f"HR approved leave for {request.employee}")
        elif self.successor:
            self.successor.handle_request(request)


class DirectorHandler(Handler):
    def handle_request(self, request):
        if request.days > 10:
            print(f"Director approved leave for {request.employee}")
        elif self.successor:
            self.successor.handle_request(request)
