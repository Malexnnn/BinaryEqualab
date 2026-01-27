"""
Estilos QSS para la aplicación Binary EquaLab (Tema Aurora).
"""
from src.utils.constants import AuroraPalette

def get_stylesheet():
    return f"""
    /* --- General Window --- */
    QMainWindow {{
        background-color: {AuroraPalette.BACKGROUND};
        color: {AuroraPalette.TEXT_PRIMARY};
    }}

    QWidget {{
        background-color: {AuroraPalette.BACKGROUND};
        color: {AuroraPalette.TEXT_PRIMARY};
        font-family: 'Segoe UI', 'Roboto', sans-serif;
        font-size: 14px;
        selection-background-color: {AuroraPalette.SECONDARY};
        selection-color: white;
    }}

    /* --- Buttons --- */
    QPushButton {{
        background-color: {AuroraPalette.BACKGROUND_LIGHT};
        border: 1px solid {AuroraPalette.BORDER};
        border-radius: 8px;
        padding: 8px 16px;
        color: {AuroraPalette.TEXT_PRIMARY};
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: #353331; /* Un poco mas claro que Light */
        border-color: {AuroraPalette.TEXT_SECONDARY};
    }}
    QPushButton:pressed {{
        background-color: {AuroraPalette.BACKGROUND_DARK};
        border-color: {AuroraPalette.SECONDARY};
    }}
    
    /* Primary Action Button (Naranja) */
    QPushButton[class="primary"] {{
        background-color: {AuroraPalette.SECONDARY};
        border: none;
        color: white;
        font-weight: bold;
    }}
    QPushButton[class="primary"]:hover {{
        background-color: {AuroraPalette.SECONDARY_HOVER};
    }}

    /* --- Inputs & Console --- */
    QLineEdit, QTextEdit, QPlainTextEdit {{
        background-color: {AuroraPalette.BACKGROUND_DARK};
        border: 1px solid {AuroraPalette.BORDER};
        border-radius: 6px;
        color: {AuroraPalette.TEXT_PRIMARY};
        padding: 8px;
        font-family: 'Consolas', 'Fira Code', monospace;
        selection-background-color: {AuroraPalette.ACCENT};
    }}
    QLineEdit:focus, QTextEdit:focus {{
        border: 1px solid {AuroraPalette.ACCENT};
        background-color: #171513;
    }}
    QLineEdit:hover {{
        border-color: {AuroraPalette.TEXT_SECONDARY};
    }}

    /* --- Tabs (QTabWidget) --- */
    QTabWidget::pane {{
        border: 1px solid {AuroraPalette.BORDER};
        border-radius: 6px;
        top: -1px; 
    }}
    QTabBar::tab {{
        background: {AuroraPalette.BACKGROUND_LIGHT};
        color: {AuroraPalette.TEXT_SECONDARY};
        padding: 8px 16px;
        margin-right: 2px;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        border: 1px solid transparent;
    }}
    QTabBar::tab:selected {{
        background: {AuroraPalette.BACKGROUND};
        color: {AuroraPalette.SECONDARY};
        border-bottom: 2px solid {AuroraPalette.SECONDARY};
        font-weight: bold;
    }}
    QTabBar::tab:hover {{
        color: {AuroraPalette.TEXT_PRIMARY};
        background: {AuroraPalette.BORDER};
    }}

    /* --- Scrollbars (Modern Style) --- */
    QScrollBar:vertical {{
        border: none;
        background: {AuroraPalette.BACKGROUND};
        width: 12px;
        margin: 0px;
    }}
    QScrollBar::handle:vertical {{
        background: #44403C;
        min-height: 30px;
        border-radius: 6px;
        margin: 2px;
    }}
    QScrollBar::handle:vertical:hover {{
        background: {AuroraPalette.TEXT_SECONDARY};
    }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
        background: none;
        height: 0px;
    }}
    
    /* --- QListWidget / items --- */
    QListWidget {{
        background-color: {AuroraPalette.BACKGROUND};
        border: none;
    }}
    QListWidget::item {{
        padding: 8px;
        border-radius: 4px;
    }}
    QListWidget::item:selected {{
        background-color: {AuroraPalette.BACKGROUND_LIGHT};
        border-left: 3px solid {AuroraPalette.SECONDARY};
    }}
    QListWidget::item:hover {{
        background-color: {AuroraPalette.BACKGROUND_DARK};
    }}

    /* --- Tooltips --- */
    QToolTip {{
        background-color: {AuroraPalette.BACKGROUND_LIGHT};
        color: {AuroraPalette.TEXT_PRIMARY};
        border: 1px solid {AuroraPalette.BORDER};
        padding: 4px;
        border-radius: 4px;
    }}
    """
