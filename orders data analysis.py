#read data from the file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[154]:


#rename columns names ..make them lower case and replace space with underscore
#df.rename(columns={'Order Id':'order_id', 'City':'city'})
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[159]:


#derive new columns discount , sale price and profit
#df['discount']=df['list_price']*df['discount_percent']*.01
#df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df


# In[162]:


#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[167]:


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[169]:
pip install psycopg2-binary

#load the data into sql server using replace option
import sqlalchemy as sal

engine = sal.create_engine(
    'postgresql+psycopg2://postgres:aryasqlpassword@localhost:5432/python_sql_project'
)

conn = engine.connect()
print("Connected successfully!")


# In[172]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn, index=False, if_exists='replace')


