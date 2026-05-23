import os
import subprocess

folder = r"D:\JavaScript\vdo\mngs-050"   # 改成你的实际路径

# 自动找视频和图片
video = next(f for f in os.listdir(folder) if f.endswith('.mp4'))
cover = next(f for f in os.listdir(folder) if f.endswith(('.jpg', '.jpeg', '.png', '.webp')))

src = os.path.join(folder, video)
cover_path = os.path.join(folder, cover)
tmp = os.path.join(folder, 'output.mp4')

cmd = [
    'ffmpeg', '-y',
    '-i', src,
    '-i', cover_path,
    '-map', '0',
    '-map', '1',
    '-c', 'copy',
    '-c:v:1', 'mjpeg',
    '-disposition:v:1', 'attached_pic',
    '-movflags', '+faststart',
    tmp
]

result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
        os.replace(tmp, src)       # 用新文件替换原文件
        os.remove(cover_path)      # 删除封面图
        print('封面嵌入成功，封面图已删除')
else:
    if os.path.exists(tmp):
        os.remove(tmp)
    print('封面嵌入失败')
    print(result.stderr)