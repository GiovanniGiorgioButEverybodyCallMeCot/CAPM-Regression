# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:59:24 2024

@author: luigi
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#time range of 24 years
t = pd.date_range(start='31/10/2000', end='31/10/2024', freq='ME')

#risk free interest rate 
rF_yearly = pd.read_excel('INTEREST_RATE.xlsx', usecols=['US FEDERAL FUNDS RATE (MONTHLY AVERAGE) NADJ'], skiprows=[1, 2], header=0)
#adding a missing value for October 2024
new_value = 4.92
rF_yearly.loc[len(rF_yearly)] = new_value
#calculation of the monthly rates
rF = rF_yearly / 12
rF = np.array(rF)

#market of reference
health_MKT = pd.read_excel('STOXX HEALTH PI.xlsx', usecols=['STOXX NTH AMER 600 HEALTH CARE E - PRICE INDEX'])
#conversion in percentual montlhy variance
rMKT = 100 * (np.log(health_MKT) - np.log(health_MKT.shift(1)))
#calculation of excess returns (market return-riskfree)
rMKT = np.array(rMKT)
eMKT = np.subtract(rMKT, rF)

#constituents
stock = pd.read_excel('Stocks_Constituents.xlsx')

#market value of constituents
mkt_value = pd.read_excel('MKT VALUE.xlsx', skiprows=[1, 2], header=0)

#Johnson&Johnson
Johnson = pd.read_excel('Stocks_Constituents.xlsx', usecols=['JOHNSON & JOHNSON - TOT RETURN IND'])
rJohnson = 100 * (np.log(Johnson) - np.log(Johnson.shift(1)))
rJohnson = np.array(rJohnson)
eJohnson = np.subtract(rJohnson, rF)

#Boston Scientific
Boston = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['BOSTON SCIENTIFIC - TOT RETURN IND'])
rBoston = 100 * (np.log(Boston) - np.log(Boston.shift(1)))
rBoston = np.array(rBoston)
eBoston = np.subtract(rBoston, rF)

#Eli Lilly
Lilly = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['ELI LILLY - TOT RETURN IND'])
rLilly = 100 * (np.log(Lilly) - np.log(Lilly.shift(1)))
rLilly = np.array(rLilly)
eLilly = np.subtract(rLilly, rF)

#Pfizer
Pfizer = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['PFIZER - TOT RETURN IND'])
rPfizer = 100 * (np.log(Pfizer) - np.log(Pfizer.shift(1)))
rPfizer = np.array(rPfizer)
ePfizer = np.subtract(rPfizer, rF)

#Teleflex
Teleflex = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['TELEFLEX - TOT RETURN IND'])
rTeleflex = 100 * (np.log(Teleflex) - np.log(Teleflex.shift(1)))
rTeleflex = np.array(rTeleflex)
eTeleflex = np.subtract(rTeleflex, rF)

#Cigna
Cigna = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['CIGNA - TOT RETURN IND'])
rCigna = 100 * (np.log(Cigna) - np.log(Cigna.shift(1)))
rCigna = np.array(rCigna)
eCigna = np.subtract(rCigna, rF)

#Revvity
Revvity = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['REVVITY - TOT RETURN IND'])
rRevvity = 100 * (np.log(Revvity) - np.log(Revvity.shift(1)))
rRevvity = np.array(rRevvity)
eRevvity = np.subtract(rRevvity, rF)

#Medtronic
Medtronic = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['MEDTRONIC - TOT RETURN IND'])
rMedtronic = 100 * (np.log(Medtronic) - np.log(Medtronic.shift(1)))
rMedtronic = np.array(rMedtronic)
eMedtronic = np.subtract(rMedtronic, rF)

#Labcorp
Labcorp = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['LABCORP HOLDINGS - TOT RETURN IND'])
rLabcorp = 100 * (np.log(Labcorp) - np.log(Labcorp.shift(1)))
rLabcorp = np.array(rLabcorp)
eLabcorp = np.subtract(rLabcorp, rF)

#Humana
Humana = pd.read_excel('Stocks_Constituents.xlsx', usecols = ['HUMANA - TOT RETURN IND'])
rHumana = 100 * (np.log(Humana) - np.log(Humana.shift(1)))
rHumana = np.array(rHumana)
eHumana = np.subtract(rHumana, rF)

#scatter plots
plt.figure()
plt.scatter(eJohnson, eMKT)
plt.title('Johnson&Johnson')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eBoston, eMKT)
plt.title('Boston Scientific')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eLilly, eMKT)
plt.title('Elli Lilly')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(ePfizer, eMKT)
plt.title('Pfizer')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eTeleflex, eMKT)
plt.title('Teleflex')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eCigna, eMKT)
plt.title('Cigna')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eRevvity, eMKT)
plt.title('Revvity')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eMedtronic, eMKT)
plt.title('Medtronic')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eLabcorp, eMKT)
plt.title('Labcorp')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')

plt.figure()
plt.scatter(eHumana, eMKT)
plt.title('Humana')
plt.ylabel('Market excess returns')
plt.xlabel('Stock excess returns')


