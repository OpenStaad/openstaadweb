import reflex as rx

from openstaadweb.components.navbar import navbar
from openstaadweb.components.foother import footer

def docs():
    return rx.vstack(
        navbar(),
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
    return rx.accordion.root(
        rx.accordion.item(
            header="Introduction",
            content="The first accordion item's content",
        ),
        rx.accordion.item(
            header="Root",
            content="The second accordion item's content",
        ),
        rx.accordion.item(
            header="Geometry",
            content="The third accordion item's content",
        ),
        variant="ghost",
        color_scheme="red",
        width = "300px"
    )

def content():
    return rx.text("Content")