![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![mypy](https://img.shields.io/badge/mypy-1A5276?style=for-the-badge&logo=python&logoColor=white)
![schedule](https://img.shields.io/badge/schedule-2ECC71?style=for-the-badge&logo=python&logoColor=white)

# 🛠️ Python Sysadmin Toolkit
> Automatización de tareas de administración de sistemas desde la terminal

Kit de herramientas en Python para sysadmins. Analiza logs SSH, audita dispositivos de red, geolocaliza IPs sospechosas, gestiona inventarios de servidores y genera informes en Excel, todo desde un menú CLI central o ejecutándose de forma programada.

---

## Características

- Menú CLI interactivo desde el que lanzar cualquier herramienta
- Parser de logs SSH que detecta IPs atacantes y cuenta intentos fallidos
- Auditoría de routers y servidores con clases, herencia y polimorfismo
- Geolocalización de IPs sospechosas via ipinfo.io
- Generación y filtrado de inventarios de 1000+ servidores con Pandas
- Exportación de informes a `.xlsx` con tres hojas (vulnerables, por departamento, completo)
- Daemon que ejecuta las tareas principales cada hora con `schedule`

---

## Tecnologías

| Librería | Uso |
|----------|-----|
| Pandas | Carga, filtrado y agrupación del inventario CSV |
| OpenPyXL | Exportación de informes a Excel |
| Requests | Consultas a la API de ipinfo.io |
| Faker | Generación de inventarios ficticios para pruebas |

| Auxiliares | Uso |
|------------|-----|
| pytest | Tests unitarios del parser de logs y el filtro de inventario |
| mypy | Verificación estática de Type Hints |
| schedule | Ejecución periódica como daemon |
| subprocess | Llamadas al sistema operativo (ping, disco) |

---

## Estructura del proyecto

```
sysadmin-toolkit/
├── sys_toolkit.py          # menú CLI y daemon
├── os_utils.py             # ping y espacio en disco
├── log_parser.py           # parser de auth.log
├── network_models.py       # clases Router y Server
├── threat_intel.py         # geolocalización de IPs
├── generate_inventory.py   # genera inventory.csv con Faker
├── inventory_manager.py    # filtros y agrupación con Pandas
├── report_generator.py     # exporta inventario a Excel
├── test_toolkit.py         # tests unitarios
├── auth.log                # log SSH de ejemplo
├── inventory.csv           # inventario generado
├── requirements.txt
└── docs/
    └── python-sysadmin.md
```

---

## Descargar y ejecutar

```bash
git clone https://github.com/troustrider/python-sysadmin-toolkit.git
cd python-sysadmin-toolkit

python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate.bat

pip install -r requirements.txt
python sys_toolkit.py
```

Para ejecutar los tests:

```bash
pytest test_toolkit.py -v
```

---

*Desarrollado durante las prácticas en [Corner Estudios](https://www.corner-estudios.com) — Karim Abatouy — 2026*
