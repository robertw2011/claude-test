# -*- coding: utf-8 -*-
"""用本地下载的视频，在页面引用的每个时间点截取高清画面，替换 img/ 里的低清截图，
然后重新生成 index.html 和离线版（download/ 目录）。

用法：
    python hd_frames.py 视频文件路径 [--width 1280]

需要：Python 3.8+，以及在 PATH 中可用的 ffmpeg。
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from data import CHAPTERS  # noqa: E402


def secs(ts):
    p = [int(x) for x in ts.split(":")]
    while len(p) < 3:
        p.insert(0, 0)
    return p[0] * 3600 + p[1] * 60 + p[2]


def main():
    ap = argparse.ArgumentParser(description="用本地视频生成高清截图并重建页面")
    ap.add_argument("video", help="下载好的视频文件，例如 course.mp4")
    ap.add_argument("--width", type=int, default=1280, help="截图宽度（像素），默认 1280")
    args = ap.parse_args()

    video = Path(args.video).expanduser().resolve()
    if not video.is_file():
        sys.exit(f"找不到视频文件：{video}")
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        sys.exit("没有找到 ffmpeg。请先安装（Mac: brew install ffmpeg；Windows: winget install ffmpeg），再重新运行。")

    times = sorted({secs(ts) for c in CHAPTERS for ts, _ in c["imgs"]})
    out_dir = HERE / "img"
    out_dir.mkdir(exist_ok=True)
    print(f"共 {len(times)} 个时间点，开始截图……")
    failed = []
    for i, t in enumerate(times, 1):
        dest = out_dir / f"t{t:05d}.jpg"
        cmd = [ffmpeg, "-loglevel", "error", "-y", "-ss", str(t), "-i", str(video),
               "-frames:v", "1", "-vf", f"scale={args.width}:-2", "-q:v", "3", str(dest)]
        r = subprocess.run(cmd)
        if r.returncode != 0 or not dest.exists():
            failed.append(t)
        print(f"\r  {i}/{len(times)}", end="", flush=True)
    print()
    if failed:
        sys.exit(f"有 {len(failed)} 个时间点截图失败：{failed}。请确认视频是完整的课程视频（约 10 小时）。")

    (HERE / "img" / ".hd").write_text(str(args.width), encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "build.py")], check=True)
    subprocess.run([sys.executable, str(HERE / "make_offline.py")], check=True)
    print("完成：高清截图已写入 img/，页面和 download/ 下的离线版已重新生成。")


if __name__ == "__main__":
    main()
