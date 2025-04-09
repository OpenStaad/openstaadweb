"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from openstaadweb.pages.docs import docs


app = rx.App()
app.add_page(docs, route="/")
