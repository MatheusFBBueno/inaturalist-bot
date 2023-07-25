from config.config import Config
from inaturalist_interface import get_species_observations
from file_downloader import FileDownloader
import requests

class InaturalistBot:

    def __init__(self):
        config = Config()
        config_dict = config.parse_config()

        self.species_name = config_dict['SPECIES_NAME']
        self.license = config_dict['LICENSE']
        self.filter_larvae = config_dict['FILTER_LARVAE']
        self.enlarge_image = config_dict['RESIZE_IMAGE']

        self.file_manager = FileDownloader(self.species_name)
        self.get_species_images()
        pass

    def get_species_images(self):
        print("Initiating image search")
        observations = get_species_observations(self.species_name, self.license, self.filter_larvae)
        print(f'Found observations: {len(observations["results"])}')
        print("Downloading images, this might take a few minutes...")
        for result in observations['results']:
            for image in result['photos']:
                url = image['url'].replace('square', 'medium') if self.enlarge_image else image['url']
                response = requests.get(url)
                if 'content-type' in response.headers.keys():
                    filetype = response.headers['content-type'].split('/')[1]
                    self.file_manager.save_image(response, filetype)
                else:
                    self.file_manager.save_image(response)
        print(f"Found total of {self.file_manager.counter_images_saved} images!")
        return

def start():
    InaturalistBot()


if __name__ == '__main__':
    InaturalistBot()