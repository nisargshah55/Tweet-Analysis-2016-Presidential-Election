
"""
Julia worked on this. DATA visualization.
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import csv,json,random,pandas
from pandas.tools.plotting import parallel_coordinates
from BeautifulSoup import BeautifulSoup
import seaborn as sns


def histogram():
    alpha = []
    f1= open('abc.txt',"r")
    for id,tweet,line in f:
        alpha.append(line)
    result_dict = dict([(i, alpha.count(i)) for i in set(alpha)])


    plt.hist(alpha, bins=5)
    plt.title("Histogram for 5 bins")
    plt.ylabel('Frequncy')
    plt.xlabel('Numbers')
    # plt.grid(True)
    plt.show()
    pass

def density_map():
    average_temp = {}
    min_value = 100; max_value = 0
    avg = 30
    reader = csv.reader(open('data.txt'), delimiter=",")
    for row in reader:
        print row[3]
        average_temp[row[4]] = row[3]
    print average_temp
    colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
    svg = open('USA_Counties_with_FIPS_and_names.svg', 'r').read()
    soup = BeautifulSoup(svg)
    paths = soup.findAll('path')
    path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
    for p in paths:
        if p['id'] not in ["State_Lines", "separator"]:
            try:
                avg = average_temp[p['id']]
            except:
                continue
            if avg > 50:
                color_class = 5
            elif avg > 40:
                color_class = 4
            elif avg > 30:
                color_class = 3
            elif avg > 20:
                color_class = 2
            elif avg > 10:
                color_class = 1
            else:
                color_class = 0
            color = colors[color_class]
            p['style'] = path_style + color
    # Write to output.svg file        
    with open('output.svg', 'w') as file_:
        file_.write(soup.prettify())



if __name__ == '__main__':
    
    desnsity_map()
    histogram()