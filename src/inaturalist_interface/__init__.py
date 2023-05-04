from pyinaturalist import *


def get_species_observations(species: str, observation_license, search_larvae=False) -> dict:
    if search_larvae:
        search_result = get_observations(taxon_name=species,
                                         license=observation_license,
                                         photos=True,
                                         per_page=300,
                                         term_id=1,
                                         term_value_id='6')
    else:
        search_result = get_observations(taxon_name=species,
                                         license=observation_license,
                                         photos=True,
                                         per_page=300)
    return search_result




