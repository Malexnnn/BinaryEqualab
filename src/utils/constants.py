"""
Constantes globales y paleta de colores para el tema Aurora.
"""

class AuroraPalette:
    # Colores Principales
    BACKGROUND = "#1C1917"       # Stone 900 - Fondo principal (oscuro cálido)
    BACKGROUND_LIGHT = "#292524" # Stone 800 - Fondo secundario / Paneles
    BACKGROUND_DARK = "#0C0A09"  # Stone 950 - Fondo inputs / terminal
    
    PRIMARY = "#B91C1C"          # Red 700 - Acento principal (Cereza profunda)
    PRIMARY_HOVER = "#DC2626"    # Red 600
    
    SECONDARY = "#EA580C"        # Orange 600 - Acento secundario (Atardecer)
    SECONDARY_HOVER = "#F97316"  # Orange 500
    
    ACCENT = "#D97706"           # Amber 600 - Detalles / Advertencias
    
    TEXT_PRIMARY = "#F5F5F4"     # Stone 100 - Texto principal
    TEXT_SECONDARY = "#A8A29E"   # Stone 400 - Texto secundario / Comentarios
    TEXT_MUTED = "#57534E"       # Stone 600 - Texto deshabilitado
    
    BORDER = "#44403C"           # Stone 700 - Bordes sutiles
    
    # Gradientes (Simulados con strings para usar en QSS)
    GRADIENT_AURORA = "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #B91C1C, stop:1 #EA580C)"

class AppConfig:
    APP_NAME = "Binary EquaLab"
    VERSION = "0.1.0-prototype"
    WINDOW_SIZE = (1200, 800)
    FONT_FAMILY_UI = "Segoe UI"
    FONT_FAMILY_CODE = "Consolas"
