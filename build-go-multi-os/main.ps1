
param (
    [string]$fileName
)

if (-Not (Test-Path "$fileName")) {
    Write-Host "Error: File $fileName not found."
    exit
}

$platforms = @(
    @{GOOS="linux"; GOARCH="amd64"},
    @{GOOS="linux"; GOARCH="arm64"},
    @{GOOS="windows"; GOARCH="amd64"},
    @{GOOS="windows"; GOARCH="arm64"}
)

foreach ($platform in $platforms) {
    $env:GOOS = $platform.GOOS
    $env:GOARCH = $platform.GOARCH

    if ($platform.GOOS -eq "windows"){
        $outputName = "$($platform.GOOS)-$($platform.GOARCH).exe"
    }else{
        $outputName = "$($platform.GOOS)-$($platform.GOARCH)"

    }

    Write-Host "Building for $($platform.GOOS)/$($platform.GOARCH)..."
    go build -o "$outputName" "$fileName"

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Success: $outputName"
    } else {
        Write-Host "Failed to build for $($platform.GOOS)/$($platform.GOARCH)"
    }
}

Write-Host "Build process completed for all 64-bit platforms."