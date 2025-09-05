import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

# Configuración del navegador
options = Options()

# Ruta hacia el archivo ChromeDriver
service = Service('/Users/leacou/Desktop/Facturador Afip/chromedriver-mac-arm64/chromedriver')

# Iniciar el navegador con ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

# Abrir la página de login de AFIP
driver.get('https://auth.afip.gob.ar/contribuyente_/login.xhtml')

try:
    # Proceso de login
    usuario = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'F1:username')))
    usuario.send_keys('27375379355')
    time.sleep(2)

    boton_siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'F1:btnSiguiente')))
    boton_siguiente.click()
    time.sleep(2)

    contraseña = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'F1:password')))
    contraseña.send_keys('Lsff1514:)')
    time.sleep(2)

    boton_siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'F1:btnIngresar')))
    boton_siguiente.click()
    time.sleep(2)

    # Hacer clic en "Comprobantes en línea"
    comprobantes_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h3[contains(text(),"Comprobantes en línea")]'))
    )
    comprobantes_element.click()
    time.sleep(2)

    # Cambiar a la nueva pestaña
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    ventanas = driver.window_handles
    driver.switch_to.window(ventanas[-1])
    time.sleep(2)

    # Hacer clic en "COURETOT LEANDRO JULIAN"
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@value="FERNANDEZ FIGULS LUCIA SOL"]'))
    )
    input_element.click()
    time.sleep(2)

    # Hacer clic en "Generar Comprobantes"
    generar_comprobantes_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="Generar Comprobantes"]'))
    )
    generar_comprobantes_element.click()
    time.sleep(2)

    # Completar el primer formulario
    try:
        select_punto_venta = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'puntoDeVenta'))
        )
        select_punto_venta = Select(select_punto_venta)
        select_punto_venta.select_by_value('1')
        print("Selección de punto de venta exitosa")
        time.sleep(2)
    except Exception as e:
        print("Error al seleccionar el punto de venta:", e)

    try:
        select_universo_comprobante = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'universoComprobante'))
        )
        select_universo_comprobante = Select(select_universo_comprobante)
        select_universo_comprobante.select_by_value('2')
        print("Selección de universo de comprobante exitosa")
        time.sleep(2)
    except Exception as e:
        print("Error al seleccionar el universo de comprobante:", e)

    try:
        boton_continuar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="Continuar >"]'))
        )
        boton_continuar.click()
        print("Clic en 'Continuar' exitoso")
        time.sleep(2)
    except Exception as e:
        print("Error al hacer clic en el botón 'Continuar':", e)

    # **Nuevo formulario datosEmisorForm**
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'datosEmisorForm')))
        
        select_id_concepto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'idConcepto'))
        )
        select_id_concepto = Select(select_id_concepto)
        select_id_concepto.select_by_value('2')
        print("Selección de concepto exitosa")
        time.sleep(2)

        select_acti_asociada = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'actiAsociadaId'))
        )
        select_acti_asociada = Select(select_acti_asociada)
        select_acti_asociada.select_by_value('741000')
        print("Selección de actividad asociada exitosa")
        time.sleep(2)

        boton_continuar_dos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="Continuar >"]'))
        )
        boton_continuar_dos.click()
        print("Clic en 'Continuar' exitoso")
        time.sleep(2)

    except Exception as e:
        print("Error en el nuevo formulario:", e)

    # **Nuevo formulario datosReceptorForm**
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'datosReceptorForm')))
        
        select_id_iva_receptor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'idIVAReceptor'))
        )
        select_id_iva_receptor = Select(select_id_iva_receptor)
        select_id_iva_receptor.select_by_value('5')
        print("Selección de IVA receptor exitosa")
        time.sleep(2)

        checkbox_forma_pago = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'formadepago1'))
        )
        checkbox_forma_pago.click()
        print("Checkbox de forma de pago marcado exitosamente")
        time.sleep(2)

        boton_continuar_tres = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="Continuar >"]'))
        )
        boton_continuar_tres.click()
        print("Clic en 'Continuar' exitoso en datosReceptorForm")
        time.sleep(2)

    except Exception as e:
        print("Error en el formulario de receptor:", e)

    # **Nuevo formulario datosOperacionForm**
    try:
        # Esperar a que el formulario "datosOperacionForm" esté disponible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'datosOperacionForm')))
        
        # Ingresar el código de artículo
        detalle_codigo_articulo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'detalleCodigoArticulo'))
        )
        detalle_codigo_articulo.send_keys("0001")
        print("Código de artículo ingresado exitosamente")
        time.sleep(2)

        # Ingresar la descripción
        detalle_descripcion = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'detalle_descripcion1'))
        )
        detalle_descripcion.send_keys("Servicios Profesionales")
        print("Descripción ingresada exitosamente")
        time.sleep(2)

        # Seleccionar la medida
        select_detalle_medida = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'detalle_medida1'))
        )
        select_detalle_medida = Select(select_detalle_medida)
        select_detalle_medida.select_by_value('7')
        print("Selección de medida exitosa")
        time.sleep(2)

        # Ingresar el precio
        detalle_precio = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'detalle_precio1'))
        )
        detalle_precio.send_keys("90000")
        print("Precio ingresado exitosamente")
        time.sleep(2)

        # Hacer clic en el botón "Continuar"
        boton_continuar_cuatro = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="Continuar >"]'))
        )
        boton_continuar_cuatro.click()
        print("Clic en 'Continuar' exitoso en datosOperacionForm")
        time.sleep(2)

    except Exception as e:
        print("Error en el formulario de operación:", e)
    try:
        # Esperar a que el formulario "datosOperacionForm" esté disponible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'datosReceptorForm')))
        # Hacer clic en el botón "Continuar"
        boton_continuar_cuatro = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="Confirmar Datos..."]'))
        )
        boton_continuar_cuatro.click()
        print("Clic en 'Confirmar Datos.' exitoso en datosReceptorForm")
        time.sleep(2)
    except Exception as e:
        print("Error en el formulario final:", e)
    
    try:
        # Esperar a que aparezca el pop-up (alerta)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        
        # Cambiar el control del navegador al pop-up
        alert = driver.switch_to.alert
        
        # Aceptar el pop-up presionando Enter (o aceptar)
        alert.accept()
        print("Pop-up aceptado y factura emitida exitosamente")
        time.sleep(2)
        
    except Exception as e:
        print("Error al manejar el pop-up:", e)


except Exception as e:
    print("Ocurrió un error:", e)

finally:
    time.sleep(2)  # Pausa de 2 segundos para observar el resultado final
    driver.quit()  # Cerrar el navegador
