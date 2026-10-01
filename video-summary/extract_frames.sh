#!/bin/bash
# 用法：bash extract_frames.sh 视频文件路径
# 在视频的 103 个时间点截图，输出到 hd_frames/，并打包成 hd_frames.zip
set -e
VIDEO="$1"
if [ ! -f "$VIDEO" ]; then echo "找不到视频文件：$VIDEO"; exit 1; fi
command -v ffmpeg >/dev/null || { echo "请先安装 ffmpeg（Mac: brew install ffmpeg）"; exit 1; }
mkdir -p hd_frames
n=0
for t in 40 135 1180 1420 1620 2080 2300 2500 2900 2960 3070 3200 3450 3520 3790 4470 5050 5250 5610 5980 6280 6985 7820 8360 8970 10120 10700 11040 11190 11650 11720 11900 12060 12200 12250 12860 12970 13410 14180 15440 15610 16240 16420 16820 16920 17410 17530 18110 18520 18760 19470 19860 19870 20280 20610 20760 20920 21300 22290 22850 23150 23480 23820 24100 24600 24790 24850 25000 25230 25950 26000 26190 26610 26740 27240 27430 27680 27820 27980 28290 28510 28570 29280 29630 29800 30380 30610 31080 31300 31760 31910 32090 32710 32900 33340 33460 34270 34370 34710 34820 35240 35890 35960; do
  n=$((n+1))
  ffmpeg -loglevel error -y -ss "$t" -i "$VIDEO" -frames:v 1 -vf scale=1280:-2 -q:v 3 "hd_frames/t$(printf %05d $t).jpg"
  printf "\r  %d/103" "$n"
done
echo
zip -qr hd_frames.zip hd_frames
echo "完成：请把 hd_frames.zip 发给 Claude。"
