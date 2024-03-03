from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path",
                                                            "test_file_path"])

DataValidationArtifact = namedtuple("DataValidationArtifact",["schema_file_path"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",
                                        ["transformed_train_file_path",
                                         "transformed_test_file_path",
                                         "preprocessed_object_file_path"])