# echo1-coco-split
echo1-coco-split provides a faster, safer way to split coco formatted datasets into train, validation and test sets. 

## Installation & Use
```shell
# Install echo1-coco-split
pip install echo1-coco-split

# Run the coco-split
coco-split \
    --has_annotations \
    --valid_ratio .2 \
    --test_ratio .1 \
    --annotations_file ./annotations/instances_default.json
```

## coco-split help
```shell
usage: coco-split [-h] --annotations_file ANNOTATIONS_FILE --valid_ratio VALID_RATIO --test_ratio
                  TEST_RATIO [--train_name TRAIN_NAME] [--valid_name VALID_NAME] [--test_name TEST_NAME]
                  [--has_annotations]
coco-split: error: the following arguments are required: --annotations_file, --valid_ratio, --test_ratio
```
