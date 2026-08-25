# ⚠️ Deprecated — moved to [segmind/segmind-python](https://github.com/segmind/segmind-python)

This repository contained an early (2023) wrapper for the Segmind API. It is **no longer maintained** and its examples no longer work.

The official Segmind Python SDK now lives at **[segmind/segmind-python](https://github.com/segmind/segmind-python)** and is published on PyPI as [`segmind`](https://pypi.org/project/segmind/):

```bash
pip install "segmind>=1.1.0"
```

```python
import segmind

result = segmind.run("seedream-4.5", prompt="a red rose on a wooden table")
print(result["output"])
```

- Documentation: https://docs.segmind.com
- SDK repository: https://github.com/segmind/segmind-python
- Model catalog: https://www.segmind.com/models

Do not use the classes from this repository (`SD2_1`, `Kadinsky`, `ControlNet`, …) — they target endpoints that have been retired.
