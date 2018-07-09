import pandas as pd
Intermountain=pd.read_csv("data/ihc_sample.csv")
lines = Intermountain[["EMPI","FCILTY_ID", "TX_TYPE_DSC","START_DT","END_DT"]]
for i in range(len(lines)):
    print(lines.loc[i,"START_DT"])