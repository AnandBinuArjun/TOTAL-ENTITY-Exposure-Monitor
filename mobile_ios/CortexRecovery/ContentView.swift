import SwiftUI

struct ContentView: View {
    @State private var riskScore: Int = 0
    @State private var isScanning: Bool = false
    
    var body: some View {
        ZStack {
            Color(hex: "0A0A0B").edgesIgnoringSafeArea(.all)
            
            VStack(spacing: 30) {
                // Header
                HStack {
                    Text("TOTAL ENTITY")
                        .font(.system(size: 24, weight: .bold, design: .monospaced))
                        .foregroundColor(.white)
                    Spacer()
                    Image(systemName: "shield.fill")
                        .foregroundColor(.green)
                }
                .padding()
                
                // Risk Dial
                ZStack {
                    Circle()
                        .stroke(Color.gray.opacity(0.2), lineWidth: 20)
                    
                    Circle()
                        .trim(from: 0, to: CGFloat(riskScore) / 100.0)
                        .stroke(
                            LinearGradient(
                                gradient: Gradient(colors: [.blue, .purple, .pink]),
                                startPoint: .topLeading,
                                endPoint: .bottomTrailing
                            ),
                            style: StrokeStyle(lineWidth: 20, lineCap: .round)
                        )
                        .rotationEffect(.degrees(-90))
                        .animation(.easeOut(duration: 2.0), value: riskScore)
                    
                    VStack {
                        Text("\(riskScore)")
                            .font(.system(size: 70, weight: .bold))
                            .foregroundColor(.white)
                        Text("RISK INDEX")
                            .font(.caption)
                            .foregroundColor(.gray)
                    }
                }
                .frame(width: 250, height: 250)
                .padding(.top, 40)
                
                // Actions
                ScrollView {
                    VStack(alignment: .leading, spacing: 15) {
                        Text("PRIORITY REMEDIATION")
                            .font(.headline)
                            .foregroundColor(.gray)
                            .padding(.bottom, 5)
                            
                        ActionRow(service: "Chase Bank", action: "Enable YubiKey", score: 9.2)
                        ActionRow(service: "Gmail", action: "Rotate Password", score: 8.5)
                        ActionRow(service: "Dropbox", action: "Enable 2FA", score: 6.0)
                    }
                }
                .padding()
                
                Button(action: {
                    startScan()
                }) {
                    Text(isScanning ? "SCANNING..." : "ANALYZE EXPOSURE")
                        .font(.headline)
                        .fontWeight(.bold)
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(LinearGradient(gradient: Gradient(colors: [Color.blue, Color.purple]), startPoint: .leading, endPoint: .trailing))
                        .cornerRadius(12)
                }
                .padding()
            }
        }
    }
    
    func startScan() {
        isScanning = true
        // Simulate API delay
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            riskScore = 72
            isScanning = false
        }
    }
}

struct ActionRow: View {
    var service: String
    var action: String
    var score: Double
    
    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text(service)
                    .font(.headline)
                    .foregroundColor(.white)
                Text(action)
                    .font(.subheadline)
                    .foregroundColor(.gray)
            }
            Spacer()
            Text("\(String(format: "%.1f", score)) ROI")
                .font(.system(.caption, design: .monospaced))
                .padding(6)
                .background(Color.white.opacity(0.1))
                .cornerRadius(4)
                .foregroundColor(.pink)
        }
        .padding()
        .background(Color.white.opacity(0.05))
        .cornerRadius(10)
    }
}

extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: // RGB (12-bit)
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: // ARGB (32-bit)
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (1, 1, 1, 0)
        }

        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue:  Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}
