import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Products
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = 'Add data to the database from excel'

    def handle(self, *args, **options):
        
        excel_file = 'static/xlsx/prices_list.xlsx'
        
        # read the excel file
        df_1 = pd.read_excel(io = excel_file, sheet_name='Lista de Precios',
        header= None, usecols='B,C,G', engine= 'openpyxl')
        df_2 = pd.read_excel(io = excel_file, sheet_name='Lista de Precios', 
        header= None, usecols='B,C,F,G', engine= 'openpyxl')

        # rename columns to work properly 
        df_1.rename(columns={1: 'Code', 2: 'Description', 6: 'Price'}, inplace=True)
        df_2.rename(columns={1: 'Code', 2: 'Description', 5: 'TC2', 6: 'Price'}, inplace=True)

        # drop the NaN rows
        a_ll = df_1.dropna()
        tc2 = df_2.dropna()

        # drop the title rows
        new = ~a_ll["Code"].isin(["Código"])
        new_2 = ~tc2["Code"].isin(["Código"])

        # update dataframes
        a_ll = a_ll[new]
        tc2 = tc2[new_2]

        # drop the new products from tc2 and saving
        last_2 = tc2["TC2"].isin(["TC 2"])
        tc2 = tc2[last_2]

        # merge the dataframes and save the dataframe to the database
        df = pd.merge(a_ll, tc2, how='outer')

        def swap_columns(df, col1, col2):
            col_list = list(df.columns)
            x, y = col_list.index(col1), col_list.index(col2)
            col_list[y], col_list[x] = col_list[x], col_list[y]
            df = df[col_list]
            return df

        df = swap_columns(df, 'Price', 'TC2')
        df = df.reset_index()
        df = df.rename(columns = {'index': 'id'})
        
        
        engine = create_engine('sqlite:///db.sqlite3')
        
        df.to_sql(Products._meta.db_table, if_exists='replace', con=engine, index=True )
        
    