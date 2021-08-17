


message = 'gux6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?.'


# Loop through every possible key
for key in range(len(SYMBOLS)):
    # It is importan to set translated to the blank string so that the previous itaration's value sor tranlated is cleared:
    translated = ''

    # The rest of the program is almost the same as Caesar program:

    # Loop through each symbol in message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound
            if translatedIndex < 0:
                translatedIndex = symbolIndex + len(SYMBOLS)

            # Append the decrypted symbols:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the sumbol without encrypting/decrypting:
            translated = translated + symbol
        
    # Display every possible decryption:
    print(translated)

