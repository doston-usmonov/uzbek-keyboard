#!/usr/bin/env python3
"""O'zbek (yangi lotin, 2026) klaviatura tartibi generatori.

Tartib bir marta shu yerda (KEYS) yoziladi, undan quyidagilar yaratiladi:
  dist/windows/uz_yangi.klc  -- Microsoft Keyboard Layout Creator (MSKLC) manbasi
  dist/linux/uz_yangi        -- XKB symbols fayli
  dist/macos/uz_yangi.keylayout -- macOS klaviatura tartibi
  android/.../assets/layout.json, ios/Keyboard/layout.json -- mobil ilovalar uchun

Ishga tushirish:  python3 build.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"

NONE = None

# Har bir tugma: (skan-kod, Windows VK, XKB nomi, caps_lock_ta'sir_qiladimi,
#                 [oddiy, Shift, AltGr, AltGr+Shift])
# Asos -- US QWERTY. Yangi harflar (Ğ Ö Ş Ç) to'g'ridan-to'g'ri [ ] ; ' tugmalarida,
# tutuq belgisi ʼ esa ` tugmasida. Siljigan belgilar AltGr qatlamida.
KEYS = [
    # --- Raqamlar qatori ---
    (0x29, "OEM_3", "TLDE", False, ["ʼ", "'", "`", "~"]),
    (0x02, "1", "AE01", False, ["1", "!", NONE, NONE]),
    (0x03, "2", "AE02", False, ["2", '"', "@", NONE]),
    (0x04, "3", "AE03", False, ["3", "#", "№", NONE]),
    (0x05, "4", "AE04", False, ["4", "$", NONE, NONE]),
    (0x06, "5", "AE05", False, ["5", "%", NONE, NONE]),
    (0x07, "6", "AE06", False, ["6", "^", NONE, NONE]),
    (0x08, "7", "AE07", False, ["7", "&", NONE, NONE]),
    (0x09, "8", "AE08", False, ["8", "*", NONE, NONE]),
    (0x0A, "9", "AE09", False, ["9", "(", "«", NONE]),
    (0x0B, "0", "AE10", False, ["0", ")", "»", NONE]),
    (0x0C, "OEM_MINUS", "AE11", False, ["-", "_", "—", "–"]),
    (0x0D, "OEM_PLUS", "AE12", False, ["=", "+", NONE, NONE]),
    # --- Yuqori qator ---
    (0x10, "Q", "AD01", True, ["q", "Q", NONE, NONE]),
    (0x11, "W", "AD02", True, ["w", "W", NONE, NONE]),
    (0x12, "E", "AD03", True, ["e", "E", "€", NONE]),
    (0x13, "R", "AD04", True, ["r", "R", NONE, NONE]),
    (0x14, "T", "AD05", True, ["t", "T", NONE, NONE]),
    (0x15, "Y", "AD06", True, ["y", "Y", NONE, NONE]),
    (0x16, "U", "AD07", True, ["u", "U", NONE, NONE]),
    (0x17, "I", "AD08", True, ["i", "I", NONE, NONE]),
    (0x18, "O", "AD09", True, ["o", "O", "ö", "Ö"]),
    (0x19, "P", "AD10", True, ["p", "P", NONE, NONE]),
    (0x1A, "OEM_4", "AD11", True, ["ğ", "Ğ", "[", "{"]),
    (0x1B, "OEM_6", "AD12", True, ["ö", "Ö", "]", "}"]),
    (0x2B, "OEM_5", "BKSL", False, ["\\", "|", NONE, NONE]),
    # --- O'rta qator ---
    (0x1E, "A", "AC01", True, ["a", "A", NONE, NONE]),
    (0x1F, "S", "AC02", True, ["s", "S", "ş", "Ş"]),
    (0x20, "D", "AC03", True, ["d", "D", NONE, NONE]),
    (0x21, "F", "AC04", True, ["f", "F", NONE, NONE]),
    (0x22, "G", "AC05", True, ["g", "G", "ğ", "Ğ"]),
    (0x23, "H", "AC06", True, ["h", "H", NONE, NONE]),
    (0x24, "J", "AC07", True, ["j", "J", NONE, NONE]),
    (0x25, "K", "AC08", True, ["k", "K", NONE, NONE]),
    (0x26, "L", "AC09", True, ["l", "L", NONE, NONE]),
    (0x27, "OEM_1", "AC10", True, ["ş", "Ş", ";", ":"]),
    (0x28, "OEM_7", "AC11", True, ["ç", "Ç", "'", '"']),
    # --- Pastki qator ---
    (0x2C, "Z", "AB01", True, ["z", "Z", NONE, NONE]),
    (0x2D, "X", "AB02", True, ["x", "X", NONE, NONE]),
    (0x2E, "C", "AB03", True, ["c", "C", "ç", "Ç"]),
    (0x2F, "V", "AB04", True, ["v", "V", NONE, NONE]),
    (0x30, "B", "AB05", True, ["b", "B", NONE, NONE]),
    (0x31, "N", "AB06", True, ["n", "N", NONE, NONE]),
    (0x32, "M", "AB07", True, ["m", "M", NONE, NONE]),
    (0x33, "OEM_COMMA", "AB08", False, [",", ";", "<", NONE]),
    (0x34, "OEM_PERIOD", "AB09", False, [".", ":", ">", NONE]),
    (0x35, "OEM_2", "AB10", False, ["/", "?", NONE, NONE]),
    (0x56, "OEM_102", "LSGT", False, ["\\", "|", NONE, NONE]),
]

# MSKLC tavsifda ' va " belgilarini qabul qilmaydi, shuning uchun ʻ (U+02BB).
LAYOUT_NAME = "Oʻzbek (yangi lotin, 2026)"

# ---------------------------------------------------------------- Windows ---

# Ctrl qatlamidagi boshqaruv belgilari (US tartibidagi kabi).
KLC_CTRL = {"OEM_4": "001b", "OEM_6": "001d", "OEM_5": "001c", "OEM_102": "001c"}

KLC_KEYNAME = """\
KEYNAME

