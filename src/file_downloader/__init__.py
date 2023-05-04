import os


class FileDownloader:

    def __init__(self, species: str):
        self.dirname = None
        self.species_name = species.lower().replace(' ', '_')
        self.make_species_folder(self.species_name)
        self.counter_images_saved = 0

    def make_species_folder(self, species):
        repo_path = f'{os.getcwd()}'
        dirname = os.path.join(repo_path, 'files')
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        self.dirname = os.path.join(dirname, species)
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def save_image(self, img_response, filetype='png'):
        self.counter_images_saved += 1
        filename=f'{self.species_name}_{self.counter_images_saved}.{filetype}'
        filepath_full = os.path.join(self.dirname, filename)

        file = open(filepath_full, "wb")
        file.write(img_response.content)
        file.close()

