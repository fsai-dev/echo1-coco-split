# echo1-coco-split
echo1-coco-split provides a faster, safer way to split coco formatted datasets into train, validation and test sets. 

## Installation & Use
```shell
# Install echo1-coco-split
pip install echo1-coco-split

# Run the coco-split
coco-split \
    --has_annotations \
    --valid_ratio .15 \
    --test_ratio .05 \
    --annotations_file ./instances_default.json
Saved 490 annotations from 53 images to train.json
Saved 136 annotations from 11 images to valid.json
Saved 34 annotations from 4 images to test.json
```

## coco-split help
```shell
usage: coco-split [-h] --annotations_file ANNOTATIONS_FILE --valid_ratio VALID_RATIO --test_ratio
                  TEST_RATIO [--train_name TRAIN_NAME] [--valid_name VALID_NAME]
                  [--test_name TEST_NAME] [--has_annotations] [--seed SEED]

Splits a coco annotations file into a training, validation, and test set.

options:
  -h, --help            show this help message and exit
  --annotations_file ANNOTATIONS_FILE
                        Path to COCO annotations file.
  --valid_ratio VALID_RATIO
                        Set valid dataset ratio
  --test_ratio TEST_RATIO
                        Set test dataset ratio
  --train_name TRAIN_NAME
                        Where to store COCO training annotations
  --valid_name VALID_NAME
                        Where to store COCO valid annotations
  --test_name TEST_NAME
                        Where to store COCO test annotations
  --has_annotations     Ignore all images without annotations. Keep only those with at least one
                        annotation
  --seed SEED           Set the seed generator
```

