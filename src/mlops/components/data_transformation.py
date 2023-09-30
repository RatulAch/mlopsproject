#components

import os
from mlops import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlops.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


## Note: We can add different data transformation techniques such as scaler, PCA and all
## All kinds of EDA in ML cycle here before passing this data to the model


# we have only added train_test_split

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into train and test")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
