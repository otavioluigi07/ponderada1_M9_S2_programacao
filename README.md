# ponderada1_M9_S2_programacao

## Business Driver Map
```mermaind
graph TD;
  A[Objetivo: Distribuição eficiente de pedidos e redução de pedidos no limbo] -->|Benefício| B[Maximização do tempo e ganhos dos entregadores]
  A -->|Métrica| C[95% dos pedidos atribuídos em menos de 2 minutos]
  A -->|Métrica| D[Taxa de pedidos não atribuídos < 1.2%]

  subgraph "Cenário 1: Atribuição otimizada de pedidos"
    E[Pedidos pendentes] --> F[Entregadores disponíveis]
    F --> G[Processamento de atribuição de pedidos]
    G --> H[95% dos pedidos atribuídos < 2 minutos]
  end

  subgraph "Cenário 2: Evitar pedidos no limbo"
    I[Novo pedido criado] --> J[Tentativa de atribuição]
    J --> K[Taxa de pedidos não atribuídos < 1.2%]
  end
```
## 📌 Business Driver Map - Eficiência e Redução de Pedidos Não Atribuídos

### 📖 Descrição da Atividade  
Este projeto tem como objetivo mapear e estruturar os **Business Drivers** relacionados à eficiência da distribuição de pedidos e à redução de pedidos não atribuídos no **Rappi**, focando na visão do **entregador** dentro do aplicativo.  

A atividade consiste na modelagem dos drivers de negócio utilizando **Mermaid.js**, detalhando os requisitos, métricas e monitoramento para otimizar a experiência dos entregadores e garantir maior eficiência na alocação de pedidos.  

### 🚀 Business Drivers Mapeados  
1. **DN1 - Eficiência na Distribuição de Pedidos**  
   - Atribuição otimizada de pedidos considerando múltiplos fatores (peso, custo, urgência, proximidade, etc.).  
   - Meta: 95% dos pedidos atribuídos a um entregador em menos de **2 minutos**.  
   - Monitoramento por **logs de distribuição** e **dashboards de tempo de resposta**.  

2. **DN2 - Redução da Taxa de Pedidos "No Limbo"**  
   - Evitar pedidos que não aparecem para lojas ou entregadores e seguem **"unassigned"**.  
   - Manter a taxa de **order loss abaixo de 1.2%**.  
   - Monitoramento com **alertas automáticos** quando a taxa ultrapassa **1%**.  

O **Mermaid.js** foi utilizado para criar um **Business Driver Map**, tornando a visualização das dependências e métricas mais clara e objetiva.  
