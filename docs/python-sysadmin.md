# Python para sysadmins

## Por qué Python además de Bash

Un sysadmin que solo sabe Bash llega hasta donde llega Bash. Python entra cuando
necesitas parsear JSON o CSV, consumir una API, procesar miles de filas de datos,
o escribir tests que verifiquen que tu script no se rompe.

## POO aplicada a inventarios de red

Al principio parece que las clases son complicar algo que podría ser un diccionario.
Pero cuando tienes 50 dispositivos de tipos distintos, la diferencia se nota.

En este proyecto hay tres clases: `NetworkDevice` es la base, con los atributos que
tienen todos los dispositivos (hostname, IP, MAC). `Router` y `Server` heredan de ella
y añaden lo suyo: el protocolo de enrutamiento en el caso del router, el sistema
operativo y la RAM en el caso del servidor.

La parte útil es el método `audit_device()`. Cada clase lo implementa a su manera.
Si tienes una lista con routers y servidores mezclados y llamas a `audit_device()` en
cada uno, Python sabe automáticamente qué versión del método ejecutar según el tipo
del objeto. Eso es polimorfismo: mismo nombre de método, comportamiento distinto según
la clase. Sin clases tendrías que usar `if tipo == "router"` en cada sitio, y eso
escala fatal.

## Salida de pytest

```
================================================= test session starts =================================================
platform win32 -- Python 3.14.5, pytest-9.0.3
collected 2 items

test_toolkit.py::test_parse_auth_log_counts PASSED                                                               [ 50%]
test_toolkit.py::test_filter_vulnerable_windows PASSED                                                           [100%]

================================================== 2 passed in 2.36s ==================================================
```

`test_parse_auth_log_counts` verifica que el parser de logs detecta correctamente las
IPs atacantes, su conteo de intentos fallidos y que los logins exitosos no se cuelan
en los resultados.

`test_filter_vulnerable_windows` verifica que el filtro de inventario identifica bien
los servidores Windows y los que tienen poca RAM, sin marcar como vulnerables los que
están bien configurados.