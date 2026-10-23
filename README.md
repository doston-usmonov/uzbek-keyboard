# O'zbek (yangi lotin, 2026) klaviatura tartibi

[![Oxirgi reliz](https://img.shields.io/github/v/release/doston-usmonov/uzbek-keyboard?label=reliz)](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest)

2026-yil 21-oktyabrdagi O'RQ-1184 qonuni bilan tasdiqlangan yangi alifbo uchun klaviatura tartibi.
Alifbo: **A B Ç D E F G Ğ H I J K L M N O Ö P Q R S Ş T U V X Y Z** va tutuq belgisi **ʼ**.

Asos sifatida US QWERTY olingan, shuning uchun lotin harflari (C va W ham) odatdagi joyida.
Yangi harflar alohida tugmalarda turadi, AltGr bilan ham yozish mumkin.

## Yuklab olish

Barcha fayllar [oxirgi relizda](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest), avvalgi versiyalar esa [relizlar sahifasida](https://github.com/doston-usmonov/uzbek-keyboard/releases).

| Tizim | Fayl | O'rnatish |
|---|---|---|
| Windows | [uz_yangi_windows.zip](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest/download/uz_yangi_windows.zip) | Arxivni oching va `setup.exe` ni ishga tushiring |
| macOS | [uz_yangi.keylayout](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest/download/uz_yangi.keylayout) | [macOS](#macos) |
| Linux | [uz_yangi](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest/download/uz_yangi) | [Linux (X11)](#linux-x11) |
| Android | [uz_yangi.apk](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest/download/uz_yangi.apk) | [Android](#android) |
| iOS | — | Manba koddan yig'iladi: [iOS](#ios) |

APK'ni o'rnatish uchun telefonda noma'lum manbalardan ilova o'rnatishga ruxsat berish kerak bo'ladi.

## Tartib

```
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│ '   │ !   │ "   │ #   │ $   │ %   │ ^   │ &   │ *   │ (   │ )   │ _   │ +   │
│ ʼ ` │ 1   │ 2 @ │ 3 № │ 4   │ 5   │ 6   │ 7   │ 8   │ 9 « │ 0 » │ - — │ =   │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
   ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
   │ Q   │ W   │ E   │ R   │ T   │ Y   │ U   │ I   │ O Ö │ P   │ Ğ { │ Ö } │ |   │
   │ q   │ w   │ e € │ r   │ t   │ y   │ u   │ i   │ o ö │ p   │ ğ [ │ ö ] │ \   │
   └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
     ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
     │ A   │ S Ş │ D   │ F   │ G Ğ │ H   │ J   │ K   │ L   │ Ş : │ Ç " │
     │ a   │ s ş │ d   │ f   │ g ğ │ h   │ j   │ k   │ l   │ ş ; │ ç ' │
     └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
        ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
        │ Z   │ X   │ C Ç │ V   │ B   │ N   │ M   │ ;   │ :   │ ?   │
        │ z   │ x   │ c ç │ v   │ b   │ n   │ m   │ , < │ . > │ /   │
        └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

Har bir katakda chapda oddiy belgi (pastda) va Shift belgisi (tepada), o'ngda AltGr va AltGr+Shift belgilari.
AltGr — o'ng Alt tugmasi (Windows'da Ctrl+Alt ham ishlaydi, macOS'da Option ⌥).

### US tartibidan farqlari

| Tugma | Oddiy | Shift | AltGr | AltGr+Shift |
|---|---|---|---|---|
| `` ` `` | ʼ (tutuq, U+02BC) | ' | ` | ~ |
| `[` | ğ | Ğ | [ | { |
| `]` | ö | Ö | ] | } |
| `;` | ş | Ş | ; | : |
| `'` | ç | Ç | ' | " |
| `2` | 2 | " | @ | |
| `,` | , | ; | < | |
| `.` | . | : | > | |

Qo'shimcha AltGr belgilari:
- `AltGr+S/G/O/C` — ş ğ ö ç (Shift bilan bosh harflar)
- `AltGr+9/0` — « »
- `AltGr+-` — — (Shift bilan –)
- `AltGr+3` — №
- `AltGr+E` — €

Caps Lock yangi harflarga ham ta'sir qiladi.

## O'rnatish

### Windows

1. [uz_yangi_windows.zip](https://github.com/doston-usmonov/uzbek-keyboard/releases/latest/download/uz_yangi_windows.zip) ni yuklab oling, arxivni oching va `setup.exe` ni ishga tushiring.
2. Kompyuterni qayta ishga tushiring (**Restart**).
3. **Win+Space** bilan **Uzbek (Latin)** ga o'ting. Agar bu til ro'yxatda bo'lmasa, uni **Settings → Time & language → Language & region** bo'limida qo'shing.

Qayta ishga tushirmasdan ishlatish uchun PowerShell'da quyidagi buyruqni bajaring, keyin ochiq dasturlarni yopib, qayta oching:

```powershell
Stop-Process -Name ctfmon -Force; Start-Process C:\Windows\System32\ctfmon.exe
```

Busiz Windows yangi tartibga o'tmay qotib qoladi va eski tilga qaytadi.

Ro'yxatda tartib "Oʻzbek (yangi lotin, 2026)" emas, "Uzbek (Latin)" deb ko'rinadi: tilda bitta tartib bo'lsa, Windows til nomini ko'rsatadi.

O'rnatish fayllarini o'zingiz yig'moqchi bo'lsangiz:

1. Microsoft saytidan **Microsoft Keyboard Layout Creator 1.4** (MSKLC) ni yuklab, o'rnating.
2. MSKLC'da **File → Load Source File** orqali `dist/windows/uz_yangi.klc` ni oching.
3. **Project → Build DLL and Setup Package** ni bosing. Paket `Documents\uzyangi\` papkasiga tushadi.

**Validate Layout** chiqaradigan "already defined more than once" va "not in the default system code page" ogohlantirishlari xavfsiz. Ba'zi harflar ataylab ikki joyda turibdi (masalan, ş `;` tugmasida ham, AltGr+S da ham).

### Linux (X11)

```sh
sudo cp dist/linux/uz_yangi /usr/share/X11/xkb/symbols/
setxkbmap uz_yangi
```

GNOME uchun:

```sh
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('xkb', 'uz_yangi')]"
```

`/usr/share/X11/xkb` dagi fayl tizim yangilanganda o'chib ketishi mumkin. Shunday bo'lsa, faylni qaytadan nusxalang.

### macOS

macOS'da AltGr o'rniga **Option (⌥)** tugmasi ishlatiladi.

```sh
cp dist/macos/uz_yangi.keylayout ~/Library/Keyboard\ Layouts/
```

1. Tizimdan chiqib qayta kiring.
2. **System Settings → Keyboard → Text Input → Edit… → +** ni bosing.
3. **Others** bo'limidan "Oʻzbek (yangi lotin, 2026)" ni tanlang.

Cmd va Ctrl bilan ishlaydigan qisqa yo'llar US tartibidagidek qoladi: masalan, `Cmd+[` "orqaga" vazifasini bajaraveradi.

## Telefon (Android va iOS)

Telefonlarda tartib faylini o'rnatib bo'lmaydi, shuning uchun ikkala tizim uchun ekrandagi klaviatura ilovasi yozilgan.
Telefon tartibi kompyuternikidan farq qiladi:

```
 q  ş  e  r  t  y  u  i  o  p
 a  s  d  f  g  h  j  k  l  ğ
 ⇧  z  x  ç  v  b  n  m  ö  ⌫
123 🌐  ʼ  [ Oʻzbek ]  .   ↵
```

- Uzoq bosish: `ş → w`, `ç → c`, `s → ş`, `o → ö`, `g → ğ`, `ʼ → '`, `. → , ? ! :`
- `⇧` bir marta bosilsa keyingi harf bosh harf bo'ladi, ikki marta tez bosilsa Caps Lock yoqiladi.
- Gap boshida bosh harf avtomatik yoqiladi.
- `🌐` keyingi klaviaturaga o'tkazadi. Android'da uni uzoq bossangiz, klaviaturalar ro'yxati ochiladi.

### Android

1. `android/` papkasini Android Studio'da oching. Gradle wrapper'ni Studio o'zi taklif qiladi.
2. **Run** bilan telefonga o'rnating yoki **Build → Build APK(s)** orqali APK yarating.
3. "Oʻzbek klaviatura" ilovasini oching, **Yoqish** va **Tanlash** tugmalarini bosing.

Android 10 va undan yangi versiyalar uchun.

### iOS

Mac, Xcode va [XcodeGen](https://github.com/yonaskolb/XcodeGen) kerak.

```sh
cd ios
brew install xcodegen
xcodegen generate
open UzYangi.xcodeproj
```

1. Ikkala target (`UzYangi`, `UzYangiKeyboard`) uchun **Signing & Capabilities** bo'limida o'z Apple Team'ingizni tanlang.
2. Telefonga o'rnating.
3. **Settings → General → Keyboard → Keyboards → Add New Keyboard…** orqali "Oʻzbek (yangi lotin)" ni qo'shing.

iOS 15 va undan yangi versiyalar uchun. Klaviatura "Full Access" so'ramaydi, ya'ni internetga va boshqa ilovalarga kira olmaydi.

## Tartibni o'zgartirish

Kompyuter tartibi `build.py` dagi `KEYS` ro'yxatida, telefon tartibi esa `MOBILE` lug'atida yozilgan. Ularni tahrirlang va barcha fayllarni qayta yarating:

```sh
python3 build.py
```

`dist/` ichidagi fayllarni va `layout.json` larni qo'lda tahrirlamang.
