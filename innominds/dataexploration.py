import pandas as pd
import logging
import re
import numpy as np


class dataExploration(object):
    '''Exploartion of Data inpput'''
    def __init__(self,fileName,logger):
        self.__fileName = pd.read_excel(fileName)
        self.__logger = logger
        
    
    
    def textConversion(self,x):
        try:
            p = re.compile(r'<.*?>')
            return p.sub('', x)
        except Exception as e:
            self.__logger.error('cannot remove html tag from the text due to %s' %(e))
            return x
    
    def cleanData(self):
        '''
        cleaning of Data
        1. Removw all the tags from the Resolutions column
        2. Replace white space with nan
        3. Remove DueDate
        4. drop na.
        '''
        self.__logger.debug(self.__fileName)
        try:
            self.__fileName['Resolution'] = self.__fileName['Resolution'].map(self.textConversion)
            self.__fileName.replace(r'\s+',np.nan,regex=True)
            self.__fileName.drop(columns=['DueDate'],axis=1,inplace=True)
            self.__fileName.dropna(inplace=True)
            self.__logger.info(self.__fileName)
            
        except Exception as e:
            self.__logger.error('unexcepted exception %s in cleanData '%(e))
            







if __name__ == '__main__':
    logging.basicConfig(format = '%(asctime)s %(message)s',level ='INFO')
    logger = logging.getLogger('dataExplo')
    obj = dataExploration('SampleInput.xlsx',logger)   
    obj.cleanData()     
    