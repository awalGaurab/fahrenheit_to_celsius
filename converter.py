def converter(fahren):
    converted_value = (fahren - 32)/1.8
    return converted_value

try:
    input_val = float(input("Enter temperature in fahrenheit: "))
    converted_temp = converter(input_val)
    print("{} fahrenheit is equivalent to {} degree celsius value.".format(round(converted_temp,2),input_val))
except Exception:
    print("Please enter integer or float number only.")