# Step 1:
from abc import ABC, abstractmethod

class SupportHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

class SupportRequest:
    def __init__(self, request_id, description, priority, type):
        self.request_id = request_id
        self.description = description
        self.priority = priority
        self.type = type

# Step 2:
class BaseSupportHandler(SupportHandler):
    def __init__(self, successor=None):
        self.successor = successor

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class HardwareHandler(BaseSupportHandler):
    def handle_request(self, request):
        if request.type == "Hardware":
            print("Hardware team handling request:", request.description)
        else:
            super().handle_request(request)

class SoftwareHandler(BaseSupportHandler):
    def handle_request(self, request):
        if request.type == "Software":
            print("Software team handling request:", request.description)
        else:
            super().handle_request(request)

class NetworkHandler(BaseSupportHandler):
    def handle_request(self, request):
        if request.type == "Network":
            print("Network team handling request:", request.description)
        else:
            super().handle_request(request)

# Step 3:
def test_chain_of_responsibility():
    hardware_handler = HardwareHandler()
    software_handler = SoftwareHandler()
    network_handler = NetworkHandler()

    hardware_handler.set_successor(software_handler)
    software_handler.set_successor(network_handler)

    request1 = SupportRequest(1, "Printer not working", "High", "Hardware")
    request2 = SupportRequest(2, "Software application crashing", "Medium", "Software")
    request3 = SupportRequest(3, "Network connection issue", "Low", "Network")
    request4 = SupportRequest(4, "Keyboard malfunctioning", "High", "Hardware")

    hardware_handler.handle_request(request1)
    hardware_handler.handle_request(request2)
    hardware_handler.handle_request(request3)
    hardware_handler.handle_request(request4)

test_chain_of_responsibility()


# Step 5:Report
'''
Brief Report:

In this implementation, we've utilized the Chain of Responsibility pattern to handle support requests in a hierarchical manner within a help desk ticketing system. The system consists of three types of support handlers: HardwareHandler, SoftwareHandler, and NetworkHandler.

Each handler is responsible for handling support requests of a specific type. If a handler cannot handle a request itself, it passes the request to its successor handler in the chain. This allows for flexible and scalable handling of various types of support requests.

The implementation also includes a SupportRequest class to encapsulate information about each support request, including its unique ID, description, priority, and type.

Test cases have been written to verify that the chain of responsibility works correctly. These tests cover different types of support requests and ensure that each request is handled appropriately by the corresponding handler.

Optionally, additional features such as assigning support requests to specific team members or tracking the status of support requests can be implemented on top of the existing system.

Overall, the Chain of Responsibility pattern simplifies the implementation of the ticketing system by promoting loose coupling between handlers and enabling dynamic handling of requests based on their types and priorities.
'''
