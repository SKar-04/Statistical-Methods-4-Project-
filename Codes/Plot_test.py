import matplotlib.pyplot as plt
data_wb = [
         {'ID': '1925', 
          'Year': '2002-03', 
          'State': 'West Bengal', 
          'value': 366.5
          }, 
         {'ID': '1926', 
          'Year': '2003-04', 
          'State': 'West Bengal', 
          'value': 410.19
          }, 
         {'ID': '1927', 
          'Year': '2004-05',
          'State': 'West Bengal', 
          'value': 413.5321144784459
          }, 
         {'ID': '1928', 
          'Year': '2005-06', 
          'State': 'West Bengal', 
          'value': 380.61
          }, 
         {'ID': '1929', 
          'Year': '2006-07',
          'State': 'West Bengal',
          'value': 396.79
          }, 
         {'ID': '1930',
          'Year': '2007-08', 
          'State': 'West Bengal',
          'value': 439.17
          },
         {'ID': '1931', 
          'Year': '2008-09',
          'State': 'West Bengal',
          'value': 442.45
          },
         {'ID': '1932', 
          'Year': '2009-10',
          'State': 'West Bengal', 
          'value': 550.1593841974191
          }, 
         {'ID': '1933',
          'Year': '2010-11',
          'State': 'West Bengal',
          'value': 537.8500555071755
          }, 
         {'ID': '1934',
          'Year': '2011-12', 
          'State': 'West Bengal',
          'value': 563.7816380443609
          }, 
         {'ID': '1935',
          'Year': '2012-13',
          'State': 'West Bengal', 
          'value': 593.8552677892066
          },
         {'ID': '1936',
          'Year': '2013-14',
          'State': 'West Bengal', 
          'value': 608.5431262542918
          },
         {'ID': '1937', 
          'Year': '2014-15',
          'State': 'West Bengal',
          'value': 647.3394656199742
          },
         {'ID': '1938',
          'Year': '2015-16',
          'State': 'West Bengal', 
          'value': 660.4697961624349
          },
         {'ID': '1939', 
          'Year': '2016-17',
          'State': 'West Bengal',
          'value': 664.7390012030029
          }, 
         {'ID': '1940',
          'Year': '2017-18',
          'State': 'West Bengal',
          'value': 698.9770644741038
          },
         {'ID': '1941', 
          'Year': '2018-19',
          'State': 'West Bengal', 
          'value': 703.2648698280861
          },
         {'ID': '1942',
          'Year': '2019-20', 
          'State': 'West Bengal',
          'value': 756.6473535086377
          },
         {"ID": "1943",
          "Year": "2020-21",
          "State": "West Bengal",
          "value": 697.2655705794077
          },
         {"ID": "1944",
          "Year": "2021-22",
          "State": "West Bengal",
          "value": 733.418004397958
          }
         ]

elec_cons=[]
for vec in data_wb:
    elec_cons.append(vec['value'])

years = ["02-03","03-04","04-05","05-06","06-07","07-08","08-09","09-10","10-11","11-12","12-13","13-14","14-15","15-16","16-17","17-18","18-19","19-20","20-21","21-22"]
values = [i for i in elec_cons]

# Plotting
plt.plot(years, values, marker='o', linestyle='-', color='teal')

# Adding labels and title
plt.title('Trend Over Years')
plt.xlabel('Year')
plt.ylabel('Consumption per Capita in KWh')
plt.xticks([])
plt.grid(True)

# Show the plot
plt.show()