from VCF import VCF
import pandas as pd
import  csv
import  time
import numpy as np
class VCF2GCDM:
    def process(self):
        f = open("data/VariantOccurrence.csv", "w", newline='', encoding="utf-8")
        writer = csv.writer(f)

        lines = pd.read_csv("data/vcf.csv")
        lines = lines.sort_values(by=['chrom', 'pos', 'start', 'ref', 'alt', "Annotation_Impact"], ascending=True)
        lines=lines.fillna("")
        lines = lines.reset_index()
        lines = np.array(lines)
        lines = lines.tolist()

        curline = VCF(lines[0])
        row=["","","","","","",curline.chrom,"",curline.start,curline.stop,"",
             curline.Gene_Name, "", "", "", "","","",curline.HGVSc, curline.HGVSp, "", "", curline.ref+">"+curline.alt]
        writer.writerow(row)
        for i in range(1, len(lines)):
            nextline = VCF(lines[i])

            if not curline.isGroup(nextline):
                row = ["", "", "", "", "", "", nextline.chrom, "", nextline.start, nextline.stop, "",
                       nextline.Gene_Name, "", "", "", "", "", "", nextline.HGVSc, nextline.HGVSp, "", "",
                       nextline.ref + ">" + nextline.alt]
                writer.writerow(row)
            curline = nextline




# if __name__=="__main__":
#     start=time.clock()
#     v=VCF2GCDM()
#     v.process()
#     end=time.clock()
#     print(end-start)