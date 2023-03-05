from runLengthEncoding import encoder

term = "AAAAAAAAAAAAABBCCCCDD"

encodedString = encoder(term)

print(encodedString)

if (encodedString != "9A4A2B4C2D"):
    print("ERRADO")
else:
    print("CORRETO")
