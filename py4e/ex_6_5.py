text = "X-DSPAM-Confidence:    0.8475"

number_pos = text.find(":")
number = text[number_pos + 1:]
number = number.strip()
number = float(number)
print(number)
