# Facturador Electrónico AFIP - Automatización con Selenium

Este proyecto automatiza la generación de facturas electrónicas en el portal de AFIP (Argentina) utilizando Selenium y Python. Es ideal como prueba técnica para puestos de **AI Ops & Automation**, ya que demuestra habilidades de scripting, automatización de procesos repetitivos y buenas prácticas DevOps.

---

## 🚀 Descripción

El script realiza las siguientes tareas de forma automática:

1. Abre el navegador y accede al login de AFIP.
2. Realiza el ingreso con credenciales.
3. Navega por los menús hasta "Comprobantes en línea".
4. Selecciona el contribuyente y punto de venta.
5. Completa los formularios requeridos:
    - Punto de venta
    - Universo de comprobante
    - Concepto y actividad asociada
    - IVA receptor y forma de pago
    - Código de artículo, descripción, medida y precio
6. Confirma la operación y emite la factura.
7. Gestiona pop-ups y alertas.
8. Cierra el navegador automáticamente al finalizar.

---

## 🧑‍💻 Tecnologías utilizadas

- **Python 3.x**
- **Selenium**
- **ChromeDriver**
- **Visual Studio Code** (desarrollo/testeo)
- MacOS (compatible)

---

## 📦 Instalación y configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/Leacou/facturador-afip-aiops.git
cd facturador-afip-aiops
```

### 2. Instala las dependencias

```bash
python3 -m venv venv
source venv/bin/activate
pip install selenium
```

### 3. Descarga ChromeDriver

- Ve a [descargas de ChromeDriver](https://chromedriver.chromium.org/downloads).
- Elige la versión compatible con tu navegador Chrome y tu Mac (Apple Silicon: `chromedriver-mac-arm64`).
- Coloca el archivo en la ruta indicada en el script:  
  `/Users/leacou/Desktop/Facturador Afip/chromedriver-mac-arm64/chromedriver`  
  *(O ajusta la ruta en el código si lo pones en otro lugar)*

---

## ⚙️ Ejecución

Abre Visual Studio Code, navega a la carpeta del proyecto y ejecuta:

```bash
python facturador_afip.py
```

*(Asegúrate de tener el entorno virtual activado y los permisos necesarios)*

---

## 🔐 Seguridad

> **¡Importante!**  
> No incluyas credenciales reales en el código si vas a compartir el proyecto.  
> Usa variables de entorno o archivos `.env` para almacenar datos sensibles (usuario y contraseña).

---

## 🛠️ Automatización y AI Ops

- El script automatiza procesos manuales, reduciendo errores humanos y ahorrando tiempo.
- Puedes integrarlo en pipelines CI/CD o ejecutarlo como parte de tareas programadas (cron jobs).
- Ejemplo de monitoreo: logs por consola y manejo de excepciones.
- Prueba fácil de modificar para diferentes usuarios, actividades o productos.

---

## 📄 Prueba técnica - ¿Qué demuestra este proyecto?

- **Scripting** avanzado en Python (automatización de browser).
- **Manejo de excepciones** y flujos complejos.
- Uso de **Selenium** para interactuar con formularios web.
- Buenas prácticas de organización y documentación.
- Adaptabilidad a diferentes escenarios de automatización.

---

## 🏷️ Estructura de archivos

```text
/
├── facturador_afip.py      # Script principal de automatización
├── README.md               # Documentación del proyecto
├── chromedriver-mac-arm64/ # Driver de Chrome (no se sube por licencia)
└── venv/                   # Entorno virtual Python (excluido en GitHub)
```

---

## 💡 Mejoras y recomendaciones

- Usar variables de entorno para credenciales.
- Añadir logs a archivo para monitoreo externo.
- Integrar con sistemas de notificaciones (Slack, email).
- Crear un workflow de GitHub Actions para pruebas automáticas.

---

## 📬 Contacto

Leandro Couretot  
[GitHub Profile](https://github.com/Leacou)  
