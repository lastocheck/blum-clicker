import pyautogui
import cv2
import numpy as np
import time

def capture_screenshot(region=None):
    if region:
        screenshot = pyautogui.screenshot(region=region)
    else:
        screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

def find_and_click(image, image_path, region=None, confidence=0.65, click_center=False):
    # Capture the screenshot
    screenshot = capture_screenshot(region)
    screenshot = cv2.resize(screenshot, (screenshot.shape[1] // 2, screenshot.shape[0] // 2))

    # Find the target in the screenshot
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)

    # Get the best match position
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Check if the best match is good enough
    if max_val >= confidence:
        target_height, target_width = image.shape
        if click_center:
            click_point = (max_loc[0] + target_width // 2, max_loc[1] + target_height // 2)
        else:
            click_point = (max_loc[0] + target_width // 2, max_loc[1] + target_height - 3)

        # Adjust the click point if a region is specified
        if region:
            click_point = (click_point[0] * 2 + region[0], click_point[1] * 2 + region[1])

        pyautogui.click(click_point)
        print(f"Found match for {image_path} with confidence {max_val}")
    else:
        print(f"No match found for image {image_path}")

def load_and_downscale_image(image_path):
    target = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if target is not None:
        target = cv2.resize(target, (target.shape[1] // 2, target.shape[0] // 2))
    return target

if __name__ == "__main__":
    flake_image_path = './img/flake.png'
    ice_image_path = './img/ice.png'
    stop_image_path = './img/stop.png'
    
    regular_region = (879, 184, 370, 580)  # Define the regular region as (left, top, width, height)
    ice_region = (874, 344, 382, 251)   # Define the specific region for ice.png
    stop_region = (945, 700, 206, 100)  # Define the specific region for stop.png

    # Load and downscale images at the start
    flake_image = load_and_downscale_image(flake_image_path)
    ice_image = load_and_downscale_image(ice_image_path)
    stop_image = load_and_downscale_image(stop_image_path)

    iteration = 0
    while True:
        find_and_click(flake_image, flake_image_path, region=regular_region)
        
        # if iteration % 5 == 0:
        #     find_and_click(ice_image, ice_image_path, region=ice_region)
        
        if iteration % 100 == 0:
            find_and_click(stop_image, stop_image_path, region=stop_region, click_center=True)
        
        iteration += 1