import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Nota: Los usuarios necesitarán instalar 'pycryptodome' para usar esto
# pip install pycryptodome

class CipherM14:
    def __init__(self, key):
        # Usamos SHA-256 para asegurar que la clave tenga la longitud correcta (32 bytes)
        self.key = hashlib.sha256(key.encode()).digest()
        self.mode = AES.MODE_CBC

    def encrypt(self, raw_text):
        cipher = AES.new(self.key, self.mode)
        # El IV (Vector de Inicialización) es necesario para el modo CBC
        iv = cipher.iv
        encrypted_bytes = cipher.encrypt(pad(raw_text.encode(), AES.block_size))
        # Combinamos el IV con el mensaje cifrado y lo pasamos a Base64
        return base64.b64encode(iv + encrypted_bytes).decode('utf-8')

    def decrypt(self, encrypted_text):
        data = base64.b64decode(encrypted_text)
        iv = data[:AES.block_size]
        encrypted_bytes = data[AES.block_size:]
        cipher = AES.new(self.key, self.mode, iv)
        return unpad(cipher.decrypt(encrypted_bytes), AES.block_size).decode('utf-8')

if __name__ == "__main__":
    print("=== SUBSISTEMA DE ENCRIPTACIÓN AES-256 - NODO M-14 ===")
    access_key = input("\n[!] Ingrese CLAVE DE ACCESO MAESTRA: ")
    cipher_tool = CipherM14(access_key)

    choice = input("\n[1] Encriptar documento\n[2] Desencriptar documento\nSeleccione: ")
    
    if choice == '1':
        text = input("Ingrese el contenido del documento: ")
        print("\n[ARCHIVO ENCRIPTADO]:\n" + cipher_tool.encrypt(text))
    elif choice == '2':
        text = input("Ingrese el bloque de datos encriptados: ")
        try:
            print("\n[CONTENIDO RECUPERADO]:\n" + cipher_tool.decrypt(text))
        except:
            print("\n[ERROR]: Clave incorrecta o integridad de datos comprometida.")
