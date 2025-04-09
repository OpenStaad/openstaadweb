import reflex as rx

def footer():
    return rx.hstack(
        rx.vstack(
            rx.heading("Docs"),
            rx.link(
                "Introduction",
                href = "/"
            ),
            rx.link(
                "First Steps",
                href = "/",
            )
        ),
        rx.vstack(
            rx.heading("Community"),
            rx.text("Discord"),
            rx.text("Github"),
            rx.text("Other"),
        ),
        rx.vstack(
            rx.heading("More"),
            rx.text("Blog"),
            rx.text("Support"),
        )
    )