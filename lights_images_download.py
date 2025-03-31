import os
import sys
from bing_image_downloader import downloader

# Suppress all print statements by redefining print
class SilentPrinter:
    def __init__(self):  # Ispravak metode __init__
        self.original_stdout = sys.stdout

    def __enter__(self):  # Ovo omogućava korištenje 'with' bloka
        sys.stdout = open(os.devnull, 'w')  # Preusmjerava izlaz u /dev/null
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # Povratak originalnom izlazu
        sys.stdout.close()
        sys.stdout = self.original_stdout

def download_images(query, num_images):
    with SilentPrinter():  # Koristi kontekstni manager za tišinu
        downloader.download(query, limit=num_images, output_dir=query, adult_filter_off=True, force_replace=False, timeout=60)

# Download images of Red traffic light
download_images('real traffic lights', 200)