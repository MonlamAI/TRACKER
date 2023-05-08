import sys
from pathlib import Path

PARENT_PATH = Path(__file__).parent / "mt" / "mt-extracted-text-pairs"

def track_text(text_ids):
    for text_id in text_ids:
        bo_text_path = PARENT_PATH / f"BO{text_id}"
        en_text_path = PARENT_PATH / f"EN{text_id}"
        if bo_text_path.exists() and en_text_path.exists():
            continue
        bo_text_path.touch()
        en_text_path.touch()
        print("-Added", text_id)

if __name__ == "__main__":
    text_ids_path = Path(sys.argv[1])
    text_ids = [text_id.strip() for text_id in text_ids_path.read_text().splitlines() if text_id]
    track_text(text_ids)