01\tEsc
0e\tBackspace
0f\tTab
1c\tEnter
1d\tCtrl
2a\tShift
36\t"Right Shift"
37\t"Num *"
38\tAlt
39\tSpace
3a\t"Caps Lock"
3b\tF1
3c\tF2
3d\tF3
3e\tF4
3f\tF5
40\tF6
41\tF7
42\tF8
43\tF9
44\tF10
45\tPause
46\t"Scroll Lock"
47\t"Num 7"
48\t"Num 8"
49\t"Num 9"
4a\t"Num -"
4b\t"Num 4"
4c\t"Num 5"
4d\t"Num 6"
4e\t"Num +"
4f\t"Num 1"
50\t"Num 2"
51\t"Num 3"
52\t"Num 0"
53\t"Num Del"
54\t"Sys Req"
57\tF11
58\tF12
7c\tF13
7d\tF14
7e\tF15
7f\tF16
80\tF17
81\tF18
82\tF19
83\tF20
84\tF21
85\tF22
86\tF23
87\tF24

KEYNAME_EXT

1c\t"Num Enter"
1d\t"Right Ctrl"
35\t"Num /"
37\t"Prnt Scrn"
38\t"Right Alt"
45\t"Num Lock"
46\tBreak
47\tHome
48\tUp
49\t"Page Up"
4b\tLeft
4d\tRight
4f\tEnd
50\tDown
51\t"Page Down"
52\tInsert
53\tDelete
54\t<00>
56\tHelp
5b\t"Left Windows"
5c\t"Right Windows"
5d\tApplication
"""


def klc_char(ch):
    return "-1" if ch is None else f"{ord(ch):04x}"


def build_klc():
    rows = []
    for sc, vk, _, caps, (base, shift, altgr, altgr_shift) in KEYS:
        cols = [
            klc_char(base),
            klc_char(shift),
            KLC_CTRL.get(vk, "-1"),
            klc_char(altgr),
            klc_char(altgr_shift),
        ]
        # 5 = CAPLOK | CAPLOKALTGR: Caps Lock AltGr qatlamidagi harflarga ham ta'sir qiladi.
        cap = (5 if altgr and altgr.isalpha() else 1) if caps else 0
        rows.append(f"{sc:02x}\t{vk}\t\t{cap}\t" + "\t".join(cols))
    rows.append("39\tSPACE\t\t0\t0020\t0020\t0020\t-1\t-1")
    rows.append("53\tDECIMAL\t\t0\t002e\t002e\t-1\t-1\t-1")

    text = (
        f'KBD\tuzyangi\t"{LAYOUT_NAME}"\n\n'
        'COPYRIGHT\t"(c) 2026"\n\n'
        'COMPANY\t"uz_yangi"\n\n'
        'LOCALENAME\t"uz-Latn-UZ"\n\n'
        'LOCALEID\t"00000443"\n\n'
        "VERSION\t1.0\n\n"
        "SHIFTSTATE\n\n"
        "0\t//Column 4\n"
        "1\t//Column 5 : Shft\n"
        "2\t//Column 6 :       Ctrl\n"
        "6\t//Column 7 :       Ctrl Alt\n"
        "7\t//Column 8 : Shft  Ctrl Alt\n\n"
        "LAYOUT\t\t;an extra '@' at the end is a dead key\n\n"
        "//SC\tVK_\t\tCap\t0\t1\t2\t6\t7\n"
        "//--\t----\t\t----\t----\t----\t----\t----\t----\n\n"
        + "\n".join(rows)
        + "\n\n\n"
        + KLC_KEYNAME
        + "\nDESCRIPTIONS\n\n"
        f"0409\t{LAYOUT_NAME}\n\n"
        "LANGUAGENAMES\n\n"
        "0409\tUzbek (Latin, Uzbekistan)\n\n"
        "ENDKBD\n"
    )
    out = DIST / "windows" / "uz_yangi.klc"
    out.parent.mkdir(parents=True, exist_ok=True)
    # MSKLC UTF-16 LE (BOM bilan) va CRLF qator oxirlarini kutadi.
    out.write_bytes(text.replace("\n", "\r\n").encode("utf-16"))
    return out


# ------------------------------------------------------------------ Linux ---

XKB_NAMES = {
    "'": "apostrophe", '"': "quotedbl", "`": "grave", "~": "asciitilde",
    "!": "exclam", "@": "at", "#": "numbersign", "$": "dollar",
    "%": "percent", "^": "asciicircum", "&": "ampersand", "*": "asterisk",
    "(": "parenleft", ")": "parenright", "-": "minus", "_": "underscore",
    "=": "equal", "+": "plus", "[": "bracketleft", "]": "bracketright",
    "{": "braceleft", "}": "braceright", "\\": "backslash", "|": "bar",
    ";": "semicolon", ":": "colon", ",": "comma", ".": "period",
    "<": "less", ">": "greater", "/": "slash", "?": "question",
    "ğ": "gbreve", "Ğ": "Gbreve", "ş": "scedilla",
    "Ş": "Scedilla", "ç": "ccedilla", "Ç": "Ccedilla",
    "ö": "odiaeresis", "Ö": "Odiaeresis", "«": "guillemotleft",
    "»": "guillemotright", "—": "emdash", "–": "endash",
    "€": "EuroSign", "№": "numerosign",
}


def xkb_sym(ch):
    if ch is None:
        return "NoSymbol"
    if ch.isascii() and ch.isalnum():
        return ch
    return XKB_NAMES.get(ch, f"U{ord(ch):04X}")


def build_xkb():
    lines = []
    for _, _, name, caps, levels in KEYS:
        syms = ", ".join(xkb_sym(c) for c in levels)
        if caps:
            alpha_altgr = levels[2] is not None and levels[2].isalpha()
            kind = "FOUR_LEVEL_ALPHABETIC" if alpha_altgr else "FOUR_LEVEL_SEMIALPHABETIC"
            lines.append(f'    key <{name}> {{ type[Group1] = "{kind}", [ {syms} ] }};')
        else:
            lines.append(f"    key <{name}> {{ [ {syms} ] }};")

    text = (
        "// " + LAYOUT_NAME + " -- build.py tomonidan yaratilgan, qo'lda tahrirlamang.\n"
        "default partial alphanumeric_keys\n"
        'xkb_symbols "basic" {\n'
        '    include "us(basic)"\n'
        f'    name[Group1] = "{LAYOUT_NAME}";\n\n'
        + "\n".join(lines)
        + '\n\n    include "level3(ralt_switch)"\n'
        "};\n"
    )
    out = DIST / "linux" / "uz_yangi"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return out


# ------------------------------------------------------------------ macOS ---

MAC_CODES = {
    "TLDE": 50, "AE01": 18, "AE02": 19, "AE03": 20, "AE04": 21, "AE05": 23,
    "AE06": 22, "AE07": 26, "AE08": 28, "AE09": 25, "AE10": 29, "AE11": 27,
    "AE12": 24, "AD01": 12, "AD02": 13, "AD03": 14, "AD04": 15, "AD05": 17,
    "AD06": 16, "AD07": 32, "AD08": 34, "AD09": 31, "AD10": 35, "AD11": 33,
    "AD12": 30, "BKSL": 42, "AC01": 0, "AC02": 1, "AC03": 2, "AC04": 3,
    "AC05": 5, "AC06": 4, "AC07": 38, "AC08": 40, "AC09": 37, "AC10": 41,
    "AC11": 39, "AB01": 6, "AB02": 7, "AB03": 8, "AB04": 9, "AB05": 11,
    "AB06": 45, "AB07": 46, "AB08": 43, "AB09": 47, "AB10": 44, "LSGT": 10,
}

# Cmd va Ctrl bilan tugmalar US belgilarini beradi, shunda Cmd+[ kabi
# qisqa yo'llar ishlayveradi.
MAC_US_BASE = {"TLDE": "`", "AD11": "[", "AD12": "]", "AC10": ";", "AC11": "'"}

# Harfdan tashqari tugmalar: barcha qatlamlarda bir xil.
MAC_SPECIAL = {
    36: 0x0D, 48: 0x09, 49: 0x20, 51: 0x08, 52: 0x03, 53: 0x1B, 76: 0x03,
    65: 0x2E, 67: 0x2A, 69: 0x2B, 71: 0x1B, 75: 0x2F, 78: 0x2D, 81: 0x3D,
    82: 0x30, 83: 0x31, 84: 0x32, 85: 0x33, 86: 0x34, 87: 0x35, 88: 0x36,
    89: 0x37, 91: 0x38, 92: 0x39,
    96: 0x10, 97: 0x10, 98: 0x10, 99: 0x10, 100: 0x10, 101: 0x10, 103: 0x10,
    105: 0x10, 106: 0x10, 107: 0x10, 109: 0x10, 111: 0x10, 113: 0x10,
    114: 0x05, 115: 0x01, 116: 0x0B, 117: 0x7F, 118: 0x10, 119: 0x04,
    120: 0x10, 121: 0x0C, 122: 0x10, 123: 0x1C, 124: 0x1D, 125: 0x1F,
    126: 0x1E,
}

MAC_CTRL = {"[": 0x1B, "\\": 0x1C, "]": 0x1D}

# (indeks, modifikatorlar). Birinchi mos kelgani tanlanadi.
MAC_MODIFIERS = [
    (0, ""),
    (1, "anyShift caps?"),
    (2, "caps"),
    (3, "anyOption"),
    (4, "anyShift anyOption caps?"),
    (5, "caps anyOption"),
    (6, "command anyShift? caps? anyOption? anyControl?"),
    (7, "anyControl anyShift? caps? anyOption?"),
]


def mac_out(ch):
    return "".join(f"&#x{ord(c):04X};" for c in ch)


def mac_layers(name, caps, levels):
    """Bitta tugmaning har bir MAC_MODIFIERS indeksidagi belgisi."""
    base, shift, opt, opt_shift = levels
    up = shift if caps else base
    opt_up = opt_shift if caps and opt and opt.isalpha() else opt
    us = MAC_US_BASE.get(name, base)
    if us.isalpha():
        ctrl = chr(ord(us) - ord("a") + 1)
    else:
        ctrl = chr(MAC_CTRL[us]) if us in MAC_CTRL else us
    return [base, shift, up, opt, opt_shift, opt_up, us, ctrl]


def build_keylayout():
    maps = []
    for index, _ in MAC_MODIFIERS:
        keys = []
        for _, _, name, caps, levels in KEYS:
            ch = mac_layers(name, caps, levels)[index]
            if ch is not None:
                keys.append(f'\t\t\t<key code="{MAC_CODES[name]}" output="{mac_out(ch)}"/>')
        for code, value in MAC_SPECIAL.items():
            keys.append(f'\t\t\t<key code="{code}" output="{mac_out(chr(value))}"/>')
        maps.append(f'\t\t<keyMap index="{index}">\n' + "\n".join(keys) + "\n\t\t</keyMap>")

    selects = "\n".join(
        f'\t\t<keyMapSelect mapIndex="{index}">\n\t\t\t<modifier keys="{keys}"/>\n\t\t</keyMapSelect>'
        for index, keys in MAC_MODIFIERS
    )

    text = (
        '<?xml version="1.1" encoding="UTF-8"?>\n'
        '<!DOCTYPE keyboard SYSTEM "file://localhost/System/Library/DTDs/KeyboardLayout.dtd">\n'
        "<!-- build.py tomonidan yaratilgan, qo'lda tahrirlamang. -->\n"
        f'<keyboard group="126" id="-24026" name="{LAYOUT_NAME}" maxout="1">\n'
        "\t<layouts>\n"
        '\t\t<layout first="0" last="0" modifiers="Modifiers" mapSet="ANSI"/>\n'
        "\t</layouts>\n"
        '\t<modifierMap id="Modifiers" defaultIndex="0">\n'
        + selects
        + "\n\t</modifierMap>\n"
        '\t<keyMapSet id="ANSI">\n'
        + "\n".join(maps)
        + "\n\t</keyMapSet>\n"
        "</keyboard>\n"
    )
    out = DIST / "macos" / "uz_yangi.keylayout"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return out


# ----------------------------------------------------------------- Mobil ---

# Ekrandagi klaviatura (Android va iOS). Ş va Ç W va C o'rnida, Ğ va Ö
# qo'shimcha tugmalarda; W, C va boshqalar uzoq bosish orqali.
# {..} -- maxsus tugmalar, qolganlari bosilganda yoziladigan matn.
MOBILE = {
    "layers": {
        "letters": [
            ["q", "ş", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ğ"],
            ["{shift}", "z", "x", "ç", "v", "b", "n", "m", "ö", "{del}"],
            ["{numbers}", "{globe}", "ʼ", "{space}", ".", "{enter}"],
        ],
        "numbers": [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["-", "/", ":", ";", "(", ")", "«", "»", "@", '"'],
            ["{symbols}", ".", ",", "?", "!", "'", "№", "%", "{del}"],
            ["{letters}", "{globe}", "{space}", ".", "{enter}"],
        ],
        "symbols": [
            ["[", "]", "{", "}", "#", "^", "*", "+", "=", "~"],
            ["_", "\\", "|", "<", ">", "€", "$", "&", "•", "`"],
            ["{numbers}", ".", ",", "?", "!", "'", "—", "…", "{del}"],
            ["{letters}", "{globe}", "{space}", ".", "{enter}"],
        ],
    },
    "longpress": {
        "ş": ["w"],
        "ç": ["c"],
        "s": ["ş"],
        "o": ["ö"],
        "g": ["ğ"],
        "ʼ": ["'"],
        ".": [",", "?", "!", ":"],
        "-": ["—", "–"],
        '"': ["«", "»", "“", "”"],
    },
}

MOBILE_TARGETS = [
    ROOT / "android" / "app" / "src" / "main" / "assets" / "layout.json",
    ROOT / "ios" / "Keyboard" / "layout.json",
]


def build_mobile():
    import json

    for rows in MOBILE["layers"].values():
        for key in (k for row in rows for k in row):
            assert len(key) == 1 or (key.startswith("{") and key.endswith("}")), key
    text = json.dumps(MOBILE, ensure_ascii=False, indent=2) + "\n"
    for out in MOBILE_TARGETS:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    return MOBILE_TARGETS


if __name__ == "__main__":
    for path in (build_klc(), build_xkb(), build_keylayout(), *build_mobile()):
        print(path.relative_to(ROOT))
