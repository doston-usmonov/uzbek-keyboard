import UIKit

/// build.py yaratadigan layout.json tartibi.
struct MobileLayout: Decodable {
    let layers: [String: [[String]]]
    let longpress: [String: [String]]

    static func load() -> MobileLayout {
        guard let url = Bundle.main.url(forResource: "layout", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let layout = try? JSONDecoder().decode(MobileLayout.self, from: data)
        else { fatalError("layout.json topilmadi yoki buzilgan") }
        return layout
    }
}

final class KeyButton: UIButton {
    var key = ""
}

final class KeyboardViewController: UIInputViewController {

    private enum Shift { case off, once, locked }

    private static let keyColor = UIColor { $0.userInterfaceStyle == .dark ? UIColor(white: 0.42, alpha: 1) : .white }
    private static let specialColor = UIColor { $0.userInterfaceStyle == .dark
        ? UIColor(white: 0.27, alpha: 1)
        : UIColor(red: 0.68, green: 0.70, blue: 0.74, alpha: 1) }

    private let layout = MobileLayout.load()
    private let rows = UIStackView()
    private var layer = "letters"
    private var shift = Shift.off
    private var lastShiftTap = Date.distantPast
    private var letterKeys: [KeyButton] = []
    private var shiftKey: KeyButton?
    private var popup: UIView?
    private var deleteTimer: Timer?

