import csv
from algorythms.phase_frequency_criteria import PhaseFrequencyCriteria
from algorythms.criteria_invertion import CriteriaInversion

print('start')
plane1 = []
plane2 = []
with open('../data/plane1.csv') as file:
    data = csv.reader(file)
    for row in data:
        plane1.append(int(row[0]))
with open('../data/plane2.csv') as file:
    data = csv.reader(file)
    for row in data:
        plane2.append(int(row[0]))
print('Plane 1 :\n    Phase-Frequency criteria: ' + str(PhaseFrequencyCriteria.is_stochastic(plane1))
      + '\n    Inversion criteria: ' + str(CriteriaInversion.is_stochastic(plane1)))
print('Plane 2 :\n    Phase-Frequency criteria: ' + str(PhaseFrequencyCriteria.is_stochastic(plane2))
      + '\n    Inversion criteria: ' + str(CriteriaInversion.is_stochastic(plane2)))
