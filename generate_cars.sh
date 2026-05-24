#!/bin/bash
# Car image generation script
# Usage: ./generate_cars.sh <angle> <slug> <prompt>

IMAGES_DIR="/home/user/workspace/gita-v2/images"
mkdir -p "$IMAGES_DIR"

generate_image() {
    local slug="$1"
    local angle="$2"
    local prompt="$3"
    local aspect_ratio="${4:-16:9}"
    local output_file="$IMAGES_DIR/${slug}-${angle}.png"
    
    if [ -f "$output_file" ]; then
        echo "SKIP: $output_file already exists"
        return 0
    fi
    
    echo "Generating: ${slug}-${angle}..."
    
    # Try once
    result=$(asi-generate-image "{\"prompt\": \"$prompt\", \"filename\": \"${slug}-${angle}\", \"model\": \"gpt_image_2\", \"aspect_ratio\": \"$aspect_ratio\"}" 2>&1)
    
    if echo "$result" | grep -q "saved to"; then
        # Move file to correct location if needed
        generated_path=$(echo "$result" | grep -oP '/home/user/workspace/[^ ]+\.png')
        if [ "$generated_path" != "$output_file" ]; then
            mv "$generated_path" "$output_file" 2>/dev/null || cp "$generated_path" "$output_file" 2>/dev/null
        fi
        echo "SUCCESS: ${slug}-${angle}"
        return 0
    else
        echo "RETRY: ${slug}-${angle}"
        sleep 3
        result2=$(asi-generate-image "{\"prompt\": \"$prompt\", \"filename\": \"${slug}-${angle}-retry\", \"model\": \"gpt_image_2\", \"aspect_ratio\": \"$aspect_ratio\"}" 2>&1)
        if echo "$result2" | grep -q "saved to"; then
            generated_path=$(echo "$result2" | grep -oP '/home/user/workspace/[^ ]+\.png')
            cp "$generated_path" "$output_file" 2>/dev/null
            echo "SUCCESS (retry): ${slug}-${angle}"
            return 0
        else
            echo "${slug}-${angle}" >> "$IMAGES_DIR/FAILED.txt"
            echo "FAILED: ${slug}-${angle}"
            return 1
        fi
    fi
}

echo "Script loaded"
