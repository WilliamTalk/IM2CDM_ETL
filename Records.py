from Constants import IHCFields
class Record:
    def __init__(self,line):
        self.line=line

    @property
    def birthday(self):
        return self.line[IHCFields.BIRTH_DT]
    @property
    def diagnosisDate(self):
        return self.line[IHCFields.DIAGNOSIS_DT]
    @property
    def empi(self):
        return self.line[IHCFields.EMPI]
    @property
    def facilityID(self):
        return self.line[IHCFields.FCILTY_ID]
    @property
    def sex(self):
        return  self.line[IHCFields.SEX_CD]
    @property
    def race(self):
        return self.line[IHCFields.RACE_DSC]
    @property
    def diagnosisCode(self):
        return self.line[IHCFields.DX_CODE_CD]
    @property
    def primaryHistology(self):
        return self.line[IHCFields.PRIMARY_HISTOLOGY_DSC]
    @property
    def grade(self):
        return self.line[IHCFields.GRADE_DSC]
    @property
    def pathStage(self):
        return self.line[IHCFields.PATH_STAGE_DSC]
    @property
    def tumorSize(self):
        return self.line[IHCFields.TUMOR_SIZE_VAL]
    @property
    def stageT(self):
        return self.line[IHCFields.T_DSC]
    @property
    def stageN(self):
        return self.line[IHCFields.N_DSC]
    @property
    def stageM(self):
        return self.line[IHCFields.M_DSC]
    @property
    def clinicM(self):
        return self.line[IHCFields.M_CLIN_DSC]
    @property
    def testDate(self):
        return self.line[IHCFields.TEST_DT]
    @property
    def testType(self):
        return self.line[IHCFields.TEST_TYPE_DSC]
    @property
    def result(self):
        return self.line[IHCFields.RESULT_DSC]
    @property
    def treatmentType(self):
        return self.line[IHCFields.TX_TYPE_DSC]
    @property
    def treatmentLine(self):
        return self.line[IHCFields.TX_REASON_DSC]
    @property
    def agent(self):
        return self.line[IHCFields.AGENT_DSC]
    @property
    def startDate(self):
        return self.line[IHCFields.START_DT]
    @property
    def endDate(self):
        return self.line[IHCFields.END_DT]
    @property
    def progressionDate(self):
        return self.line[IHCFields.PROGRESSION_DT]
    @property
    def doseDelivery(self):
        return self.line[IHCFields.DOSE_DELIVERY_DSC]
    @property
    def doseValue(self):
        return self.line[IHCFields.DOSE_VAL]
    @property
    def status(self):
        return self.line[IHCFields.PATIENT_STATUS_DSC]
    @property
    def deathDate(self):
        return self.line[IHCFields.DEATH_DT]
    @property
    def causeofDeath(self):
        return self.line[IHCFields.CAUSE_OF_DEATH_DSC]
    @property
    def recurrenceDate(self):
        return self.line[IHCFields.RECURRENCE_DT]
    @property
    def recurrenceSite(self):
        return self.line[IHCFields.RECURRENCE_SITE]








