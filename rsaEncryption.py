import math
import sys
from millersTest import isPrimeMonteCarlo


class RSA:

    def __init__(self):
        self.alphabet1 = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet2 = (
            ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        )

    def GenerateKeys(self, str1, str2):
        p = self.textIntoBase10(self.alphabet1, str1)
        q = self.textIntoBase10(self.alphabet1, str2)

        # Verify length >= 10^200
        limit = 10**200
        if p < limit or q < limit:
            print("Error: Input strings are too short.")
            sys.exit(1)

        p = p % limit
        q = q % limit

        p = self.nextPrime(p)
        q = self.nextPrime(q)

        if p == q:
            q = self.nextPrime(q + 2)

        n = p * q
        r = (p - 1) * (q - 1)
        e = 10**398 + 1
        while math.gcd(e, r) != 1:
            e += 2

        # Modular inverse
        d = pow(e, -1, r)

        # Save keys to public.txt and private.txt
        with open("public.txt", "w", encoding="utf-8") as file:
            file.write(f"{n}\n{e}\n")

        with open("private.txt", "w", encoding="utf-8") as file:
            file.write(f"{n}\n{d}\n")

    def textIntoBase10(self, lettersList, text):
        base = len(lettersList)
        retNum = 0
        for char in text:
            if char not in lettersList:
                raise ValueError(f"Character {repr(char)} is not in alphabet!")
            retNum = retNum * base + lettersList.index(char)
        return retNum

    def base10IntoText(self, lettersList, num):
        if num == 0:
            return lettersList[0]
        base = len(lettersList)
        chars = []
        while num > 0:
            letter = num % base
            chars.append(lettersList[letter])
            num = num // base
        return "".join(reversed(chars))

    def isPrime(self, num):
        return isPrimeMonteCarlo(num)

    def nextPrime(self, num):
        if num % 2 == 0:
            num += 1
        while not self.isPrime(num):
            num += 2
        return num

    def Encrypt(self, inputfile, outputfile):
        with open("public.txt", "r", encoding="utf-8") as file:
            n = int(file.readline().strip())
            e = int(file.readline().strip())

        with open(inputfile, "rb") as fin:
            PlainTextBinary = fin.read()
            PlainText = PlainTextBinary.decode("utf-8")

        block_size = 216
        encrypted_blocks = []

        for i in range(0, len(PlainText), block_size):
            block = PlainText[i : i + block_size]
            m = self.textIntoBase10(self.alphabet2, block)

            c = pow(m, e, n)

            cipher_block = self.base10IntoText(self.alphabet2, c)
            encrypted_blocks.append(cipher_block + "$")

        stringMessage = "".join(encrypted_blocks)

        with open(outputfile, "wb") as fout:
            fout.write(stringMessage.encode("utf-8"))

    def Decrypt(self, inputfile, outputfile):
        with open("private.txt", "r", encoding="utf-8") as file:
            n = int(file.readline().strip())
            d = int(file.readline().strip())

        with open(inputfile, "rb") as fin:
            CipherTextBinary = fin.read()
            CipherText = CipherTextBinary.decode("utf-8")

        # everything after the last $ is not a block (e.g. a trailing newline)
        blocks = CipherText.split("$")[:-1]

        decrypted_blocks = []
        for cipher_block in blocks:
            c = self.textIntoBase10(self.alphabet2, cipher_block)

            m = pow(c, d, n)

            plain_block = self.base10IntoText(self.alphabet2, m)
            decrypted_blocks.append(plain_block)

        stringMessage = "".join(decrypted_blocks)

        with open(outputfile, "wb") as fout:
            fout.write(stringMessage.encode("utf-8"))


def main():
    rsa = RSA()
    testSecretString = (
        "helloandwelcometomytestwherewelearnhowtoprogramrsaanditskindacoollikeitscrazythatpeoplehavefiguredthisoutlikegoodforushahabutimissmyfianceihatedoinglongdistandbrolikewhatamievendoingpleasecomeandhelpme"
    )
    secretString2 = (
        "anothercompletelydifferentandequallylongsecretpassphraseforthesecondtwohundreddigitprimenumbertoensurestrongsecurityandproperencryptionblocksandmoretext"
    )

    print("\nCurrently making the 200-digit prime numbers...")
    rsa.GenerateKeys(testSecretString, secretString2)
    print("Keys are now saved in public.txt and private.txt")

    sample_paragraph = (
        "Hello World! This is a test of our custom RSA encryption and decryption system.\n"
        "We are verifying that multiblock encoding works cleanly across newlines,\ttabs, "
        "punctuation marks like periods, commas, question marks?, and exclamation points! "
        "Numbers 0123456789 and uppercase and lowercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        "abcdefghijklmnopqrstuvwxyz are all included in the 70 character alphabet.\r\n"
    )

    original_message = sample_paragraph * 4

    with open("plaintext.txt", "wb") as file:
        file.write(original_message.encode("utf-8"))

    print(f"Created plaintext.txt ({len(original_message)} characters).")

    rsa.Encrypt("plaintext.txt", "encrypted.txt")
    print("Encrypted plaintext.txt -> encrypted.txt")

    rsa.Decrypt("encrypted.txt", "decrypted.txt")
    print("Decrypted encrypted.txt -> decrypted.txt")

    with open("plaintext.txt", "rb") as f1, open("decrypted.txt", "rb") as f2:
        orig_bytes = f1.read()
        dec_bytes = f2.read()

    if orig_bytes == dec_bytes:
        print("SUCCESS: decrypted.txt matches plaintext.txt byte-for-byte!")
    else:
        print("FAILURE: Mismatch between original and decrypted files.")


if __name__ == "__main__":
    main()

