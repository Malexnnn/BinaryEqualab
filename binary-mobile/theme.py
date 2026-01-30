
import flet as ft

class AuroraTheme:
    # Colors
    BACKGROUND = "#09090b"  # Zinc 950
    SURFACE    = "#18181b"  # Zinc 900
    SURFACE_2  = "#27272a"  # Zinc 800
    PRIMARY    = "#f97316"  # Orange 500
    PRIMARY_DIM= "#c2410c"  # Orange 700
    TEXT       = "#fafafa"  # Zinc 50
    TEXT_DIM   = "#a1a1aa"  # Zinc 400
    ERROR      = "#ef4444"  # Red 500

    @staticmethod
    def theme():
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=AuroraTheme.PRIMARY,
                surface=AuroraTheme.SURFACE,
                on_primary="#ffffff",
            ),
            font_family="Roboto", # Or standard font
            use_material3=True,
        )

# Components styles
BUTTON_STYLE_NUMBER = {
    "bgcolor": AuroraTheme.SURFACE_2,
    "color": AuroraTheme.TEXT,
}

BUTTON_STYLE_OP = {
    "bgcolor": AuroraTheme.PRIMARY,
    "color": "#ffffff",
}

BUTTON_STYLE_ACTION = {
    "bgcolor": AuroraTheme.SURFACE, 
    "color": AuroraTheme.PRIMARY,
}
