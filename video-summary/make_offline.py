# -*- coding: utf-8 -*-
"""从 index.html 生成可离线保存的两个版本，输出到仓库根目录的 download/：
- claude-code-course-guide.html：单文件，图片以 base64 内嵌，双击即可打开
- claude-code-course-guide-site.zip：index.html + img/ 文件夹
"""
import base64
import re
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "download"


def full_document(fragment):
    # index.html 是 Artifact 用的片段（发布时才加骨架），离线版补上完整文档结构
    end = fragment.index("</style>") + len("</style>")
    return ("<!doctype html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            + fragment[:end] + "\n</head>\n<body>\n" + fragment[end:] + "\n</body>\n</html>\n")


def main():
    page = full_document((HERE / "index.html").read_text(encoding="utf-8"))
    OUT.mkdir(exist_ok=True)

    def inline(m):
        data = (HERE / m.group(1)).read_bytes()
        return 'src="data:image/jpeg;base64,' + base64.b64encode(data).decode() + '"'

    single = re.sub(r'src="(img/[^"]+)"', inline, page)
    (OUT / "claude-code-course-guide.html").write_text(single, encoding="utf-8")

    with zipfile.ZipFile(OUT / "claude-code-course-guide-site.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("index.html", page)
        for img in sorted((HERE / "img").glob("*.jpg")):
            z.write(img, f"img/{img.name}")
    print("离线版已生成：", OUT)


if __name__ == "__main__":
    main()
