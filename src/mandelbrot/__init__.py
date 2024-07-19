# the existence of an __init__.py file in a directory makes it a package 
# Then we can `import mandelbrot` and call it's main() function from any other python app
# including run_app.py

from .mandelbrot import Mandelbrot
from .main import main