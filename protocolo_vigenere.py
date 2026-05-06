def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Determinar el desplazamiento basado en la clave
            shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'decrypt':
                shift = -shift
            
            # Aplicar el cifrado/descifrado preservando mayúsculas/minúsculas
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            
            key_index += 1
        else:
            result += char  # Mantener espacios y símbolos
            
    return result

if __name__ == "__main__":
    print("=== SUBSISTEMA DE COMUNICACIÓN CIFRADA - NODO M-14 ===")
    
    # El usuario podrá elegir si cifrar un secreto o intentar descifrar uno encontrado
    op = input("\n[1] Cifrar mensaje\n[2] Descifrar mensaje\nSeleccione protocolo: ")
    
    msg = input("Ingrese el mensaje: ")
    clave = input("Ingrese la CLAVE DE ACCESO: ")
    
    if op == '1':
        print("\nMensaje Cifrado: " + vigenere_cipher(msg, clave, 'encrypt'))
    else:
        print("\nMensaje Descifrado: " + vigenere_cipher(msg, clave, 'decrypt'))
