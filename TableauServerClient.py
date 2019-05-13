import tableauserverclient as TSC
import re
import codecs
from argparse import ArgumentParser
import csv
import pandas as pd
import sys
from datetime import datetime, timedelta
import logging
from utils.Utils import Utils
from utils.DBUils import DBUtils
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TableauServerClient():

    def __init__(self):

        # create an auth object
        self.tableau_auth = TSC.TableauAuth('ldua', 'workharder247', site_id='vpr')

        # create an instance for your self.server
        self.server = TSC.Server('https://tableau.sfu.ca')


        #self.dbUtils = DBUtils.get_instance()
        
        # self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        # self.auth.set_access_token(access_token, access_token_secret)

        # self.api = tweepy.API(self.auth,wait_on_rate_limit=True)

        # # Current UTC Date
        # self.current_utc_date = datetime.utcnow().date()

        # self.filename = "twitter_accounts.csv"
        # self.tablename = "twitter_accounts"
        # self.tablename_history = self.tablename + "_history"

        # text_file = open("SFU Research Files/Twitter Accounts - Latest.txt", "r")
        # self.twitter_account_list_new = text_file.read().strip().split('\n')

        # self.args = Utils.get_opts(sys.argv)


    def get_account_details(self):
        
        logger.info(" Signing in\n")
        
        with self.server.auth.sign_in(self.tableau_auth):
            

            logger.info(" TOKEN - {}".format(self.server.auth_token))
            logger.info(" SITE_ID - {}".format(self.server.site_id))
            logger.info(" USER_ID - {}\n".format(self.server.user_id))

        
            self.project_id = "669ac120-ed2b-481b-806a-f553e56c9f9c"
            # Commented becuase project id is static
            """
            all_projects, pagination_item = self.server.projects.get()

            for project in all_projects:
                logger.info(" Project Name - {}".format(project.name))
                logger.info(" Project Name - {}".format(project.id))
            """

            self.publish_datasource()

                

            
    

            

    def publish_datasource(self):
        
        
        new_datasource = self.server.datasources.publish(
                    new_datasource, file_path, 'CreateNew')



if __name__ == "__main__":
    tsc = TableauServerClient()
    # Signs in to get an authentication token and site ID to use later
    tsc.get_account_details()
    #tsc.publish()