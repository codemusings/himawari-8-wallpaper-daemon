# Himawari 8 Wallpaper daemon

Copy `set-himawari-wallpaper.py` to `/usr/local/bin/` and make it executable. Copy the systemd service and timer file to `/etc/systemd/system/` and enable them with:

```bash
systemctl enable himawari-8-wallpaper-daemon.service
systemctl enable himawari-8-wallpaper-daemon.timer
```

Start the daemon with:

```bash
systemctl start himawari-8-wallpaper-daemon.timer
```

Tested on Debian 8.

Python dependencies:
* Python Imaging Library (PIL)
* Python Bindings for GLib/GObject/GIO/GTK+ (`python-gi` on Debian)
