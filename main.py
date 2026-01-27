"""
Punto de entrada para Binary EquaLab.
"""
import sys
from PyQt6.QtWidgets import QApplication
import qdarktheme

from src.ui.main_window import MainWindow
from src.ui.styles import get_stylesheet
from src.utils.constants import AppConfig

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(AppConfig.APP_NAME)
    
    # Aplicar Tema Oscuro Base (qdarktheme) + Nuestro Tema Aurora (Stylesheet)
    qdarktheme.setup_theme()
    app.setStyleSheet(get_stylesheet())
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
