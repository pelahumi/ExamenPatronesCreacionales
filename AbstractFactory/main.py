from launcher import launcher
from abstractFactory import HistModeFactory, HistMeanFactory, HistMedianFactory, BarModeFactory, BarMeanFactory, BarMedianFactory

if __name__ == "__main__":

    #En el launcher ponemos la factoría que queremos usar ej:
    launcher(HistModeFactory())