Simple tool to list the gnome extensions that are currently installed.

## Usage

```sh
$ ./list-gnome-extensions.py --help
usage: list-gnome-extensions.py [-h] [-n] [-u] [-d] [-l] [-i] [-v] [-a]
                                [--group] [--versions VERSIONS]
                                [--not-versions NOT_VERSIONS]

List currently installed gnome extensions.

optional arguments:
  -h, --help            show this help message and exit
  -n, --name            Display extension names (default)
  -u, --url             Display extension URLs
  -d, --desc, --description
                        Display extension descriptions
  -l, --location        Display extension installation locations
  -i, --uuid            Display extension UUIDs
  -v, --version, --shell-version
                        Display supported gnome-shell versions
  -a, --all             Dump all extension metadata
  --group               Group extensions by installation location
  --versions VERSIONS   Filter by supported gnome-shell versions (comma
                        separated)
  --not-versions NOT_VERSIONS
                        Filter by unsupported gnome-shell versions (comma
                        separated)
```

## Example output

`$ ./list-gnome-extensions.py -nu --group`

```json
[
    {
        "extensions": [
            {
                "name": "Workspace Indicator",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Launch new instance",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Window List",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Screenshot Window Sizer",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "windowNavigator",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Volume Mixer",
                "url": "https://github.com/aleho/gnome-shell-volume-mixer"
            },
            {
                "name": "Hello, World!",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "User Themes",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Auto Move Windows",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "GPaste",
                "url": "http://github.com/Keruspe/GPaste"
            },
            {
                "name": "Removable Drive Menu",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Native Window Placement",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Applications Menu",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Hibernate Status Button",
                "url": "https://github.com/arelange/gnome-shell-extension-hibernate-status"
            },
            {
                "name": "TopIcons Plus",
                "url": "https://github.com/phocean/TopIcons-plus"
            },
            {
                "name": "AlternateTab",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            },
            {
                "name": "Places Status Indicator",
                "url": "http://git.gnome.org/gnome-shell-extensions"
            }
        ],
        "location": "/usr/share/gnome-shell/extensions"
    },
    {
        "extensions": [
            {
                "name": "Disconnect Wifi",
                "url": "https://github.com/kgshank/gse-disconnect-wifi"
            },
            {
                "name": "Applications Overview Tooltip",
                "url": "https://github.com/RaphaelRochet/applications-overview-tooltip"
            },
            {
                "name": "Refresh Wifi Connections",
                "url": "https://github.com/kgshank/gse-refresh-wifi"
            },
            {
                "name": "Gnome Shell Extension Reloader",
                "url": "https://nls1729.github.io/extension-reloader.html"
            },
            {
                "name": "Caffeine",
                "url": "https://github.com/eonpatapon/gnome-shell-extension-caffeine"
            }
        ],
        "location": "/home/mischka/.local/share/gnome-shell/extensions"
    }
]
```
