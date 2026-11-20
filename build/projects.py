"""Projects (meta/SPEC.md §17.13): one folder per project, `projects/<slug>/project.md`,
a YAML header and a Markdown write-up, with figures beside it.

A public build reads only `projects/`; it never reads the private store
(`private/projects/`, SPEC §17.9.3). The private build comes in a later round.
Checks that need the rest of the repository (course ids, assignment nodes,
relationship targets) are in check.py and relations.py; this module only
validates the file on its own. Model code reads projects through `load()`.
"""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ID = re.compile(r"prj-[a-z0-9]+(?:-[a-z0-9]+)*")
KINDS = ("course", "personal")             # coursework is not a project (SPEC §17.13.1 item 4)
STATUSES = ("draft", "reviewed")
STAGES = ("planned", "active", "done", "paused", "dropped")
FIELDS = {"id", "title", "kind", "status", "stage", "course", "assignment", "repo",
          "started", "finished", "relations"}
SHA = re.compile(r"[0-9a-f]{7,40}")
FRONT = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


@dataclass
class Project:
    id: str
    path: Path                         # projects/<slug>/project.md
    title: str
    kind: str
    status: str
    stage: str
    course: str = ""
    assignment: str = ""
    repo: dict = field(default_factory=dict)    # {url, commit}
    started: str = ""
    finished: str = ""
    relations: dict = field(default_factory=dict)   # type -> [ids], read by relations.Graph
    body: str = ""                     # the write-up (Markdown)
    problems: list[str] = field(default_factory=list)
    visibility: str = "public"         # follows from the location (SPEC §17.9.2)

    @property
    def slug(self) -> str:
        return self.id[len("prj-"):]


def _date(value, key: str, problems: list[str]) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, dt.date):
        return value.isoformat()
    try:
        return dt.date.fromisoformat(str(value)).isoformat()
    except ValueError:
        problems.append(f"{key} '{value}' must be a date (YYYY-MM-DD)")
        return ""


def parse(path: Path) -> Project:
    problems: list[str] = []
    m = FRONT.match(path.read_text(encoding="utf-8"))
    if not m:
        problems.append("missing YAML header (--- ... ---)")
        d: dict = {}
        body = ""
    else:
        try:
            d = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            problems.append(f"YAML error: {str(exc).splitlines()[0]}")
            d = {}
        body = m.group(2)
    if not isinstance(d, dict):
        problems.append("the YAML header must be a mapping")
        d = {}
    slug = path.parent.name
    pid = str(d.get("id", ""))
    if not ID.fullmatch(pid):
        problems.append(f"id '{pid}' must be prj-<lowercase words joined by hyphens>")
    elif pid != "prj-" + slug:
        problems.append(f"id '{pid}' must match the folder name (prj-{slug})")
    for key in sorted(set(d) - FIELDS):
        problems.append(f"unknown field '{key}' (SPEC §17.13.3)")
    for key in ("title", "kind", "status", "stage"):
        if not d.get(key):
            problems.append(f"missing field '{key}'")
    for key, allowed in (("kind", KINDS), ("status", STATUSES), ("stage", STAGES)):
        if d.get(key) and d[key] not in allowed:
            problems.append(f"{key} '{d[key]}' not in {' | '.join(allowed)}")
    if d.get("kind") == "personal" and d.get("course"):
        problems.append("a personal project has no course")
    repo = d.get("repo") or {}
    if not isinstance(repo, dict):
        problems.append("repo must be a mapping {url, commit}")
        repo = {}
    else:
        for key in sorted(set(repo) - {"url", "commit"}):
            problems.append(f"repo: unknown field '{key}'")
        if repo and not str(repo.get("url", "")).startswith("https://"):
            problems.append("repo: url must be an https:// link")
        if repo.get("commit") and not SHA.fullmatch(str(repo["commit"])):
            problems.append(f"repo: commit '{repo['commit']}' must be a commit sha")
    started = _date(d.get("started"), "started", problems)
    finished = _date(d.get("finished"), "finished", problems)
    if started and finished and finished < started:
        problems.append(f"finished {finished} is before started {started}")
    rel = d.get("relations") or {}
    if not isinstance(rel, dict):
        problems.append("relations must map a type to a list of ids")
        rel = {}
    return Project(pid or "prj-" + slug, path, str(d.get("title") or ""), str(d.get("kind") or ""),
                   str(d.get("status") or ""), str(d.get("stage") or ""),
                   str(d.get("course") or ""), str(d.get("assignment") or ""),
                   {k: str(v) for k, v in repo.items()}, started, finished, rel, body, problems)


def load(root: Path) -> dict[str, Project]:
    """All public projects: projects/<slug>/project.md under root (never private/)."""
    folder = root / "projects"
    out = {}
    for p in sorted(folder.glob("*/project.md")) if folder.exists() else []:
        prj = parse(p)
        out[prj.id] = prj
    return out
