# 用法（PowerShell）：powershell -ExecutionPolicy Bypass -File extract_frames.ps1 视频文件路径
# 在视频的 103 个时间点截图，输出到 hd_frames\，并打包成 hd_frames.zip
param([Parameter(Mandatory=$true)][string]$Video)
if (-not (Test-Path $Video)) { Write-Host "找不到视频文件：$Video"; exit 1 }
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) { Write-Host "请先安装 ffmpeg（winget install ffmpeg），然后重新打开 PowerShell"; exit 1 }
New-Item -ItemType Directory -Force -Path hd_frames | Out-Null
$times = @(40,135,1180,1420,1620,2080,2300,2500,2900,2960,3070,3200,3450,3520,3790,4470,5050,5250,5610,5980,6280,6985,7820,8360,8970,10120,10700,11040,11190,11650,11720,11900,12060,12200,12250,12860,12970,13410,14180,15440,15610,16240,16420,16820,16920,17410,17530,18110,18520,18760,19470,19860,19870,20280,20610,20760,20920,21300,22290,22850,23150,23480,23820,24100,24600,24790,24850,25000,25230,25950,26000,26190,26610,26740,27240,27430,27680,27820,27980,28290,28510,28570,29280,29630,29800,30380,30610,31080,31300,31760,31910,32090,32710,32900,33340,33460,34270,34370,34710,34820,35240,35890,35960)
$n = 0
foreach ($t in $times) {
  $n++
  $out = "hd_frames\t{0:D5}.jpg" -f $t
  ffmpeg -loglevel error -y -ss $t -i "$Video" -frames:v 1 -vf scale=1280:-2 -q:v 3 $out
  Write-Host -NoNewline "`r  $n/103"
}
Write-Host ""
Compress-Archive -Force -Path hd_frames -DestinationPath hd_frames.zip
Write-Host "完成：请把 hd_frames.zip 发给 Claude。"
