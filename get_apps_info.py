import re
from pathlib import Path
from configparser import ConfigParser

desktop_dirs = [
    Path("~/.local/share/applications").expanduser(),
    Path("/usr/share/applications"),
    Path('desktop')
]

apps = []

def clean_exec(exec_cmd):
    return re.sub(r"\s*%[a-zA-Z]", "", exec_cmd).strip()

def get_app_info():
    for directory in desktop_dirs:
        if not directory.exists():
            continue
        for file in directory.glob("*.desktop"):
            config = ConfigParser(interpolation=None, strict=False)
            config.read(file, encoding="utf-8")
            try:
                name = config.get("Desktop Entry", "Name")
                exec_cmd = config.get("Desktop Entry", "Exec", fallback="")
                icon = config.get("Desktop Entry", "Icon", fallback="")

                exec_cmd = clean_exec(exec_cmd)

                if name and exec_cmd:
                    apps.append((name, exec_cmd, icon))
            except Exception as e:
                print(f"Error reading {file}: {e}")
    return apps

# for name, exec_cmd, icon in get_app_info():
#     print(f"{name} | {exec_cmd} | {icon}")