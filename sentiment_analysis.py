import pickle
filename='I:\Download\model_v1.pkl'
loaded_model=pickle.load(open(filename,'rb'))
#loaded_model.predict_proba(["my name is dilshad and i love playing pubg"])
loffs="%2.1f%% Positive" % (100 * loaded_model.predict_proba(["i admire pubg",'my name is dilshad','i love you','love','how love u'])[0:1][:,1][0])
#loaded_model.predict_proba(["my name is dilshad and i hate playing pubg love"])
print(loffs)




