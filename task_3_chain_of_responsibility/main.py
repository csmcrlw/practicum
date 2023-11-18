from request_processor import LeaveRequest, LeaveRequestProcessor


def main():
    # Создаем цепочку обязанностей через LeaveRequestProcessor
    processor = LeaveRequestProcessor()

    # Создаем заявки на отпуск
    request_patrick = LeaveRequest(employee="Patrick Bateman", days=12)
    request_tyler = LeaveRequest(employee="Tyler Durden", days=4)
    request_marla = LeaveRequest(employee="Marla Singer", days=8)

    # Обрабатываем заявки
    processor.process_request(request_patrick)
    processor.process_request(request_tyler)
    processor.process_request(request_marla)


if __name__ == "__main__":
    main()
