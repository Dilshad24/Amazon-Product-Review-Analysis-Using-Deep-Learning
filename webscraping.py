from bs4 import BeautifulSoup as bs
import requests
# good product
# https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/product-reviews/B07XVLMZHH/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
# bad product

link='https://www.amazon.in/PORTABLEWASH-Virgin-Bucket-Washing-Machine/dp/B07JC7F56N/ref=sr_1_9?dchild=1&pf_rd_p=2890ff01-c470-4516-a2eb-887bd7e4c219&pf_rd_r=WZQ83H9VFMEJC4X8ZQSW&qid=1595141703&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-9'
page=requests.get(link)
page

page_content=page.content
soup=bs(page_content,'html.parser')
#print(soup.prettify())
reviewer_name = soup.find_all("span","a-profile-name")
rating = soup.find_all("i",{"data-hook":"review-star-rating"})
review = soup.find_all("span",{"data-hook":"review-body"})

#review
review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
reviewer_name_content=[]
for i in range(0,len(reviewer_name)):
    reviewer_name_content.append(reviewer_name[i].get_text())
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
#review_content[:] = [reviews.lstrip('\n') for reviews in review_content]
#review_content[:] = [reviews.rstrip('\n') for reviews in review_content]
print(review_content)
print(len(review_content))
print(reviewer_name_content)
print(rate)
review_info=[reviewer_name_content,rate,review_content]
print(review_info)
import pandas as pd
column=["name","rating","review"]
df=pd.DataFrame(review_info)
print(df)
import pickle
filename='I:\Download\wjejfoe\model_v1.pkl'
loaded_model=pickle.load(open(filename,'rb'))
#loaded_model.predict_proba(["my name is dilshad and i love playing pubg"])
loffs="%2.1f%% Positive" % (100 * loaded_model.predict_proba(review_content)[0:1][:,1][0])
#loaded_model.predict_proba(["my name is dilshad and i hate playing pubg love"])
print(loffs)
