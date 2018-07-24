class Table_last_ids():
    def __init__(self,filename):
        self.filename=filename

    def load(self):
        with open(self.filename,"r") as f:
            line=f.readline()
            ids=line.split(",")
            self.last_caresite_id=int(ids[0])
            self.last_person_id = int(ids[1])
            self.last_visitoccurrence_id = int(ids[2])
            self.last_conditionoccurrence_id = int(ids[3])
            self.last_observation_id = int(ids[4])
            self.last_death_id = int(ids[5])
            self.last_sequencing_id = int(ids[6])
            self.last_variantoccurrence_id = int(ids[7])
            self.last_procedureoccurrence_id = int(ids[8])
            self.last_drugexposure_id = int(ids[9])
            self.last_measurement_id = int(ids[10])

    def save(self):
        with open(self.filename,"w") as f_out:
            f_out.write('{0},'.format(self.last_caresite_id))
            f_out.write('{0},'.format(self.last_person_id))
            f_out.write('{0},'.format(self.last_visitoccurrence_id))
            f_out.write('{0},'.format(self.last_conditionoccurrence_id))
            f_out.write('{0},'.format(self.last_observation_id))
            f_out.write('{0},'.format(self.last_death_id))
            f_out.write('{0},'.format(self.last_sequencing_id))
            f_out.write('{0},'.format(self.last_variantoccurrence_id))
            f_out.write('{0},'.format(self.last_procedureoccurrence_id))
            f_out.write('{0},'.format(self.last_drugexposure_id))
            f_out.write('{0}'.format(self.last_measurement_id))




