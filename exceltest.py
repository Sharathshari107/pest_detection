import pandas as pd
def process(predicted_class):
    data = pd.read_excel("pest.xlsx", sheet_name="Sheet1")
    print(data.head(10))
    print(data.columns)
    cname=data.loc[data['PEST name'] == predicted_class]['Comman name'].values
    affectcrop=data.loc[data['PEST name'] == predicted_class]['crops it affects'].values
    pc=data.loc[data['PEST name'] == predicted_class]['Pest Control Strategies'].values
    return cname,affectcrop,pc
# c,a,p=process("Adristyrannus")
# print("comonname=",c)
# print("affeced crop==",a)
# print("pestcontrol==",p)