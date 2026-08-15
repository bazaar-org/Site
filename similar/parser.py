import gzip
import shutil
import tempfile
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

import gi
gi.require_version("AppStream", "1.0")
from gi.repository import AppStream, Gio

APPSTREAM_URL = "https://dl.flathub.org/repo/appstream/x86_64/appstream.xml.gz"

SKIP_IDS = {
    "net.krafting.PleasureDVR",
    "io.github.ladaapp.lada",
}

@dataclass
class App:
    id: str
    kind: str
    name: str
    summary: str
    description: str
    categories: list = field(default_factory=list)
    keywords: list = field(default_factory=list)
    developer_name: str = None
    extends: list = field(default_factory=list)


def download_and_decompress(url: str, dest: Path):
    with urllib.request.urlopen(url) as resp:
        with gzip.GzipFile(fileobj=resp) as gz, open(dest, "wb") as out:
            shutil.copyfileobj(gz, out)


def get_components_list(pool):
    if hasattr(pool, "as_array"):
        return list(pool.as_array())
    if hasattr(pool, "index_safe"):
        return [pool.index_safe(i) for i in range(pool.get_size())]
    if hasattr(pool, "index"):
        return [pool.index(i) for i in range(pool.get_size())]

def get_app_id(cpt) -> str:
    launchable = cpt.get_launchable(AppStream.LaunchableKind.DESKTOP_ID)
    if launchable:
        entries = launchable.get_entries()
        if entries and len(entries) == 1:
            entry = entries[0]
            if entry.endswith(".desktop"):
                return entry[:-len(".desktop")]
            return entry
    return cpt.get_id()

def component_to_app(cpt) -> App:
    dev = cpt.get_developer()
    developer_name = dev.get_name() if dev else None

    return App(
        id=get_app_id(cpt),
        kind=cpt.get_kind().value_nick if cpt.get_kind() else None,
        name=cpt.get_name(),
        summary=cpt.get_summary(),
        description=cpt.get_description(),
        categories=list(cpt.get_categories()),
        keywords=list(cpt.get_keywords()) if cpt.get_keywords() else [],
        developer_name=developer_name,
        extends=list(cpt.get_extends()) if cpt.get_extends() else [],
    )


def fetch_apps() -> list[App]:
    with tempfile.TemporaryDirectory() as tmp:
        xml_path = Path(tmp) / "appstream.xml"
        download_and_decompress(APPSTREAM_URL, xml_path)
        
        metadata = AppStream.Metadata.new()
        metadata.set_format_style(AppStream.FormatStyle.CATALOG)
        metadata.parse_file(Gio.File.new_for_path(str(xml_path)), AppStream.FormatKind.XML)
        
        pool = metadata.get_components()
        components = get_components_list(pool)
    apps = [component_to_app(c) for c in components]
    return [
        app for app in apps
        if app.kind == "desktop-app"
        and not app.extends
        and app.id not in SKIP_IDS
    ]
