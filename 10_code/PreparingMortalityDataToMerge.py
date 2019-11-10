import os
import pandas as pd
import numpy as np

#Open file
os.chdir("C:/Users/Felipe/Desktop/Duke MIDS/Practical Tools in Data Science/")
cod = pd.read_csv("drug_data_full.csv") #Cause of death
<<<<<<< HEAD

#cod.sample(3)
#cod['Drug/Alcohol Induced Cause'].value_counts()

#Create list with death causes we wish to analyse
#I only comment the ones we do not want, so we can easily
#add new ones, if we wish to. All we'll have to do is
#un-comment the ones we wish to add.
prescription_overdose = [
'Drug poisonings (overdose) Unintentional (X40-X44)',
#'All other alcohol-induced causes',
#'Drug poisonings (overdose) Suicide (X60-X64)',
#'Drug poisonings (overdose) Undetermined (Y10-Y14)',
#'All other drug-induced causes' #,
#'Alcohol poisonings (overdose) (X45, X65, Y15)',
#'Drug poisonings (overdose) Homicide (X85)'
]

#Filter rows refering to the causes of death we are interested in
cod = cod[cod['Drug/Alcohol Induced Cause'].isin(prescription_overdose)]

#Remove unnecessary columns
cod = cod.loc[:,['County Code','Year','Drug/Alcohol Induced Cause']].copy()

#Transform County Code to numpy int64 type
cod['County Code'] = np.int64(cod['County Code'])

#Rename County Code to FIPS
cod = cod.rename(columns = {'County Code':'FIPS'})

#Save dataset
cod.to_parquet("Causes_of_Death_ready_to_merge.gzip")
=======
data_drop = cod.drop((['Drug/Alcohol Induced Cause','Notes', 'Year Code','County']), axis=1)
data_drop.rename(columns = {'County Code':'FIPS'}, inplace = True)
dd = data_drop.dropna(how='all')
mortality_data = dd[(dd['Drug/Alcohol Induced Cause Code'] != 'A9') &
(dd['Drug/Alcohol Induced Cause Code'] != 'D9') &
(dd['Drug/Alcohol Induced Cause Code'] != 'O9')]
mortality_data
>>>>>>> 7fe1e7a933cdfb7568fa31a63596a7f955a42df5