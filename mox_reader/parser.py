import re
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET


def _strip_ns(root):
    """Remove XML namespaces for easier tag access."""
    for el in root.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]


def mox_to_dataframe(filename: str) -> pd.DataFrame:
    """
    Convert a .mox (XML) file into a pandas DataFrame.

    Each column corresponds to a channel (channel_label),
    and values are parsed as floats.

    Parameters
    ----------
    filename : str
        Path to the .mox XML file

    Returns
    -------
    pd.DataFrame
        DataFrame containing all channels
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    _strip_ns(root)

    channels = root.findall('.//viewer_channel')
    data = {}

    for ch in channels:
        label = ch.findtext('channel_label')
        raw = ch.findtext('raw_channel_data/channel_data')

        if label is None or raw is None:
            continue

        nums = np.array([
            float(x) for x in re.findall(
                r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', raw
            )
        ])

        data[label] = nums

    if not data:
        return pd.DataFrame()

    maxlen = max(len(v) for v in data.values())

    for k, v in data.items():
        if len(v) < maxlen:
            data[k] = np.pad(
                v, (0, maxlen - len(v)), constant_values=np.nan
            )

    return pd.DataFrame(data)