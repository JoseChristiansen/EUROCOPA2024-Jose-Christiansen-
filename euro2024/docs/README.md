IMPORTANTE: antes de iniciar el programa se tienen que descargar las dependencias con este codigo: pip install -r requirements.txt

El programa es un sistema de gestión para la Eurocopa Alemania 2024. El sistema permitirá vender entradas, registrar asistencia, administrar restaurantes y generar estadísticas, funcionalidad que no esta terminada. El programa se compone de seis módulos principales:

    Gestión de partidos y estadios: Administra los equipos, enfrentamientos y estadios, utilizando información de una API externa.
    - Archivos: api_client y models
    Gestión de venta de entradas: Permite a los usuarios comprar entradas para partidos, incluyendo opciones de asiento VIP y descuentos.
    - Archivos: partido_manager y entrada_manager
    Gestión de asistencia a partidos: Verifica la validez de las entradas y registra la asistencia al partido. 
    - Archivo: entrada_manager
    Gestión de restaurantes: Administra el restaurante del estadio, incluyendo la gestión de productos, precios y ventas.
    - Archivo: restaurante_manager
    Gestión de venta de restaurantes: Permite a los usuarios comprar productos en el restaurante.
    - Archivo: restaurante_manager
    Indicadores de gestión (estadísticas): Genera informes con estadísticas sobre la asistencia al partido, las ventas de entradas y productos del restaurante. (Sin terminar.)

El programa está diseñado para ser fácil de usar y proporcionar información precisa y completa a los organizadores de la Eurocopa.