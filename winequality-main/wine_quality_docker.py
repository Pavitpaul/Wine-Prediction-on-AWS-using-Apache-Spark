from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import sys
from pyspark import SparkContext
import pandas as pd
import findspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import trim
from pyspark.sql import SQLContext
from pyspark.sql import DataFrameNaFunctions
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import Binarizer
from pyspark.ml.feature import OneHotEncoder, VectorAssembler, StringIndexer, VectorIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.sql.functions import avg
from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import *
from pyspark.ml import Pipeline
from pyspark.ml.tuning import ParamGridBuilder
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml import PipelineModel
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from sklearn.metrics import f1_score
from pyspark.ml.tuning import CrossValidatorModel

spark = SparkSession.builder.master('local[*]')\
                            .appName('wine_quality_model')\
                            .getOrCreate()

def return_parsed_df(path):
    temp_df = spark.read.csv(path,header='true', inferSchema='true', sep=';')
    temp_df_pd = temp_df.toPandas()
    temp_df_pd.columns = temp_df_pd.columns.str.strip('""')
    return spark.createDataFrame(temp_df_pd)

arg_test_data_df = return_parsed_df(sys.argv[1])

rf_wine_model = CrossValidatorModel.load('wine_quality_model.model')

rf_wine_predictions_DF = rf_wine_model.transform(arg_test_data_df)

rf_wine_predictions_DF.select('features', 'label', 'prediction').show(20)

evaluator = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy")

print('Test Area Under PR: ', evaluator.evaluate(rf_wine_predictions_DF))

predictions_pandas = rf_wine_predictions_DF.toPandas()

f1 = f1_score(predictions_pandas.label, predictions_pandas.prediction, average='weighted')


print('F1 SCORE: ',f1)





