import SwiftUI

@main
struct UzYangiApp: App {
    var body: some Scene {
        WindowGroup { SetupView() }
    }
}

/// Klaviaturani yoqish va sinab ko'rish uchun ekran.
struct SetupView: View {
    @State private var text = ""

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Oʻzbek (yangi lotin) klaviaturasi")
                .font(.title2.bold())
            Text("""
                1. Settings → General → Keyboard → Keyboards → Add New Keyboard… ni oching.
                2. «Oʻzbek (yangi lotin)» ni tanlang.
                3. Yozayotganda 🌐 tugmasi bilan unga oʻting.
                """)
            Button("Sozlamalarni ochish") {
                if let url = URL(string: UIApplication.openSettingsURLString) {
                    UIApplication.shared.open(url)
                }
            }
            TextField("Shu yerda sinab koʻring", text: $text)
                .textFieldStyle(.roundedBorder)
            Spacer()
        }
        .padding()
    }
}
