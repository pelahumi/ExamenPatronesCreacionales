from launcher import launcher
from abstractFactory import HistModeFactory, HistMeanFactory, HistMedianFactory, BarModeFactory, BarMeanFactory, BarMedianFactory

if __name__ == "__main__":
    
    launcher(HistMedianFactory())