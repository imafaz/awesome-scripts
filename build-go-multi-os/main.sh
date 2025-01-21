#!/bin/bash

fileName=$1

if [ -z "$fileName" ]; then
    echo "Error: File name not provided."
    exit 1
fi

if [ ! -f "$fileName" ]; then
    echo "Error: File $fileName not found."
    exit 1
fi

platforms=(
    "linux amd64"
    "linux arm64"
    "windows amd64"
    "windows arm64"
)

for platform in "${platforms[@]}"; do
    GOOS=$(echo $platform | cut -d' ' -f1)
    GOARCH=$(echo $platform | cut -d' ' -f2)

    if [ "$GOOS" == "windows" ]; then
        outputName="${GOOS}-${GOARCH}.exe"
    else
        outputName="${GOOS}-${GOARCH}"
    fi

    echo "Building for $GOOS/$GOARCH..."
    GOOS=$GOOS GOARCH=$GOARCH go build -o "$outputName" "$fileName"

    if [ $? -eq 0 ]; then
        echo "Success: $outputName"
    else
        echo "Failed to build for $GOOS/$GOARCH"
    fi
done

echo "Build process completed for all 64-bit platforms."