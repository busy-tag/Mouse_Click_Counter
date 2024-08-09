import json
from pynput import mouse
from image_operations import generate_image

left_click_count = 0

def update_config(drive_letter, image_filename):
    config_path = f"{drive_letter}://config.json"
    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
        
        config_data['show_after_drop'] = False
        config_data['image'] = image_filename
        config_data["activate_pattern"] = True
        config_data["pattern_repeat"] = 2
        config_data["custom_pattern_arr"] = [
            {"led_bits": 127, "color": "000000", "speed": 10, "delay": 10},
            {"led_bits": 136, "color": "00FF00", "speed": 10, "delay": 5}
        ]

        with open(config_path, 'w') as file:
            json.dump(config_data, file, indent=4)
        
        print("Config file updated successfully.")
    except FileNotFoundError:
        print("Config file not found. Please ensure the correct drive letter is provided and the config.json file exists.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please ensure the config.json file is properly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def on_click(x, y, button, pressed, drive_letter):
    global left_click_count
    if button == mouse.Button.left and pressed:
        left_click_count += 1
        print(f"Left click count: {left_click_count}")
        generate_image(left_click_count, drive_letter)