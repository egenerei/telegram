#!/bin/bash

# Define input and output directories
INPUT_DIR="/input"
OUTPUT_DIR="/output"
LOG_FILE="/app/convert.log"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log "Starting FFmpeg conversion service. Watching directory: $INPUT_DIR"

# Monitor the input folder for new files
inotifywait -m -e close_write,moved_to --format '%w%f' "$INPUT_DIR" | while read file; do
    if [[ -f "$file" ]]; then
        filename=$(basename -- "$file")
        filename_noext="${filename%.*}"
        output_file="$OUTPUT_DIR/${filename_noext}.mp3"

        log "Processing: $file -> $output_file"

        # Convert video to MP4 using H.264 codec
        ffmpeg -i "$file" -vn -acodec libmp3lame -b:a 320k "$output_file" -y >> "$LOG_FILE" 2>&1

        # Check if conversion was successful
        if [[ $? -eq 0 ]]; then
            log "Conversion successful: $file -> $output_file"
            rm "$file" # Delete original file after conversion
        else
            log "Conversion failed: $file"
        fi
    fi
done
