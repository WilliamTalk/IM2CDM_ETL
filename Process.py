from VCF import VCF
import pandas as pd
import  csv
class VCF2GCDM:
    def VCF2GCDM(self):
        f = open("data/VariantOccurrence.csv", "a", newline='', encoding="utf-8")
        writer = csv.writer(f)

        lines = pd.read_csv("data/vcf.csv")
        lines = lines.sort_values(by=['chrom', 'pos', 'start', 'ref', 'alt', "Annotation_Impact"], ascending=True)
        lines = lines.reset_index()

        curline = VCF(lines.loc[0, :])
        row=["","","","","","",curline.chrom,"",curline.start,curline.stop,"",
             curline.Gene_Name, "", "", "", "","","",curline.HGVSc, curline.HGVSp, "", "", curline.ref+">"+curline.alt]
        writer.writerow(lines.loc[0, :])
        for i in range(1, len(lines)):
            nextline = VCF(lines.loc[i, :])

            if not curline.isGroup(nextline):
                writer.writerow(lines.loc[i, :])
            curline = nextline
            # if i == 355:
            #     a1 = VCF(lines.loc[354, :])
            #     a2 = VCF(lines.loc[355, :])
            #     print(lines.loc[354, :])
            #     print(a1.chrom)
            #
            #     print(a2.chrom)
            #     print(a1.isGroup(a2))
            #     print(a1.chrom == a2.chrom, a1.start == a2.start, a1.stop == a2.stop, a1.ref == a2.ref,
            #           a1.alt == a1.alt)
