class Table_ID_Values(object):
    def __init__(self):
        self.last_condition_occurrence_id = 1
        self.last_drug_exposure_id = 1
        self.last_location_id = 1
        self.last_measurement_id = 1
        self.last_observation_id = 1
        self.last_person_id = 1
        self.last_procedure_occurrence_id = 1
        self.last_visit_occurrence_id = 1
        self.last_care_site_id = 1
        self.last_variant_occurrence_id=1
        self.last_sequencing_id=1


    def Load(self, filename):
        with open(filename,'r') as f_in:
            line = f_in.readline()
            flds = line.split("\t")
            if len(flds) == 11:
                self.last_condition_occurrence_id = int(flds[0])
                self.last_drug_exposure_id = int(flds[1])
                self.last_location_id = int(flds[2])
                self.last_measurement_id = int(flds[3])
                self.last_observation_id = int(flds[4])
                self.last_person_id = int(flds[5])
                self.last_procedure_occurrence_id = int(flds[6])
                self.last_visit_occurrence_id = int(flds[7])
                self.last_care_site_id = int(flds[8])
                self.last_visit_occurrence_id =int(flds[9])
                self.last_sequencing_id = int(flds[10])


    def Save(self, filename):
        with open(filename,'w') as f_out:

            f_out.write('{0}\t'.format(self.last_condition_occurrence_id))
            f_out.write('{0}\t'.format(self.last_drug_exposure_id))
            f_out.write('{0}\t'.format(self.last_location_id))
            f_out.write('{0}\t'.format(self.last_measurement_id))
            f_out.write('{0}\t'.format(self.last_observation_id))
            f_out.write('{0}\t'.format(self.last_person_id))
            f_out.write('{0}\t'.format(self.last_procedure_occurrence_id))
            f_out.write('{0}\t'.format(self.last_visit_occurrence_id))
            f_out.write('{0}\t'.format(self.last_care_site_id))
            f_out.write('{0}\t'.format(self.last_visit_occurrence_id))
            f_out.write('{0}\t'.format(self.last_sequencing_id))
            f_out.write('\n')