    override func viewDidLoad() {
        super.viewDidLoad()
        rows.axis = .vertical
        rows.spacing = 10
        rows.distribution = .fillEqually
        rows.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(rows)
        let height = rows.heightAnchor.constraint(equalToConstant: 4 * 44 + 3 * 10)
        height.priority = UILayoutPriority(999)
        NSLayoutConstraint.activate([
            rows.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 3),
            rows.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -3),
            rows.topAnchor.constraint(equalTo: view.topAnchor, constant: 8),
            rows.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -4),
            height,
        ])
    }

    // needsInputModeSwitchKey faqat viewWillAppear'dan keyin aniq bo'ladi.
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        shift = .off
        showLayer("letters")
        updateShift()
    }

    override func textDidChange(_ textInput: UITextInput?) {
        super.textDidChange(textInput)
        updateShift()
    }

    // MARK: - Tugmalar

    private func showLayer(_ name: String) {
        layer = name
        dismissPopup()
        rows.arrangedSubviews.forEach { $0.removeFromSuperview() }
        letterKeys.removeAll()
        shiftKey = nil
        for row in layout.layers[name] ?? [] {
            let keys = row.filter { $0 != "{globe}" || needsInputModeSwitchKey }
            let line = UIStackView()
            line.spacing = 6
            let buttons = keys.map(makeKey)
            buttons.forEach(line.addArrangedSubview)
            if let first = buttons.first {
                for (button, key) in zip(buttons, keys).dropFirst() {
                    let ratio = weight(key) / weight(first.key)
                    button.widthAnchor.constraint(equalTo: first.widthAnchor, multiplier: ratio).isActive = true
                }
            }
            rows.addArrangedSubview(line)
        }
        refreshLabels()
    }

    private func makeKey(_ key: String) -> KeyButton {
        let special = isSpecial(key)
        let button = KeyButton(type: .custom)
        button.key = key
        button.setTitle(label(key), for: .normal)
        button.setTitleColor(.label, for: .normal)
        button.titleLabel?.font = .systemFont(ofSize: special ? 16 : 22)
        button.backgroundColor = special ? Self.specialColor : Self.keyColor
        button.layer.cornerRadius = 5

        switch key {
        case "{shift}":
            shiftKey = button
            on(button) { $0.tapShift() }
        case "{del}":
            button.addTarget(self, action: #selector(deleteDown), for: .touchDown)
            button.addTarget(self, action: #selector(deleteUp), for: [.touchUpInside, .touchUpOutside, .touchCancel])
        case "{enter}":
            on(button) { $0.insert("\n") }
        case "{space}":
            on(button) { $0.insert(" ") }
        case "{globe}":
            button.addTarget(self, action: #selector(handleInputModeList(from:with:)), for: .allTouchEvents)
        case "{letters}", "{numbers}", "{symbols}":
            let target = String(key.dropFirst().dropLast())
            on(button) { $0.showLayer(target) }
        default:
            if key.contains(where: \.isLetter) { letterKeys.append(button) }
            on(button) { $0.insert($0.cased(key)) }
            if layout.longpress[key] != nil {
                button.addGestureRecognizer(UILongPressGestureRecognizer(target: self, action: #selector(longPress)))
            }
        }
        return button
    }

    private func on(_ button: UIButton, _ action: @escaping (KeyboardViewController) -> Void) {
        button.addAction(UIAction { [weak self] _ in
            guard let self else { return }
            self.dismissPopup()
            action(self)
        }, for: .touchUpInside)
    }

    private func label(_ key: String) -> String {
        switch key {
        case "{shift}": return "⇧"
        case "{del}": return "⌫"
        case "{enter}": return "↵"
        case "{space}": return "Oʻzbek"
        case "{globe}": return "🌐"
        case "{letters}": return "ABC"
        case "{numbers}": return "123"
        case "{symbols}": return "#+="
        default: return key
        }
    }

    private func weight(_ key: String) -> CGFloat {
        switch key {
        case "{space}": return 4
        case "{enter}": return 2
        case "{shift}", "{del}", "{letters}", "{numbers}", "{symbols}": return 1.5
        default: return 1
        }
    }

    private func isSpecial(_ key: String) -> Bool { key.count > 1 && key.hasPrefix("{") }

    private func cased(_ text: String) -> String { shift == .off ? text : text.uppercased() }

    // MARK: - Yozish

    private func insert(_ text: String) {
        textDocumentProxy.insertText(text)
        updateShift()
    }

    private func tapShift() {
        let now = Date()
        switch shift {
        case .locked: shift = .off
        case _ where now.timeIntervalSince(lastShiftTap) < 0.3: shift = .locked
        case .once: shift = .off
        case .off: shift = .once
        }
        lastShiftTap = now
        refreshLabels()
    }

    /// Gap boshida va h.k. bosh harfni avtomatik yoqadi.
    private func updateShift() {
        guard shift != .locked else { return }
        let before = textDocumentProxy.documentContextBeforeInput ?? ""
        let on: Bool
        switch textDocumentProxy.autocapitalizationType ?? .sentences {
        case .allCharacters:
            on = true
        case .words:
            on = before.isEmpty || before.last?.isWhitespace == true
        case .sentences:
            let trimmed = before.trimmingCharacters(in: .whitespaces)
            on = before.isEmpty || before.last?.isNewline == true
                || (before.last == " " && trimmed.last.map { ".!?".contains($0) } == true)
        default:
            on = false
        }
        shift = on ? .once : .off
        refreshLabels()
    }

    private func refreshLabels() {
        for button in letterKeys { button.setTitle(cased(button.key), for: .normal) }
        shiftKey?.setTitle(shift == .locked ? "⇪" : "⇧", for: .normal)
        shiftKey?.backgroundColor = shift == .off ? Self.specialColor : Self.keyColor
    }

    @objc private func deleteDown() {
        dismissPopup()
        textDocumentProxy.deleteBackward()
        deleteTimer = Timer.scheduledTimer(withTimeInterval: 0.4, repeats: false) { [weak self] _ in
            self?.deleteTimer = Timer.scheduledTimer(withTimeInterval: 0.05, repeats: true) { [weak self] _ in
                self?.textDocumentProxy.deleteBackward()
            }
        }
    }

    @objc private func deleteUp() {
        deleteTimer?.invalidate()
        deleteTimer = nil
        updateShift()
    }

    // MARK: - Uzoq bosish

    /// Bitta muqobil bo'lsa darhol yoziladi, bir nechta bo'lsa tanlash paneli chiqadi.
    @objc private func longPress(_ gesture: UILongPressGestureRecognizer) {
        guard gesture.state == .began, let anchor = gesture.view as? KeyButton,
              let alternates = layout.longpress[anchor.key] else { return }
        let options = alternates.map(cased)
        if options.count == 1 {
            insert(options[0])
            return
        }
        dismissPopup()
        let frame = anchor.convert(anchor.bounds, to: view)
        let bar = UIStackView()
        bar.distribution = .fillEqually
        bar.backgroundColor = Self.specialColor
        bar.layer.cornerRadius = 8
        bar.clipsToBounds = true
        for option in options {
            let button = UIButton(type: .custom)
            button.setTitle(option, for: .normal)
            button.setTitleColor(.label, for: .normal)
            button.titleLabel?.font = .systemFont(ofSize: 22)
            on(button) { $0.insert(option) }
            bar.addArrangedSubview(button)
        }
        let width = frame.width * CGFloat(options.count)
        let x = min(max(frame.minX, 0), view.bounds.width - width)
        let y = max(frame.minY - frame.height - 8, 0)
        bar.frame = CGRect(x: x, y: y, width: width, height: frame.height)
        view.addSubview(bar)
        popup = bar
    }

    private func dismissPopup() {
        popup?.removeFromSuperview()
        popup = nil
    }
}
