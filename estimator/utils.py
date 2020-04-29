import math


def getDurationDays(data):
  '''convert weeks and months to days'''

  if data['periodType'] == 'weeks':
    return data['timeToElapse'] * 7
  elif data['periodType'] == 'months':
    return data['timeToElapse'] * 30
  return data['timeToElapse']


def impactEstimator(data):
  '''estimates the imapact using the data provided'''

  currentlyInfected = data['reportedCases'] * 10
  exp = getDurationDays(data) / 3
  infectionsByRequestedTime = currentlyInfected * math.ceil((2**exp))
  severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
  hospitalBedsByRequestedTime = (0.35 * data['totalHospitalBeds']) / severeCasesByRequestedTime
  casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
  casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
  dollarsInFlight = (infectionsByRequestedTime * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * getDurationDays(data)

  return {
    'currentlyInfected': currentlyInfected,
    'infectionsByRequestedTime': infectionsByRequestedTime,
    'severeCasesByRequestedTime': severeCasesByRequestedTime,
    'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
    'casesForICUByRequestedTime': casesForICUByRequestedTime,
    'casesForVentilatorsByRequestedTime': casesForVentilatorsByRequestedTime,
    'dollarsInFlight': dollarsInFlight
  }


def severeImactEstimator(data):
  '''estimates the severe impact using the data provided'''

  currentlyInfected = data['reportedCases'] * 50
  exp = getDurationDays(data) / 3
  infectionsByRequestedTime = currentlyInfected * (2**exp)
  severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
  hospitalBedsByRequestedTime = (0.35 * data['totalHospitalBeds']) / severeCasesByRequestedTime
  casesForICUByRequestedTime = 0.05 * infectionsByRequestedTime
  casesForVentilatorsByRequestedTime = 0.02 * infectionsByRequestedTime
  dollarsInFlight = (infectionsByRequestedTime * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * getDurationDays(data)

  return {
    'currentlyInfected': currentlyInfected,
    'infectionsByRequestedTime': infectionsByRequestedTime,
    'severeCasesByRequestedTime': severeCasesByRequestedTime,
    'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
    'casesForICUByRequestedTime': casesForICUByRequestedTime,
    'casesForVentilatorsByRequestedTime': casesForVentilatorsByRequestedTime,
    'dollarsInFlight': dollarsInFlight
  }
