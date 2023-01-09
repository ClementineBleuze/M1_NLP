import argparse
import collections

import pandas as pd
import numpy as np

from monkey_model import Monkey
from utils import check_hexacolor, hexacolor_to_int, euclidean_distance, get_cli_args, VALID_OBS, patch_color_int


def read_monkeys_from_csv(csv_filepath:str, strict:bool=False) -> pd.DataFrame:
    """Read a monkey data from a CSV file and produce and return a dataframe"""
    
    # Write your code here
    pass


def compute_knn(df:pd.DataFrame, k:int=5, columns:list=["fur_color_int", "bmi"])->pd.DataFrame:
    """update species information for a Monkey DataFrame using a KNN.
    Arguments:
        `df`: dataframe as obtained from `read_monkeys_from_csv`
        `k`: number of neighbors to consider
        `columns`: list of observations to consider. Are valid observations:
            - fur_color_int,
            - fur_color_int_r (for red hue of fur),
            - fur_color_int_g (for green hue of fur),
            - fur_color_int_b (for blue hue of fur),
            - weight
            - size
            - bmi
    Returns: the dataframe `df`, modified in-place
    """

    # Write your code here
    pass


def save_to_csv(dataframe:pd.DataFrame, csv_filename:str):
    """Save monkey dataframe to CSV file"""
    dataframe.drop(columns=["monkey", "fur_color_int", "bmi"]).to_csv(csv_filename, index=False)


def main():
    args = get_cli_args()
    if args.command == "knn":
        df = read_monkeys_from_csv(args.input_csv)
        df = compute_knn(df, k=args.k, columns=args.obs)
        save_to_csv(df, args.output_csv)
    elif args.command == "visualize":
        from monkey_visualize import scatter
        scatter(args.input_csv, args.obs_a, args.obs_b)
    else:
        # this should be dead code.
        raise RuntimeError("invalid command name")


# main entry point
if __name__ == "__main__":
    main()
