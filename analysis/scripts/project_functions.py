{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os

def load_and_process(path='C:/Naoshad/Year 4/Term 1/DATA301/Project/course-project-solo_326/data/processed/COVID-19 Dataset.csv'):

    # Method Chain 1: Load data, drop unnecessary columns, rename columns

    df1 = (
            pd.read_csv('COVID-19 Dataset.csv')
            .drop(['Date.1', 'Year', 'Month','Date.2','Cases_Ethnicity_Unknown', 'Cases_Ethnicity_NonHispanic', 'Deaths_Ethnicity_Unknown', 'Deaths_Ethnicity_NonHispanic'], axis=1)
            .rename(columns={"Cases_Total": "Total Cases", "Cases_White": "Cases - White Ethnicity", "Cases_Black": "Cases - Black Ethnicity", "Cases_LatinX": "Cases - Latinx Ethnicity", "Cases_Asian": "Cases - Asian Ethnicity", "Cases_AIAN":"Cases - AIAN Ethnicity", "Cases_NHPI":"Cases - NHPI Ethnicity", "Cases_Multiracial":"Cases - Multiracial Ethnicity", "Cases_Other":"Cases - Other Ethnicity", "Cases_Unknown":"Cases - Unknown Ethnicity", "Cases_Ethnicity_Hispanic":"Cases - Hispanic Ethnicity"})
            .rename(columns={"Deaths_Total":"Total Deaths", "Deaths_White": "Deaths - White Ethnicity", "Deaths_Black": "Deaths - Black Ethnicity", "Deaths_LatinX": "Deaths - Latinx Ethnicity", "Deaths_Asian": "Deaths - Asian Ethnicity", "Deaths_AIAN":"Deaths - AIAN Ethnicity", "Deaths_NHPI":"Deaths - NHPI Ethnicity", "Deaths_Multiracial":"Deaths - Multiracial Ethnicity", "Deaths_Other":"Deaths - Other Ethnicity", "Deaths_Unknown":"Deaths - Unknown Ethnicity", "Deaths_Ethnicity_Hispanic":"Deaths - Hispanic Ethnicity"})
            )


    # Method Chain 2: Replaced blank values with 'No Data', 

    df2 = ( 
            df1.fillna('No Data')
            )
    
    return df2