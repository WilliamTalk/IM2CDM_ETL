from Records import Record
from FileControl import  FileControl
from Table_ID_Value import  Table_ID_Values
person_id={}
care_site_id={}
basedictionary="F:/dome/IM2CDM_ETL"

def writeCareSite(data):
    # define the columns
    columns = [
        "care_site_id",
        "care_site_name",
        "location_id",
        "care_site_source_value",
        "place_of_service_concept_id",
        "place_of_service_source_value"
    ]
    personwriter = FileControl(basedictionary, "CareSite", "w", columns)
    personwriter.write2Table(data)


def writePerson():
    # define the columns
    columns = [
        "organization_id",
        "person_id",
        "person_source_value",
        "year_of_birth",
        "month_of_birth",
        "day_of_birth",
        "birth_datetime",
        "location_id",
        "provider_id",
        "care_site_id",
        "gender_concept_id",
        "gender_source_value",
        "gender_source_concept_id",
        "race_concept_id",
        "race_source_value",
        "race_source_concept_id",
        "ethnicity_concept_id",
        "ethnicity_source_value",
        "ethnicity_source_concept_id"
    ]
    personwriter = FileControl(basedictionary, "Person", "w", columns)
    personwriter.write2Table()

class Process(object):
    pass

