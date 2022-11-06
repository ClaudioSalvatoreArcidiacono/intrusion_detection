from intrusion_detection.feature_selection.pipeline import (
    get_feature_selection_pipeline,
)
from intrusion_detection.modelling.blender import Blender
from intrusion_detection.modelling.cyber_attack_detector import CyberAttackDetector
from intrusion_detection.modelling.ddos_detector import DDOSDetector
from intrusion_detection.preprocessing.pipeline import get_preprocessing_pipeline
from pyod.models.hbos import HBOS
from pyod.models.iforest import IForest
from sklearn.pipeline import Pipeline


def get_final_model_pipeline(df):

    numerical_columns = df.select_dtypes(exclude=object).columns.to_list()

    preprocessing_pipeline = get_preprocessing_pipeline()
    feature_selection_pipeline = get_feature_selection_pipeline(numerical_columns)
    ddos_detector_pipeline = Pipeline(
        [*feature_selection_pipeline.steps, ("model", DDOSDetector())]
    )

    return CyberAttackDetector(
        preprocessing_pipeline=preprocessing_pipeline,
        ddos_detector_pipeline=ddos_detector_pipeline,
        anomaly_detection_pipeline=Blender(
            [HBOS(), IForest(n_jobs=1)],
        ),
    )
