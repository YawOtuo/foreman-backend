from core.models import Constituency, Area

# Constituency and their respective areas
from .constituencyareas import constituency_area_mapping

def populate_constituencies_and_areas():
    for constituency_name, areas in constituency_area_mapping.items():
        # Create or get the Constituency
        constituency, created = Constituency.objects.get_or_create(name=constituency_name)
        
        # Create areas for the constituency
        for area_name in areas:
            Area.objects.get_or_create(name=area_name, constituency=constituency)
    
    print("Constituencies and areas populated successfully!")

# Call the function to populate the database
populate_constituencies_and_areas()
