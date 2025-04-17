import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

years = np.array([i for i in range(1,21)])
values = np.array([i for i in elec_cons])

X = years.reshape(-1, 1)
y = values

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values using the model
trend = model.predict(X)
slope = model.coef_[0]
intercept = model.intercept_
from sklearn.metrics import r2_score
print(r2_score(values,trend))

print(f"Model: y = {intercept:.2f} + {slope:.2f} * year")

# Plot original data and trend line
plt.plot(years, values, marker='o', label='Original Data')
plt.plot(years, trend, color='red', linestyle='--', label='Linear Trend')
plt.title('Linear Trend Over Years')
plt.xlabel('Years')
plt.ylabel('Electricity Consumption (in kWh)')
plt.xticks([])
plt.legend()
plt.grid(True)
plt.show()

expected_values=[]
for i in range(19,22):
    expected_values.append(intercept+slope*i)
print(expected_values)
