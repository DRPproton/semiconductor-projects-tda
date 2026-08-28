from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi


DATASET = "qingyi/wm811k-wafer-map"
OUTPUT_DIR = Path("../raw_data/wm811k")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"Downloading {DATASET}...")

    api.dataset_download_files(
        DATASET,
        path=str(OUTPUT_DIR),
        unzip=True,
    )

    print(f"Download complete: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()