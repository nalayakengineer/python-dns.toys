from dnslib import DNSRecord, DNSHeader, RR, TXT
from socket import socket, AF_INET, SOCK_DGRAM
import logging
from utils.time_query import handle_time_query
from utils.epoch import current_epoch_time
from utils.base import convert_base
from utils.random_number import random_number

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DNSServer:
    def __init__(self, host='0.0.0.0', port=53):
        self.host = host
        self.port = port
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        self.handlers = {
            'time': handle_time_query,
            'epoch': current_epoch_time,
            'base': convert_base,
            'random': random_number
        }

    def handle_query(self, data, addr):
        request = DNSRecord.parse(data)
        response = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)

        for question in request.questions:
            logging.info(f"Received query for {question.qname} of type {question.qtype} from {addr}")   
            qname_str = str(question.qname).strip('.')
            parts = qname_str.split('.')
            if len(parts) > 1 and parts[-1] in self.handlers:
                handler = self.handlers[parts[-1]]
                txt_response = handler(question.qname)
                response.add_answer(RR(question.qname, rtype=16, rclass=1, ttl=60, rdata=TXT(txt_response)))
            else:
                response.add_answer(RR(question.qname, rtype=16, rclass=1, ttl=60, rdata=TXT("Unknown query")))  
            logging.info(f"response:\n {response}")
        self.socket.sendto(response.pack(), addr)
        logging.info(f"Sent response to {addr}")


    def start(self):
        logging.info(f"DNS Server is running on {self.host}:{self.port}")
        while True:
            data, addr = self.socket.recvfrom(512)
            self.handle_query(data, addr)

if __name__ == "__main__":
    server = DNSServer()
    server.start()