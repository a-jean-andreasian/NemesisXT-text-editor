from src.abstractions import InitialContent


class InitialUserConfig(InitialContent):
    file_name = "user_config.json"

    content = {
        "font_size": 34
    }
