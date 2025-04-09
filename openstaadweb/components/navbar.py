import reflex as rx

def navbar ():
    return rx.hstack(
        rx.image("logo.png", width = "50px"),
        rx.link(
            "Docs",
            href="/"
        ),
        rx.link(
            "Gallery",
            href="/"
        ),
        rx.link(
            "Roadmap",
            href="/"
        ),
        rx.link(
            "blog",
            href="/"
        ),
        
    )