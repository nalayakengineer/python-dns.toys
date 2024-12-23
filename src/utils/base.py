BASE_MAPPING ={
    'bin': 2,
    'oct': 8,
    'dec': 10,
    'hex': 16,
}

def convert_base(qname):
    # Extract the number and base conversion details from the query
    qname_str = str(qname).strip('.')
    parts = qname_str.split('.')
    if  parts[-1] != 'base' or len(parts) <2:
        return "failing here --> Invalid query"

    try:
        number_str = parts[-2]
        number, source_base, target_base = number_str.split('-')
        source_base = source_base.lower()
        target_base = target_base.lower()
        source_base = BASE_MAPPING.get(source_base, source_base)
        target_base = BASE_MAPPING.get(target_base, target_base)
        decimal_value = int(number, source_base)
        # Then, convert the decimal value to the desired base
        if target_base == 2:
            result = bin(decimal_value)[2:]  # Remove '0b' prefix
        elif target_base == 8:
            result = oct(decimal_value)[2:]  # Remove '0o' prefix
        elif target_base == 16:
            result =  hex(decimal_value)[2:]  # Remove '0x' prefix
        elif target_base == 10:
            result = str(decimal_value)
        else:
            return f"Unsupported base: {target_base}"
        return f"Number in base {target_base}: {result or '0'}"
    except ValueError:
        return "Invalid number or base"