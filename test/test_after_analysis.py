'''
Created on 6/27/2023

@author: Hugo JOBY - HJO
'''
import unittest
from cast.application.test import run
from cast.application import create_postgres_engine


class TestIntegration(unittest.TestCase):

    def test1(self):
        
        run(kb_name='calport_local',
            application_name='Calport',
            engine=create_postgres_engine(host='localhost', port=2284))


if __name__ == "__main__":
    unittest.main()
