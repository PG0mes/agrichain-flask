graph TD
    %% Nós com aspas para evitar erros com emojis
    Produtor("👨‍🌾 Produtor")
    Distribuidor("🚛 Distribuidor")
    Varejista("🏪 Varejista")
    Consumidor("👥 Consumidor")
    Blockchain[("🔗 Blockchain / DB")]
    Etiqueta("🏷️ Etiqueta do Produto")
    Gondola("🛒 Gôndola / Prateleira")
    App("📱 AgriChain App")

    %% Fluxo do Produtor
    Produtor -->|"1. Registra Safra"| Blockchain
    Produtor -->|"2. Gera QR Code"| Etiqueta

    %% Fluxo do Distribuidor
    Etiqueta -->|"3. Leitura do Código"| Distribuidor
    Distribuidor -->|"4. Atualiza: Em Trânsito"| Blockchain
    Distribuidor -->|"5. Monitora Temp"| Blockchain

    %% Fluxo do Varejista
    Distribuidor -->|"6. Entrega na Loja"| Varejista
    Varejista -->|"7. Confirma Recebimento"| Blockchain
    Varejista -->|"8. Põe à Venda"| Gondola

    %% Fluxo do Consumidor
    Gondola -->|"9. Compra"| Consumidor
    Consumidor -->|"10. Escaneia QR"| App
    App -.->|"11. Consulta Origem"| Blockchain
    Blockchain -.->|"12. Retorna Dados"| App

    %% Estilização
    classDef roles fill:#f0fdf4,stroke:#16a34a,stroke-width:2px;
    class Produtor,Distribuidor,Varejista,Consumidor roles;
