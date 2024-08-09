import time
from pynput import mouse
from image_operations import generate_image
from click_counter_operations import update_config, on_click

def main():
    drive_letter = input("Please enter the drive letter assigned to Busy Tag device (e.g., D): ").strip().upper()

    image_filename = "click_count.png"
    generate_image(0, drive_letter)
    update_config(drive_letter, image_filename)

    listener = mouse.Listener(on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, drive_letter))
    listener.start()

    print("Left click counter started. Press 'Ctrl+C' to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the click counter...")
        listener.stop()  

if __name__ == "__main__":
    main()