import argparse, json, funcy
from sklearn.model_selection import train_test_split


def save_coco(file, info, licenses, images, annotations, categories):
    with open(file, "wt", encoding="UTF-8") as coco:
        json.dump(
            {
                "info": info,
                "licenses": licenses,
                "images": images,
                "annotations": annotations,
                "categories": categories,
            },
            coco,
            indent=2,
            sort_keys=True,
        )


# Filters the annotations for saving
def filter_annotations(annotations, images):
    image_ids = funcy.lmap(lambda i: int(i["id"]), images)
    return funcy.lfilter(lambda a: int(a["image_id"]) in image_ids, annotations)


# The main function for execution
def main(args):

    # Open the annotations file
    with open(args.annotations_file, "rt", encoding="UTF-8") as annotations:
        # Decode the json from the annotations file string
        coco = json.load(annotations)

        # Set a default for info which is an optional field
        if "info" in coco:
            info = coco["info"]
        else:
            info = {}

        # Set a default for licenses which is an optional field
        if "licenses" in coco:
            licenses = coco["licenses"]
        else:
            licenses = []

        # Set the images field
        images = coco["images"]

        # Set the annotations field
        annotations = coco["annotations"]

        # Set the categories field
        categories = coco["categories"]

        # If the has_annotations flag is set
        if args.has_annotations:
            # Get the images with annotations
            images_with_annotations = funcy.lmap(
                lambda a: int(a["image_id"]), annotations
            )

            # Filter images that do not have annotations
            images = funcy.lremove(
                lambda i: i["id"] not in images_with_annotations, images
            )

        # Try to split based on the test ratio and if this fails, we assume that there is not a test set
        try:
            train_before, test = train_test_split(images, test_size=args.test_ratio)
        except:
            train_before = images
            test = []

        ratio_remaining = 1 - args.test_ratio

        valid_ratio_adjusted = args.valid_ratio / ratio_remaining

        # Try to get the train and validation set
        try:
            train, valid = train_test_split(
                train_before, test_size=valid_ratio_adjusted
            )
        except:
            train = train_before
            valid = []

        save_mappings = [
            (args.train_name, train),
            (args.valid_name, valid),
            (args.test_name, test),
        ]

        for m in save_mappings:
            try:
                # Do not save if there are no annotations
                if len(m[1]) == 0:
                    raise Exception(
                        "There are no annotations to save. Skipping {}...".format(m[0])
                    )
                _annotations = filter_annotations(annotations, m[1])
                save_coco(
                    m[0],
                    info,
                    licenses,
                    m[1],
                    _annotations,
                    categories,
                )
                print(
                    "Saved {} annotations from {} images to {}".format(
                        len(_annotations), len(m[1]), m[0]
                    )
                )
            except:
                pass


def app():
    parser = argparse.ArgumentParser(
        description="Splits a coco annotations file into a training, validation, and test set."
    )
    parser.add_argument(
        "--annotations_file",
        type=str,
        dest="annotations_file",
        help="Path to COCO annotations file.",
        required=True,
    )
    parser.add_argument(
        "--valid_ratio",
        type=float,
        dest="valid_ratio",
        help="set valid dataset ratio",
        required=True,
    )
    parser.add_argument(
        "--test_ratio",
        type=float,
        dest="test_ratio",
        help="set test dataset ratio",
        required=True,
    )
    parser.add_argument(
        "--train_name",
        type=str,
        default="train.json",
        help="Where to store COCO training annotations",
    )
    parser.add_argument(
        "--valid_name",
        type=str,
        default="valid.json",
        help="Where to store COCO valid annotations",
    )
    parser.add_argument(
        "--test_name",
        type=str,
        default="test.json",
        help="Where to store COCO test annotations",
    )
    parser.add_argument(
        "--has_annotations",
        dest="has_annotations",
        action="store_true",
        help="Ignore all images without annotations. Keep only these with at least one annotation",
    )

    args = parser.parse_args()

    main(args)
