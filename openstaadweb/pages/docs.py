import reflex as rx

from openstaadweb.components.navbar import navbar
from openstaadweb.components.foother import footer

def docs():
    return rx.vstack(
        navbar(),
        rx.spacer(),
        docs_view(),
        rx.spacer(),
        footer(),
        min_height = "100vh",
        width = "100%",
        spacing="0",
    )

def docs_view():
    return rx.hstack(
        side_bar(),
        content()
    )

def side_bar():
    return rx.text("Side Bar")

def content():
    return rx.text("Content")