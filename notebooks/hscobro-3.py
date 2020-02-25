import sys

sys.executable

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

df19 = pd.read_excel("C:/Users/zcole/my_projects/hsco_bro_20/inputs/pir_export_2019/pir_export_2019.xlsx", 
                     sheet_name="Section C", 
                     header=1, 
                     skipfooter=1)

df18 = pd.read_excel("C:/Users/zcole/my_projects/hsco_bro_20/inputs/pir_export_2018/pir_export_2018.xlsx", 
                     sheet_name="Section C", 
                     header=1, 
                     skipfooter=1)

df17 = pd.read_excel("C:/Users/zcole/my_projects/hsco_bro_20/inputs/pir_export_2017/pir_export_2017.xlsx", 
                     sheet_name="Section C", 
                     header=1, 
                     skipfooter=1)

df16 = pd.read_excel("C:/Users/zcole/my_projects/hsco_bro_20/inputs/pir_export_2016/pir_export_2016.xlsx", 
                     sheet_name="Section C", 
                     header=1, 
                     skipfooter=1)

df15 = pd.read_excel("C:/Users/zcole/my_projects/hsco_bro_20/inputs/pir_export_2015/pir_export_2015.xlsx", 
                     sheet_name="Section C", 
                     header=1, 
                     skipfooter=1)

df19['yr'] = "2019"
df18['yr'] = "2018"
df17['yr'] = "2017"
df16['yr'] = "2016"
df15['yr'] = "2015"

frames = [df19,df18,df17,df16,df15]

df = pd.concat(frames, join='outer', sort=False)

ok = df[df.State == "OK"]

hs = ok[(ok['Program Number'] < 200)].groupby(['yr'], as_index=False)[['C.11-1', 'C.11-2']].agg("sum")
ehs = ok[(ok['Program Number'] == 200)].groupby(['yr'], as_index=False)[['C.11-1', 'C.11-2']].agg("sum")
#cahok = ok.groupby(['yr'], as_index=False)[['C.5-1','C.5-2']].agg("sum")

plt.get_backend()

plt.rcdefaults()

plt.style.use('seaborn-whitegrid')

#plt.rcParams.update({"figure.autolayout": True})
plt.rcParams["figure.autolayout"] = "True"

plt.rcParams["axes.spines.top"] = "False"
plt.rcParams["axes.spines.bottom"] = "False"
plt.rcParams["axes.spines.left"] = "False"
plt.rcParams["axes.spines.right"] = "False"

#plt.rcParams["axes.grid"] = "True"
#plt.rcParams["axes.axisbelow"] = "True"
plt.rcParams["grid.linewidth"] = 0.5

plt.rcParams["figure.figsize"] = [12.8,6.8]

plt.rcParams["legend.borderpad"] = 0
plt.rcParams["legend.borderaxespad"] = 0
plt.rcParams["legend.labelspacing"] = 0
plt.rcParams["legend.handlelength"] = 0.8
plt.rcParams["legend.handletextpad"] = 0.125
#plt.rcParams["legend.loc"] = "upper left"

labels = hs.yr
a = hs['C.11-1']
b = hs['C.11-2']
#c = hs['C.19.a.1']

x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/1.75, a, width, color="#b92053", label="At Enrollment")
rects2 = ax.bar(x + width/1.75, b, width, color="#005282", label="End of Year")
#rects3 = ax.bar(x + 0.75/2.0, c, width, color="#000000", label="Diagnosed as Needing Treatment")

#ax.set_ylim(0, 17000)
ax.set_yticks([0,5000,10000,15000,20000])
ax.set_ylabel("Children (EHS & HS)", size=24)
ax.set_title("Head Start Immunization", color="#b92053", weight="bold", size=36)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.tick_params(axis="both", labelsize=26)
ax.legend(fontsize=24)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate("{}".format(height), 
                    xy=(rect.get_x() + rect.get_width() / 2, height), 
                    xytext=(0, 3), 
                    textcoords="offset points", 
                    ha="center", va="bottom")
        
    
#autolabel(rects1)
#autolabel(rects2)

#plt.savefig("C:/Users/zcole/my_projects/hsco_bro_20/outputs/hs-im1.svg",transparent=True)

plt.show()