# Pearls

Pearls is a program making a pearl layout from a picture. The idea is, that you can load in a picture in the program and it will be shown in a big coordinate system as pearls, so you can copy it to the real world.

## How to get started?

1. Install python and pip. Remember to add Python and pip to path
2. Download and unpack the repository.
3. `cd` into the folder with the program.
4. Run `pip install -r requirements`. If you gain errors, instead run `pip install pygame opencv-python`
5. Run `python .\main.py`.
6. Type FPS, for instance `60` and press enter.
7. You should now see a gui with the default image.

## How to use?

- You can use drag around with the mouse and use <kbd>←</kbd>, <kbd>↑</kbd>, <kbd>→</kbd> and <kbd>↓</kbd> to move around.
- You can use the mouse wheel, <kbd>+</kbd> and <kbd>-</kbd> to zoom in and out.
- By pressing <kbd>?</kbd> and typing a coordinate, you can get a specific pearl color. For intance press <kbd>?</kbd>, type `23, 12`, press <kbd>Enter</kbd> and you should see the pearl color in the terminal: `[12, 2] = [185 107  60] = Hama midi Nougat mørk`.
- If you would like to use another image than the default image, replace the image `final 3 s.png` in `./assets/` with another one.

![screenshot](https://user-images.githubusercontent.com/12400097/172066882-9474e9cf-6a46-4804-8702-3bf84b9739f2.png)
