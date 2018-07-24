class PersonDict():
    GENDER={
        "F":"8532",
        "M":"8507",
        "U":"8551"
    }
    RACE={
        "AMERICAN INDIAN OR ALASKA NATIVE":"8657",
        "ASIAN":"8515",
        "BLACK OR AFRICAN AMERICAN":"8516",
        "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER":"8557",
        "WHITE":"8527",
        "UNKNOWN/UNAVAILABLE":"8552",
        "HISPANIC":"4188159"
    }
class DeathDict:
    DEATHTYPE={
       "Unrelated to Disease":"173000",
       "Unrelated to Cancer but with Disease":"173003",
       "Unknown cause but with Disease":"173002",
       "Secondary Primary Cancer":"173004",
       "Complications of Treatment":"173001",
       "Primary Cancer":"4312326",
       "Unknown cause and unknown Disease Status":"441413"
    }
class ObservationDict:
    TREAMMENTlINE={
        "Adjuvant":"40272698",
        "1st Line":"45769570",
        "2nd Line":"45769571",
        "3rd Line":"45769572"
    }
class VisitOccurenceDict:

    VISITTYPE={
        "Visit derived from EHR record":"44818518"

    }
    VISIT={
        "Outpatient":"9202"
    }
class ConditionOccurrenceDict:
    CONDITION={
        "C186":"443382",
        "C180":"443391",
        "C183":"4180791",
        "C184":"443384",
        "C181":"443383",
        "C199":"4180792",
        "C187":"443381",
        "C182":"435754",
        "C185":"4181344"
    }
    SITE={
        "Soft Tissue":"4338971",
        "Lung":"4213162",
        "Local/Regional":"174003",
        "Liver":"4009105",
        "Bone":"4154333",
        "CNS":"4063669",
        "Lymph Nodes":"4241958",
        "Other":"9177"

    }
class ProcedureOccurrenceDict:
    TREAMMENTTYPE={
        "Chemotherapy":"4273629",
        "Radiation":"4220084"
    }
class VariantOccurrenceDict:
    TYPE = {
        "MSI":"172012",
        "PMS2":"172017",
        "MSH6":"172011",
        "MLH1":"172009",
        "BRAF":"172002",
        "EGFR":"172003",
        "PIK3CA":"172016",
        "KRAS":"172008",
        "MSH2":"172010",
        "NARS":"172013"
    }
class DrugExposureDict:
    Drug={
        "FOLFOX":"173005",
        "Bevacizumab":"173006",
        "Capecitabine":"173007",
        "Erbitux":"173008",
        "Irinotecan Hydrochloride":"173009",
        "Oxaliplatin":"173010",
        "Cetuximab":"173011",
        "Panitumumab":"173012",
        "FOLFIRI":"173013",
        "Fluorouracil":"173014",
        "Stivarga":"173015",
        "Mitomycin C":"173016",
        "Other Specified Antibiotics":"173010",
        "External Beam":"4036742"

    }
class IHCFields(object):
    BIOREPOSITORY_STUDY_NO=0
    AGE_AT_DX_YRS         =1
    BIRTH_DT              =2
    CANCER_STUDY_ID=3
    DIAGNOSIS_DT=4
    EMPI=5
    FCILTY_ID= 6
    SEX_CD= 7
    RACE_CD=8
    RACE_DSC=9
    DX_CODE_CD=10
    PRIMARY_HISTOLOGY_DSC=11
    GRADE_DSC=12
    PATH_STAGE_DSC=13
    TUMOR_SIZE_VAL=14
    NSN_EXAMINED_CNT= 15
    NSN_POSITIVE_CNT=16
    T_DSC=17
    N_DSC= 18
    M_DSC=19
    M_CLIN_DSC=20
    TEST_DT=21
    TEST_TYPE_DSC=22
    RESULT_DSC=23
    TX_TYPE_DSC=24
    TX_REASON_DSC=25
    AGENT_DSC=26
    START_DT=27
    END_DT=28
    PROGRESSION_DT=29
    DOSE_DELIVERY_DSC=30
    DOSE_VAL=31
    NO_TX_REASON_DSC=32
    PATIENT_STATUS_DSC=33
    DEATH_DT=34
    CAUSE_OF_DEATH_DSC=35
    RECURRENCE_DT=36
    RECURRENCE_SITE=37
