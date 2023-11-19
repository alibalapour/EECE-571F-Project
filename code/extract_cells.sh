#!/bin/bash

# Set absolute paths for directories and files
SOURCE_DIR="$( pwd -P )"
IMG_DIR="$1"
HOVERNET_OUTPUT_DIR="$2"
OUTPUT_DIR="$3"

# Start running cell extraction code
python "code/extract_cells.py" \
    --image_dir "$IMG_DIR" \
    --json_dir "$HOVERNET_OUTPUT_DIR" \
    --cell_image_patches_dir "$OUTPUT_DIR"
    

