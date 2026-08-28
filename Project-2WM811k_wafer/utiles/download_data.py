import argparse
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download and extract a Kaggle dataset."
    )
    parser.add_argument(
        "dataset",
        help="Dataset identifier, for example: uciml/iris",
    )
    parser.add_argument(
        "--output",
        default="data",
        help="Destination directory (default: data)",
    )

    args = parser.parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        args.dataset,
        path=str(output_dir),
        unzip=True,
    )

    print(f"Downloaded to {output_dir.resolve()}")


if __name__ == "__main__":
    main()