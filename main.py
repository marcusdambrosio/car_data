import pandas as pd
import json
import sys,os,time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def _turo():
    turoFile = open('turo_database.json')
    turo = json.load(turoFile)
    r = turo[0]
    print(r.keys())

def rental_data():
    r = pd.read_csv('CarRentalDataV1.csv')
    reno = r[r['airportcity'] == 'Reno']
    slc = r[r['airportcity'] == 'Salt Lake City']
    denver = r[r['airportcity'] == 'Denver']
    return reno,slc,denver
def numrentals(by = 'vehicle.make'):
    reno,slc,denver = rental_data()
    fig,ax = plt.subplots(1, 3, figsize = (24,12))
    for i,city in enumerate([reno, slc, denver]):
        grouped = city.groupby(by)
        x = [c[0] for c in grouped]
        y = [len(c[1]) for c in grouped]
        temp = pd.Series(y, index = x).sort_values()
        ax[i].bar(temp.index, temp.values)
        ax[i].set_xticklabels(x, rotation = 90)
        ax[i].set_title(city['airportcity'].tolist()[0])
    plt.savefig(f'viz/num_by{by.replace(".", "")}.png')
    plt.show()


def cost(by = 'vehicle.make'):
    reno,slc,denver = rental_data()
    fig,ax = plt.subplots(1, 3, figsize = (24,12))
    for i, city in enumerate([reno,slc,denver]):
        plt.scatter()