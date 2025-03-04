#!/bin/bash

# Define input and output directories
INPUT_DIR="/input"
OUTPUT_DIR="/output"
LOG_FILE="/app/convert.log"
TRACKLIST_FILE="$OUTPUT_DIR/converted_files.txt"

# Ensure output directory and tracklist file exist
mkdir -p "$OUTPUT_DIR"
touch "$TRACKLIST_FILE"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log "Starting FFmpeg MP3 conversion service. Watching directory: $INPUT_DIR"

# Monitor the input folder for new files
inotifywait -m -e close_write,moved_to --format '%w%f' "$INPUT_DIR" | while read file; do
    if [[ -f "$file" ]]; then
        filename=$(basename -- "$file")
        filename_noext="${filename%.*}"
        output_file="$OUTPUT_DIR/${filename_noext}.ogg"

        log "Processing: $file -> $output_file"

        # Convert video/audio to MP3 with high quality (320kbps)
        ffmpeg -i "$file" -vn -acodec libvorbis -b:a 192k "$output_file" -y >> "$LOG_FILE" 2>&1


        # Check if conversion was successful
        if [[ $? -eq 0 ]]; then
            log "Conversion successful: $file -> $output_file"
            
            # Append the filename to the tracklist file
            echo "/etc/ices2/audio/$filename_noext.ogg" >> "$TRACKLIST_FILE"
            
            # Delete original file after conversion
            rm "$file"
        else
            log "Conversion failed: $file"
        fi
    fi
done
