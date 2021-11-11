import scanner #librería a utilizar para scannear puertos

# Ejemplo de función básica
ports = scanner.getOpenPorts("tusitio.com")
print("Open ports basic:", ports)
# Determinando Puertos
ports = scanner.getOpenPorts("unam.mx", [79, 82])
print("Open ports range given:", ports)
# Verbosidad
ports = scanner.getOpenPorts("hotmail.con", [], True)
print("Open ports range give + verbose:", ports)
