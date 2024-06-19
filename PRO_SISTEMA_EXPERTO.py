import pygame
import sys

pygame.init()

# Colores-----------------------------------------------------------------------------------------------------------------------------------------------------
GRIS = (200, 200, 200)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)

# Tamaño de la ventana-----------------------------------------------------------------------------------------------------------------------------------------------------
ANCHO = 1250
ALTO = 740

# Inicializar la ventana-----------------------------------------------------------------------------------------------------------------------------------------------------
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sistema Experto")

# Cargar la imagen de fondo-----------------------------------------------------------------------------------------------------------------------------------------------------
fondo = pygame.image.load("Fondo_Sistema.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
fondo_categorias = pygame.image.load("Fondo_Categorias.png")
fondo_categorias = pygame.transform.scale(fondo_categorias, (ANCHO, ALTO))
fondo_matrix = pygame.image.load("Fondo_Matrix.png")
fondo_matrix = pygame.transform.scale(fondo_matrix, (ANCHO, ALTO))
fondo_aseptic = pygame.image.load("Fondo_Aseptic.png")
fondo_aseptic = pygame.transform.scale(fondo_aseptic, (ANCHO, ALTO))
fondo_evo = pygame.image.load("Fondo_Evo.png")
fondo_evo = pygame.transform.scale(fondo_evo, (ANCHO, ALTO))
fondo_cermex = pygame.image.load("Fondo_Cermex.png")
fondo_cermex = pygame.transform.scale(fondo_cermex, (ANCHO, ALTO))
fondo_super = pygame.image.load("Fondo_Super.png")
fondo_super = pygame.transform.scale(fondo_super, (ANCHO, ALTO))

# Definir estados-----------------------------------------------------------------------------------------------------------------------------------------------------
ESTADO_INICIO = 1
ESTADO_MENU_PRINCIPAL = 2
ESTADO_MATRIX = 3
ESTADO_PREDIS = 4
ESTADO_EVO = 5
ESTADO_SUPER = 6
ESTADO_CERMEX = 7
ESTADO_ERROR = 8

# Estado inicial-----------------------------------------------------------------------------------------------------------------------------------------------------
estado_actual = ESTADO_INICIO

# Crear el TextArea-----------------------------------------------------------------------------------------------------------------------------------------------------
TEXTAREA_ANCHO = 624
TEXTAREA_ALTO = 490
input_box = pygame.Rect(465, 250, 300, 40)
text_area_rect = pygame.Rect(565, 210, 624, 490)
#Scroll TextArea-----------------------------------------------------------------------------------------------------------------------------------------------------
def draw_scrollbar(surface, scroll_y, textarea_rect, text_lines, font):
    total_content_height = len(text_lines) * font.get_linesize()
    visible_area_height = textarea_rect.height
    scrollbar_height = min(1, visible_area_height / total_content_height) * visible_area_height
    scrollbar_y = (scroll_y / total_content_height) * (visible_area_height - scrollbar_height)
    pygame.draw.rect(surface, (100, 100, 100), (textarea_rect.right + 5, textarea_rect.top, 10, textarea_rect.height))
    pygame.draw.rect(surface, (150, 150, 150), (textarea_rect.right + 5, textarea_rect.top + scrollbar_y, 10, scrollbar_height))
# Fuente-----------------------------------------------------------------------------------------------------------------------------------------------------
fuente = pygame.font.SysFont("Arial", 27)
fuente1 = pygame.font.SysFont("Arial", 22)
botones = pygame.font.SysFont("Arial", 20)
font = pygame.font.SysFont("Arial", 22)

# Preguntas-----------------------------------------------------------------------------------------------------------------------------------------------------
PregInicial = fuente1.render("¿Estas Listo para Empezar El Diagnostico?", True, NEGRO) 
PregConvensar = fuente1.render("PRESIONA SI PARA COMENZAR!!", True, ROJO) 

Preg1 = fuente1.render("¿Las Botellas Estan Mal Formadas?", True, NEGRO)                                 #Soplado
Preg2 = fuente1.render("¿Las Botellas Tienen Defectos de Superficie?", True, NEGRO)

Preg3 = fuente1.render("¿El Volumen del Producto Esta Sobrellenado?", True, NEGRO)                       #Llenado 

Preg4 = fuente1.render("¿Los Tapones estan Mal Colocados?", True, NEGRO)                                 #Taponado 
Preg5 = fuente1.render("¿Las Botellas Presentan Jugas en el area del Tapon?", True, NEGRO) 

Preg6 = fuente1.render("¿Las Botellas se Llegan a Atascar en la Linea de Produccion ?", True, NEGRO)     #Sistema_transporte
Preg7 = fuente1.render("¿Las Botellas se dañan durante el transporte?", True, NEGRO) 

Preg8 = fuente1.render("¿Las Pantallas y Paneles de Instrumentacion Responden?", True, NEGRO)            #Instrumentos_instrumentacion

Preg9 = fuente1.render("¿Aumento el Incremento de Paradas en la Linea de Produccion?", True, NEGRO)      #Mantenimiento_insuficiente
Preg10 = fuente1.render("¿Disminuyo el Rendimmiento de la Maquina?", True, NEGRO) 

Preg11 = fuente1.render("¿Se Encuntra Contaminados los Productos al ser Terminados?", True, NEGRO)       #Esterilizacion 

Preg12 = fuente1.render("¿Las Botellas Inconsistencias en el Grosor?", True, NEGRO)                      #Deformacion

Preg13 = fuente1.render("¿El Tiempo de Soplado aumento?", True, NEGRO)                                   #Precalentamiento

Preg14 = fuente1.render("¿Aumento el Consumo de Energia?", True, NEGRO)                                  #Eficiencia_Energetica

Preg15 = fuente1.render("¿Alimentación inconsistente de productos a la máquina?", True, NEGRO)           #Ingreso_Productos

Preg16 = fuente1.render("¿El Empaque esta Defectuoso?", True, NEGRO)                                     #Sistema_Empaque

Preg17 = fuente1.render("¿La Etiqueta esta Desalineada o Incorrecta?", True, NEGRO)                      #Etiquetado
Preg18 = fuente1.render("¿Faltan Etiquetas en los Productos?", True, NEGRO)

PregFinal = fuente1.render("¿Deseas Obtener Solucion Respecto al Diagnostico?", True, NEGRO)  

ResSI = fuente1.render("-> Excelente, Observa el TextArea a tu Derecha ->", True, NEGRO)
ResSi = fuente1.render("¿Te Gustaria Saber las Causas de las Fallas?", True, ROJO)
ResS = fuente1.render("PRESIONA REINICIAR PARA EMPEZAR DE NUEVO!!", True, ROJO)
ResNO = fuente1.render("Okey, PRESIONA REINICIAR PARA EMPEZAR DE NUEVO!!", True, ROJO)
# Crear los botones-----------------------------------------------------------------------------------------------------------------------------------------------------
boton_inicio_rect = pygame.Rect(520, 350, 190, 37)
boton_matrix = pygame.Rect(155, 410, 60, 30)
boton_predis = pygame.Rect(600, 410, 60, 30)
boton_evo = pygame.Rect(1050, 410, 60, 30)
boton_cermex = pygame.Rect(155, 680, 60, 30)
boton_super = pygame.Rect(1050, 680, 60, 30)
boton_atras = pygame.Rect(80, 110, 60, 30)
boton_reiniciar = pygame.Rect(110, 410, 75, 30)
boton_si = pygame.Rect(210, 410, 60, 30)
boton_no = pygame.Rect(295, 410, 60, 30)
boton_ok = pygame.Rect(520, 350, 190, 37)

# Fuente y texto del botón-----------------------------------------------------------------------------------------------------------------------------------------------------
entrar = botones.render(" Entrar", True, BLANCO)
texto_matrix_rect = entrar.get_rect(center=boton_matrix.center)
texto_predis_rect = entrar.get_rect(center=boton_predis.center)
texto_evo_rect = entrar.get_rect(center=boton_evo.center)
texto_super_rect = entrar.get_rect(center=boton_super.center)
texto_cermex_rect = entrar.get_rect(center=boton_cermex.center)
atras = botones.render("< Atras", True, BLANCO)
texto_atras_rect = atras.get_rect(center=boton_atras.center)
reiniciar = botones.render("Reiniciar", True, BLANCO)
texto_reiniciar_rect = reiniciar.get_rect(center=boton_reiniciar.center)
si = botones.render("SI", True, BLANCO)
texto_si_rect = si.get_rect(center=boton_si.center)
no = botones.render("NO", True, BLANCO)
texto_no_rect = no.get_rect(center=boton_no.center)
ok = botones.render("OK", True, BLANCO)
texto_ok_rect = ok.get_rect(center=boton_ok.center)

# Texto ingresado por el usuario-----------------------------------------------------------------------------------------------------------------------------------------------------
texto_ingresado = ""
texto_activo = False
usuario = "Ruben Dios"

#Funcion Preguntas\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Preguntas(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI):
    #Preguntas------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if PI:
        ventana.blit(PregInicial, (60, 260))
        ventana.blit(PregConvensar, (90, 310))
    elif P1:
        ventana.blit(Preg1, (90, 260))
    elif P2:
        ventana.blit(Preg2, (50, 260))
    elif P3:
        ventana.blit(Preg3, (50, 260))
    elif P4:
        ventana.blit(Preg4, (80, 260))
    elif P5:
        ventana.blit(Preg5, (35, 260))
    elif P6:
        ventana.blit(Preg6, (25, 260))
    elif P7:
        ventana.blit(Preg7, (50, 260))
    elif P8:
        ventana.blit(Preg8, (25, 260))
    elif P9:
        ventana.blit(Preg9, (10, 260))
    elif P10:
        ventana.blit(Preg10, (50, 260))
    elif P11:
        ventana.blit(Preg11, (25, 260))
    elif P12:
        ventana.blit(Preg12, (65, 260))
    elif P13:
        ventana.blit(Preg13, (90, 260))
    elif P14:
        ventana.blit(Preg14, (90, 260))
    elif P15:
        ventana.blit(Preg15, (25, 260))
    elif P16:
        ventana.blit(Preg16, (100, 260))
    elif P17:
        ventana.blit(Preg17, (60, 260))
    elif P18:
        ventana.blit(Preg18, (90, 260))
    elif PF:
        ventana.blit(PregFinal, (40, 260))
    elif RS:
        ventana.blit(ResSI, (40, 260))
        ventana.blit(ResS, (30, 310))
    elif RN:
        ventana.blit(ResNO, (30, 260))
    elif RSI and not RS:
        ventana.blit(ResSI, (40, 260))
        ventana.blit(ResSi, (50, 310))
#Mostrar error\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_error():
    ventana.fill(GRIS)
    ventana.blit(fondo, (0, 0))
    bien = fuente.render("Bienvenido al Sistema Experto de Sidel", True, NEGRO)
    intro = fuente.render("Diagnóstico de fallas comunes en máquinas de Sidel", True, NEGRO)
    texto_boton = botones.render("OK", True, BLANCO)
    if texto_ingresado.strip() == "":
        error_mensaje = fuente.render("Error: No se ha ingresado texto en el área requerida.", True, ROJO)
    else:
        error_mensaje = fuente.render("Error: Usuario no Registrado, Favor de Verificar.", True, ROJO)
    ventana.blit(bien, (420, 125))
    ventana.blit(intro, (370, 170))
    ventana.blit(error_mensaje, (380, 250))
    pygame.draw.rect(ventana, NEGRO, boton_ok)
    texto_boton_rect = texto_boton.get_rect(center=boton_ok.center)
    ventana.blit(texto_boton, texto_boton_rect.topleft)
#Fundion de Ventana Principal\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_inicio():
    ventana.fill(GRIS)
    ventana.blit(fondo, (0, 0))
    bien = fuente.render("Bienvenido al Sistema Experto de Sidel", True, NEGRO)
    intro = fuente.render("Diagnóstico de fallas comunes en máquinas de Sidel", True, NEGRO)
    Text = fuente1.render("Ingresar Usuario:", True, ROJO,)
    texto_boton = botones.render("Iniciar Sesión", True, BLANCO)
    ventana.blit(bien, (420, 125))
    ventana.blit(intro, (370, 170))
    ventana.blit(Text, (460, 220))
    # Dibujar Textarea y boton-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, BLANCO, input_box)
    pygame.draw.rect(ventana, NEGRO, boton_inicio_rect)
    texto_boton_rect = texto_boton.get_rect(center=boton_inicio_rect.center)
    ventana.blit(texto_boton, texto_boton_rect.topleft)
    # Dibujar el texto ingresado
    txt_surface = fuente.render(texto_ingresado, True, NEGRO)
    ventana.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(ventana, NEGRO, input_box, 2)
#Funcion de Categorias\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_menu_principal():
    ventana.fill(GRIS)
    ventana.blit(fondo_categorias, (0, 0))
    # Dibujar los botones-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, NEGRO, boton_matrix)
    ventana.blit(entrar, texto_matrix_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_predis) 
    ventana.blit(entrar, texto_predis_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_evo)
    ventana.blit(entrar, texto_evo_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_super)
    ventana.blit(entrar, texto_super_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_cermex) 
    ventana.blit(entrar, texto_cermex_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_atras)  
    ventana.blit(atras, texto_atras_rect.topleft)
#Funcion Sidel Matrix\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_matrix(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI):
    ventana.fill(GRIS)
    ventana.blit(fondo_matrix, (0, 0))
    pygame.draw.rect(ventana, NEGRO, boton_atras)  
    ventana.blit(atras, texto_atras_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_reiniciar)  
    ventana.blit(reiniciar, texto_reiniciar_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_si)  
    ventana.blit(si, texto_si_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_no)  
    ventana.blit(no, texto_no_rect.topleft)
    # Dibujar área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, BLANCO, text_area_rect)
    pygame.draw.rect(ventana, NEGRO, text_area_rect, 2)
    Preguntas(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
#Funcion Sidel Aseptic Combi Predis\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_predis(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI):
    ventana.fill(GRIS)
    ventana.blit(fondo_aseptic, (0, 0))
    pygame.draw.rect(ventana, NEGRO, boton_atras)  
    ventana.blit(atras, texto_atras_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_reiniciar)  
    ventana.blit(reiniciar, texto_reiniciar_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_si)  
    ventana.blit(si, texto_si_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_no)  
    ventana.blit(no, texto_no_rect.topleft)
    # Dibujar área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, BLANCO, text_area_rect)
    pygame.draw.rect(ventana, NEGRO, text_area_rect, 2)
    Preguntas(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
#Funcion de Sidel EvoBlow\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_evo(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI):
    ventana.fill(GRIS)
    ventana.blit(fondo_evo, (0, 0))
    pygame.draw.rect(ventana, NEGRO, boton_atras)  
    ventana.blit(atras, texto_atras_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_reiniciar)  
    ventana.blit(reiniciar, texto_reiniciar_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_si)  
    ventana.blit(si, texto_si_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_no)  
    ventana.blit(no, texto_no_rect.topleft)
    # Dibujar área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, BLANCO, text_area_rect)
    pygame.draw.rect(ventana, NEGRO, text_area_rect, 2)
    Preguntas(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
#Funcion de Sidel Super Combi\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_super(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI):
    ventana.fill(GRIS)
    ventana.blit(fondo_super, (0, 0))
    pygame.draw.rect(ventana, NEGRO, boton_atras)  
    ventana.blit(atras, texto_atras_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_reiniciar)  
    ventana.blit(reiniciar, texto_reiniciar_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_si)  
    ventana.blit(si, texto_si_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_no)  
    ventana.blit(no, texto_no_rect.topleft)
    # Dibujar área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, BLANCO, text_area_rect)
    pygame.draw.rect(ventana, NEGRO, text_area_rect, 2)
    Preguntas(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
#Funcion de Sidel Cermex\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def mostrar_cermex(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI):
    ventana.fill(GRIS)
    ventana.blit(fondo_cermex, (0, 0))
    pygame.draw.rect(ventana, NEGRO, boton_atras)  
    ventana.blit(atras, texto_atras_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_reiniciar)  
    ventana.blit(reiniciar, texto_reiniciar_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_si)  
    ventana.blit(si, texto_si_rect.topleft)
    pygame.draw.rect(ventana, NEGRO, boton_no)  
    ventana.blit(no, texto_no_rect.topleft)
    # Dibujar área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.draw.rect(ventana, BLANCO, text_area_rect)
    pygame.draw.rect(ventana, NEGRO, text_area_rect, 2)
    Preguntas(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
#Funcion Respuestas\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Respuestas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res):
    Res = "\n El Diagnostico fue Ejecutado Correctamente!! \n Las Soluciones son las Siguientes:\n"
    if R1 or R2:  #SOPLADO
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Soplado:\n  • Asegurar la correcta calibración y mantenimiento de los moldes.\n • Monitorizar y controlar la temperatura de las preformas de manera precisa.\n • Verificar y mantener la presión de aire adecuada.\n • Realizar inspecciones regulares y reemplazar moldes desgastados."
    if R3:      #LLENADO
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Llenado:\n  • Calibrar correctamente las válvulas de llenado según las especificaciones\n del producto.\n • Limpiar regularmente las boquillas de llenado para evitar obstrucciones.\n • Monitorizar y ajustar la presión del gas para mantenerla dentro de los\n parámetros óptimos."
    if R4 or R5:  #Taponado
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Taponado:\n • Asegurar la correcta alineación del cabezal de taponado.\n • Inspeccionar y reemplazar cabezales de taponado desgastados.\n • Verificar la calidad de los tapones y asegurar un suministro consistente."
    if R6 or R7:  #Sistema_Transporte
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas en el Sistema de Transporte:\n • Verificar y corregir la alineación de los transportadores.\n • Ajustar las velocidades de transporte para evitar atascos y daños.\n • Mantener y calibrar los sensores y actuadores regularmente."
    if R8:          #Instrumentos
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Probelmas en Instrumentación:\n • Actualizar el software y firmware del sistema de control regularmente.\n • Verificar y mantener los PLCs y otros componentes electrónicos.\n • Inspeccionar y asegurar las conexiones eléctricas para evitar fallos."
    if R9 or R10:  #Mantenimiento_Insuficiente
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Desgaste y Mantenimiento Insuficiente:\n  • Implementar un programa de mantenimiento preventivo riguroso.\n • Utilizar piezas de repuesto originales de Sidel.\n • Realizar inspecciones regulares y reemplazar componentes desgastados\n según sea necesario."
    if R11:         #Esterilizacion 
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Esterilización:\n  •	Mal funcionamiento del sistema de esterilización de preformas.\n • Fugas en las juntas o sellos que permiten la entrada de contaminantes.\n • Desgaste de las lámparas de esterilización UV o componentes del sistema\n de peróxido de hidrógeno."
    if R12:          #Defromacion_Botellas
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Formación de Botellas:\n • Asegurar un control preciso de la temperatura de las preformas.\n • Mantener y ajustar adecuadamente la presión de aire.\n • Realizar inspecciones regulares y reemplazar moldes desgastados o\n dañados.\n • Verificar y corregir la alineación de los moldes."
    if R13:          #Precalentamiento
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Precalentamiento:\n • Verificar y calibrar regularmente los hornos de precalentamiento.\n • Reemplazar las lámparas de infrarrojos desgastadas.\n • Inspeccionar y calibrar los sensores de temperatura."
    if R14:          #Eficiencia_Energetica 
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Eficiencia Energética:\n • Mejorar el aislamiento térmico y la eficiencia del sistema de calentamiento.\n • Mantener y ajustar el sistema de aire comprimido para evitar pérdidas."
    if R15:          #Ingreso de Producto
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas en Ingreso de Productos:\n • Ajustar la configuración de los alimentadores según los requisitos del\n producto.\n • Inspeccionar y mantener los transportadores de entrada regularmente.\n • Verificar y calibrar los sensores de detección para garantizar su correcto\n funcionamiento."
    if R16:          #Sistema_Empaque
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Fallos en el Sistema de Empaque:\n • Ajustar la configuración de la máquina de empaque según las\n especificaciones del producto.\n • Reemplazar los componentes desgastados del sistema de sellado.\n • Verificar y mantener el suministro adecuado de material de empaque."
    if R17 or R18:  #Etiquetado
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Etiquetado de Producto:\n •	Verificar y ajustar la configuración de la máquina de etiquetado.\n • Mantener y calibrar el sistema de alimentación de etiquetas.\n • Inspeccionar y reemplazar los sensores de detección de etiquetas si es necesario."
    return Res
#Funcion Respuestas\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def Causas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res):
    Res = "\n El Diagnostico fue Ejecutado Correctamente!! \n Esas son las Principales Causas de las Fallas:\n"
    if R1 or R2:  #SOPLADO
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Soplado:\n  • Calibración incorrecta de los moldes de soplado.\n • Variaciones en la temperatura de las preformas.\n • Presión de aire inadecuada durante el proceso de soplado.\n • Desgaste de los moldes."
    if R3:      #LLENADO
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Llenado:\n •	Calibración incorrecta de las válvulas de llenado.\n • Obstrucciones en las boquillas de llenado.\n • Variaciones en la presión del gas de llenado."
    if R4 or R5:  #Taponado
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Taponado:\n • Alineación incorrecta del cabezal de taponado.\n • Desgaste de los cabezales de taponado.\n • Calidad inconsistente de los tapones."
    if R6 or R7:  #Sistema_Transporte
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas en el Sistema de Transporte:\n • Desalineación de los transportadores.\n • Velocidades de transporte inadecuadas.\n • Fallos en los sensores o actuadores del sistema de transporte."
    if R8:          #Instrumentos
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Probelmas en Instrumentación:\n • Problemas de software o firmware.\n • Fallos en los PLCs (Controladores Lógicos Programables).\n • Conexiones eléctricas defectuosas."
    if R9 or R10:  #Mantenimiento_Insuficiente
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Desgaste y Mantenimiento Insuficiente:\n • Piezas y componentes que han excedido su vida útil.\n • Falta de un programa de mantenimiento preventivo adecuado.\n • Uso de piezas de repuesto no originales o de baja calidad."
    if R11:         #Esterilizacion 
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Esterilización:\n  •	Mal funcionamiento del sistema de esterilización de preformas.\n • Fugas en las juntas o sellos que permiten la entrada de contaminantes.\n • Desgaste de las lámparas de esterilización UV o componentes del sistema\n de peróxido de hidrógeno."
    if R12:          #Defromacion_Botellas
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Formación de Botellas:\n • Variaciones en la temperatura de las preformas.\n • Presión de aire inadecuada durante el proceso de soplado.\n • Desgaste o daños en los moldes de soplado.\n • Alineación incorrecta de los moldes."
    if R13:          #Precalentamiento
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Precalentamiento:\n • Mal funcionamiento de los hornos de precalentamiento.\n • Desgaste de las lámparas de infrarrojos.\n • Problemas en los sensores de temperatura."
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Eficiencia Energética:\n • Ineficiencia en el sistema de calentamiento.\n • Pérdidas de energía en el sistema de aire comprimido."
    if R15:          #Ingreso de Producto
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas en Ingreso de Productos:\n • Configuración incorrecta de los alimentadores.\n • Desgaste o daño en los transportadores de entrada.\n • Problemas con los sensores de detección de productos."
    if R16:          #Sistema_Empaque
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Fallos en el Sistema de Empaque:\n • Configuración incorrecta de la máquina de empaque.\n • Desgaste de los componentes del sistema de sellado.\n • Problemas con el suministro de material de empaque."
    if R17 or R18:  #Etiquetado
        Res += "\n-------------------------------------------------------------------------------------------------------\n - Problemas de Etiquetado de Producto:\n•	Ajustes incorrectos en la máquina de etiquetado.\n • Problemas con el sistema de alimentación de etiquetas.\n • Fallos en los sensores de detección de etiquetas."
    return Res
#Funcion Principal\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def main():
    global estado_actual, texto_ingresado, texto_activo
    R1 =False
    R2 =False
    R3 =False
    R4 =False
    R5 =False
    R6 =False
    R7 =False
    R8 =False
    R9 =False
    R10 =False
    R11 =False
    R12 =False
    R13 =False
    R14 =False
    R15 =False
    R16 =False
    R17 =False
    R18 =False
    PI = True
    P1 = False
    P2 = False
    P3 = False
    P4 = False
    P5 = False
    P6 = False
    P7 = False
    P8 = False
    P9 = False
    P10 = False
    P11 = False
    P12 = False
    P13 = False
    P14 = False
    P15 = False
    P16 = False
    P17 = False
    P18 = False
    PF = False
    RSI = False  
    RS = False
    RN = False

    scroll_y = 0
    scroll_speed = 10
    Res = ""

    while True:
        # Renderizar y mostrar el texto en el área de texto-----------------------------------------------------------------------------------------------------------------------------------------------------
        lines = Res.split('\n')
        total_content_height = len(lines) * font.get_linesize()
        max_scroll_y = -(total_content_height - TEXTAREA_ALTO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Cerrar ventana
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Click del mouse
                if estado_actual == ESTADO_INICIO:
                    if boton_inicio_rect.collidepoint(evento.pos):         #Boton Inicial Seccion
                        if texto_ingresado.strip() == usuario:
                            estado_actual = ESTADO_MENU_PRINCIPAL
                        else:
                            estado_actual = ESTADO_ERROR
                elif boton_ok.collidepoint(evento.pos) and estado_actual == ESTADO_ERROR:   #Boton Ok (Error)
                    estado_actual = ESTADO_INICIO
                    texto_ingresado = ""
                elif estado_actual == ESTADO_MENU_PRINCIPAL:
                    if boton_matrix.collidepoint(evento.pos):
                        estado_actual = ESTADO_MATRIX
                    elif boton_predis.collidepoint(evento.pos):
                        estado_actual = ESTADO_PREDIS
                    elif boton_evo.collidepoint(evento.pos):
                        estado_actual = ESTADO_EVO
                    elif boton_super.collidepoint(evento.pos):
                        estado_actual = ESTADO_SUPER
                    elif boton_cermex.collidepoint(evento.pos):
                        estado_actual = ESTADO_CERMEX
                    elif boton_atras.collidepoint(evento.pos):
                        estado_actual = ESTADO_INICIO
                        texto_ingresado = ""
                elif estado_actual in [ESTADO_MATRIX, ESTADO_PREDIS, ESTADO_EVO, ESTADO_SUPER, ESTADO_CERMEX]:
                    if boton_atras.collidepoint(evento.pos):
                        estado_actual = ESTADO_MENU_PRINCIPAL     
                        scroll_y = 0                 
                        Res = ""
                        R1 =False
                        R2 =False
                        R3 =False
                        R4 =False
                        R5 =False
                        R6 =False
                        R7 =False
                        R8 =False
                        R9 =False
                        R10 =False
                        R11 =False
                        R12 =False
                        R13 =False
                        R14 =False
                        R15 =False
                        R16 =False
                        R17 =False
                        R18 =False
                        PI = True
                        P1 = False
                        P2 = False
                        P3 = False
                        P4 = False
                        P5 = False
                        P6 = False
                        P7 = False
                        P8 = False
                        P9 = False
                        P10 = False
                        P11 = False
                        P12 = False
                        P13 = False
                        P14 = False
                        P15 = False
                        P16 = False
                        P17 = False
                        P18 = False
                        PF = False
                        RS = False
                        RN = False 
                        RSI = False
                    elif boton_si.collidepoint(evento.pos) and PI:                     #Pregunta 1
                        PI = False
                        P1 = True   
                    elif boton_si.collidepoint(evento.pos) and P1:                    #Pregunta 2
                        P1 = False
                        P2 = True
                        R1 = True
                    elif boton_no.collidepoint(evento.pos) and P1:
                        P1 = False
                        P2 = True
                        R1 = False
                    elif boton_si.collidepoint(evento.pos) and P2:                    #Pregunta 3
                        P2 = False
                        P3 = True
                        R2 = True
                    elif boton_no.collidepoint(evento.pos) and P2:
                        P2 = False
                        P3 = True
                        R2 = False
                    elif boton_si.collidepoint(evento.pos) and P3:                    #Pregunta 4
                        P3 = False
                        P4 = True
                        R3 = True
                    elif boton_no.collidepoint(evento.pos) and P3:
                        P3 = False
                        P4 = True
                        R3 = False
                    elif boton_si.collidepoint(evento.pos) and P4:                    #Pregunta 5
                        P4 = False
                        P5 = True
                        R4 = True
                    elif boton_no.collidepoint(evento.pos) and P4:
                        P4 = False
                        P5 = True
                        R4 = False
                    elif boton_si.collidepoint(evento.pos) and P5:                    #Pregunta 6
                        P5 = False
                        P6 = True
                        R5 = True
                    elif boton_no.collidepoint(evento.pos) and P5:
                        P5 = False
                        P6 = True
                        R5 = False
                    elif boton_si.collidepoint(evento.pos) and P6:                    #Pregunta 7
                        P6 = False
                        P7 = True
                        R6 = True
                    elif boton_no.collidepoint(evento.pos) and P6:
                        P6 = False
                        P7 = True
                        R6 = False
                    elif boton_si.collidepoint(evento.pos) and P7:                    #Pregunta 8
                        P7 = False
                        P8 = True
                        R7 = True
                    elif boton_no.collidepoint(evento.pos) and P7:
                        P7 = False
                        P8 = True
                        R7 = False
                    elif boton_si.collidepoint(evento.pos) and P8:                    #Pregunta 9
                        P8 = False
                        P9 = True
                        R8 = True
                    elif boton_no.collidepoint(evento.pos) and P8:
                        P8 = False
                        P9 = True
                        R8 = False
                    elif boton_si.collidepoint(evento.pos) and P9:                    #Pregunta 10
                        P9= False
                        P10 = True
                        R9 = True
                    elif boton_no.collidepoint(evento.pos) and P9:
                        P9 = False
                        P10 = True
                        R9 = False
                    elif boton_si.collidepoint(evento.pos) and P10:                    #Pregunta 11
                        P10 = False
                        P11 = True
                        R10 = True
                    elif boton_no.collidepoint(evento.pos) and P10:
                        P10 = False
                        P11 = True
                        R10 = False
                    elif boton_si.collidepoint(evento.pos) and P11:                    #Pregunta 12
                        P11 = False
                        P12 = True
                        R11 = True
                    elif boton_no.collidepoint(evento.pos) and P11:
                        P11 = False
                        P12 = True
                        R11 = False
                    elif boton_si.collidepoint(evento.pos) and P12:                    #Pregunta 13
                        P12 = False
                        P13 = True
                        R12 = True
                    elif boton_no.collidepoint(evento.pos) and P12:
                        P12 = False
                        P13 = True
                        R12 = False
                    elif boton_si.collidepoint(evento.pos) and P13:                    #Pregunta 14
                        P13 = False
                        P14 = True
                        R13 = True
                    elif boton_no.collidepoint(evento.pos) and P13:
                        P13 = False
                        P14 = True
                        R13 = False
                    elif boton_si.collidepoint(evento.pos) and P14:                    #Pregunta 15
                        P14 = False
                        P15 = True
                        R14 = True
                    elif boton_no.collidepoint(evento.pos) and P14:
                        P14 = False
                        P15 = True
                        R14 = False
                    elif boton_si.collidepoint(evento.pos) and P15:                    #Pregunta 16
                        P15 = False
                        P16 = True
                        R15 = True
                    elif boton_no.collidepoint(evento.pos) and P15:
                        P15 = False
                        P16 = True
                        R15 = False
                    elif boton_si.collidepoint(evento.pos) and P16:                    #Pregunta 17
                        P16 = False
                        P17 = True
                        R16 = True
                    elif boton_no.collidepoint(evento.pos) and P16:
                        P16 = False
                        P17 = True
                        R16 = False
                    elif boton_si.collidepoint(evento.pos) and P17:                    #Pregunta 18
                        P17 = False
                        P18 = True
                        R17 = True
                    elif boton_no.collidepoint(evento.pos) and P17:
                        P17 = False
                        P18 = True
                        R17 = False
                    elif boton_si.collidepoint(evento.pos) and P18:                    #Pregunta Final
                        P18 = False
                        PF = True
                        R18 = True
                    elif boton_no.collidepoint(evento.pos) and P18:
                        P18 = False
                        PF = True
                        R18 = False
                    elif boton_si.collidepoint(evento.pos) and PF:                    #Pregunta Final
                        PF = False
                        RSI = True
                    elif boton_no.collidepoint(evento.pos) and PF:
                        PF = False
                        RN = True
                    elif boton_si.collidepoint(evento.pos) and RSI and not RN:                    #Pregunta Final
                        RSI = False
                        RS = True
                        scroll_y = 0
                    elif boton_no.collidepoint(evento.pos) and RSI:
                        RN = True
                    elif boton_reiniciar.collidepoint(evento.pos):
                        R1 =False
                        R2 =False
                        R3 =False
                        R4 =False
                        R5 =False
                        R6 =False
                        R7 =False
                        R8 =False
                        R9 =False
                        R10 =False
                        R11 =False
                        R12 =False
                        R13 =False
                        R14 =False
                        R15 =False
                        R16 =False
                        R17 =False
                        R18 =False
                        PI = True
                        P1 = False
                        P2 = False
                        P3 = False
                        P4 = False
                        P5 = False
                        P6 = False
                        P7 = False
                        P8 = False
                        P9 = False
                        P10 = False
                        P11 = False
                        P12 = False
                        P13 = False
                        P14 = False
                        P15 = False
                        P16 = False
                        P17 = False
                        P18 = False
                        PF = False 
                        RS = False
                        RN = False
                        RSI = False
                    if text_area_rect.collidepoint(evento.pos):
                        texto_activo = True
                    else:
                        texto_activo = False
                    if evento.button == 4:  # Scroll up
                        scroll_y = min(scroll_y + scroll_speed, 0)
                    elif evento.button == 5:  # Scroll down
                        scroll_y = max(scroll_y - scroll_speed, max_scroll_y)

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if texto_ingresado.strip() == usuario:
                        estado_actual = ESTADO_MENU_PRINCIPAL
                    else:
                        estado_actual = ESTADO_ERROR
                elif evento.key == pygame.K_BACKSPACE:
                    texto_ingresado = texto_ingresado[:-1]
                else:
                    texto_ingresado += evento.unicode

        if estado_actual == ESTADO_INICIO:
            mostrar_inicio()
        elif estado_actual == ESTADO_MENU_PRINCIPAL:
            mostrar_menu_principal()
        elif estado_actual == ESTADO_MATRIX:
            mostrar_matrix(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
            R11 = False
            R12 = False
            R13 = False
            R14 = False
            R15 = False
            R16 = False
            R17 = False
            R18 = False
            Res = "\n           Bienvenido al Diagnostico para la Maquina Matrix Combi!!\n\n        Responde las siguientes Preguntas para Realizar una Solucion \n\n        <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <---\n\n • Descripción de Maquina: \n Un sistema integrado que combina soplado, llenado y taponado en una sola \n máquina.\n • Aplicaciones:\n Adecuada para bebidas carbonatadas y no carbonatadas, aguas, jugos, té\n y bebidas funcionales.\n • Beneficios:\n Ahorro de espacio, reducción de costos operativos y mayor eficiencia en el \n proceso de envasado."
            if RSI and not RS:
                Res = Respuestas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            if RS:
                Res = Causas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            draw_scrollbar(ventana, scroll_y, text_area_rect, lines, font)
        elif estado_actual == ESTADO_PREDIS:
            mostrar_predis(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
            R12 = False
            R13 = False
            R14 = False
            R15 = False
            R16 = False
            R17 = False
            R18 = False
            Res = "\n           Bienvenido al Diagnostico para la Maquina Aseptic Combi!!\n\n        Responde las siguientes Preguntas para Realizar una Solucion \n\n        <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <---\n\n • Descripción de Maquina: \n Una solución de soplado, llenado y taponado aséptico que utiliza \n esterilización seca de preformas.\n • Aplicaciones:\n Ideal para productos lácteos, jugos, néctares, isotónicos y té.\n • Beneficios:\n Garantiza una alta seguridad alimentaria, reducción del consumo de\n productos químicos y ahorro de energía."
            if RSI and not RS:
                Res = Respuestas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            if RS:
                Res = Causas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            draw_scrollbar(ventana, scroll_y, text_area_rect, lines, font)
        elif estado_actual == ESTADO_EVO:
            mostrar_evo(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
            R1 = False
            R2 = False
            R3 = False
            R4 = False
            R5 = False
            R11 = False
            R15 = False
            R16 = False
            R17 = False
            R18 = False
            Res = "\n              Bienvenido al Diagnostico para la Maquina EvoBLOW!!\n\n        Responde las siguientes Preguntas para Realizar una Solucion \n\n        <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <---\n\n • Descripción de Maquina:\n Una máquina de soplado modular y flexible para la producción de\n botellas de PET.\n • Aplicaciones:\n Adecuada para una variedad de tamaños y formas de botellas para\n diferentes tipos de bebidas.\n • Beneficios:\n Alta velocidad de producción, flexibilidad en el diseño de botellas y\n eficiencia energética."
            if RSI and not RS:
                Res = Respuestas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            if RS:
                Res = Causas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            draw_scrollbar(ventana, scroll_y, text_area_rect, lines, font)
        elif estado_actual == ESTADO_SUPER:
            mostrar_super(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
            R1 = False
            R2 = False
            R6 = False
            R7 = False
            R11 = False
            R12 = False
            R13 = False
            R15 = False
            R16 = False
            Res = "\n            Bienvenido al Diagnostico para la Maquina Super Combi!!\n\n        Responde las siguientes Preguntas para Realizar una Solucion \n\n        <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <---\n\n • Descripción de Maquina:\n Una solución integrada todo en uno que combina cinco procesos:\n alimentación de preformas, soplado, etiquetado, llenado y taponado.\n • Aplicaciones:\n Ideal para bebidas, incluyendo aguas, refrescos y jugos.\n • Beneficios:\n Simplificación del proceso, reducción de costos operativos y\n máxima eficiencia."
            if RSI and not RS:
                Res = Respuestas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            if RS:
                Res = Causas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            draw_scrollbar(ventana, scroll_y, text_area_rect, lines, font)
        elif estado_actual == ESTADO_CERMEX:
            R1 =False
            R2 =False
            R3 =False
            R4 =False
            R5 =False
            R6 =False
            R7 =False
            R11 =False
            R12 =False
            R13 =False
            R14 =False
            mostrar_cermex(PI,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,PF,RS,RN,RSI)
            Res = "\n              Bienvenido al Diagnostico para la Maquina Cermex!!\n\n        Responde las siguientes Preguntas para Realizar una Solucion \n\n        <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <--- <---\n\n • Descripción de Maquina:\n Soluciones de embalaje secundario que incluyen encajadoras, agrupadoras\n y paletizadoras.\n • Aplicaciones:\n Adecuada para diferentes sectores como bebidas, alimentos y productos de\n cuidado personal.\n • Beneficios:\n Alta velocidad de operación, flexibilidad y robustez en el embalaje."
            if RSI and not RS:
                Res = Respuestas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            if RS:
                Res = Causas(R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,Res)
            draw_scrollbar(ventana, scroll_y, text_area_rect, lines, font)
        elif estado_actual == ESTADO_ERROR:
            mostrar_error()

        max_lines = TEXTAREA_ALTO // font.get_linesize()
        start_line = max(0, min(-scroll_y // font.get_linesize(), len(lines) - max_lines))
        end_line = min(len(lines), start_line + max_lines)

        for i in range(start_line, end_line):
            line_surface = font.render(lines[i], True, NEGRO)
            ventana.blit(line_surface, (text_area_rect.x + 5, text_area_rect.y + 5 + (i - start_line) * font.get_linesize()))

        pygame.display.update()

# Llamar a la función principal-----------------------------------------------------------------------------------------------------------------------------------------------------
main()
