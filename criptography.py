from cryptography.fernet import Fernet

def encrypt(password: str, secret_key:str) ->str:
    
    fernet = Fernet(secret_key)

    # Criptografa
    return fernet.encrypt(password.encode()).decode()

def decrypt(cryptographic_key: str, secret_key:str)->str:

    fernet = Fernet(secret_key)
    # Descriptografa
    return fernet.decrypt(cryptographic_key.encode()).decode()    

def generate_key():

    # Gera a chave corretamente no formato que o Fernet exige
    key = Fernet.generate_key()

    return key.decode()

def main():

    options = int(input("1 - Encypt Pass: 2 - Decrypt Pass: "))

    if options == 1:

        input_password = input("What's is the password for encrypt? ")

        new_secret_key = generate_key()

        encrypt_pass = encrypt(password=input_password, secret_key=new_secret_key)

        print(f" Encrypt pass: {encrypt_pass}\n Secret Key: {new_secret_key}")
    
    elif options == 2:

        input_secret_key = input("What's is the secret key? ")
        input_password = input("What's is the encrypt password? ")

        output_decrypt_pass = decrypt(secret_key= input_secret_key, cryptographic_key= input_password)

        print(f" Decrypt pass: {output_decrypt_pass}")
      


if __name__ == '__main__':
        
    main()