# Arkapong
A Pygame mashup of ping pong and brick-breaker arcade games.

![Arkapong04](https://github.com/rdagger/Arkapong/assets/106355/ea16495d-2545-485e-86ad-59224c58341f)


I created this game specifically for my vintage cocktail table arcade machine.  It is optimized for a 1024x1280 vertical monitor resolution. However, it is also compatible with other common resolutions. Most settings can be modified in the settings.ini file such as resolution, difficulty and keyboard/mouse controls.

Player paddles are controlled using mouse motion.  The game supports both one-on-one matches between two players and single-player mode against the computer.  For Player 1, I'm utilizing the X-axis of a Turbo Twist spinner, while Player 2 uses the Y-axis. Single-player games can also be played with a regular mouse. You can easily switch between relative motion and actual mouse position depending on your input device.

The game currently offers 39 levels. I designed these levels using an Excel spreadsheet, which you can find in the utils folder. The good news is that you can expand the game by adding more levels. There's a handy utility called parse_excel_levels.py that converts Excel designs into Python code, which can then be inserted into the levels.py folder to seamlessly integrate new levels.

![Levels 1-39](https://github.com/rdagger/Arkapong/assets/106355/af29d94e-c3d9-4f68-82d5-0ca37fc87c21)
