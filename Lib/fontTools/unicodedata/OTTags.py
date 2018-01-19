# Data updated to OpenType 1.8.2 as of January 2018.

# Complete list of OpenType script tags at:
# https://www.microsoft.com/typography/otspec/scripttags.htm

# Most of the script tags are the same as the ISO 15924 tag but lowercased,
# so we only have to handle the exceptional cases:
# - KATAKANA and HIRAGANA both map to 'kana';
# - spaces at the end are preserved, unlike ISO 15924;
# - we map special script codes for Inherited, Common and Unknown to DFLT.

DEFAULT_SCRIPT = "DFLT"

SCRIPT_EXCEPTIONS = {
    "Hira": "kana",
    "Hrkt": "kana",
    "Laoo": "lao ",
    "Yiii": "yi  ",
    "Nkoo": "nko ",
    "Vaii": "vai ",
    "Zinh": DEFAULT_SCRIPT,
    "Zyyy": DEFAULT_SCRIPT,
    "Zzzz": DEFAULT_SCRIPT,
}

NEW_SCRIPT_TAGS = {
    "Beng": ("bng2",),
    "Deva": ("dev2",),
    "Gujr": ("gjr2",),
    "Guru": ("gur2",),
    "Knda": ("knd2",),
    "Mlym": ("mlm2",),
    "Orya": ("ory2",),
    "Taml": ("tml2",),
    "Telu": ("tel2",),
    "Mymr": ("mym2",),
}
