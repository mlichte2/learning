# Build a list of Unicode codepoints from a string, take two
# Uses listcomps

symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]

print(codes)
