from src.abstractions import InitialContent


class InitialThemes(InitialContent):
    file_name = "themes.json"

    content = {
        "black": {
            "background": "black",
            "menu_background": "darkgray",
            "menu_foreground": "white",
            "text_background": "black",
            "text_foreground": "white",
            "cursor": "white"
        },

        "light": {
            "background": "white",
            "menu_background": "lightgray",
            "menu_foreground": "black",
            "text_background": "white",
            "text_foreground": "black",
            "cursor": "black"
        },

        "atom": {
            "text_background": "#282A36",
            "text_foreground": "#F8F8F2",
            "cursor": "#BD93F9",

            "selection": "#44475A",
            "comment": "#6272A4",
            "string": "#50FA7B",
            "keyword": "#FF79C6",
            "function": "#8BE9FD",
            "variable": "#FF5555",
            "number": "#BD93F9"
        },

        "sublime-text": {
            "text_background": "#282C34",
            "text_foreground": "#ABB2BF",
            "cursor": "#528BFF",

            "selection": "#3E4451",
            "comment": "#5C6370",
            "string": "#98C379",
            "keyword": "#C678DD",
            "function": "#61AFEF",
            "variable": "#E5C07B",
            "number": "#D19A66"
        }
    }
