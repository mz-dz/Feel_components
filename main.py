import flet as ft
from typing import List, Callable, Union

class FlexComponent(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs

class Text(FlexComponent):
    def __init__(self, text: str = "", **kwargs):
        super().__init__(**kwargs)
        self.text_control = ft.Text(text, **kwargs)

    def build(self):
        return self.text_control

    @property
    def value(self):
        return self.text_control.value

    @value.setter
    def value(self, v):
        self.text_control.value = v
        self.update()

class Button(FlexComponent):
    def __init__(self, text: str = "", color: str = None, on_click: Callable = None, **kwargs):
        super().__init__(**kwargs)
        self.button = ft.ElevatedButton(
            text=text,
            style=ft.ButtonStyle(color={"": color}) if color else None,
            on_click=on_click,
            **kwargs
        )

    def build(self):
        return self.button

class Input(FlexComponent):
    def __init__(self, placeholder: str = "", **kwargs):
        super().__init__(**kwargs)
        self.input = ft.TextField(hint_text=placeholder, **kwargs)

    def build(self):
        return self.input

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, v):
        self.input.value = v
        self.update()

class Div(FlexComponent):
    def __init__(self, *controls, **kwargs):
        super().__init__(**kwargs)
        self.controls = controls

    def build(self):
        return ft.Container(content=ft.Column(controls=list(self.controls)), **self.kwargs)

class Image(FlexComponent):
    def __init__(self, src: str = "", **kwargs):
        super().__init__(**kwargs)
        self.image = ft.Image(src=src, **kwargs)

    def build(self):
        return self.image

class Heading(FlexComponent):
    def __init__(self, level: int, text: str = "", **kwargs):
        super().__init__(**kwargs)
        sizes = {1: 32, 2: 24, 3: 18.72, 4: 16, 5: 13.28, 6: 10.72}
        self.text = ft.Text(text, size=sizes.get(level, 16), weight="bold", **kwargs)

    def build(self):
        return self.text

class Paragraph(FlexComponent):
    def __init__(self, text: str = "", **kwargs):
        super().__init__(**kwargs)
        self.paragraph = ft.Text(text, **kwargs)

    def build(self):
        return self.paragraph

class Link(FlexComponent):
    def __init__(self, text: str = "", url: str = "", **kwargs):
        super().__init__(**kwargs)
        self.link = ft.TextButton(text=text, url=url, **kwargs)

    def build(self):
        return self.link

class UnorderedList(FlexComponent):
    def __init__(self, *items, **kwargs):
        super().__init__(**kwargs)
        self.items = items

    def build(self):
        return ft.Column(
            controls=[ft.Text(f"• {item}") for item in self.items],
            **self.kwargs
        )

class OrderedList(FlexComponent):
    def __init__(self, *items, **kwargs):
        super().__init__(**kwargs)
        self.items = items

    def build(self):
        return ft.Column(
            controls=[ft.Text(f"{i+1}. {item}") for i, item in enumerate(self.items)],
            **self.kwargs
        )

class Table(FlexComponent):
    def __init__(self, headers: List[str], rows: List[List[str]], **kwargs):
        super().__init__(**kwargs)
        self.headers = headers
        self.rows = rows

    def build(self):
        return ft.DataTable(
            columns=[ft.DataColumn(ft.Text(header)) for header in self.headers],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row]) for row in self.rows],
            **self.kwargs
        )

class Form(FlexComponent):
    def __init__(self, *controls, on_submit: Callable = None, **kwargs):
        super().__init__(**kwargs)
        self.controls = controls
        self.on_submit = on_submit

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    *list(self.controls),
                    ft.ElevatedButton("Submit", on_click=self.on_submit)
                ]
            ),
            **self.kwargs
        )

class Checkbox(FlexComponent):
    def __init__(self, label: str = "", value: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.checkbox = ft.Checkbox(label=label, value=value, **kwargs)

    def build(self):
        return self.checkbox

    @property
    def value(self):
        return self.checkbox.value

    @value.setter
    def value(self, v):
        self.checkbox.value = v
        self.update()

class RadioGroup(FlexComponent):
    def __init__(self, *options, **kwargs):
        super().__init__(**kwargs)
        self.options = options
        self.radio_group = ft.RadioGroup(
            content=ft.Column([ft.Radio(value=option, label=option) for option in options]),
            **kwargs
        )

    def build(self):
        return self.radio_group

    @property
    def value(self):
        return self.radio_group.value

    @value.setter
    def value(self, v):
        self.radio_group.value = v
        self.update()

class Dropdown(FlexComponent):
    def __init__(self, *options, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(option) for option in options],
            **kwargs
        )

    def build(self):
        return self.dropdown

    @property
    def value(self):
        return self.dropdown.value

    @value.setter
    def value(self, v):
        self.dropdown.value = v
        self.update()

class Slider(FlexComponent):
    def __init__(self, min: float = 0, max: float = 100, value: float = 0, **kwargs):
        super().__init__(**kwargs)
        self.slider = ft.Slider(min=min, max=max, value=value, **kwargs)

    def build(self):
        return self.slider

    @property
    def value(self):
        return self.slider.value

    @value.setter
    def value(self, v):
        self.slider.value = v
        self.update()

class ProgressBar(FlexComponent):
    def __init__(self, value: float = 0, **kwargs):
        super().__init__(**kwargs)
        self.progress_bar = ft.ProgressBar(value=value, **kwargs)

    def build(self):
        return self.progress_bar

    @property
    def value(self):
        return self.progress_bar.value

    @value.setter
    def value(self, v):
        self.progress_bar.value = v
        self.update()

class Tabs(FlexComponent):
    def __init__(self, *tabs: Union[ft.Tab, dict], **kwargs):
        super().__init__(**kwargs)
        self.tabs = ft.Tabs(
            tabs=[ft.Tab(**tab) if isinstance(tab, dict) else tab for tab in tabs],
            **kwargs
        )

    def build(self):
        return self.tabs

class Alert(FlexComponent):
    def __init__(self, text: str = "", severity: str = "info", **kwargs):
        super().__init__(**kwargs)
        colors = {
            "info": ft.colors.BLUE,
            "success": ft.colors.GREEN,
            "warning": ft.colors.ORANGE,
            "error": ft.colors.RED,
        }
        self.alert = ft.Container(
            content=ft.Text(text),
            bgcolor=colors.get(severity, ft.colors.BLUE),
            padding=10,
            border_radius=5,
            **kwargs
        )

    def build(self):
        return self.alert
