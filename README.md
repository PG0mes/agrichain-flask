```mermaid
flowchart TD
    %% Definição dos Nós com Aspas para evitar erros
    Produtor["👨‍🌾 Produtor"]
    Blockchain[("🔗 Blockchain / DB")]
    Etiqueta["🏷️ Etiqueta"]
    Distribuidor["🚛 Distribuidor"]
    Varejista["🏪 Varejista"]
    Gondola["🛒 Gôndola"]
    Consumidor["👥 Consumidor"]
    App["📱 App AgriChain"]

    %% Fluxo
    Produtor -->|"1. Registra Safra"| Blockchain
    Produtor -->|"2. Gera QR Code"| Etiqueta

    Etiqueta -->|"3. Leitura"| Distribuidor
    Distribuidor -->|"4. Atualiza: Em Trânsito"| Blockchain
    Distribuidor -->|"5. Entrega"| Varejista

    Varejista -->|"6. Confirmação"| Blockchain
    Varejista -->|"7. Venda"| Gondola

    Gondola -->|"8. Compra"| Consumidor
    Consumidor -->|"9. Scan QR"| App
    App -.->|"10. Consulta Origem"| Blockchain
    Blockchain -.->|"11. Retorna Dados"| App
