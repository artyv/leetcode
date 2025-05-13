import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer = customer.drop_duplicates(keep='first')
    products_len = product.shape[0]
    
    customer_counts = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    
    return customer_counts[customer_counts['product_key'] == products_len][['customer_id']]
