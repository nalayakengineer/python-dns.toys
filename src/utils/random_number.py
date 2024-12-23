import random

def random_number(qname=None):
    #Extract the range from the query
    qname_str = str(qname).strip('.')
    parts = qname_str.split('.')
    if len(parts) < 2 or parts[-1] != 'random':
        return f'Invalid query'
    
    range_str = parts[-2]
    start_str, end_str = range_str.split('-')
    try:
        start = int(start_str)
        end = int(end_str)
        if start >= end:
            return f'Invalid range'
        return f'Random Number b/w {start}-{end} : {random.randint(start, end)}'
    except ValueError:
        return f'Invalid range'