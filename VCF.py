class VCFFields:
    chrom=1
    pos=2
    start=3
    stop=4
    ref=5
    alt=6
    Gene_Name=7
    Annotation_Impact=8
    HGVSc=9
    HGVSp=10
    #define
    HIGH=99
    MODERATE=98
    LOW=97
    MODIFIER=96


class VCF:
    def __init__(self,line):
        self.line=line
    @property
    def chrom(self):
        return self.line[VCFFields.chrom]

    @property
    def pos(self):
        return self.line[VCFFields.pos]

    @property
    def start(self):
        return self.line[VCFFields.start]

    @property
    def stop(self):
        return self.line[VCFFields.stop]

    @property
    def ref(self):
        return self.line[VCFFields.ref]
    @property
    def alt(self):
        return self.line[VCFFields.alt]

    @property
    def Gene_Name(self):
        return self.line[VCFFields.Gene_Name]

    @property
    def Annotation_Impact(self):
        return self.line[VCFFields.Annotation_Impact]

    @property
    def HGVSc(self):
        return self.line[VCFFields.HGVSc]

    @property
    def HGVSp(self):
        return self.line[VCFFields.HGVSp]

    def isGroup(self,vcf):
        if self.chrom== vcf.chrom and self.start ==vcf.start and self.stop==vcf.stop \
                and self.ref==vcf.ref and self.alt==vcf.alt:
            return True
        else:
            return False
