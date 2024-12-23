import time

def current_epoch_time(qname_str=None):
    #parse the qname to get the query type.
    qname_str = str(qname_str).strip('.')
    query = qname_str.split('.')[-2]
    print(query)
    if query =='now':
        return str(int(time.time())) 
    else: 
        converted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(query)))
        return f'converted epoch time: {converted_time}'
