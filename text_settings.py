import obsws_python as ws
import os
from dotenv import load_dotenv


class SettingOBS:
    def __init__(self) -> None:
        load_dotenv()
        password = os.environ.get('OBS_WS_PASSWORD')
        host = os.environ.get('OBS_WS_HOST')
        port = os.environ.get('OBS_WS_PORT')

        if (password is None or host is None or port is None):
            raise Exception('OBS Not Configured')
        self.ws = ws.ReqClient(host=host, port=port, password=password)

    def output_source_id(self, scene_name):
        # get the item ID in "scene_name"
        print("ID: sourceName")
        dicts = self.ws.get_scene_item_list(name=scene_name).scene_items
        for dict in dicts:
            print(f"{dict["sceneItemId"]}: {dict["sourceName"]}")

    def output_settings(self, source_name):
        # check the config and value of "source_name"
        dicts = self.ws.get_input_settings(name=source_name).input_settings

        for key, value in dicts.items():
            print(f"{key}: {value}")

    def change_text_display(self, scene_name, item_id):
        self.ws.set_scene_item_enabled(scene_name=scene_name,
                                       item_id=item_id,
                                       enabled=True)

    def change_text_settings(self, source_name, item_id, scene_name):
        settings = {
            "font": {"size": 128, "face": "Arial"},
            "text": "test",
            "vertical": False,
            "color": 255,
            "opacity": 100,
            "gradient": False,
            "gradient_color": 0,
            "bk_color": 0,
            "bk_opacity": 0,
            "align": "right",  # left, center, right
            "valign": "bottom",  # top, center, bottom
            "outline": True,
            "outline_size": 5,
            "outline_color": 0,
            "outline_opacity": 0,
            }

        self.ws.set_input_settings(name=source_name,
                                   settings=settings,
                                   overlay=True)


if __name__ == '__main__':
    source_name = "test"
    scene_name = "test_scene"
    item_id = 1

    obsAdapter = SettingOBS()

    # obsAdapter.output_source_id(scene_name)
    # obsAdapter.output_settings(source_name)
    # obsAdapter.change_text_settings(source_name, item_id, scene_name)
