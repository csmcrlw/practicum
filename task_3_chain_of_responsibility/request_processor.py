""" Создаем и обрабатываем заявку на отпуск """

from handlers import ManagerHandler, HRHandler, DirectorHandler


class LeaveRequest:
    def __init__(self, employee, days):
        self.employee = employee
        self.days = days


class LeaveRequestProcessor:
    def __init__(self):
        self.manager = ManagerHandler()
        self.hr = HRHandler(successor=self.manager)
        self.director = DirectorHandler(successor=self.hr)

    def process_request(self, request):
        print(f"Processing leave request for {request.employee}...")
        self.director.handle_request(request)
        print("Leave request processing completed.\n")
