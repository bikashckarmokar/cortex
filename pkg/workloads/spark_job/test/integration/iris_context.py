# Copyright 2019 Cortex Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import consts

"""
HOW TO GENERATE CONTEXT

1. cx deploy
2. get a path to a context
3. ssh into a docker container (spark/tf_train)
docker run -it --entrypoint "/bin/bash" cortexlabs/spark
4. run the following in python3 shell

from lib import util
from lib.storage import S3
bucket, key = S3.deconstruct_s3_path('s3://<cortex-bucket>/apps/<app-name>/contexts/<context-id>.msgpack')
S3(bucket, client_config={}).get_msgpack(key)
"""


def get(input_data_path):
    raw_ctx["environment_data"]["csv_data"]["path"] = input_data_path
    raw_ctx["cortex_config"]["api_version"] = consts.CORTEX_VERSION

    return raw_ctx


raw_ctx = {
    "raw_dataset": {
        "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/data_raw/raw.parquet",
        "metadata_key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/data_raw/metadata.json",
    },
    "aggregates": {
        "class_index": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/54ead5d565a57cad06972cc11d2f01f05c4e9e1dbfc525d1fa66b7999213722.msgpack",
            "tags": {},
            "type": ["STRING"],
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "class_index",
            "id": "54ead5d565a57cad06972cc11d2f01f05c4e9e1dbfc525d1fa66b7999213722",
            "aggregator": "cortex.index_string",
            "index": 8,
            "id_with_tags": "2bd062924097b0add1143dab547387307cf68f40870f52443ce5902006e00d9",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "class"}, "args": {}},
        },
        "sepal_width_mean": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/38159191e6018b929b42c7e73e8bfd19f5778bba79e84d9909f5d448ac15fc9.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "sepal_width_mean",
            "id": "38159191e6018b929b42c7e73e8bfd19f5778bba79e84d9909f5d448ac15fc9",
            "aggregator": "cortex.mean",
            "index": 2,
            "id_with_tags": "850aaab46427d39c331dd996e4a44af1bb326e45b47caaf699a5676863463f6",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "sepal_width"}, "args": {}},
        },
        "petal_width_stddev": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/986fd2cbc2b1d74aa06cf533b67d7dd7f54b5b7bf58689c58d0ec8c2568bae8.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "petal_width_stddev",
            "id": "986fd2cbc2b1d74aa06cf533b67d7dd7f54b5b7bf58689c58d0ec8c2568bae8",
            "aggregator": "cortex.stddev",
            "index": 7,
            "id_with_tags": "b8f7440e0f71ec502cccbead6b52da80c119b833baaee1d00315542a6ab907c",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "petal_width"}, "args": {}},
        },
        "petal_width_mean": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/317856401885874d95fffd349fe0878595e8c04833ba63c4546233ffd899e4d.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "petal_width_mean",
            "id": "317856401885874d95fffd349fe0878595e8c04833ba63c4546233ffd899e4d",
            "aggregator": "cortex.mean",
            "index": 6,
            "id_with_tags": "d8b09430972c97c3679fe3e90d67b69f19f1effcc2b587eb0876fb8f7d7dc55",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "petal_width"}, "args": {}},
        },
        "sepal_length_stddev": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/e7191b1effd1e4d351580f251aa35dc7c0b9825745b207fbb8cce904c94a937.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "sepal_length_stddev",
            "id": "e7191b1effd1e4d351580f251aa35dc7c0b9825745b207fbb8cce904c94a937",
            "aggregator": "cortex.stddev",
            "index": 1,
            "id_with_tags": "a7da8887f18dfac4523dd1f2135913046001c1dc04701c9a1010e6b049db943",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "sepal_length"}, "args": {}},
        },
        "petal_length_stddev": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/6a9481dc91eb3f82458356f1f5f98da6f25a69b460679e09a67988543f79e3f.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "petal_length_stddev",
            "id": "6a9481dc91eb3f82458356f1f5f98da6f25a69b460679e09a67988543f79e3f",
            "aggregator": "cortex.stddev",
            "index": 5,
            "id_with_tags": "325ae37b8684886d194ca37af19f4660c549c07880833a45ced4848895670a4",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "petal_length"}, "args": {}},
        },
        "sepal_width_stddev": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/64594f51d3cfb55a3776d013102d5fdab29bfe7332ce0c4f7c916d64d3ca29f.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "sepal_width_stddev",
            "id": "64594f51d3cfb55a3776d013102d5fdab29bfe7332ce0c4f7c916d64d3ca29f",
            "aggregator": "cortex.stddev",
            "index": 3,
            "id_with_tags": "29e071e808b973aa21af717e9ee3d91f077b40baa5b890d4a58c9dc64a12d4b",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "sepal_width"}, "args": {}},
        },
        "sepal_length_mean": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/690f97171881c08770cac55137c672167a84324efba478cfd583ec98dd18844.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "sepal_length_mean",
            "id": "690f97171881c08770cac55137c672167a84324efba478cfd583ec98dd18844",
            "aggregator": "cortex.mean",
            "index": 0,
            "id_with_tags": "1feedb4635d8955765dc82f58122e9756b1b797b3a7dcf3477ec99e655f05f2",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "sepal_length"}, "args": {}},
        },
        "petal_length_mean": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/aggregates/4deea2705f55fa8a38658546ea5c2d31e37d4aad43a874e091f1c1667b63a6e.msgpack",
            "tags": {},
            "type": "FLOAT",
            "embed": None,
            "file_path": "resources/aggregates.yaml",
            "name": "petal_length_mean",
            "id": "4deea2705f55fa8a38658546ea5c2d31e37d4aad43a874e091f1c1667b63a6e",
            "aggregator": "cortex.mean",
            "index": 4,
            "id_with_tags": "34a2792b8c2c8489ea3c8db81533a946d8005eb9e547a4863673e0eae011259",
            "resource_type": "aggregate",
            "inputs": {"columns": {"col": "petal_length"}, "args": {}},
        },
    },
    "transformers": {
        "cortex.normalize": {
            "id": "eab74305749aa9eaff514882156111fd49b8b740018da396693147cd4443a9e",
            "impl_key": "/transformers/normalize.py",
            "embed": None,
            "file_path": "/home/ubuntu/src/github.com/cortexlabs/cortex/pkg/transformers/transformers.yaml",
            "name": "normalize",
            "namespace": "cortex",
            "path": "",
            "output_type": "FLOAT_COLUMN",
            "index": 1,
            "id_with_tags": "eab74305749aa9eaff514882156111fd49b8b740018da396693147cd4443a9e",
            "resource_type": "transformer",
            "inputs": {
                "columns": {"num": "FLOAT_COLUMN|INT_COLUMN"},
                "args": {"stddev": "INT|FLOAT", "mean": "INT|FLOAT"},
            },
        },
        "cortex.index_string": {
            "id": "81bcee8795009e19f3378b2c3ea10fa6048741f2ad6ef841e5ed55c81319a0c",
            "impl_key": "/transformers/index_string.py",
            "embed": None,
            "file_path": "/home/ubuntu/src/github.com/cortexlabs/cortex/pkg/transformers/transformers.yaml",
            "name": "index_string",
            "namespace": "cortex",
            "path": "",
            "output_type": "INT_COLUMN",
            "index": 2,
            "id_with_tags": "81bcee8795009e19f3378b2c3ea10fa6048741f2ad6ef841e5ed55c81319a0c",
            "resource_type": "transformer",
            "inputs": {"columns": {"text": "STRING_COLUMN"}, "args": {"index": ["STRING"]}},
        },
    },
    "python_packages": {},
    "key": "apps/iris/contexts/33d7d279749ec97d342614cd77c5e81314a74ae0c0407ff71a120e83736a658.msgpack",
    "raw_columns": {
        "raw_float_columns": {
            "sepal_length": {
                "tags": {},
                "workload_id": "jjd3l0fi4fhwqtgmpatg",
                "values": None,
                "embed": None,
                "type": "FLOAT_COLUMN",
                "required": False,
                "file_path": "resources/raw_columns.yaml",
                "name": "sepal_length",
                "id": "9479e84647a126fe5ce36e6eeac35aacb7156cd8c8e0773e572a91a7f9c1e92",
                "min": 0.0,
                "max": 10.0,
                "index": 0,
                "resource_type": "raw_column",
                "id_with_tags": "b68cec533b973640329709bd4f7628bd8e8da5e3040bf227a1df5a7ce05807c",
            },
            "sepal_width": {
                "tags": {},
                "workload_id": "jjd3l0fi4fhwqtgmpatg",
                "values": None,
                "embed": None,
                "type": "FLOAT_COLUMN",
                "required": False,
                "file_path": "resources/raw_columns.yaml",
                "name": "sepal_width",
                "id": "690b9a1c2e717c7ec4304804d4d7fd54fba554d8ce4829062467a3dc4d5f0f8",
                "min": 0.0,
                "max": 10.0,
                "index": 1,
                "resource_type": "raw_column",
                "id_with_tags": "01430cc2265647e61dd8d8f9bec1b3918468968bdd8b27d0c6088848501da44",
            },
            "petal_length": {
                "tags": {},
                "workload_id": "jjd3l0fi4fhwqtgmpatg",
                "values": None,
                "embed": None,
                "type": "FLOAT_COLUMN",
                "required": False,
                "file_path": "resources/raw_columns.yaml",
                "name": "petal_length",
                "id": "eb81ff65ce934e409ce18627cbb7d77c804289404fd62850fa5f915a1a9d87f",
                "min": 0.0,
                "max": 10.0,
                "index": 2,
                "resource_type": "raw_column",
                "id_with_tags": "b89d5ef63dc22bfeb81684631d0f6e387e33cb26a52f7bb1b5de73ab49f40df",
            },
            "petal_width": {
                "tags": {},
                "workload_id": "jjd3l0fi4fhwqtgmpatg",
                "values": None,
                "embed": None,
                "type": "FLOAT_COLUMN",
                "required": False,
                "file_path": "resources/raw_columns.yaml",
                "name": "petal_width",
                "id": "98ee0c5e9935442ea77835297777f4ab916830db5cb1ec82590d8b03f53eb6c",
                "min": 0.0,
                "max": 10.0,
                "index": 3,
                "resource_type": "raw_column",
                "id_with_tags": "0d148b5ccc0e9266e3fd349793efd12e6880c4f1577d311e6bbef792b939d85",
            },
        },
        "raw_string_columns": {
            "class": {
                "workload_id": "jjd3l0fi4fhwqtgmpatg",
                "values": ["Iris-setosa", "Iris-versicolor", "Iris-virginica"],
                "embed": None,
                "required": False,
                "type": "STRING_COLUMN",
                "tags": {},
                "file_path": "resources/raw_columns.yaml",
                "name": "class",
                "id": "397a3c2785bcfdab244acdd11d65b415e3e4258b762deb8c17e600ce187c425",
                "index": 4,
                "resource_type": "raw_column",
                "id_with_tags": "7fa09a7ca3544e1631bd60a792d23719a76bc9f77a350277a68efd3670a1f66",
            }
        },
        "raw_int_columns": {},
    },
    "environment_data": {
        "csv_data": {
            "drop_null": False,
            "type": "csv",
            "path": "/workspace/iris.csv",
            "csv_config": {
                "negative_inf": None,
                "null_value": None,
                "sep": None,
                "ignore_leading_white_space": None,
                "empty_value": None,
                "max_columns": None,
                "positive_inf": None,
                "max_chars_per_column": None,
                "nan_value": None,
                "comment": None,
                "ignore_trailing_white_space": None,
                "multiline": None,
                "char_to_escape_quote_escaping": None,
                "encoding": None,
                "escape": None,
                "quote": None,
                "header": None,
            },
            "schema": ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"],
        },
        "parquet_data": None,
    },
    "apis": {
        "iris-type": {
            "workload_id": "rvxejtv4uoy3jfuawokc",
            "embed": None,
            "tags": {},
            "file_path": "resources/apis.yaml",
            "name": "iris-type",
            "id": "07c60601edc687a5c3106bad0ad49fef497bb207487c5fd0a36226068a3166b",
            "path": "/iris/iris-type",
            "index": 0,
            "id_with_tags": "e574b47b359b60f47132d3c919fc5c82fb5684c7784665a0e61bb42316b5b31",
            "resource_type": "api",
            "compute": {"mem": None, "replicas": 1, "cpu": None, "gpu": 0},
            "model_name": "dnn",
        }
    },
    "constants": {},
    "id": "33d7d279749ec97d342614cd77c5e81314a74ae0c0407ff71a120e83736a658",
    "dataset_version": "2019-03-08-09-58-35-701834",
    "environment": {
        "log_level": {"spark": "WARN", "tensorflow": "INFO"},
        "index": 0,
        "limit": {
            "random_seed": None,
            "randomize": None,
            "fraction_of_rows": None,
            "num_rows": None,
        },
        "embed": None,
        "file_path": "resources/environments.yaml",
        "name": "dev",
        "id": "3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554",
    },
    "status_prefix": "apps/iris/resource_statuses",
    "transformed_columns": {
        "sepal_length_normalized": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "embed": None,
            "type": "FLOAT_COLUMN",
            "tags": {},
            "file_path": "resources/transformed_columns.yaml",
            "name": "sepal_length_normalized",
            "id": "a44a0acbb54123d03d67b47469cf83712df2045b90aa99036dab99f37583d46",
            "transformer": "cortex.normalize",
            "index": 0,
            "id_with_tags": "d4f335e49dec681bd7a79766a79ab7682c8205e51a2ec46e40207785835f35a",
            "resource_type": "transformed_column",
            "inputs": {
                "columns": {"num": "sepal_length"},
                "args": {"stddev": "sepal_length_stddev", "mean": "sepal_length_mean"},
            },
        },
        "petal_width_normalized": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "embed": None,
            "type": "FLOAT_COLUMN",
            "tags": {},
            "file_path": "resources/transformed_columns.yaml",
            "name": "petal_width_normalized",
            "id": "41221f15eea0328c2987c44171f323529bfa7a196a697b1a87ff4915c143531",
            "transformer": "cortex.normalize",
            "index": 3,
            "id_with_tags": "a3ad56b29de6467931c40c992ac84b8a238a9f6d9611345bf4e338df314bf6d",
            "resource_type": "transformed_column",
            "inputs": {
                "columns": {"num": "petal_width"},
                "args": {"stddev": "petal_width_stddev", "mean": "petal_width_mean"},
            },
        },
        "sepal_width_normalized": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "embed": None,
            "type": "FLOAT_COLUMN",
            "tags": {},
            "file_path": "resources/transformed_columns.yaml",
            "name": "sepal_width_normalized",
            "id": "360fe839dbc1ee1db2d0e0f0e8ca0d1a2cc54aed69e29843e0361d285ddb700",
            "transformer": "cortex.normalize",
            "index": 1,
            "id_with_tags": "9aa22e1962c62aab2ea56f4cfc1369ed3e559bfaa70a5e8a2e17b82d1042f48",
            "resource_type": "transformed_column",
            "inputs": {
                "columns": {"num": "sepal_width"},
                "args": {"stddev": "sepal_width_stddev", "mean": "sepal_width_mean"},
            },
        },
        "petal_length_normalized": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "embed": None,
            "type": "FLOAT_COLUMN",
            "tags": {},
            "file_path": "resources/transformed_columns.yaml",
            "name": "petal_length_normalized",
            "id": "7cbc111099c4bf38e27d6a05f9b2d37bdb9038f6f934be10298a718deae6db5",
            "transformer": "cortex.normalize",
            "index": 2,
            "id_with_tags": "0c1923b1cc93679e8df3ec21f212656c050cb32d980604ffbd89fac0815ddcc",
            "resource_type": "transformed_column",
            "inputs": {
                "columns": {"num": "petal_length"},
                "args": {"stddev": "petal_length_stddev", "mean": "petal_length_mean"},
            },
        },
        "class_indexed": {
            "workload_id": "jjd3l0fi4fhwqtgmpatg",
            "embed": None,
            "type": "INT_COLUMN",
            "tags": {},
            "file_path": "resources/transformed_columns.yaml",
            "name": "class_indexed",
            "id": "6097e63c46b62b3cf70d86d9e1282bdd77d15d62bc4d132d9154bb5ddc1861d",
            "transformer": "cortex.index_string",
            "index": 4,
            "id_with_tags": "f3b94376e20e64f67d0808c3589d8a4bb09196e38ff81ba775408be38148c1e",
            "resource_type": "transformed_column",
            "inputs": {"columns": {"text": "class"}, "args": {"index": "class_index"}},
        },
    },
    "models": {
        "dnn": {
            "aggregates": ["class_index"],
            "impl_id": "2d7091a3fff24213d9e67cf2a846e5e31fd27f406fffbdb341140419f138f48",
            "training_columns": [],
            "key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/models/4989cb227eb56c2d3ccc1904cb3dbcab9a1ceb1ebf8cdb9f95a20b86a8df019.zip",
            "embed": None,
            "type": "classification",
            "tags": {},
            "id": "4989cb227eb56c2d3ccc1904cb3dbcab9a1ceb1ebf8cdb9f95a20b86a8df019",
            "name": "dnn",
            "impl_key": "model_implementations/2d7091a3fff24213d9e67cf2a846e5e31fd27f406fffbdb341140419f138f48.py",
            "feature_columns": [
                "sepal_length_normalized",
                "sepal_width_normalized",
                "petal_length_normalized",
                "petal_width_normalized",
            ],
            "target_column": "class_indexed",
            "resource_type": "model",
            "hparams": {"hidden_units": [4, 2]},
            "prediction_key": "",
            "workload_id": "aokhfrzyw6ju730nbwli",
            "dataset": {
                "metadata_key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/data_training/5bdaecf9c5a0094d4a18df15348f709be8acfd3c6faf72c3f243956c3896e76/metadata.json",
                "train_key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/data_training/5bdaecf9c5a0094d4a18df15348f709be8acfd3c6faf72c3f243956c3896e76/train.tfrecord",
                "workload_id": "jjd3l0fi4fhwqtgmpatg",
                "eval_key": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554/data_training/5bdaecf9c5a0094d4a18df15348f709be8acfd3c6faf72c3f243956c3896e76/eval.tfrecord",
                "embed": None,
                "file_path": "resources/models.yaml",
                "name": "dnn/training_dataset",
                "id": "5bdaecf9c5a0094d4a18df15348f709be8acfd3c6faf72c3f243956c3896e76",
                "index": 0,
                "id_with_tags": "166a9c191c7d058a596fc2396ded7c39e27c8021bffd7b91ff2bbb07e26f729",
                "resource_type": "training_dataset",
                "model_name": "dnn",
            },
            "data_partition_ratio": {"evaluation": 0.2, "training": 0.8},
            "file_path": "resources/models.yaml",
            "path": "implementations/models/dnn.py",
            "training": {
                "keep_checkpoint_every_n_hours": 10000,
                "shuffle": True,
                "batch_size": 10,
                "log_step_count_steps": 100,
                "num_epochs": None,
                "keep_checkpoint_max": 3,
                "tf_random_seed": 1788,
                "save_summary_steps": 100,
                "save_checkpoints_steps": None,
                "num_steps": 1000,
                "save_checkpoints_secs": 600,
                "tf_randomize_seed": False,
            },
            "evaluation": {
                "shuffle": False,
                "batch_size": 40,
                "num_epochs": None,
                "throttle_secs": 600,
                "num_steps": 100,
                "start_delay_secs": 120,
            },
            "index": 0,
            "compute": {"mem": None, "cpu": None, "gpu": None},
            "id_with_tags": "4989cb227eb56c2d3ccc1904cb3dbcab9a1ceb1ebf8cdb9f95a20b86a8df019",
        }
    },
    "app": {
        "id": "47612b3175fece07f6c3e91992412c5b16ca88a9068cb72fecbcf653eb5ffcd",
        "name": "iris",
    },
    "cortex_config": {
        "region": "us-west-2",
        "log_group": "cortex",
        "api_version": "master",
        "id": "da5e65b994ba4ebb069bdc19cf73da64aee79e5d83f466038dc75b3ef04fa63",
    },
    "root": "apps/iris/data/2019-03-08-09-58-35-701834/3976c5679bcf7cb550453802f4c3a9333c5f193f6097f1f5642de48d2397554",
    "aggregators": {
        "cortex.mean": {
            "id": "a68b354ddadc2e14348698e03af74db72cba92d7acb162e3163629e3e343373",
            "impl_key": "aggregators/71c8aa1ce07d9d7059e305ed2b180504c36a41452e73fb251ef532bf679f851.py",
            "embed": None,
            "file_path": "/home/ubuntu/src/github.com/cortexlabs/cortex/pkg/aggregators/aggregators.yaml",
            "name": "mean",
            "namespace": "cortex",
            "path": "",
            "output_type": "FLOAT",
            "index": 13,
            "id_with_tags": "a68b354ddadc2e14348698e03af74db72cba92d7acb162e3163629e3e343373",
            "resource_type": "aggregator",
            "inputs": {"columns": {"col": "FLOAT_COLUMN|INT_COLUMN"}, "args": {}},
        },
        "cortex.stddev": {
            "id": "51ca32fabf602a0c8fd7a9b4f5bb9a3d92bb6b3bbc356a727d7a25b19787353",
            "impl_key": "aggregators/b8fa468e54c55083bf350f8b482c5323bd4bc12dd5fa0d859908ab2829aea7f.py",
            "embed": None,
            "file_path": "/home/ubuntu/src/github.com/cortexlabs/cortex/pkg/aggregators/aggregators.yaml",
            "name": "stddev",
            "namespace": "cortex",
            "path": "",
            "output_type": "FLOAT",
            "index": 18,
            "id_with_tags": "51ca32fabf602a0c8fd7a9b4f5bb9a3d92bb6b3bbc356a727d7a25b19787353",
            "resource_type": "aggregator",
            "inputs": {"columns": {"col": "FLOAT_COLUMN|INT_COLUMN"}, "args": {}},
        },
        "cortex.index_string": {
            "id": "c32f21159377d5dc3ddc664fe5cabbe7b275eadc82b5f6ed711faa1a988deb4",
            "impl_key": "/aggregators/index_string.py",
            "embed": None,
            "file_path": "/home/ubuntu/src/github.com/cortexlabs/cortex/pkg/aggregators/aggregators.yaml",
            "name": "index_string",
            "namespace": "cortex",
            "path": "",
            "output_type": ["STRING"],
            "index": 29,
            "id_with_tags": "c32f21159377d5dc3ddc664fe5cabbe7b275eadc82b5f6ed711faa1a988deb4",
            "resource_type": "aggregator",
            "inputs": {"columns": {"col": "STRING_COLUMN"}, "args": {}},
        },
    },
}
