graph TD
    %% Atores e Nós
    Produtor([👨‍🌾 Produtor])
    Distribuidor([🚛 Distribuidor])
    Varejista([🏪 Varejista])
    Consumidor([👥 Consumidor])
    Blockchain[(🔗 Blockchain / DB)]

    %% Fluxo do Produtor
    Produtor -->|1. Registra Safra/Produto| Blockchain
    Produtor -->|2. Gera QR Code/ID| Etiqueta[🏷️ Etiqueta do Produto]

    %% Fluxo do Distribuidor
    Etiqueta -->|3. Leitura do Código| Distribuidor
    Distribuidor -->|4. Atualiza: Em Trânsito| Blockchain
    Distribuidor -->|5. Monitora Temperatura| Blockchain

    %% Fluxo do Varejista
    Distribuidor -->|6. Entrega no Ponto de Venda| Varejista
    Varejista -->|7. Confirma Recebimento| Blockchain
    Varejista -->|8. Disponibiliza para Venda| Gôndola[🛒 Gôndola / Prateleira]

    %% Fluxo do Consumidor
    Gôndola -->|9. Compra Produto| Consumidor
    Consumidor -->|10. Escaneia QR Code| App[📱 AgriChain App]
    App -.->|11. Consulta Origem| Blockchain
    Blockchain -.->|12. Retorna Jornada Completa| App

    %% Estilização (Opcional)
    classDef roles fill:#f9f,stroke:#333,stroke-width:2px;
    class Produtor,Distribuidor,Varejista,Consumidor roles;
