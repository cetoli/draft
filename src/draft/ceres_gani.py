from csv import reader
import matplotlib.pyplot as plt

with open('ceres-ganimedes.csv', 'rb') as ceres_gani_file:
    ceres_gani = reader(ceres_gani_file, delimiter=',')
    # x, y = zip(*[(x, y) for x, y in ceres_gani])
    xy = [(x, y) for x, y in ceres_gani]
    print(xy)
    plt.plot(xy)
    plt.show()

