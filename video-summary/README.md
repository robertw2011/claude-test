# Claude Code 十小时课程精讲

Nate Herk《Build & Sell with Claude Code (10+ Hour Course)》（https://youtu.be/mpALXah_PBg）的中文分章讲解页面。

| 文件 | 作用 |
| --- | --- |
| `data.py` | 全部讲解内容：章节、要点、截图时间点与说明、术语表 |
| `template.html` | 页面样式与布局 |
| `build.py` | 用 `data.py` + `template.html` 生成 `index.html` |
| `make_offline.py` | 生成离线版到仓库根目录 `download/`（单文件 HTML + zip） |
| `hd_frames.py` | 用本地视频截取高清截图，并自动运行上面两个脚本 |
| `img/` | 截图（文件名 `t<秒数>.jpg`）和封面 |

## 在本地用下载好的视频换成高清截图

仓库里的截图来自 YouTube 进度条预览图，只有 160×90。下载完整视频后，可以在本地换成高清截图。

1. 准备环境：Python 3.8+ 和 ffmpeg
   - Mac：`brew install ffmpeg`
   - Windows：`winget install ffmpeg`（装完重新打开终端）
2. 获取代码：
   ```bash
   git clone https://github.com/robertw2011/claude-test.git
   cd claude-test
   git checkout claude/tender-ptolemy-vp14x3
   ```
3. 运行（路径换成你的视频文件）：
   ```bash
   python video-summary/hd_frames.py ~/Downloads/课程视频.mp4
   ```
   可以加 `--width 960` 调整截图宽度，默认 1280。103 张截图一般几分钟内完成。
4. 完成后：
   - 打开 `video-summary/index.html` 查看页面（这个文件没有完整的 HTML 头，建议直接用下面的离线版）
   - `download/claude-code-course-guide.html`：单文件版，双击打开
   - `download/claude-code-course-guide-site.zip`：网站文件夹版

视频必须是完整的那一个（约 10 小时）。截图时间点是按原视频定的，剪辑过的版本会对不上。

## 只改内容

编辑 `data.py` 后运行：

```bash
python video-summary/build.py
python video-summary/make_offline.py
```
