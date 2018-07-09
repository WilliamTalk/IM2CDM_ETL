
import pandas as pd
from Constants import  PersonDict,ProcedureOccurrenceDict
from Constants import  DeathDict,CaresiteDict,MeasurementDict,ObservationDict,VisitOccurenceDict,ConditionOccurrenceDict
from  Constants import  VariantOccurrenceDict,DrugExposureDict
import os
import  traceback

class Mapping:


    """
    constructor is to obtain the handler of the source data and all of destination table paths
    """
    def __init__(self,path):
        if os.path.exists(path):
            self.Intermountain=pd.read_csv(path)
        else:
            print("this path is not in the current directionary, please check the path!")
        #to save person dictionary (person_id:EMPI)
        self.Dict={}
        #to save sequencing dictionary
        self.DictSequencing={}
        #to save care site
        self.DictCareSite={}
    def CreateCareSite(self):
        table = {
            "care_site_id": [],
            "care_site_name": [],
            "location_id":[],
            "care_site_source_value": [],
            "place_of_service_concept_id": [],
            "place_of_service_source_value": []
        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["FCILTY_ID"]]
        #reomve the duplicate records
        lines = lines.drop_duplicates(["FCILTY_ID"])
        #reset the idnex of the dataframe
        lines=lines.reset_index()
        #
        for i in range(len(lines)):
            table["care_site_id"].append(i)
            table["care_site_name"].append(lines.loc[i, "FCILTY_ID"])
            self.DictCareSite[lines.loc[i, "FCILTY_ID"]]=i
            table["location_id"].append("")
            table["care_site_source_value"].append("")
            table["place_of_service_concept_id"].append("")
            table["place_of_service_source_value"].append("")

        # define the columns
        columns = [
            "care_site_id",
            "care_site_name",
            "location_id",
            "care_site_source_value",
            "place_of_service_concept_id",
            "place_of_service_source_value"
        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("CareSite.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreatePerson(self):

        #create a dictionanry for the table, every element in the dictionary is a list for the column
        table={
            "person_id": [],
            "person_source_value":[],
            "year_of_birth":[],
            "month_of_birth":[],
            "day_of_birth":[],
            "birth_datetime":[],
            "location_id":[],
            "provider_id":[],
            "care_site_id":[],
            "gender_concept_id":[],
            "gender_source_value":[],
            "gender_source_concept_id":[],
            "race_concept_id":[],
            "race_source_value":[],
            "race_source_concept_id":[],
            "ethnicity_concept_id":[],
            "ethnicity_source_value":[],
            "ethnicity_source_concept_id":[]
        }
        #select the neccesary columns from teh intermountain
        lines=self.Intermountain[["EMPI","BIRTH_DT","SEX_CD","RACE_DSC","FCILTY_ID"]]
        #remove the duplicate records
        lines=lines.drop_duplicates(["EMPI","BIRTH_DT","SEX_CD","RACE_DSC","FCILTY_ID"])
        #re-index for the data
        lines=lines.reset_index()

        for i in range(len(lines)):
            table["person_id"].append(i)
            table["person_source_value"].append(lines.loc[i, "EMPI"])
            self.Dict[lines.loc[i, "EMPI"]]=i
            #split birthday to year,month and day
            birthday=str(lines.loc[i, "BIRTH_DT"]).split('/')
            birthtime=str(lines.loc[i, "BIRTH_DT"])+" 00:00:00"
            table["year_of_birth"].append(birthday[0])
            table["month_of_birth"].append(birthday[1])
            table["day_of_birth"].append(birthday[2])
            table["birth_datetime"].append(birthtime)
            table["location_id"].append("")
            table["provider_id"].append("")
            table["care_site_id"].append(self.DictCareSite[lines.loc[i,"FCILTY_ID"]])
            table["gender_source_value"].append(lines.loc[i, "SEX_CD"])
            #find the concept_id  in dictionary of gender defined  in Constants
            table["gender_concept_id"].append(PersonDict.GENDER[lines.loc[i, "SEX_CD"]])
            table["gender_source_concept_id"].append("")
            table["race_source_value"].append(lines.loc[i, "RACE_DSC"])
            table["race_concept_id"].append(PersonDict.RACE[lines.loc[i, "RACE_DSC"].upper()])
            table["race_source_concept_id"].append("")
            table["ethnicity_concept_id"].append("")
            table["ethnicity_source_value"].append("")
            table["ethnicity_source_concept_id"].append("")

        #define the columns
        columns=[
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
        #define the dataFrame using the new table data and save them in its path
        df=pd.DataFrame(table)
        df.to_csv('Person.csv',sep=",",encoding="utf-8",index=False,columns=columns)

    def CreateConditionOccurrence(self):
        table = {
            "person_id":[],
            "condition_occurrence_id":[],
            "condition_start_date": [],
            "condition_start_datetime": [],
            "condition_end_date": [],
            "condition_end_datetime": [],
            "condition_concept_id": [],
            "condition_source_value": [],
            "condition_type_concept_id": [],
            "stop_reason":[],
            "provider_id":[],
            "visit_occurrence_id":[],
            "visit_detail_id":[],
            "condition_source_concept_id":[],
            "condition_status_source_value":[],
            "condition_status_concept_id":[]

        }
        #from RECURRENCE_DT and RECURRENCE_SITE
        lines = self.Intermountain[["EMPI","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL", "RECURRENCE_DT", "RECURRENCE_SITE"]]
        lines = lines.drop_duplicates(["EMPI","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL", "RECURRENCE_DT", "RECURRENCE_SITE"])
        lines = lines.reset_index()
        count=0
        for i in range(len(lines)):
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["condition_occurrence_id"].append(count)
            count=count+1
            table["condition_start_date"].append(lines.loc[i, "RECURRENCE_DT"])
            if not pd.isnull(lines.loc[i, "RECURRENCE_DT"]):
                table["condition_start_datetime"].append(str(lines.loc[i, "RECURRENCE_DT"]) + " 00:00:00")
            else:
                table["condition_start_datetime"].append("")
            table["condition_end_date"].append("")
            table["condition_end_datetime"].append("")
            table["condition_source_value"].append(lines.loc[i, "RECURRENCE_SITE"])
            table["condition_type_concept_id"].append("")
            if not pd.isnull(lines.loc[i, "RECURRENCE_SITE"]):
                table["condition_concept_id"].append(ConditionOccurrenceDict.SITE[lines.loc[i, "RECURRENCE_SITE"]])
            else:
                table["condition_concept_id"].append("")
            table["stop_reason"].append("")
            table["provider_id"].append("")
            table["visit_occurrence_id"].append(i)
            table["visit_detail_id"].append("")
            table["condition_source_concept_id"].append("")
            table["condition_status_source_value"].append("")
            table["condition_status_concept_id"].append("")
        # from DX_CODE_CD and DIAGNOSIS_DT
        lines = self.Intermountain[["EMPI", "DX_CODE_CD", "DIAGNOSIS_DT","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI", "DX_CODE_CD", "DIAGNOSIS_DT","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"])
        lines=lines.reset_index()
        for i in range(len(lines)):
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["condition_occurrence_id"].append(count)
            count=count+1
            table["condition_start_date"].append(lines.loc[i, "DIAGNOSIS_DT"])
            table["condition_start_datetime"].append(lines.loc[i, "DIAGNOSIS_DT"]+" 00:00:00")
            table["condition_end_date"].append("")
            table["condition_end_datetime"].append("")
            table["condition_source_value"].append(lines.loc[i,"DX_CODE_CD"])
            table["condition_type_concept_id"].append("")
            table["condition_concept_id"].append(ConditionOccurrenceDict.CONDITION[lines.loc[i,"DX_CODE_CD"]])
            table["stop_reason"].append("")
            table["provider_id"].append("")
            table["visit_occurrence_id"].append(i)
            table["visit_detail_id"].append("")
            table["condition_source_concept_id"].append("")
            table["condition_status_source_value"].append("")
            table["condition_status_concept_id"].append("")

        # define the columns
        columns = [
            "person_id",
            "condition_occurrence_id",
            "condition_start_date",
            "condition_concept_id",
            "condition_source_value",
            "condition_type_concept_id",
            "stop_reason",
            "provider_id",
            "visit_occurrence_id",
            "visit_detail_id",
            "condition_source_concept_id",
            "condition_status_source_value",
            "condition_status_concept_id"

        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df=df.dropna(subset=["condition_start_date"])
        df.to_csv("ConditionOccurrence.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateObservation(self):
        table = {

            "observation_id": [],
            "person_id": [],
            "observation_concept_id": [],
            "observation_date": [],
            "observation_datetime": [],
            "observation_type_concept_id": [],
            "value_as_number": [],
            "value_as_string": [],
            "value_as_concept_id": [],
            "qualifier_concept_id": [],
            "unit_concept_id": [],
            "provider_id": [],
            "visit_occurrence_id": [],
            "visit_detail_id": [],
            "observation_source_value": [],
            "observation_source_concept_id": [],
            "unit_source_value": [],
            "qualifier_source_value":[]

        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","FCILTY_ID", "TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI","FCILTY_ID", "TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"])
        lines=lines.reset_index()
        #
        for i in range(len(lines)):
            table["observation_id"].append(i)
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["observation_date"].append(lines.loc[i,"START_DT"])
            if not pd.isnull(lines.loc[i,"START_DT"]):
                table["observation_datetime"].append(lines.loc[i,"START_DT"]+" 00:00:00")
            else:
                table["observation_datetime"].append("")
            table["observation_concept_id"].append("4176642")
            if not pd.isnull(lines.loc[i, "TX_REASON_DSC"]):
                #table["observation_type_concept"].append(lines.loc[i, "TX_REASON_DSC"])
                table["observation_type_concept_id"].append(ObservationDict.TREAMMENTlINE[lines.loc[i, "TX_REASON_DSC"]])
            else:
                #table["observation_type_concept"].append("")
                table["observation_type_concept_id"].append("")
            table["value_as_number"].append("")
            table["value_as_string"].append("")
            table["value_as_concept_id"].append("")
            table["qualifier_concept_id"].append("")
            table["unit_concept_id"].append("")
            table["provider_id"].append("")
            table["visit_occurrence_id"].append(i)
            table["visit_detail_id"].append("")
            table["observation_source_value"].append("")
            table["observation_source_concept_id"].append("")
            table["unit_source_value"].append("")
            table["qualifier_source_value"].append("")


        # define the columns
        columns = [

            "observation_id",
            "person_id",
            "observation_concept_id",
            "observation_date",
            "observation_datetime",
            "observation_type_concept_id",
            "value_as_number",
            "value_as_string",
            "value_as_concept_id",
            "qualifier_concept_id",
            "unit_concept_id",
            "provider_id",
            "visit_occurrence_id",
            "visit_detail_id",
            "observation_source_value",
            "observation_source_concept_id",
            "unit_source_value",
            "qualifier_source_value"

        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("Observation.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateDeath(self):
        table = {
            "person_id": [],
            "death_date": [],
            "death_datetime":[],
            "cause_concept_id": [],
            "cause_source_value": [],
            "cause_source_concept_id":[],
            "death_type_concept_id":[]

        }
        # select the neccesary columns from teh intermountain and remove thPATIENT_STATUS_DSCe duplicate records
        lines = self.Intermountain[["EMPI", "PATIENT_STATUS_DSC","DEATH_DT", "CAUSE_OF_DEATH_DSC"]]
        #lines = lines.dropna().drop_duplicates(["EMPI", "DEATH_DT", "CAUSE_OF_DEATH_DSC"])
        #selectc distinct records and PATIENT_STATUS_DSC=Dead
        lines = lines.loc[lines["PATIENT_STATUS_DSC"] == "Dead"].drop_duplicates(["EMPI","PATIENT_STATUS_DSC", "DEATH_DT", "CAUSE_OF_DEATH_DSC"])
        lines=lines.reset_index()
        #
        for i in range(len(lines)):
            table["person_id"].append(self.Dict[lines.loc[i,"EMPI"]])
            table["death_date"].append(lines.loc[i, "DEATH_DT"])
            table["death_datetime"].append(lines.loc[i, "DEATH_DT"]+" 00:00:00")
            table["cause_source_value"].append(lines.loc[i, "CAUSE_OF_DEATH_DSC"])
            table["cause_concept_id"].append(DeathDict.DEATHTYPE[lines.loc[i,"CAUSE_OF_DEATH_DSC"]])
            table["death_type_concept_id"].append("")
            table["cause_source_concept_id"].append("")

        # define the columns
        columns = [
            "person_id",
            "death_date",
            "death_datetime",
            "cause_concept_id",
            "cause_source_value",
            "cause_source_concept_id",
            "death_type_concept_id"
        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("Death.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateVisitOccurrence(self):
        table = {
            "visit_occurrence_id": [],
            "person_id": [],
            "visit_concept_id": [],
            "visit_start_date": [],
            "visit_start_datetime": [],
            "visit_end_date": [],
            "visit_end_datetime": [],
            "visit_type_concept_id": [],
            #"visit_type_concept_id": [],
            "provider_id": [],
            "care_site_id": [],
            "visit_source_value": [],
            "visit_source_concept_id": [],
            "admitting_source_concept_id": [],
            "admitting_source_value": [],
            "discharge_to_concept_id": [],
            "discharge_to_source_value": [],
            "preceding_visit_occurrence_id":[]

        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","FCILTY_ID", "TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI","FCILTY_ID","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"])
        lines=lines.reset_index()
        #
        for i in range(len(lines)):
            table["visit_occurrence_id"].append(i)
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["visit_concept_id"].append("")
            table["visit_start_date"].append(lines.loc[i, "START_DT"])
            if not pd.isnull(lines.loc[i, "START_DT"]):
               table["visit_start_datetime"].append(str(lines.loc[i, "START_DT"])+" 00:00:00")
            else:
                table["visit_start_datetime"].append("")
            table["visit_end_date"].append(lines.loc[i, "END_DT"])
            if not pd.isnull(lines.loc[i, "START_DT"]):
                table["visit_end_datetime"].append(str(lines.loc[i, "END_DT"])+" 00:00:00")
            else:
                table["visit_end_datetime"].append("")
            table["visit_type_concept_id"].append(VisitOccurenceDict.VISITTYPE[lines.loc[i, "TX_TYPE_DSC"]])
            #table["visit_type_concept_id"].append("")
            table["provider_id"].append("")
            table["care_site_id"].append(self.DictCareSite[lines.loc[i, "FCILTY_ID"]])
            table["visit_source_value"].append("")
            table["visit_source_concept_id"].append("")
            table["admitting_source_concept_id"].append("")
            table["admitting_source_value"].append("")
            table["discharge_to_concept_id"].append("")
            table["discharge_to_source_value"].append("")
            table["preceding_visit_occurrence_id"].append("")

            # define the columns
        columns = [

            "visit_occurrence_id",
            "person_id",
            "visit_concept_id",
            "visit_start_date",
            "visit_start_datetime",
            "visit_end_date",
            "visit_end_datetime",
            "visit_type_concept_id",
            #"visit_type_concept_id",
            "provider_id",
            "care_site_id",
            "visit_source_value",
            "visit_source_concept_id",
            "admitting_source_concept_id",
            "admitting_source_value",
            "discharge_to_concept_id",
            "discharge_to_source_value",
            "preceding_visit_occurrence_id"

        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("VisitOccurrence.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateSequencing(self):
        table = {
            "sequencing_id": [],
            "person_id": [],
            "sequencing_date": [],
            "order_date": [],
            "order_code": [],
            "procedure_id": [],
            "specimen_id": [],
            "note_id": [],
            "device_concept_id": [],
            "device_source_value": [],
            "library_preparation_concept_id": [],
            "library_preparation_source_value": [],
            "target_capture_concept_id": [],
            "target_capture_source_value": [],
            "read_type_concept_id": [],
            "read_type_source_value": [],
            "read_length": [],
            "alignment_tools_concept_id": [],
            "alignment_tools_source_value": [],
            "variant_calling_tools_concept_id": [],
            "variant_calling_tools_source_val": [],
            "annotation_tools_concept_id": [],
            "annotation_tools_source_value": [],
            "annotation_databases_concept_id": [],
            "annotation_databases_source_value": [],
            "chromosome_coordinate_concept_id": [],
            "specimen_type_concept_id": [],
            "specimen_type_source_value": [],
            "source_class_concept_id": [],
            "source_class_source_value": [],
            "tissue_type_concept_id": [],
            "tissue_type_source_value": [],
            "tumor_purity": [],
            "reference_genome": [],
            "pathologic_diagnosis_concept_id": [],
            "pathologic_diagnosis_source_value": [],
            "staging_t": [],
            "staging_n": [],
            "staging_m": [],
            "stage_reference": []
        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","TEST_DT"]]
        lines = lines.dropna().drop_duplicates(["EMPI","TEST_DT"])
        lines=lines.reset_index()

        for i in range(len(lines)):
            key=str(lines.loc[i, "EMPI"])+str(lines.loc[i, "TEST_DT"])
            self.DictSequencing[key]=i
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["sequencing_id"].append(i)
            table["sequencing_date"].append(lines.loc[i,"TEST_DT"])
            table["order_date"].append("")
            table["order_code"].append("")
            table["procedure_id"].append("")
            table["specimen_id"].append("")
            table["note_id"].append("")
            table["device_concept_id"].append("")
            table["device_source_value"].append("")
            table["library_preparation_concept_id"].append("")
            table["library_preparation_source_value"].append("")
            table["target_capture_concept_id"].append("")
            table["target_capture_source_value"].append("")
            table["read_type_concept_id"].append("")
            table["read_type_source_value"].append("")
            table["read_length"].append("")
            table["alignment_tools_concept_id"].append("")
            table["alignment_tools_source_value"].append("")
            table["variant_calling_tools_concept_id"].append("")
            table["variant_calling_tools_source_val"].append("")
            table["annotation_tools_concept_id"].append("")
            table["annotation_tools_source_value"].append("")
            table["annotation_databases_concept_id"].append("")
            table["annotation_databases_source_value"].append("")
            table["chromosome_coordinate_concept_id"].append("")
            table["specimen_type_concept_id"].append("")
            table["specimen_type_source_value"].append("")
            table["source_class_concept_id"].append("")
            table["source_class_source_value"].append("")
            table["tissue_type_concept_id"].append("")
            table["tissue_type_source_value"].append("")
            table["tumor_purity"].append("")
            table["reference_genome"].append("")
            table["pathologic_diagnosis_concept_id"].append("")
            table["pathologic_diagnosis_source_value"].append("")
            table["staging_t"].append("")
            table["staging_n"].append("")
            table["staging_m"].append("")
            table["stage_reference"].append("")


        # define the columns
        columns = [
            "sequencing_id",
            "person_id",
            "sequencing_date",
            "order_date",
            "order_code",
            "procedure_id",
            "specimen_id",
            "note_id",
            "device_concept_id",
            "device_source_value",
            "library_preparation_concept_id",
            "library_preparation_source_value",
            "target_capture_concept_id",
            "target_capture_source_value",
            "read_type_concept_id",
            "read_type_source_value",
            "read_length",
            "alignment_tools_concept_id",
            "alignment_tools_source_value",
            "variant_calling_tools_concept_id",
            "variant_calling_tools_source_val",
            "annotation_tools_concept_id",
            "annotation_tools_source_value",
            "annotation_databases_concept_id",
            "annotation_databases_source_value",
            "chromosome_coordinate_concept_id",
            "specimen_type_concept_id",
            "specimen_type_source_value",
            "source_class_concept_id",
            "source_class_source_value",
            "tissue_type_concept_id",
            "tissue_type_source_value",
            "tumor_purity",
            "reference_genome",
            "pathologic_diagnosis_concept_id",
            "pathologic_diagnosis_source_value",
            "staging_t",
            "staging_n",
            "staging_m",
            "stage_reference"
        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("Sequencing.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateVariantOccurrence(self):

        table = {
            "variant_occurrence_id": [],
            "person_id": [],
            "sequencing_id": [],
            "variant_type_concept_id": [],
            "variant_type_source_value": [],
            "variant_function_concept_id": [],
            "chrid_1": [],
            "chrid_2": [],
            "start_pos": [],
            "end_pos": [],
            "gene1_symbol_concept_id": [],
            "gene1_symbol_source_value": [],
            "gene2_symbol_concept_id": [],
            "gene2_symbol_source_value": [],
            "quality_score": [],
            "genotype": [],
            "copy_number": [],
            "exon_number": [],
            "hgvs_nomenclature": [],
            "hgvs_p": [],
            "read_depth": [],
            "allele_frequency": [],
            "allele_frequency_reference": []
        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","TEST_DT","TEST_TYPE_DSC","RESULT_DSC"]].drop_duplicates(["EMPI","TEST_DT","TEST_TYPE_DSC","RESULT_DSC"])
        lines = lines.loc[lines["RESULT_DSC"] == "Positive"]
        lines=lines.reset_index()
        for i in range(len(lines)):
            key = str(lines.loc[i, "EMPI"]) + str(lines.loc[i, "TEST_DT"])
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["variant_occurrence_id"].append(i)
            table["sequencing_id"].append(self.DictSequencing[key])
            table["variant_type_concept_id"].append("")
            table["variant_type_source_value"].append("")
            table["variant_function_concept_id"].append("")
            table["chrid_1"].append("")
            table["chrid_2"].append("")
            table["start_pos"].append("")
            table["end_pos"].append("")
            table["gene1_symbol_concept_id"].append(VariantOccurrenceDict.TYPE[lines.loc[i,"TEST_TYPE_DSC"]])
            table["gene1_symbol_source_value"].append(lines.loc[i,"TEST_TYPE_DSC"])
            table["gene2_symbol_concept_id"].append(VariantOccurrenceDict.TYPE[lines.loc[i,"TEST_TYPE_DSC"]])
            table["gene2_symbol_source_value"].append(lines.loc[i, "TEST_TYPE_DSC"])
            table["quality_score"].append("")
            table["genotype"].append("")
            table["copy_number"].append("")
            table["exon_number"].append("")
            table["hgvs_nomenclature"].append("")
            table["hgvs_p"].append("")
            table["read_depth"].append("")
            table["allele_frequency"].append("")
            table["allele_frequency_reference"].append("")

            # define the columns
        columns = [

            "variant_occurrence_id",
            "person_id",
            "sequencing_id",
            "variant_type_concept_id",
            "variant_type_source_value",
            "variant_function_concept_id",
            "chrid_1",
            "chrid_2",
            "start_pos",
            "end_pos",
            "gene1_symbol_concept_id",
            "gene1_symbol_source_value",
            "gene2_symbol_concept_id",
            "gene2_symbol_source_value",
            "quality_score",
            "genotype",
            "copy_number",
            "exon_number",
            "hgvs_nomenclature",
            "hgvs_p",
            "read_depth",
            "allele_frequency",
            "allele_frequency_reference"
        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("VariantOccurrence.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateProcedureOccurrence(self):

        table = {
            "procedure_occurrence_id": [],
            "person_id": [],
            "procedure_concept_id": [],
            "procedure_date": [],
            "procedure_datetime": [],
            "procedure_type_concept_id": [],
            "modifier_concept_id": [],
            "quantity": [],
            "provider_id": [],
            "visit_occurrence_id": [],
            "visit_detail_id": [],
            "procedure_source_value": [],
            "procedure_source_concept_id": [],
            "modifier_source_value":[]

        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI","TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"])
        lines=lines.reset_index()
        #
        for i in range(len(lines)):
            table["procedure_occurrence_id"].append(i)
            table["procedure_concept_id"].append(ProcedureOccurrenceDict.TREAMMENTTYPE[lines.loc[i, "TX_TYPE_DSC"]])
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["procedure_date"].append("")
            table["procedure_datetime"].append("")
            table["procedure_type_concept_id"].append("4322976")
            table["modifier_concept_id"].append("")
            table["quantity"].append("")
            table["provider_id"].append("")
            table["visit_occurrence_id"].append(i)
            table["visit_detail_id"].append("")
            table["procedure_source_value"].append(lines.loc[i, "TX_TYPE_DSC"])
            table["procedure_source_concept_id"].append("")
            table["modifier_source_value"].append("")

        # define the columns
        columns = [
            "procedure_occurrence_id",
            "person_id",
            "procedure_concept_id",
            "procedure_date",
            "procedure_datetime",
            "procedure_type_concept_id",
            "modifier_concept_id",
            "quantity",
            "provider_id",
            "visit_occurrence_id",
            "visit_detail_id",
            "procedure_source_value",
            "procedure_source_concept_id",
            "modifier_source_value"

        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("ProcedureOccurrence.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateDrugExposure(self):
        table = {
            "drug_exposure_id": [],
            "person_id": [],
            "drug_concept_id": [],
            "drug_exposure_start_date": [],
            "drug_exposure_start_time": [],
            "drug_exposure_end_date": [],
            "drug_exposure_end_time": [],
            "verbatim_end_date": [],
            "drug_type_concept_id": [],
            "stop_reason": [],
            "refills": [],
            "quantity": [],
            "days_supply": [],
            "sig": [],
            "route_concept_id": [],
            "lot_number": [],
            "provider_id": [],
            "visit_occurrence_id": [],
            "visit_detail_id": [],
            "drug_source_value": [],
            "drug_source_concept_id": [],
            "route_source_value": [],
            "dose_unit_source_value":[]
        }
        "EMPI", "FCILTY_ID", "TX_TYPE_DSC", "TX_REASON_DSC", "AGENT_DSC", "START_DT", "END_DT", "PROGRESSION_DT", "DOSE_DELIVERY_DSC", "DOSE_VAL"
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","FCILTY_ID", "TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI","FCILTY_ID", "TX_TYPE_DSC","TX_REASON_DSC","AGENT_DSC","START_DT","END_DT","PROGRESSION_DT","DOSE_DELIVERY_DSC","DOSE_VAL"])
        lines=lines.reset_index()
        #
        for i in range(len(lines)):
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["drug_exposure_id"].append(i)
            if not pd.isnull(lines.loc[i, "AGENT_DSC"]):
             table["drug_concept_id"].append(DrugExposureDict.Drug[str(lines.loc[i,"AGENT_DSC"]).strip()])
            elif not pd.isnull(lines.loc[i, "DOSE_DELIVERY_DSC"]):
                table["drug_concept_id"].append(DrugExposureDict.Drug[lines.loc[i,"DOSE_DELIVERY_DSC"]])
            else:
                table["drug_concept_id"].append("")

            table["drug_exposure_start_date"].append(lines.loc[i, "START_DT"])
            if not pd.isnull(lines.loc[i, "START_DT"]):
               table["drug_exposure_start_time"].append(lines.loc[i, "START_DT"]+" 00:00:00")
            else:
                table["drug_exposure_start_time"].append("")

            table["drug_exposure_end_date"].append(lines.loc[i, "END_DT"])
            if not pd.isnull(lines.loc[i, "END_DT"]):
              table["drug_exposure_end_time"].append(lines.loc[i, "END_DT"]+" 00:00:00")
            else:
                table["drug_exposure_end_time"].append("")
            table["verbatim_end_date"].append("")
            table["drug_type_concept_id"].append("")
            table["stop_reason"].append("")
            table["refills"].append("")
            table["quantity"].append(lines.loc[i, "DOSE_VAL"])
            table["days_supply"].append("")
            table["sig"].append(""),
            table["route_concept_id"].append("")
            table["lot_number"].append("")
            table["provider_id"].append("")
            table["visit_occurrence_id"].append(i)
            table["visit_detail_id"].append("")
            table["drug_source_value"].append(lines.loc[i,"AGENT_DSC"])
            table["drug_source_concept_id"].append("")
            table["route_source_value"].append("")
            table["dose_unit_source_value"].append(lines.loc[i, "DOSE_VAL"])

        # define the columns
        columns = [
            "drug_exposure_id",
            "person_id",
            "drug_concept_id",
            "drug_exposure_start_date",
            "drug_exposure_start_time",
            "drug_exposure_end_date",
            "drug_exposure_end_time",
            "verbatim_end_date",
            "drug_type_concept_id",
            "stop_reason",
            "refills",
            "quantity",
            "days_supply",
            "sig",
            "route_concept_id",
            "lot_number",
            "provider_id",
            "visit_occurrence_id",
            "visit_detail_id",
            "drug_source_value",
            "drug_source_concept_id",
            "route_source_value",
            "dose_unit_source_value",

        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        #remove the records where drug_concept_id is null
        df=df.dropna(subset=['drug_concept_id'])
        df.to_csv("DrugExposure.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def CreateMeasurement(self):

        table = {
                "measurement_id": [],
                "person_id": [],
                "measurement_concept_id": [],
                "measurement_date": [],
                "measurement_datetime": [],
                "measurement_time": [],
                "measurement_type_concept_id":[],
                "operator_concept_id": [],
                "value_as_number": [],
                "value_as_concept_id": [],
                "unit_concept_id": [],
                "range_low": [],
                "range_high": [],
                "provider_id": [],
                "visit_occurrence_id": [],
                "visit_detail_id": [],
                "measurement_source_value": [],
                "measurement_source_concept_id": [],
                "unit_source_value": [],
                "value_source_value":[]

        }
        # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI", "PRIMARY_HISTOLOGY_DSC", "GRADE_DSC","TUMOR_SIZE_VAL","PATH_STAGE_DSC","T_DSC","N_DSC","M_DSC","M_CLIN_DSC",
                                    "TX_TYPE_DSC", "TX_REASON_DSC", "AGENT_DSC", "START_DT", "END_DT", "PROGRESSION_DT",
                                    "DOSE_DELIVERY_DSC", "DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI", "PRIMARY_HISTOLOGY_DSC", "GRADE_DSC","TUMOR_SIZE_VAL","PATH_STAGE_DSC","T_DSC","N_DSC","M_DSC","M_CLIN_DSC",
                                       "TX_TYPE_DSC", "TX_REASON_DSC", "AGENT_DSC", "START_DT", "END_DT",
                                       "PROGRESSION_DT", "DOSE_DELIVERY_DSC", "DOSE_VAL"])
        lines=lines.reset_index()
        count=0

        for i in range(len(lines)):
            if not pd.isnull(lines.loc[i, "PRIMARY_HISTOLOGY_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("171001")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "PRIMARY_HISTOLOGY_DSC"])

            if not pd.isnull(lines.loc[i, "GRADE_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4197325")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "GRADE_DSC"])
            if not pd.isnull(lines.loc[i, "TUMOR_SIZE_VAL"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4139794")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "TUMOR_SIZE_VAL"])
            if not pd.isnull(lines.loc[i, "PATH_STAGE_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4226407")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "PATH_STAGE_DSC"])
            if not pd.isnull(lines.loc[i, "M_CLIN_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4221079")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "M_CLIN_DSC"])

            if not pd.isnull(lines.loc[i, "T_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4233793")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "T_DSC"])

            if not pd.isnull(lines.loc[i, "N_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4233793")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "N_DSC"])

            if not pd.isnull(lines.loc[i, "M_DSC"]):
                table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
                table["measurement_id"].append(count)
                count = count + 1
                table["measurement_concept_id"].append("4233793")
                table["measurement_date"].append("")
                table["measurement_datetime"].append("")
                table["measurement_time"].append(""),
                table["measurement_type_concept_id"].append("45876052")
                table["operator_concept_id"].append("")
                table["value_as_number"].append("")
                table["value_as_concept_id"].append("")
                table["unit_concept_id"].append("")
                table["range_low"].append("")
                table["range_high"].append("")
                table["provider_id"].append("")
                table["visit_occurrence_id"].append(i)
                table["visit_detail_id"].append("")
                table["measurement_source_value"].append("")
                table["measurement_source_concept_id"].append("")
                table["unit_source_value"].append("")
                table["value_source_value"].append(lines.loc[i, "M_DSC"])
                # select the neccesary columns from teh intermountain and remove the duplicate records
        lines = self.Intermountain[["EMPI","TX_TYPE_DSC", "TX_REASON_DSC", "AGENT_DSC", "START_DT", "END_DT",
                                       "PROGRESSION_DT", "DOSE_DELIVERY_DSC", "DOSE_VAL"]]
        lines = lines.drop_duplicates(["EMPI","TX_TYPE_DSC", "TX_REASON_DSC", "AGENT_DSC", "START_DT", "END_DT",
                                       "PROGRESSION_DT", "DOSE_DELIVERY_DSC", "DOSE_VAL"])
        lines = lines.reset_index()
        for i in range(len(lines)):
            table["person_id"].append(self.Dict[lines.loc[i, "EMPI"]])
            table["measurement_id"].append(count)
            count = count + 1
            table["measurement_concept_id"].append("4168352")
            table["measurement_date"].append(lines.loc[i,"PROGRESSION_DT"])
            if not pd.isnull(lines.loc[i,"PROGRESSION_DT"]):
               table["measurement_datetime"].append(str(lines.loc[i,"PROGRESSION_DT"])+" 00:00:00")
            else:
               table["measurement_datetime"].append("")
            table["measurement_time"].append(""),
            table["measurement_type_concept_id"].append("4322976")
            table["operator_concept_id"].append("")
            table["value_as_number"].append("")
            table["value_as_concept_id"].append("")
            table["unit_concept_id"].append("")
            table["range_low"].append("")
            table["range_high"].append("")
            table["provider_id"].append("")
            table["visit_occurrence_id"].append(i)
            table["visit_detail_id"].append("")
            table["measurement_source_value"].append("")
            table["measurement_source_concept_id"].append("4168352")
            table["unit_source_value"].append("")
            table["value_source_value"].append("")

        # define the columns
        columns = [
                  "measurement_id",
                  "person_id",
                  "measurement_concept_id",
                  "measurement_date",
                  "measurement_datetime",
                  "measurement_time",
                  "measurement_type_concept_id",
                  "operator_concept_id",
                  "value_as_number",
                  "value_as_concept_id",
                  "unit_concept_id",
                  "range_low",
                  "range_high",
                  "provider_id",
                  "visit_occurrence_id",
                  "visit_detail_id",
                  "measurement_source_value",
                  "measurement_source_concept_id",
                  "unit_source_value",
                  "value_source_value"
        ]
        # define the dataFrame using the new table data and save them in its path
        df = pd.DataFrame(table)
        df.to_csv("Measurement.csv", sep=",", encoding="utf-8", index=False, columns=columns)

    def workflow(self):
        funlst=[self.CreateCareSite(),self.CreatePerson(),self.CreateConditionOccurrence(),self.CreateObservation(),self.CreateDeath(),
                self.CreateVisitOccurrence(),self.CreateSequencing(),self.CreateVariantOccurrence(),
                self.CreateProcedureOccurrence(),self.CreateDrugExposure(),self.CreateMeasurement()]
        print("transform si in processing ")

        for func in funlst:
            func

        print("transform is completed")

if __name__=="__main__":
   #please put the csv file in the same directionary with this  scripts
    m=Mapping("data/ihc_sample.csv")
    m.workflow()
    m.CreatePerson()
    # m.CreateSequencing()
    # m.CreateVariantOccurrence()





