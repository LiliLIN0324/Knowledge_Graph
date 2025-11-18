import subprocess

size_limit = 50 * 1024 * 1024  # 50MB

# 获取所有对象
output = subprocess.check_output(
    ['git', 'rev-list', '--objects', '--all'], text=True
).splitlines()

for line in output:
    sha, *rest = line.split()
    info = subprocess.check_output(
        ['git', 'cat-file', '-s', sha], text=True
    )
    size = int(info)
    if size >= size_limit:
        print(f"{sha} - {size} bytes - {' '.join(rest)}")

